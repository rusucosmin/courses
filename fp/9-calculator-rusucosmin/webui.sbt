lazy val webUI = project.in(file("web-ui")).
  enablePlugins(ScalaJSPlugin).
  settings(
    scalaVersion := "2.12.7",
    // Add the sources of the calculator project
    unmanagedSourceDirectories in Compile += baseDirectory.value / ".." / "src" / "main" / "scala" / "calculator",
    libraryDependencies += "org.scala-js" %%% "scalajs-dom" % "0.9.6",
    scalaJSUseMainModuleInitializer := true
  )
