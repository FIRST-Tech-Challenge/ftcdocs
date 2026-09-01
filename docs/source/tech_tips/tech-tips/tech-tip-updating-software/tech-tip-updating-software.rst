Updating and Exploring Your Robot Controller Software
=====================================================

Started in the 2023-2024 season, Tech Tips are segments released in the
*FIRST* Tech Challenge `Team E-mail Blast
<https://www.firstinspires.org/resource-library/ftc/team-blast-archive>`__.
Sometimes the Tech Tips are included in whole in the email blast, but sometimes
there is more content than is reasonable in the email blast so partial content
is included in the blast with the rest of the content here.

.. _updateRobotControllerApp:

Updating the Robot Controller App
---------------------------------

If you use :ref:`Android Studio
<programming_resources/android_studio_java/Android-Studio-Tutorial:android studio programming tutorial>`,
did you know that you're not supposed to use the `REV Hardware Client
<https://docs.revrobotics.com/rev-hardware-client/>`__ to update the Robot
Controller (RC) App? Blocks and OnBot Java programs are stored on the Robot
Controller (Control Hub or SmartPhone) differently than Android Studio
programs, and this has a major effect on how updates can be managed on the
device. Read more about this at :ref:`Updating the Robot Controller (RC) App
<ftc_sdk/updating/rc_app/Updating-the-RC-App:Updating the Robot Controller (RC) App>`.

.. _updatingthesdkmanifest:

Don't Update the SDK by Editing the Manifest
--------------------------------------------

This section comes to us from an amalgamation of emailed questions asking
about allowed ways to update an FtcRobotController SDK project. An approximate
summary of the emailed questions along this topic is as follows:

- *"Is merely editing the Android Manifest file in the TeamCode directory of
  the FtcRobotController SDK project an acceptable way of easily updating the
  SDK?"*

Even though it's not forbidden, that doesn't mean you should do it - like
putting pineapple on pizza (sorry, the door was open, I couldn't stop
myself). Seriously, though, 4 times out of 5 you can likely get away with
updating the SDK through editing the Android Manifest to point to the latest
version of the SDK libraries. However, that assumes that all the Tech Team
does is update the SDK libraries, which is never ever the case. In addition
to also updating programming samples, often enough the Tech Team must also
update tooling, dependencies, and other build items in addition to the SDK
libraries, and simply updating the Android Manifest is going to get you into
real trouble (things will appear to work, until they don't, and you won't
know why). As a corollary, you can choose to simply only put gas in your car
and ignore all the other fluids, but eventually you're going to wish you
hadn't.

The proper way of updating your SDK is to use Git/GitHub to update your
robot source each time the SDK software updates. The Tech Team always
updates the FtcRobotController in-place (meaning the same repo is always
updated each version), so if you're using Git you can easily pull the
changes made upstream and accept the changes within your code. You should
never be manually updating files, like the Android Manifest file, because
Git can tell you all of the files you need to update and can do that for
you. If you use Git or GitHub, we highly recommend reading our guide on
ftc-docs for :ref:`managing your Android Studio project repositories
<programming_resources/tutorial_specific/android_studio/fork_and_clone_github_repository/Fork-and-Clone-From-GitHub:forks vs. clones>`.

For example, check out these changelists. The `FtcRobotController v9.0
<https://github.com/FIRST-Tech-Challenge/FtcRobotController/pull/674/files>`__
commit/change is everything that needs to be changed to upgrade from version
8.2 to 9.0 - there are 75 changed files there, which include samples, a core
interface module change, gradle dependencies, and in that changelist the
Tech Team also rearchitected the asset structure. However, the
`FtcRobotController v9.0.1
<https://github.com/FIRST-Tech-Challenge/FtcRobotController/pull/731/files>`__
and `FtcRobotController v9.1
<https://github.com/FIRST-Tech-Challenge/FtcRobotController/pull/941/files>`__
pull requests only changed a handful of files (mostly samples), and the core
changes are in the AndroidManifest.xml and build.dependencies.gradle files.
In general our major version releases (where we increase the first number in
the version string) are the big ones, and then the dot-releases are almost
always fairly small targeted releases. The Tech Team tries very hard not to
make big-scale changes to build systems or major dependencies during the
season.

In summary, teams should never simply change the Android Manifest,
they should be updating the software appropriately - as Voltaire warned,
with great "Android Studio" power comes great "GitHub" responsibility.

.. _ladybug1011:

Android Studio "LadyBug" and the FTC SDK
----------------------------------------

This is an important message for teams who use Android Studio to program
their robots. Teams who use Blocks or OnBot Java are not impacted.

