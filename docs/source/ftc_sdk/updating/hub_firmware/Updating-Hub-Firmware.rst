Updating Hub Firmware
=====================

Firmware is low-level software that controls a device’s circuit boards, or
electronic **hardware**. This must sometimes be updated on the REV Expansion
Hub and the REV Control Hub in order for the :doc:`Software Development Kit
(SDK) </ftc_sdk/overview/index>` to perform correctly.

Here are 5 methods: 

1. REV Hardware Client (RHC) 
2. Driver Station app
3. Robot Controller (RC) app - on RC phone 
4. Manage page on computer 
5. Manage page on Driver Station device (DS phone or Driver Hub)

.. dropdown:: Method 1 - REV Hardware Client (RHC) - Windows computers only

   1. For REV Control Hub, apply 12V robot power. For REV Expansion Hub,
      12V power is optional.

   2. Plug the REV Hub directly into a computer running the REV Hardware
      Client, with a USB data cable (not charge-only). The Expansion Hub’s
      port is Mini USB (not micro). On the Control Hub, use only the USB-C
      port, not its Mini USB port.

   3. Click the hub’s large icon/rectangle. Under “Expansion/Control Hub
      Firmware”, see the current/latest mismatch, if any (yellow oval,
      below).

      .. figure:: images/350-RHC-EH-firmware.png
         :alt: Updating Firmware
         :width: 80%
         :align: center

         Updating Firmware

      Here’s an example with Control Hub:

      .. figure:: images/400-RHC-EH-CH-firmware.png
         :alt: Updating Firmware
         :width: 80%
         :align: center

         Updating Firmware

      Confirm the Latest Version in the drop-down menu, then click the blue
      “Re-install” rectangle (green arrow, above). This is done quickly, since
      :doc:`in Updating the REV Hardware Client 
      </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
      the required update file was previously downloaded.

      Done! The Hub’s firmware is now updated.

   More info about using the RHC to update Hub firmware is `at REV Robotics’ excellent documentation site <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware>`__.

.. dropdown:: Method 2 - Driver Station app

   This method applies to any DS app, running on a DS phone or a Driver
   Hub.

   1. For REV Control Hub, apply 12V robot power. For REV Expansion Hub,
      connect directly to Robot Controller (RC) phone, open RC app, **and**
      apply 12V power. The Expansion Hub being updated must be **plugged
      directly** into the RC phone, with no intermediate Control Hub or
      other (primary) Expansion Hub. After updating you can return that Hub
      to its secondary position, if needed.

   2. Connect/pair the DS app to the RC device, from a DS phone or Driver
      Hub. Select DS Settings, Advanced (Robot Controller) Settings, REV
      Hub Firmware Update.

      .. figure:: images/150-DS-firmware-double.png
         :alt: Updating Firmware
         :width: 80%
         :align: center

         Updating Firmware

      Review the list of available Hub firmware, whether stored on the RC
      device and/or “bundled” in the app.

   3. If the latest does **not** appear on the list, you can transfer the
      firmware file from a computer to the Robot Controller. Use a USB data
      cable (not a charge-only cable) to store the firmware file in the RC
      device’s subfolder called FIRST/updates/Expansion Hub Firmware.

      Current and older firmware files can be found at the 
      `REV Robotics website <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware/firmware-changelog>`__.

      Then return to this list of available firmware.

   4. Now select the latest firmware version and touch “Update Hub
      Firmware” (green arrow, above). Wait for the process to finish; do
      not unplug the Hub or restart the robot.

   That’s it! The Hub’s firmware is now updated.

.. dropdown:: Method 3 - Robot Controller (RC) app - on RC phone

   This method is **exactly the same** as Method #2 immediately above,
   since the DS app was simply providing a portal or window to the RC app.

   It’s listed separately here, because it applies only to **Expansion
   Hub**, not Control Hub – which doesn’t use an RC phone. In other words,
   users do not normally interface directly with the RC app on a Control
   Hub.

   Again, the Expansion Hub must be plugged **directly** into an RC phone,
   with no intermediate (primary) Expansion Hub. After updating you can
   return that Hub to its secondary position, if needed.

.. dropdown:: Method 4 - Manage page on computer

   1. Connect the computer via Wi-Fi to the Control Hub or RC phone. In the
      Chrome browser, open the Manage interface.

   2. Click on the Manage tab, scroll down to Update REV Hub Firmware.

      .. figure:: images/250-manage-firmware.png
         :alt: Updating Firmware
         :width: 80%
         :align: center

         Updating Firmware

      See if the grey box (see green arrow, above) offers the latest firmware
      version, included or bundled with the RC app.

   3. If not, click the “Select Firmware…” box. Navigate to the desired
      firmware file stored on the computer, and select it.

      As part of the update process, that selected firmware file will be
      stored on the Control Hub or RC phone, in a subfolder called
      FIRST/updates/Expansion Hub Firmware.

      Current and older firmware files can be found at the       
      `REV Robotics website <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware/firmware-changelog>`__.

   4. Now click the box called “Update to…” or “Update using…” (see green
      arrow, above).

      .. figure:: images/255-manage-firmware-confirm.png
         :alt: Managing Firmware
         :width: 80%
         :align: center

         Managing Firmware

   5. At the confirmation prompt, click the blue box “Update Hub Firmware”.
      Wait for the process to finish; do not unplug the Hub or restart the
      robot.

   That’s it! The Hub’s firmware is now updated.

.. dropdown:: Method 5 - Manage page on Driver Station device - DS phone or Driver Hub

   1. Connect the DS app to the Control Hub or RC phone, from the DS app’s
      Settings menu (never with the Android device Wi-Fi settings).

   2. From the DS app’s menu, select “Program and Manage”. Then touch the 3
      bars at top right, and select “Manage”.

      This is the same Manage page that appears in a laptop browser. So the
      following instructions are similar to Method 4 above.

   3. Scroll down to Update REV Hub Firmware.

      .. figure:: images/270-manage-firmware-DS-CH-landscape.png
         :alt: Update Hub Firmware
         :width: 80%
         :align: center

         Update Hub Firmware

      See if the grey box “Update to…” offers the latest firmware version,
      included or bundled with the DS app.

   3. If not, you can transfer the desired firmware file to the **Driver
      Station device**.

      Yes, that’s correct: transfer to the DS device, not to the RC device.
      This Method 5 uses a local file on the DS device, while Methods 2 and 3
      (above) use a local file on the RC device.

      Use a USB data cable (not a charge-only cable) to store the firmware
      file in the DS device’s Downloads folder.

      Current and older firmware files can be found at the REV Robotics
      website
      `here <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-firmware/firmware-changelog>`__.

      Then click the “Select Firmware…” box. Navigate to the DS device’s
      Downloads folder, and select the desired firmware file.

   4. Now click the box called “Update to…” or “Update using…” (second
      green arrow, above).

      .. figure:: images/257-manage-firmware-confirm-DS.png
         :alt: Update Hub Firmware
         :width: 80%
         :align: center

         Update Hub Firmware

   5. At the confirmation prompt, scroll down and click the blue box
      “Update Hub Firmware”. Wait for the process to finish; do not unplug
      the Hub or restart the robot.

   That’s it! The Hub’s firmware is now updated.

Questions, comments and corrections to westsiderobotics@verizon.net

