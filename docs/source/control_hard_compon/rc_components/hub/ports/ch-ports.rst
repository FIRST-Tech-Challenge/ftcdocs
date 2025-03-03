Control Hub Ports
=================

.. figure:: images/CH-HUB.png
    :alt: REV Control Hub

    Part number REV-31-1595

.. include:: std-ports.rst


.. figure:: images/CH-HUB-FRONT.png
    :alt: The ports from left to right are: USB 2.0, USB 3.0, USB C, USB Mini (below the USB C port),  HDMI, and Micro SD.

    Control Hub Front Ports


USB 2.0 Port
------------

This is a female USB A port that can be used for connecting USB devices as allowed for in the Competition Manual.

.. warning:: An ESD event on the USB 2.0 port on the Control Hub can cause Wi-Fi disconnects.

   The REV Control Hub has a 
   `known ESD issue <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/troubleshooting-the-control-system#esd-mitigation-techniques>`_
   with devices plugged into the USB 2.0 port. 
   Using the USB 2.0 Port may cause ESD to affect your Control Hub's Wi-Fi Chip (causing Wi-Fi disconnects with the driver hub). 
   Ensure that you plug USB devices, such as a Camera, into the USB 3.0 Port on your Control Hub. 

USB 3.0 Port

This is a female USB A port that is primarily used for connecting USB video device class (UVC) cameras (webcams).

USB-C Port
----------

A Control Hub has a USB-C port. This is primarily used for connecting to a
laptop for loading the SDK but can also be used with a UVC Camera.

Mini-USB Port
-------------

This is a female USB Mini-B port is used only to communicate directly to
the I/O system. In this case, it is only for the purpose of uploading firmware
to the device.

HDMI
-----

The Control Hub lacks a display of its own even though it is a fully-fledged
Android device. The Control Hub has an HDMI port that provides video output for
the device; this HDMI port can be used to connect to an external display.

Micro SD
--------

This is a port for a Micro SD memory card. It is not normally used.