Control Hub Ports
=================

.. figure:: images/CH-HUB.png
    :alt: REV Control Hub

    Part number REV-31-1595

.. include:: std-ports.rst


.. figure:: images/CH-HUB-FRONT.png
    :alt: The ports from left to right are: USB 2.0, USB 3.0, USB C, USB Mini (below the USB C port),  HDMI, and Micro SD.

    Control Hub Front Ports

USB Ports
---------

Universal Serial Bus (USB) is an industry standard that allows data exchange and delivery of power between many types of electronics.
The control hub has four USB ports described below. 

USB 2.0 and USB 3.0 refer to the USB specifications that relate to data exchange rate and power delivery.

USB Type-A and USB-C and USB Mini-B refer to the type of connector. 

- USB Type-A is a larger rectangular connector.
- USB-C is a smaller oval connector.
- USB Mini-B is a smaller rectagular connector with a beveled edge.

USB 2.0
^^^^^^^

This is a female USB Type-A port that implements USB 2.0 and can be used for connecting USB devices as allowed for in the Competition Manual.

.. warning:: An ESD event on the USB 2.0 port on the Control Hub can cause Wi-Fi disconnects.

   The REV Control Hub has a 
   `known ESD issue <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/troubleshooting-the-control-system#esd-mitigation-techniques>`_
   with devices plugged into the USB 2.0 port. 
   Using the USB 2.0 Port may cause ESD to affect your Control Hub's Wi-Fi Chip (causing Wi-Fi disconnects with the driver hub). 
   Ensure that you plug USB devices, such as a Camera, into the USB 3.0 Port on your Control Hub. 

USB 3.0
^^^^^^^

This is a female USB Type-A port that implements USB 3.0 and is primarily used for connecting USB video device class (UVC) cameras (webcams).

USB C
^^^^^

A Control Hub has a female USB-C port that implements USB 2.0. This is primarily used for connecting to a
laptop for loading the SDK but can also be used with a UVC Camera.

MINI USB
^^^^^^^^

This is a female USB Mini-B port that implements USB 2.0. Iis used only to communicate directly to
the I/O system. In this case, it is only for the purpose of uploading firmware
to the device.

HDMI
-----

The Control Hub lacks a display of its own even though it is a fully-fledged
Android device. The Control Hub has an HDMI port that provides video output for
the device; this HDMI port can be used to connect to an external display.

MICRO SD
--------

This is a port for a Micro SD memory card. It is not normally used.
