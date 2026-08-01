Before You Start :bdg-success:`AS`
==================================

This page is the starting point for a team that is beginning directly in
Android Studio. It describes the Control System setup that the rest of this
tutorial assumes, points to the documentation a Java team needs alongside it,
and gives a checklist to work through before writing any code.

You do not need to have completed the Blocks or OnBot Java tutorials first.

Supported Control System Setup
------------------------------

This tutorial is written for the officially supported setup:

-  a **REV Robotics Control Hub** as the ROBOT CONTROLLER, and
-  a **REV Robotics Driver Hub** as the DRIVER STATION.

.. important:: Smartphones are not officially supported. They are legal to use
   in competition, but a team who uses one is responsible for all of their own
   testing and troubleshooting. Only the REV Control Hub and the REV Driver Hub
   are officially supported.

Where a page in this tutorial describes more than one setup, follow the Control
Hub and Driver Hub instructions unless your team is using one of the smartphone
setups below.

Smartphone Setups
^^^^^^^^^^^^^^^^^

Two smartphone setups appear throughout the Control System documentation. Both
are covered by the same pages this tutorial links to, in sections labeled for
smartphones:

-  A **smartphone ROBOT CONTROLLER** connected to a REV Robotics Expansion Hub.
   This setup needs extra steps that a Control Hub does not: renaming the
   phone, placing it in airplane mode with Wi-Fi on, pairing it to the DRIVER
   STATION, and
   :doc:`enabling Developer Options <../../tutorial_specific/android_studio/enabling_developer_options/Enabling-Developer-Options>`
   so Android Studio can install the app onto it.
-  A **smartphone DRIVER STATION** in place of a Driver Hub. This setup needs
   the phone renamed and paired, and needs a Micro USB OTG adapter cable to
   connect a gamepad.

.. note:: A Control Hub has Developer Options enabled from the factory, so
   teams using the supported setup can skip the phone-only preparation
   steps.

Documentation You Will Need
---------------------------

Read or bookmark these before working through the rest of this tutorial. They
are the pages that describe the hardware side of the Control System, which
Android Studio itself does not cover.

-  :doc:`Control System Introduction <../../shared/control_system_intro/The-FTC-Control-System>`
   -- what each component of the Control System does.
-  :doc:`Required Materials <../../shared/required_materials/Required-Materials>`
   -- the hardware needed to complete this tutorial.
-  :doc:`Computer Requirements </programming_resources/laptops/laptops>`
   -- the laptop specifications recommended for running Android Studio.
-  :doc:`Configuring Your Android Devices <../../shared/configuring_android/Configuring-Your-Android-Devices>`
   -- installing apps, updating firmware, and pairing the DRIVER STATION to the
   ROBOT CONTROLLER.
-  :doc:`Connecting Devices to a Control or Expansion Hub </hardware_and_software_configuration/connecting_devices/index>`
   -- wiring power, motors, servos, and sensors to the hub.
-  :doc:`Configuring Your Hardware </hardware_and_software_configuration/configuring/index>`
   -- creating the robot configuration file from the DRIVER STATION, which is
   how your OpMode finds each device by name.
-  :doc:`Managing a Control Hub <../../shared/managing_control_hub/Managing-a-Control-Hub>`
   -- renaming the Control Hub, changing its password, and updating Hub
   firmware.
-  :doc:`Managing a Driver Hub <../../shared/managing_smartphone_ds/Managing-a-Smartphone-Driver-Station>`
   -- renaming the Driver Hub and updating the DRIVER STATION app.
-  :doc:`Updating Components of the Control System </ftc_sdk/updating/index>`
   -- keeping the Control Hub OS, Driver Hub OS, and apps current.

Before Writing Code
-------------------

Work through this checklist first. Each item links to the page in the
documentation that covers it.

.. list-table::
   :widths: 40 60
   :class: longtable
   :header-rows: 1

   * - Check
     - Where it is covered
   * - The Control Hub is wired to a 12V battery through a REV switch, and any
       Expansion Hub, motors, servos, and sensors are connected.
     - :doc:`Connecting Devices to a Control or Expansion Hub </hardware_and_software_configuration/connecting_devices/index>`
   * - The Control Hub and Driver Hub have been renamed to match the team
       number naming requirements in the Competition Manual.
     - :doc:`Managing a Control Hub <../../shared/managing_control_hub/Managing-a-Control-Hub>`,
       :doc:`Managing a Driver Hub <../../shared/managing_smartphone_ds/Managing-a-Smartphone-Driver-Station>`
   * - The Driver Hub is paired to the Control Hub, and the DRIVER STATION app
       shows the ROBOT CONTROLLER as connected.
     - :doc:`Configuring Your Android Devices <../../shared/configuring_android/Configuring-Your-Android-Devices>`
   * - A robot configuration file has been created, saved, and activated from
       the DRIVER STATION, and each device name matches the name your OpMode
       will use.
     - :doc:`Configuring Your Hardware </hardware_and_software_configuration/configuring/index>`
   * - The Control Hub OS, Driver Hub OS, Hub firmware, and the DRIVER STATION
       app are up to date.
     - :doc:`Updating Components of the Control System </ftc_sdk/updating/index>`
   * - Android Studio is installed and the ``FtcRobotController`` project has
       been downloaded and opened.
     - :doc:`Installing Android Studio <../../tutorial_specific/android_studio/installing_android_studio/Installing-Android-Studio>`,
       :doc:`Downloading the Android Studio Project Folder <../../tutorial_specific/android_studio/downloading_as_project_folder/Downloading-the-Android-Studio-Project-Folder>`
   * - The ``FtcRobotController`` project and the DRIVER STATION app both come
       from the current season's release.
     - :doc:`Downloading the Android Studio Project Folder <../../tutorial_specific/android_studio/downloading_as_project_folder/Downloading-the-Android-Studio-Project-Folder>`
   * - A USB Type C cable connects the laptop to the Control Hub's Type C port,
       and Android Studio lists the hub as an available deployment target.
     - :doc:`Creating and Running an OpMode <../../tutorial_specific/android_studio/creating_op_modes/Creating-and-Running-an-Op-Mode-(Android-Studio)>`

.. important:: Android Studio builds and installs the entire ROBOT CONTROLLER
   app, replacing the one on the Control Hub. The app it installs must be
   compatible with the DRIVER STATION app on the Driver Hub, so update both
   from the same season's release.

.. note:: This tutorial deploys the app over the USB Type C connection
   described above. The Control Hub also broadcasts a Program & Manage Wi-Fi
   network, used by the Blocks and OnBot Java tools and described in
   :doc:`Connecting a Laptop to the Program & Manage Network <../../shared/program_and_manage_network/Connecting-a-Laptop-to-the-Program-&-Manage-Network>`.
