Configuring your Android Devices
================================

What Needs to Be Configured for My Control System?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Control Hub Configuration 
^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: 
   References to the Driver Station smartphone may instead apply to the
   `REV Driver Hub <https://docs.revrobotics.com/duo-control/control-system-overview/driver-hub-specifications>`__,
   which is preloaded with the Driver Station (DS) app.

Teams who are using a Control Hub (which has an integrated Android Device)
will only need to configure a single smartphone for use as a Driver
Station. The process is as follows: 

*  Rename the smartphone to "<TEAM NUMBER>-DS" (where <TEAM NUMBER> is replaced by your team number). 
*  Install the Driver Station (DS) app onto the Driver Station phone. (The DS app is pre-installed on the REV Driver Hub.) 
*  Put your phone into Airplane Mode (with the WiFi radio still on). 
*  Pair (i.e., wirelessly connect) the Driver Station to the Control Hub.

.. image:: images/ControlHubAndPhone.jpg
   :align: center

|

.. important:: Eventually the Control Hub will need be renamed so
   that its name complies with Game Manual rule <RS01>, but for now we will
   use the Control Hub with its default name. You can learn how to manage a
   Control Hub (and modify its name, password, etc.) in 
   :doc:`this tutorial <../managing_control_hub/Managing-a-Control-Hub>`.

Two Android Smartphone Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teams who have two smartphones and are not using a Control Hub will need
to configure one smartphone for use as a Robot Controller and a second
smartphone for use as a Driver Station. The process is as follows, 

*  Rename one smartphone to "<TEAM NUMBER>-RC" (replace <TEAM NUMBER> with your team number). 
*  Install the Robot Controller app onto the Robot Controller phone. 
*  Rename a second smartphone to "<TEAM NUMBER>-DS" (where <TEAM NUMBER> is replaced by your team number). 
*  Install the Driver Station app onto the Driver Station phone. (The DS app is pre-installed on the REV Driver Hub.) 
*  Put your phones into Airplane Mode (with the WiFi radios still on). 
*  Pair (i.e., wirelessly connect) the Driver Station to the Robot Controller.

.. image:: images/twoAndroidPhones.jpg
   :align: center

|

.. Do not change the name of the following Header title, as it's linked from elsewhere. Currently it is called "Renaming Your Smartphones".

Renaming Your Smartphones
~~~~~~~~~~~~~~~~~~~~~~~~~

The official rules of the FIRST Tech Challenge (see <RS01>) require that
you change the Wi-Fi name of your smartphones to include your team
number and "-RC" if the phone is a Robot Controller or "-DS" if it is a
Driver Station. A team can insert an additional dash and a letter ("A",
"B", "C", etc.) if the team has more than one set of Android phones.

If, for example, a team has a team number of 9999 and the team has
multiple sets of phones, the team might decide to name one phone
"9999-C-RC" for the Robot Controller and the other phone "9999-C-DS" for
the Driver Station. The "-C" indicates that these devices belong to the
third set of phones for this team.

The name of a Robot Controller phone can be changed in the RC app, using
instructions :ref:`found here <programming_resources/shared/managing_smartphone_rc/Managing-a-Smartphone-Robot-Controller:changing the name>`.
It can also be changed at the *Manage* page from the RC app, a paired DS
app, or a connected laptop; click ``Apply Wi-Fi Settings`` when done.

The name of a Driver Station phone can be changed in the DS app, using
instructions
:ref:`found here <programming_resources/shared/managing_smartphone_ds/Managing-a-Smartphone-Driver-Station:changing the name>`.

As an alternate, the device names can be changed at the Android system
level, as described below.

.. note:: It will take an estimated 5 minutes per phone to complete this
   task.

.. |rename1| image:: images/RenameStep1.jpg
.. |rename2| image:: images/RenameStep2.jpg
.. |rename3| image:: images/RenameStep3.jpg
.. |rename4| image:: images/RenameStep4.jpg
.. |rename5| image:: images/RenameStep5.jpg
.. |rename6| image:: images/RenameStep6.jpg
.. |rename7| image:: images/RenameStep7.jpg
.. |rename8| image:: images/RenameStep8.jpg

