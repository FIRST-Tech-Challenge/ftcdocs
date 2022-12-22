.. meta::
   :title: FIRST Tech Challenge Software Development Kit
   :description: A brief introduction to the FTC SDK
   :keywords: FTC Docs, FIRST Tech Challenge, FTC, RC, Robot Controller, DS, Driver Station

*FIRST* Tech Challenge Software Development Kit
===============================================

The Software Development Kit (SDK) is the collection of tools for developing
software and executing it on a *FIRST* Tech Challenge robot. SDK Software
includes:

-  *FIRST* Tech Challenge Driver Station App 

   *  Includes Self-Inspect, :doc:`Robot Configuration </hardware_and_software_configuration/configuring/index>`, and others

-  *FIRST* Tech Challenge Robot Controller App

   *  Includes :doc:`Blocks Programming Environment </programming_resources/blocks/Blocks-Tutorial>`
   *  Includes :doc:`OnBot Java Programming Environment </programming_resources/onbot_java/OnBot-Java-Tutorial>`

-  `Android Studio Project <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__  
   for building the Robot Controller App with 
   :doc:`Android Studio </programming_resources/android_studio_java/Android-Studio-Tutorial>`
-  `Javadoc Reference Documentation <https://javadoc.io/doc/org.firstinspires.ftc>`__
-  Season-Specific Assets (TensorFlow models, Vuforia databases, etc...)

All released apps/source can be found in the `SDK GitHub Repository <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__.

SDK Releases
------------

The Software Development Kit is developed and maintained by a core group, known
as the *FIRST* Tech Challenge *Technology Team*, within a private GitHub repository.
This repository is kept private in order to prevent leaking the details of
future *FIRST* Tech Challenge game secrets, features in development, and other
aspects of development. Development and maintenance is ongoing year round.

Release Content
"""""""""""""""

Once the SDK is ready to be released, the private SDK repository is built and exported. 
This build consists of:

-  Built Driver Station App (``FtcDriverStation-release.apk``)
-  Built Robot Controller App (``FtcRobotController-release.apk``)
-  Android Studio Project source code (``vX.X.zip``, ``vX.X.tar.gz``)
-  `Javadoc Reference Documentation <https://javadoc.io/doc/org.firstinspires.ftc>`__
-  Season-Specific Assets (TensorFlow models, Vuforia databases, etc... hosted separately)

The export is then pushed to the `FtcRobotController GitHub Repository
<https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ as a `software
release
<https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases>`__. 

The `FtcRobotController GitHub Repository
<https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__ is also updated
with the exported Android Studio Project source so that changes can be tracked and the GitHub
repository can be `forked
<https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks>`__
or `cloned
<https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>`__
by teams.
This update is a one-way push, however, which is why public contributions
(`Pull Requests
<https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>`__)
to the FtcRobotController repository are not accepted.  The community is free
and encouraged to create issues at the repository for the *Technology Team* to
consider and address, however.

.. note:: 
   Some season-specific assets, such as TensorFlow models and Vuforia
   Databases, are not included directly in the FtcRobotController GitHub
   repository. Instead, they are packaged in an ``.AAR`` hosted on 
   Maven Central. When using the Robot Controller App, these assets are
   included in the app. When using Android Studio, these assets are 
   downloaded and included in your project the first time you compile
   the project (so an active internet connection is necessary).

Release Schedule
""""""""""""""""

These releases happen on a regular schedule, even if the exact dates aren't
specifically defined:

-  **Kickoff SDK Release** - Generally released within a week or two of the
   *FIRST* Tech Challenge Kickoff. The Kickoff SDK is typically the minimal
   software version required for use during the season.
-  **Update / Patch Releases** - These are typically released during the
   *FIRST* Tech Challenge season, when critical issues or helpful features are
   available for teams. Update/Patch releases aren't generally required for
   competition unless a critical patch or bugfix is issued.  
-  **Offseason Release** - Offseason releases are used to prepare teams for
   breaking changes or to provide a technology preview for new features in the
   upcoming season.

Software SDK updates are announced via the |blog|_ and on social media.

.. _blog: https://firsttechchallenge.blogspot.com/ 
.. |blog| replace:: *FIRST* Tech Challenge Blog 

SDK Release Notes
-----------------

One of the most important elements of the SDK Release is the 
`SDK Release Notes <https://github.com/FIRST-Tech-Challenge/FtcRobotController#release-information>`__. 
The SDK Release Notes contain important aspects of each release, including
breaking changes, enhancements, and critical bug fixes of note. 

Breaking Changes
""""""""""""""""

Breaking changes are as the name suggests, which are changes made within the
SDK's APIs or general architecture that may break existing code or
configurations that may already exist. It is especially important for all users
of the SDK to read the Breaking Changes section of the release notes, if one
exists for a given release, and determine the impact on their existing code.

Enhancements
""""""""""""

Enhancements are new features or (non-breaking) improvements made to existing
features of the SDK. Enhancements might include items such as improved logging,
new user interfaces (UI), better user experience (UX), new APIs, better
performance, or greater reliability. Not all enhancements of the SDK are listed
in the release notes, but those that have a direct user impact should.

Bug Fixes
"""""""""

Virtually every release of the SDK includes bug fixes, but when the *Technology
Team* wishes to elevate the visibility of an important bug fix it is included
in a Bug Fixes section of the Release Notes. Sometimes team code can be
affected if the bug required a workaround, and being elevated in the Release
Notes is a way for the *Technology Team* to notify teams that the workaround is
no longer necessary.

Updating SDK Software
---------------------

It is important to update the SDK software each time it is updated. Updates
mid-season may not be required, check with the minimum software version in the
Game Manual 1.  It is recommended to use the REV Hardware Client to update
hardware, if a 64-bit Windows computer is available. If not, then alternate
methods provided can be used to update the software.

-  :doc:`Updating the REV Hardware Client </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
-  :doc:`Updating the Driver Station App </ftc_sdk/updating/ds_app/Updating-the-DS-App>`
-  :doc:`Updating the Robot Controller App </ftc_sdk/updating/rc_app/Updating-the-RC-App>`
-  :doc:`Updating the Driver Hub OS </ftc_sdk/updating/driverhub_os/Updating-the-Driver-Hub-OS>`
-  :doc:`Updating the Control Hub OS </ftc_sdk/updating/controlhub_os/Updating-the-Control-Hub-OS>`
-  :doc:`Updating the Hub Firmware </ftc_sdk/updating/hub_firmware/Updating-Hub-Firmware>`


