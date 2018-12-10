addSbtPlugin("io.get-coursier" % "sbt-coursier" % "1.0.2")

addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "0.14.5")

addSbtPlugin("org.scala-js" % "sbt-scalajs" % "0.6.25")

// For grading-infra
addSbtPlugin("io.spray" % "sbt-revolver" % "0.9.1")

addSbtPlugin("ch.epfl.scala" % "sbt-scalafix" % "0.9.0")

// In case we want to use an sbt-dotty version before it's fully released
resolvers += Resolver.sonatypeRepo("staging")

addSbtPlugin("ch.epfl.lamp" % "sbt-dotty" % "0.2.4")