+------------------------------------------------+---------------------+
| Step                                           | Image               |
+================================================+=====================+
| 1. Browse the list of available apps on the    | |rename1|           |
| smartphone and locate the **Settings** icon.   |                     |
| Click on **Settings** icon to display the      |                     |
| Settings screen.                               |                     |
+------------------------------------------------+---------------------+
| 2. Click on **Wi-Fi** to launch the Wi-Fi      | |rename2|           |
| screen.                                        |                     |
|                                                |                     |
|                                                |                     |
+------------------------------------------------+---------------------+
| 3. Touch the three vertical dots to display a  | |rename3|           |
| pop-up menu.                                   |                     |
|                                                |                     |
|                                                |                     |
+------------------------------------------------+---------------------+
| 4. Select **Advanced** from the pop-up menu.   | |rename4|           |
|                                                |                     |
|                                                |                     |
|                                                |                     |
+------------------------------------------------+---------------------+
| 5. Select **Wi-Fi Direct** from the **Advanced | |rename5|           |
| Wi-Fi** screen.                                |                     |
|                                                |                     |
|                                                |                     |
+------------------------------------------------+---------------------+
| 6. Touch the three vertical dots to display a  | |rename6|           |
| pop-up menu.                                   |                     |
|                                                |                     |
|                                                |                     |
+------------------------------------------------+---------------------+
| 7. Select **Configure Device** from the pop-up | |rename7|           |
| menu.                                          |                     |
|                                                |                     |
|                                                |                     |
+------------------------------------------------+---------------------+
| 8. Use touch pad to enter new name of device.  | |rename8|           |
| If the device will be a Robot Controller,      |                     |
| specify your team number and -RC. If the       |                     |
| device will bea Driver Station, specify your   |                     |
| team number and -DS. You can also set the      |                     |
| Wi-Fi Direct inactivity timeout to *Never      |                     |
| disconnect* and then hit the\ **SAVE** button  |                     |
| to save your changes. Note that in the         |                     |
| screenshot shown to the right, the team number |                     |
| is 9999. The "-C" indicates that this is from  |                     |
| the third pair of smartphones forthis team.    |                     |
| The -RC indicates that this phonewill be a     |                     |
| Robot Controller.                              |                     |
+------------------------------------------------+---------------------+
| 9. After renaming phone, power cycle the       |                     |
| device.                                        |                     |
+------------------------------------------------+---------------------+

Installing the *FIRST* Tech Challenge Apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**As of 2021, the SDK apps (v 6.1 and higher) are no longer available on
Google Play.**

The `REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__
software will allow you to download the apps to devices: REV Control
Hub, REV Expansion Hub, REV Driver Hub, and other approved Android
devices (*see section below, called Updating Apps on Android
Phones*). Here are some of the benefits: 

*  Connect to a REV Control Hub via WiFi. 
*  One Click update of all software on connected devices. 
*  Pre-download software updates without a connected device. 
*  Back up and restore user data from Control Hub. 
*  Install and switch between DS and RC applications on Android Devices. 
*  Access the Robot Control Console on the Control Hub.

The app releases are also available on the `FTCRobotController
Github
repository <https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases>`__.
It is possible to "side-load" the apps onto the Robot Controller
(RC) and Driver Station (DS) phones. However, this section of the document 
does **not** include such instructions; other document pages describe
side-loading the :ref:`RC app <programming_resources/shared/managing_smartphone_rc/Managing-a-Smartphone-Robot-Controller:Updating the Robot Controller App>`
and the :ref:`DS app <programming_resources/shared/managing_smartphone_ds/Managing-a-Smartphone-Driver-Station:Updating the Driver Station App>`.

Updating Apps and Firmware on REV Devices (REV Expansion Hub, REV Control Hub, REV Driver Hub)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__
software is used to install and update apps, firmware and/or
operating systems on devices from REV Robotics. Simply connect the
device via USB to your PC with the REV Hardware Client installed and
running, and the software will detect connected hardware. After
detection, the REV Hardware Client can then 
`update the Robot Controller (RC) app on a REV Control Hub <https://docs.revrobotics.com/rev-hardware-client/control-hub/updating-control-hub>`__,
`update the Driver Station (DS) app on a REV Driver Hub <https://docs.revrobotics.com/rev-hardware-client/driver-hub/updating-a-driver-hub>`__,
or 
`update firmware <https://docs.revrobotics.com/rev-hardware-client/expansion-hub/updating-expansion-hub>`__.

