name := course.value + "-" + assignment.value

scalaVersion := "0.9.0-RC1"

scalacOptions ++= Seq("-deprecation")

fork := true

libraryDependencies += "com.novocode" % "junit-interface" % "0.11" % Test

testOptions in Test += Tests.Argument(TestFrameworks.JUnit, "-a", "-v")

commonSourcePackages += "common"

courseId := "bRPXgjY9EeW6RApRXdjJPw"

// In case we want to use a Dotty version before it's fully released
resolvers += Resolver.sonatypeRepo("staging")