On October 1, 2024 `Android Studio
<https://developer.android.com/studio/releases>`__ released a new version of
their software, 2024.2.1 codenamed "LadyBug", which brought a major user
interface change as well as several other changes (bundled software and
tooling changes) that affects how Android Studio builds projects.
Unfortunately these tooling changes broke the native compatibility with the
:ref:`*FIRST* Tech Challenge Software Development Kit (SDK)
<ftc_sdk/overview/index:*FIRST* Tech Challenge Software Development Kit>`,
most notably with the `FtcRobotController project
<https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__.  *FIRST* Tech
Challenge teams who use Android Studio with software projects version 10.1
and older are not able to use Android Studio "LadyBug" without performing
additional steps (see
:ref:`System Requirements <programming_resources/tutorial_specific/android_studio/installing_android_studio/Installing-Android-Studio:System Requirements>`)
to restore compatibility.

Teams do not need to update Android Studio to "LadyBug" to continue building
current software, however if they do, a new version of the
`FtcRobotController project
(10.1.1) <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ has
been released which is designed to work with Android Studio "LadyBug." Users
will be required to upgrade their Android Studio software minimally to
Android Studio 2024.2.1 "LadyBug" in order to use the 10.1.1 version of the
SDK and newer. There are no feature updates to SDK 10.1.1, it is merely a
compatibility update which updates the build tools used by the SDK -
including the underlying Gradle tools and the Android Gradle plugin - and
eliminates the need to perform any additional steps to use Android Studio
"LadyBug" and newer. It is expected that future updates of the SDK will
build upon this update, and will minimally require "LadyBug." Teams who are
using older versions of Android Studio who upgrade to SDK 10.1.1 will
receive notifications within Android Studio to update the version of Android
Studio, which may require an internet connection to update.

Teams are encouraged to read the :doc:`Managing an Android Studio Project
</programming_resources/android_studio_java/manage/manage>`
article on ftc-docs for tips on managing their projects using GitHub and the
git version control system. Teams managing software projects outside of GitHub
and git may re-download the project, reapply their changes, and copy over their
TeamCode folder. Teams who need technical assistance may use the
`FTC Community Forums <https://ftc-community.firstinspires.org/>`__ to receive
technical help and advice.

.. _robotcontrollersourcecode:

Reading the Robot Controller Source Code
----------------------------------------

Have you ever been programming your robot (especially in Blocks and OnBot
Java) using FTC SDK APIs and wished you could see the source code under the
hood that executes the commands you're calling? Let's explore the
`Extracted-RC GitHub repository
<https://github.com/OpenFTC/Extracted-RC>`__.  Note that Android Studio
users can already view source code within Android Studio!

Several years ago, *FIRST* Tech Challenge gave permission for the OpenFTC
project to extract AAR's from our SDK releases and publicly post an
extracted version of the Robot Controller source code. The `Extracted-RC
<https://github.com/OpenFTC/Extracted-RC>`__ repository has `branches
<https://github.com/OpenFTC/Extracted-RC/branches/all>`__ that contain
source code for each release of the SDK, as far back as SDK 5.2 through SDK
9.0.1. You can look up how `setPower() works on a Continuous Rotation Servo
<https://github.com/OpenFTC/Extracted-RC/blob/c04e3db091c5b63c2f4da31abb540c06ca33ac14/RobotCore/src/main/java/com/qualcomm/robotcore/hardware/CRServoImpl.java#L125>`__,
how `REV Core Hex motors are defined
<https://github.com/OpenFTC/Extracted-RC/blob/c04e3db091c5b63c2f4da31abb540c06ca33ac14/Hardware/src/main/java/com/qualcomm/hardware/motors/RevRoboticsCoreHexMotor.java#L49>`__,
how `Blocks OpModes are started
<https://github.com/OpenFTC/Extracted-RC/blob/master/Blocks/src/main/java/com/google/blocks/ftcrobotcontroller/runtime/BlocksOpMode.java#L235>`__,
and even see the `built-in driver for the HuskyLens vision camera
<https://github.com/OpenFTC/Extracted-RC/blob/c04e3db091c5b63c2f4da31abb540c06ca33ac14/Hardware/src/main/java/com/qualcomm/hardware/dfrobot/HuskyLens.java#L55>`__.

The Extracted-RC repository will not accept Pull Requests (PR's) since the
repository has no actual development purpose - it is only to allow
interested folks the ability to read the source code and see how things are
implemented. Only *FIRST* staff and Tech Team members have access to the
development source. Are you interested in joining the *FIRST* Tech Challenge
Tech Team? Let us know by filling out `this survey
<https://forms.microsoft.com/pages/responsepage.aspx?id=v8Pzh9Ft7ES9j5nk5iLvhJz4rTMLMkNKttplG8GSviZUQjdSTU1UQVU0S1dDSkQwRjhDWEUyTEo3Uy4u&route=shorturl>`__!

Got any questions about updating your robot software? Come start or join the
conversation on the `FTC Community Forums
<https://ftc-community.firstinspires.org/>`__!