Updating Apps on Android Phones
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__
software is used to install, uninstall, and 
`update apps on Android phones <https://docs.revrobotics.com/rev-hardware-client/android-device/installing-rc-ds-applications>`__.
However, the phones must have **Developer Options** enabled in order for
the phone to be properly recognized and updated by the REV Hardware
Client software. The process for enabling Developer Options is as
follows:

.. |devop1| image:: images/1-developer-options.jpg
.. |devop2a| image:: images/2a-developer-options.jpg
.. |devop2b| image:: images/2b-developer-options.jpg
.. |devop4| image:: images/4-developer-options.jpg
.. |devop5| image:: images/5-developer-options.*

+------------------------------------------------+---------------------+
| Step                                           | Image               |
+================================================+=====================+
| 1. Go to "Settings", then tap "About device"   |                     |
| or "About phone".                              |  |devop1|           |
|                                                |                     |
|                                                |                     |
+------------------------------------------------+---------------------+
| 2. Scroll down, then tap Build number seven    | |devop2a|           |
| times.Depending on your device and operating   |                     |
| system, you may need to tap Software           |                     |
| information, then tap Build number seven       |                     |
| times.                                         |                     |
|                                                |                     |
|                                                |                     |
|                                                | |devop2b|           |
+------------------------------------------------+---------------------+
| 3. Enter your pattern, PIN or password to      |                     |
| enable the Developer options menu.             |                     |
+------------------------------------------------+---------------------+
| 4. The "Developer options" menu will now       | |devop4|            |
| appear in your Settings menu. Depending on     |                     |
| your device, it may appear under Settings >    |                     |
| General > Developer options.                   |                     |
+------------------------------------------------+---------------------+
| 5. To disable the Developer options at any     | |devop5|            |
| time, tap the switch.                          |                     |
|                                                |                     |
|                                                |                     |
+------------------------------------------------+---------------------+

Placing Phones into Airplane Mode with Wi-Fi On
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the FIRST Tech Challenge competitions, it is important that you
place your Robot Controller and Driver Station phones into Airplane mode
but keep their Wi-Fi radios turned on. This is important because you do
not want any of the cellular telephone functions to be enabled during a
match. The cellular telephone functions could disrupt the function of
the robot during a match.

.. note:: It will take an estimated 2.5 minutes per phone to complete this
   task. Also note that the screens displayed on your Android devices might
   differ slightly from the images contained in this document.

.. |airplane1| image:: images/AirplaneStep1.jpg
.. |airplane2| image:: images/AirplaneStep2.jpg

+------------------------------------------------+---------------------+
| Step                                           | Image               |
+================================================+=====================+
| 1. On the main Android screen of each          | |airplane1|         |
| smartphone, use your finger to slide from the  |                     |
| top of the screen down towards the bottom of   |                     |
| the screen to display the quick configuration  |                     |
| screen.Note that for some smartphones you      |                     |
| might have to swipe down more than once to     |                     |
| display the quick configuration screen,        |                     |
| particularly if there are messages or          |                     |
| notifications displayed at the top of your     |                     |
| screen.Look for the Airplane mode icon (which  |                     |
| is shaped like an airplane) and if the icon is |                     |
| not activated, touch the icon to put the phone |                     |
| into airplane mode.                            |                     |
+------------------------------------------------+---------------------+
| 2. Placing the phone into airplane mode will   | |airplane2|         |
| turn off the Wi-Fi radio. If the Wi-Fi icon    |                     |
| has a diagonal line through it (see Step 1     |                     |
| above), then the Wi-Fi radio is disabled. You  |                     |
| will need to touch the **Wi-Fi** icon on the   |                     |
| quick configuration screen to turn the Wi-Fi   |                     |
| radio back on.                                 |                     |
+------------------------------------------------+---------------------+

