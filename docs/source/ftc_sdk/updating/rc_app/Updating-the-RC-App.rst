Updating the Robot Controller (RC) App
======================================

The Robot Controller App is one of the Apps provided with the *FIRST* Tech
Challenge :doc:`Software Development Kit (SDK) <../index>`. The Robot
Controller App is the application that runs on the Robot Controller Android
Device (REV Control Hub or an approved Android RC phone). This app 
communicates with the Driver Station App to control the robot.

The Robot Controller App also contains the programming environments for
Blocks and OnBot Java, but not the Team Code developed using those 
environments. When building using the Android Studio project, however,
a full build and deploy with Android Studio builds and deploys the 
Robot Controller application with the Java Team Code built-in. Therefore,
when updating the Robot Controller App, it is important to understand 
which programming environments the team uses to know how to correctly
update the Robot Controller App.

This page shows how to update the Robot Controller (RC) app on these
devices:

-  An approved Android RC smartphone
-  REV Control Hub

**Android Studio** teams should **not** use these steps to update the RC
app. **Android Studio** teams should ensure that their projects are up to
date with the `SDK GitHub Repo <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__.

.. dropdown:: Robot Controller (RC) app on Android phone

   Here are 2 methods to update the RC app on a Robot Controller (RC)
   phone:

   1. REV Hardware Client (RHC)
   2. “Side loading” with APK

   .. note:: 
      The Manage page, under Program and Manage, on a computer or Driver
      Station device, **does not** offer updating an RC app on a connected
      Robot Controller phone.

   .. dropdown:: Method 1 - REV Hardware Client - Windows computers only

      Plug the RC phone directly into the computer with RHC installed and
      open. Use a USB data cable, not a charge-only cable. Make sure the
      “Hardware” tab is active, at top left. The RC app on the phone does
      **not** need to be open.

      Here the computer does not need to be connected to the internet, since
      :doc:`in Updating the REV Hardware Client 
      </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
      the required DS update file was previously downloaded.

      The RHC app will recognize the phone, as shown here:

      .. figure:: images/080-RHC-recognize-RC-phone.png
         :alt: Recognizing the Phone
         :width: 80%
         :align: center

         Recognizing the Phone

      If the phone is not recognized, ensure that the phone has :doc:`developer
      options
      </programming_resources/tutorial_specific/android_studio/enabling_developer_options/Enabling-Developer-Options>`
      enabled. If necessary, click the "Scan for Devices" button in the
      lower-left of the REV Hardware Client app to force the RHC to rescan
      devices.

      Once recognized, click on that phone’s large icon/rectangle. The RHC app
      now displays the update status of the DS app, if any.

      .. figure:: images/082-RHC-update-RC-phone.png
         :alt: Update Status of Phone
         :width: 80%
         :align: center

         Update Status of Phone

      Simply click the blue Update rectangle (green arrow) – done!

      The update was fast, because you had already downloaded the RC app to
      the RHC. That was noted with ’(Already Downloaded)“, to the left of the
      blue Update rectangle.

      You could have selected an **older** version of the RC app, in the
      drop-down list just above the blue Update rectangle.

      After install, drag the RC app icon from the menu to the phone’s home
      screen.

      You may now unplug the RC phone from the computer, and close the RHC
      app. The updated RC app is ready to use.

   .. dropdown:: Method 2 - Side-load

      Here you will work directly with the Android Package or **APK file** to
      install the RC app on the Android phone. Any computer can be used, PC or
      Mac, old or new. This method is sometimes called “side-loading”.

      1. Connect your computer to the internet, open a web browser, and
         navigate to the `SDK github
         repository <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__.

         .. figure:: images/050-FTC-repo.png
            :alt: SDK GitHub Repo
            :width: 80%
            :align: center

            SDK GitHub Repo

         At the right side under “Releases”, click the “Latest” icon (yellow
         oval, above).

         In the next page, scroll down slightly in the “Latest” section, to the
         short list of “Assets”. Click on the file
         “FtcRobotController-release.apk”, to download it to your computer.

         .. figure:: images/090-github-assets-RC.png
            :alt: SDK GitHub Releases
            :width: 80%
            :align: center

            SDK GitHub Releases

         At this time, you could rename the file to reflect its current version
         number. For example, ``FtcRobotController-release-8.0.apk`` or simply
         ``RC-8.0-release.apk``. This distinguishes the file from other versions
         that might be stored later on that RC phone.

      2. Transfer the APK file from the computer to the RC phone’s Downloads
         (or Download) folder. Use a USB data cable (not a charge-only cable).
         When complete, you may unplug the RC phone from the computer.

      3. Uninstall the existing (obsolete) RC app, by dragging its icon to a
         Trash/Uninstall icon. Or, touch and hold the RC icon for “App info”,
         then choose Uninstall.

      4. On the RC phone, navigate to the Downloads folder. This can be done
         in several ways:

         -  at the main app menu (swipe up), touch the Files icon or the
            Downloads icon (if present)
         -  use the basic file manager in Settings/Storage: touch Explore or
            Files
         -  use a third-party app such as FX File Explorer (from the Google Play
            Store)

         Touch the APK filename that you transferred. Respond to the prompts, to
         install the updated RC app.

         After install, drag the RC app icon from the app menu to the RC phone’s
         home screen.

      Done! The updated RC app is now ready to use.

.. dropdown:: Robot Controller (RC) app on REV Control Hub

   Here are 3 methods to update the RC app on a REV Control Hub:

   #. REV Hardware Client (RHC)
   #. Manage page on computer
   #. Manage page on DS phone or Driver Hub

   .. note:: 
      “Side loading”, while possible, is not described here for the Control Hub
      as it requires a cumbersome procedure with extra equipment.

   .. dropdown:: Method 1 - REV Hardware Client - Windows computers only

      Use a USB data cable to connect the REV Control Hub’s USB-C port to the
      Windows computer.  Make sure the “Hardware” tab on the RHC is active, at
      top left. 

      Here the computer does not need to be connected to the internet, since
      :doc:`in Updating the REV Hardware Client 
      </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
      the required DS update file was previously downloaded.

      The RHC app will recognize the Control Hub, as shown here:

      .. figure:: images/070-RHC-recognize-CH.png
         :alt: Recognizing the Control Hub
         :width: 80%
         :align: center

         Recognizing the Control Hub

      Once recognized, click on the Control Hub’s large icon/rectangle. The RHC app now displays
      the update status of the RC app, if any.

      .. figure:: images/082-RHC-update-RC-CH.png
         :alt: Updating the Control Hub
         :width: 80%
         :align: center

         Updating the Control Hub

      Simply click the blue Update rectangle (green arrow) – done!
      
   .. dropdown:: Method 2 - Manage page on computer

      Here you will work directly with the Android Package or **APK file** to
      install the RC app on the Android phone. Any computer can be used, PC or
      Mac, old or new. This method is sometimes called “side-loading”.

      1. Connect your computer to the internet, open a web browser, and
         navigate to the `SDK github
         repository <https://github.com/FIRST-Tech-Challenge/FtcRobotController>`__.

         .. figure:: images/050-FTC-repo.png
            :alt: SDK GitHub Repo
            :width: 80%
            :align: center

            SDK GitHub Repo

         At the right side under “Releases”, click the “Latest” icon (yellow
         oval, above).

         In the next page, scroll down slightly in the “Latest” section, to the
         short list of “Assets”. Click on the file
         “FtcRobotController-release.apk”, to download it to your computer.

         .. figure:: images/090-github-assets-RC.png
            :alt: SDK GitHub Releases
            :width: 80%
            :align: center

            SDK GitHub Releases

         At this time, you could rename the file to reflect its current version
         number. For example, ``FtcRobotController-release-8.0.apk`` or simply
         ``RC-8.0-release.apk``. This distinguishes the file from other versions
         that might be stored later on that RC phone.

      2. Turn on the Control Hub (apply robot power), wait for green LED.

      3. Connect a laptop via Wi-Fi to the Control Hub. Open the Chrome
         browser, enter the usual address ``http://192.168.43.1:8080``

         Click the Manage tab, then scroll down to “Update Robot Controller App”.

         .. figure:: images/300-manage-RC-app.png
            :alt: Update RC App
            :width: 80%
            :align: center

            Update RC App

         Click “Select App…”. Navigate to the laptop folder where the RC APK file
         is stored, and select that file.

         Now click the “Update” button (green arrow, above).

         The software will replace the existing RC app with your new updated RC
         app. The connection between laptop and Control Hub will temporarily be
         lost, then automatically restored.

      When the completion message appears, the updated RC app is ready to use.

   .. dropdown:: Method 3 - Manage page on DS phone or Driver Hub

      This method can be used if your computer is unavailable or unable to
      connect via Wi-Fi to the Control Hub. For example, your desktop computer
      might have only a wired (Ethernet) network port, lacking Wi-Fi.

      But this method does require the RC APK file to be stored in the
      Download (or Downloads) folder on the DS phone or Driver Hub. That’s
      correct: **Robot Controller APK** stored on the **Driver Station**
      device.

      First download the RC APK file from the github repo to the computer,
      as shown in Step 1 of Method 2. Then transfer that APK file from the
      computer to the DS device’s Download folder, using a USB data cable. When
      complete, you may unplug the DS device from the computer.

      Connect the DS app to the Control Hub, from the DS app’s Settings menu
      (never with the Android device Wi-Fi settings).

      From the DS app’s menu, select “Program and Manage”. Then touch the 3
      bars at top right, and select “Manage”.

      This is the same Manage page that appears in a laptop browser. So the
      following instructions are the same as Method 2 above.

      Scroll down to “Update Robot Controller App”.

      .. figure:: images/330-manage-RC-app-CH-DS.png
         :alt: Update RC App
         :width: 80%
         :align: center

         Update RC App

      Touch “Select App…”. Navigate to the DS device’s Download folder, and
      select the latest RC APK file.

      Now touch the “Update” button (green arrow, above).

      The software will replace the existing RC app with your new updated RC
      app. The connection between Driver Station and Control Hub will
      temporarily be lost, then automatically restored.

      When the completion message appears, the updated RC app is ready to use.

Other descriptions of updating the RC app are
`at REV Robotics’ excellent documentation site <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-robot-controller-application>`__.

Questions, comments and corrections to westsiderobotics@verizon.net

