package ch.epfl.lamp

import sbt._
import Keys._
import java.io.{File, FileInputStream, IOException}
import java.nio.file.FileSystems

import org.apache.commons.codec.binary.Base64

import scala.util.{Failure, Success, Try}
import MOOCPlugin.autoImport._
import scalafix.sbt.ScalafixPlugin.autoImport._


case class AssignmentInfo(
  key: String,
  itemId: String,
  premiumItemId: Option[String],
  partId: String
)

/**
  * Provides tasks for submitting the assignment
  */
object StudentPlugin extends AutoPlugin {

  object autoImport {
    val assignmentInfo = SettingKey[AssignmentInfo]("assignmentInfo")
  }
  import autoImport._

  // Run scalafix linting after compilation to avoid seeing parser errors twice
  private val scalafixLinting = (scalafix in Compile).toTask(" --check").dependsOn(compile in Compile)

  override lazy val projectSettings = Seq(
    // Don't lint the sources of scalacheck embedded in one of the projects
    unmanagedSources in scalafix in Compile := {
      val matcher = FileSystems.getDefault.getPathMatcher("glob:**/org/scalacheck/**")
      (unmanagedSources in Compile).value
        .filterNot(file => matcher.matches(file.toPath))
    },
    // Run scalafix linting in parallel with the tests
    (test in Test) := {
      scalafixLinting.value
      (test in Test).value
    },

    packageSubmissionSetting,
    commonSourcePackages := Seq() // see build.sbt
  ) ++ packageSubmissionZipSettings

  /** **********************************************************
    * SUBMITTING A SOLUTION TO COURSERA
    */

  val packageSourcesOnly = TaskKey[File]("packageSourcesOnly", "Package the sources of the project")

  val packageSubmissionZip = TaskKey[File]("packageSubmissionZip")

  val packageSubmissionZipSettings = Seq(
    packageSubmissionZip := {
      val submission = crossTarget.value / "submission.zip"
      val sources = (packageSourcesOnly in Compile).value
      val binaries = (packageBin in Compile).value
      IO.zip(Seq(sources -> "sources.zip", binaries -> "binaries.jar"), submission)
      submission
    },
    // Exclude resources from binaries
    mappings in (Compile, packageBin) := {
      val relativePaths =
        (unmanagedResources in Compile).value.flatMap(Path.relativeTo((unmanagedResourceDirectories in Compile).value)(_))
      (mappings in (Compile, packageBin)).value.filterNot { case (_, path) => relativePaths.contains(path) }
    },
    artifactClassifier in packageSourcesOnly := Some("sources")
  ) ++ inConfig(Compile)(Defaults.packageTaskSettings(packageSourcesOnly, Defaults.sourceMappings))

  val maxSubmitFileSize = {
    val mb = 1024 * 1024
    10 * mb
  }

  /** Check that the jar exists, isn't empty, isn't crazy big, and can be read
    * If so, encode jar as base64 so we can send it to Coursera
    */
  def prepareJar(jar: File, s: TaskStreams): String = {
    val errPrefix = "Error submitting assignment jar: "
    val fileLength = jar.length()
    if (!jar.exists()) {
      s.log.error(errPrefix + "jar archive does not exist\n" + jar.getAbsolutePath)
      failSubmit()
    } else if (fileLength == 0L) {
      s.log.error(errPrefix + "jar archive is empty\n" + jar.getAbsolutePath)
      failSubmit()
    } else if (fileLength > maxSubmitFileSize) {
      s.log.error(errPrefix + "jar archive is too big. Allowed size: " +
        maxSubmitFileSize + " bytes, found " + fileLength + " bytes.\n" +
        jar.getAbsolutePath)
      failSubmit()
    } else {
      val bytes = new Array[Byte](fileLength.toInt)
      val sizeRead = try {
        val is = new FileInputStream(jar)
        val read = is.read(bytes)
        is.close()
        read
      } catch {
        case ex: IOException =>
          s.log.error(errPrefix + "failed to read sources jar archive\n" + ex.toString)
          failSubmit()
      }
      if (sizeRead != bytes.length) {
        s.log.error(errPrefix + "failed to read the sources jar archive, size read: " + sizeRead)
        failSubmit()
      } else encodeBase64(bytes)
    }
  }

  /** Task to package solution to a given file path */
  val packageSubmission = inputKey[Unit]("package solution as an archive file")
  lazy val packageSubmissionSetting = packageSubmission := {
    // Fail if scalafix linting does not pass.
    scalafixLinting.value

    val args: Seq[String] = Def.spaceDelimited("[path]").parsed
    val s: TaskStreams = streams.value // for logging
    val jar = (packageSubmissionZip in Compile).value

    val base64Jar = prepareJar(jar, s)

    val path = args.headOption.getOrElse((baseDirectory.value / "submission.jar").absolutePath)
    scala.tools.nsc.io.File(path).writeAll(base64Jar)
  }

  def failSubmit(): Nothing = {
    sys.error("Submission failed")
  }

  /**
    * *****************
    * DEALING WITH JARS
    */
  def encodeBase64(bytes: Array[Byte]): String =
    new String(Base64.encodeBase64(bytes))
}