Pairing the Driver Station to the Robot Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _control-hub-users-1:

Control Hub Pairing
^^^^^^^^^^^^^^^^^^^

The REV Robotics Control Hub should come with the Robot Controller app
pre-installed. Once you have successfully installed the Driver
Station on an Android phone, you will want to establish a secure
wireless connection between the Control Hub and the Driver Station. This
connection will allow your Driver Station phone to select op modes on
your Robot Controller and send gamepad input to these programs.
Likewise, it will allow your op modes running on your Robot Controller
to send telemetry data to your Driver Station phone where it can be
displayed for your drivers. The process to connect the two devices is
known as "pairing."

.. note:: the Control Hub does not have its own internal battery. Before you
   can connect a Driver Station to the Control Hub, you must connect the
   Control Hub to a 12V battery.

Also note that it will take an estimated 10 minutes to complete this
task.

.. |pairing1| image:: images/PairingControlHubStep1.jpg
.. |pairing2| image:: images/PairingControlHubStep2.jpg
.. |pairing3| image:: images/PairingControlHubStep3.jpg
.. |pairing4| image:: images/PairingControlHubStep4.jpg
.. |pairing5| image:: images/PairingControlHubStep5.jpg
.. |pairing6| image:: images/PairingControlHubStep6.jpg
.. |pairing7| image:: images/PairingControlHubStep7.jpg
.. |pairing8| image:: images/PairingControlHubStep8.jpg
.. |pairing9| image:: images/PairingControlHubStep9.jpg
.. |pairing10| image:: images/PairingControlHubStep10.jpg
.. |pairing11| image:: images/PairingControlHubStep11.jpg
.. |pairing12| image:: images/PairingControlHubStep12.jpg
.. |pairing13| image:: images/PairingControlHubStep13.jpg

