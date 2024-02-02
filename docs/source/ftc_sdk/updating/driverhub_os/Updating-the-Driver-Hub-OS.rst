Updating the Driver Hub OS
==========================

An Operating System (OS) is software that supports a computer’s basic
functions, such as scheduling tasks, executing applications, and
controlling peripherals. This must sometimes be updated on the **REV
Driver Hub**. While this OS update is not specifically part of the 
:doc:`Software Development Kit (SDK) </ftc_sdk/overview/index>`, the SDK requires
these updates for the Driver Hub in order to perform correctly.

Here are two methods for updating the Driver Hub OS: 

1. REV Hardware Client (RHC) 
2. Software Manager on Driver Hub

More info about updating the Driver Hub OS is
`at REV Robotics’ excellent documentation site <https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-the-driver-hub>`__.

.. dropdown:: Method 1 - REV Hardware Client (RHC) - Windows computers only

   1. Turn on the Driver Hub. Plug it directly into a computer running the
      REV Hardware Client, with a USB-C data cable.

   2. Click the Driver Hub’s large icon/rectangle. Under “Driver Hub
      Operating System”, see the current/latest mismatch, if any (yellow
      oval, below).

      .. figure:: images/600-RHC-DH-OS.png
         :alt: Updating the Driver Hub OS
         :width: 80%
         :align: center

         Updating the Driver Hub OS

      Confirm the Latest Version in the drop-down menu, if any. Then click the
      blue rectangle, labeled “Update” when applicable. The speed of this
      update is improved, since       
      :doc:`in Updating the REV Hardware Client 
      </ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client>`
      the required update file was previously downloaded.


   Done! The Driver Hub’s OS is now updated.

.. dropdown:: Method 2 - Software Manager

   The REV Driver Hub has a built-in app called the Software Manager, which
   can automatically update the Driver Hub OS (and other related
   software). It requires only an internet connection.

   1. Close all apps, and open the Driver Hub’s Wi-Fi menu (in Settings, or
      swipe down twice from top of home screen). Temporarily connect the
      Driver Hub to the internet via Wi-Fi.

   2. Open the Software Manager app at the Driver Hub home screen (left
      image, below).

      .. figure:: images/910-DH-double.png
         :alt: Updating the Software Manager
         :width: 80%
         :align: center

         Updating the Software Manager

   3. The Software Manager will automatically check for any updates needed,
      and display the results (right image, above). Touch the grey button
      to perform the updates, including the Driver Hub Operating System
      (OS) if needed.

      .. note:: 
         While REV Robotics does provide a downloadable OS image file for the
         Driver Hub, the tools available in this tutorial do not accept providing
         this file for updating the OS.

   4. When all is complete, “Forget” the Wi-Fi network used for internet
      access. Now the Driver Hub is ready for regular competition use.

Questions, comments and corrections to westsiderobotics@verizon.net

