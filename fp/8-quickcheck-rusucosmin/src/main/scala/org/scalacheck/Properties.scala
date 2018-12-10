/*-------------------------------------------------------------------------*\
**  ScalaCheck                                                             **
**  Copyright (c) 2007-2016 Rickard Nilsson. All rights reserved.          **
**  http://www.scalacheck.org                                              **
**                                                                         **
**  This software is released under the terms of the Revised BSD License.  **
**  There is NO WARRANTY. See the file LICENSE for the full text.          **
\*------------------------------------------------------------------------ */

package org.scalacheck

import language.reflectiveCalls

import util.ConsoleReporter

/** Represents a collection of properties, with convenient methods
 *  for checking all properties at once. This class is itself a property, which
 *  holds if and only if all of the contained properties hold.
 *  <p>Properties are added in the following way:</p>
 *
 *  {{{
 *  object MyProps extends Properties("MyProps") {
 *    property("myProp1") = forAll { (n:Int, m:Int) =>
 *      n+m == m+n
 *    }
 *  }
 *  }}}
 */
class Properties(val name: String) {

  private val props = new scala.collection.mutable.ListBuffer[(String,Prop)]

  /**
   * Changes to the test parameters that are specific to this class.
   * Can be used to set custom parameter values for this test.
   */
  def overrideParameters(p: Test.Parameters): Test.Parameters = p

  /** Returns all properties of this collection in a list of name/property
   *  pairs.  */
  def properties: Seq[(String,Prop)] = props

  /** Convenience method that checks the properties with the given parameters
   *  (or default parameters, if not specified)
   *  and reports the result on the console. Should only be used when running
   *  tests interactively within the Scala REPL.
   *
   *  If you need to get the results
   *  from the test use the `check` methods in [[org.scalacheck.Test]]
   *  instead. */
  def check(prms: Test.Parameters = Test.Parameters.default): Unit = {
    val params = overrideParameters(prms)
    Test.checkProperties(
      params.withTestCallback(ConsoleReporter(1) chain params.testCallback), this
    )
  }

  /** Adds all properties from another property collection to this one */
  def include(ps: Properties): Unit =
    include(ps, prefix = "")

  /** Adds all properties from another property collection to this one
   *  with a prefix this is prepended to each included property's name. */
  def include(ps: Properties, prefix: String): Unit =
    for((n,p) <- ps.properties) property(prefix + n) = p

  /** Used for specifying properties. Usage:
   *  {{{
   *  property("myProp") = ...
   *  }}}
   */
  sealed class PropertySpecifier() {
    // TODO: Delete this in 1.14 -- kept for binary compat with 1.13.3 and prior
    protected def update(propName: String, p: Prop) = {
      props += ((name+"."+propName, p))
    }
    def update(propName: String, p: => Prop) = {
      props += ((name+"."+propName, Prop.delay(p)))
    }
  }

  lazy val property = new PropertySpecifier()
}