+------------------------------------------------+---------------------+
| Step                                           | Image               |
+================================================+=====================+
| 1. Connect an approved 12V battery to the      | |pairing1|          |
| power switch (REV-31-1387) and make sure the   |                     |
| switch is in the off position. Connect the     |                     |
| switch to an XT30 port on the Control Hub and  |                     |
| turn the switch on. The LED should initially   |                     |
| be blue on the Control Hub.                    |                     |
+------------------------------------------------+---------------------+
| 2. It takes approximately 18 seconds for the   | |pairing2|          |
| Control Hub to power on. The Control Hub is    |                     |
| ready to pair with the Driver Station when the |                     |
| LED turns green. Note: the light blinks blue   |                     |
| every ~5 seconds to indicate that the Control  |                     |
| Hub is healthy.                                |                     |
+------------------------------------------------+---------------------+
| 3. On the Driver Station device, browse the    | |pairing3|          |
| available apps and locate the **Driver         |                     |
| Station** icon. Tap on the icon to launch the  |                     |
| Driver Station app. Note that the first time   |                     |
| you launch the app your Android device might   |                     |
| prompt you for permissions that the app will   |                     |
| need to run properly. Whenever prompted, press |                     |
| **Allow** to grant the requested permission.   |                     |
+------------------------------------------------+---------------------+
| 4. Touch the three vertical dots on the upper  | |pairing4|          |
| right hand corner of the main screen of the    |                     |
| Driver Station app. This will launch a         |                     |
| pop-up menu.                                   |                     |
+------------------------------------------------+---------------------+
| 5. Select **Settings** from the pop-up menu.   | |pairing5|          |
|                                                |                     |
|                                                |                     |
|                                                |                     |
+------------------------------------------------+---------------------+
| 6. From the **Settings** screen, look for and  | |pairing6|          |
| select \ **Pairing Method** to launch the      |                     |
| **Pairing** \ **Method** screen.               |                     |
|                                                |                     |
+------------------------------------------------+---------------------+
| 7. Touch the words **Control Hub** to indicate | |pairing7|          |
| that this Driver Station will be pairing with  |                     |
| a Control Hub.                                 |                     |
|                                                |                     |
+------------------------------------------------+---------------------+
| 8. From the **Settings** screen, look for and  | |pairing8|          |
| select \ **Pair with Robot Controller** to     |                     |
| launch the **Pair** \ **with Robot             |                     |
| Controller** screen.                           |                     |
+------------------------------------------------+---------------------+
| 9. From **Pair with Robot Controller** screen, | |pairing9|          |
| look for and press the **Wifi Settings**       |                     |
| button to launch the device's Android Wifi     |                     |
| Settings screen.                               |                     |
+------------------------------------------------+---------------------+
| 10. Find the name of your Control Hub's        | |pairing10|         |
| wireless network from the list of available    |                     |
| WiFi networks. Click on the network name to    |                     |
| select the network. If this is the first time  |                     |
| you are connecting to the Control Hub, then    |                     |
| the default network name should begin with the |                     |
| prefix FTC- (FTC-1Ybr in this example).        |                     |
| The default network name should be listed on a |                     |
| sticker attached to the bottom side of the     |                     |
| Control Hub.                                   |                     |
+------------------------------------------------+---------------------+
| 11. When prompted, specify the password for    | |pairing11|         |
| the Control Hub's WiFi network and press       |                     |
| \ **Connect** to connect to the Hub. Note that |                     |
| the default password for the Control Hub       |                     |
| network is password. Also note that when you   |                     |
| connect to the Control Hub's WiFi network      |                     |
| successfully, the Driver Station will not have |                     |
| access to the Internet.                        |                     |
+------------------------------------------------+---------------------+
| 12. After you successfully connected to the    | |pairing12|         |
| Hub, use the back arrow to navigate to the     |                     |
| previous screen. You should see the name of    |                     |
| the WiFi network listed under "Current Robot   |                     |
| Controller:". Use the back-arrow key to return |                     |
| to the Settings screen. Then press the         |                     |
| back-arrow key one more time to return to the  |                     |
| main Driver Station screen.                    |                     |
+------------------------------------------------+---------------------+
| 13. Verify that the Driver Station screen has  | |pairing13|         |
| changed and that it now indicates that it is   |                     |
| connected to the Control Hub.The name of the   |                     |
| Control Hub's WiFi network (FTC-1Ybr in this   |                     |
| example) should be displayed in the Network    |                     |
| field on the Driver Station.                   |                     |
+------------------------------------------------+---------------------+

.. _users-with-two-android-smartphones-1:

Two Android Smartphone Pairing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. important:: If your Driver Station was previously paired to a
   Control Hub, and you currently would like to connect to an Android
   smartphone Robot Controller, then before attempting to pair to the Robot
   Controller, you should forget the Wi-Fi network for the previous Control
   Hub (using the Android Wifi Settings screen on the Driver Station) and
   then power cycle the Driver Station phone. If the previous Control Hub
   is powered on and if you haven't forgotten this network, then the Driver
   Station might try and connect to the Control Hub and might be unable to
   connect to the Robot Controller smartphone.

Once you have successfully installed the apps onto your Android
phones, you will want to establish a secure wireless connection between
the two devices. This connection will allow your Driver Station phone to
select op modes on your Robot Controller phone and send gamepad input to
these programs. Likewise, it will allow your op modes running on your
Robot Controller phone to send telemetry data to your Driver Station
phone where it can be displayed for your drivers. The process to connect
the two phones is known as pairing.

Note that it will take an estimated 10 minutes to complete this task.

.. |pairingns1| image:: images/PairingNewStep1.jpg
.. |pairingns1b| image:: images/PairingNewStep1b.jpg
.. |pairingns2| image:: images/PairingNewStep1.jpg
.. |pairingns3| image:: images/PairingNewStep3.jpg
.. |pairingns3b| image:: images/PairingNewStep3b.jpg
.. |pairingns4| image:: images/PairingNewStep4.jpg
.. |pairingns5| image:: images/PairingNewStep5.jpg
.. |pairingns6| image:: images/PairingNewStep6.jpg
.. |pairingns7| image:: images/PairingNewStep7.jpg
.. |pairingns8| image:: images/PairingNewStep8.jpg
.. |pairingns9| image:: images/PairingNewStep9.jpg
.. |pairingns10| image:: images/PairingNewStep10.jpg
.. |pairingns11| image:: images/PairingNewStep11.jpg
.. |pairingns12| image:: images/PairingNewStep12.jpg

