Updating the Control Hub OS
===========================

An Operating System (OS) is software that supports a computer’s basic
functions, such as scheduling tasks, executing applications, and
controlling peripherals. This must sometimes be updated on the **REV
Control Hub**. While this OS update is not specifically part of the
:doc:`Software Development Kit (SDK) <../index>`, the SDK requires
these updates for the Control Hub in order to perform correctly.

Here are two methods for updating the Control Hub OS: 

1. REV Hardware Client (RHC) 
2. Manage page on computer

More info about updating the Control Hub OS is
`at REV Robotics’ excellent documentation site <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-operating-system>`__.

.. dropdown:: Method 1 - REV Hardware Client (RHC) - Windows computers only

   1. Apply 12V robot power to the REV Control Hub.

   2. Plug the Control Hub directly into a computer running the REV
      Hardware Client, with a USB-C data cable.

   3. Click the hub’s large icon/rectangle. Under “Control Hub Operating
      System”, see the current/latest mismatch, if any (yellow oval,
      below).

      .. figure:: images/650-RHC-OS.png
         :alt: Updating the Control Hub OS
         :width: 80%
         :align: center

         Updating the Control Hub OS

   Confirm the Latest Version in the drop-down menu, then click the blue
   “Update” rectangle (green arrow, above). The speed of this update is
   improved, since    :doc:`in Updating the REV Hardware Client
   </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
   the required update file was previously downloaded.

   Done! The Control Hub’s OS is now updated.

.. dropdown:: Method 2 - Manage page on computer

   1. Connect the computer via Wi-Fi to the Control Hub. In the Chrome
      browser, open the FTC interface.

   2. Click on the Manage tab, scroll down to Update Control Hub Operating
      System.

      .. figure:: images/700-manage-OS.png
         :alt: Updating the Control Hub OS
         :width: 80%
         :align: center

         Updating the Control Hub OS

   3. If needed, download the latest OS file from the REV Robotics `Control
      Hub OS web
      page <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-operating-system#using-the-robot-controller-console>`__.
      Do not extract or “un-zip” this file.

   4. At the Manage page, click “Select Update File…” and navigate to the
      computer’s folder where you downloaded the OS file.

   5. Select that file, and click “Update & Reboot” (green arrow, above).

   That’s it! The Control Hub’s OS is now updated.
   
Questions, comments and corrections to westsiderobotics@verizon.net

