name		:= "dython-types"

version		:= "0.1.0"

organization 	:= "io.nuvo"

scalaVersion 	:= "2.11.6"

resolvers += "Vortex Snapshot Repo" at "https://dl.dropboxusercontent.com/u/19238968/vortex/mvn-repo"

libraryDependencies += "com.prismtech.cafe" % "cafe" % "2.1.2-SNAPSHOT"

autoCompilerPlugins := true

scalacOptions ++= Seq(
  "-Xelide-below", "MINIMUM",
  "-Xdev",
  "-optimise",
  "-deprecation",
  "-unchecked",
  "-language:postfixOps",
  "-feature",
  "-Yinline-warnings",
  "-Xlint:_"
)