+------------------------------------------------+---------------------+
| Step                                           | Image               |
+================================================+=====================+
| 1. On the Robot Controller device, browse the  | |pairingns1|        |
| available apps and locate the **Robot          | |pairingns1b|       |
| Controller** icon. Tap on the icon to launch   |                     |
| the Robot Controller app. Note that the first  |                     |
| time you launch the app your Android device    |                     |
| might prompt you for permissions that the app  |                     |
| will need to run properly. Whenever prompted,  |                     |
| press **Allow** to grant the requested         |                     |
| permission.                                    |                     |
+------------------------------------------------+---------------------+
| 2. Verify that the Robot Controller app is     | |pairingns2|        |
| running. The **Robot Status** field should     |                     |
| read running if it is working properly.        |                     |
|                                                |                     |
+------------------------------------------------+---------------------+
| 3. On the Driver Station device, browse the    | |pairingns3|        |
| available apps and locate the **Driver         | |pairingns3b|       |
| Station** icon. Tap on the icon to launch the  |                     |
| Driver Station app. Note that the first time   |                     |
| you launch the app your Android device might   |                     |
| prompt you for permissions that the app will   |                     |
| need to run properly. Whenever prompted, press |                     |
| **Allow** to grant the requested permission.   |                     |
+------------------------------------------------+---------------------+
| 4. Touch the three vertical dots on the upper  | |pairingns4|        |
| right hand corner of the main screen of the    |                     |
| Driver Station app. This will launch a         |                     |
| pop-up menu.                                   |                     |
+------------------------------------------------+---------------------+
| 5. Select **Settings** from the pop-up menu.   | |pairingns5|        |
|                                                |                     |
|                                                |                     |
|                                                |                     |
+------------------------------------------------+---------------------+
| 6. From the **Settings** screen, look for and  | |pairingns6|        |
| select \ **Pairing Method** to launch the      |                     |
| **Pairing** \ **Method** screen.               |                     |
|                                                |                     |
+------------------------------------------------+---------------------+
| 7. Verify that the **Wifi Direct** mode is     | |pairingns7|        |
| selected, which means that this Driver Station |                     |
| will be pairing with another Android device.   |                     |
|                                                |                     |
+------------------------------------------------+---------------------+
| 8. From the **Settings** screen, look for and  | |pairingns8|        |
| select \ **Pair with Robot Controller** to     |                     |
| launch the **Pair**\ \ **with Robot            |                     |
| Controller** screen.                           |                     |
+------------------------------------------------+---------------------+
| 9. Find the name of your Robot Controller from | |pairingns9|        |
| the list and select it.After you have made     |                     |
| your selection, use the back-arrow key to      |                     |
| return to the Settings screen.Then press the   |                     |
| back-arrow key one more time to return to the  |                     |
| main Driver Station screen.                    |                     |
+------------------------------------------------+---------------------+
| 10. When the Driver Station returns to its     | |pairingns10|       |
| main screen, the first time you attempt to     |                     |
| connect to the Robot Controller a prompt       |                     |
| should appear on the Robot Controller          |                     |
| screen.Click on the **ACCEPT** button to       |                     |
| accept the connection request from the Driver  |                     |
| Station.                                       |                     |
+------------------------------------------------+---------------------+
| 11. Verify that the Driver Station screen has  | |pairingns11|       |
| changed and that it now indicates that it is   |                     |
| connected to the Robot Controller.The name of  |                     |
| the Robot Controller's remote network          |                     |
| (9999-C-RC in this example) should be          |                     |
| displayed in the Network field on the Driver   |                     |
| Station.                                       |                     |
+------------------------------------------------+---------------------+
| 12. Verify that the Robot Controller screen    | |pairingns12|       |
| has changed and that it now indicates that it  |                     |
| is connected to the Driver Station.The Network |                     |
| status should read active, connected on the    |                     |
| Robot Controller's main screen.                |                     |
+------------------------------------------------+---------------------+

