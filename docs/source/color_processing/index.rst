Color Processing Introduction
===============================

Overview
--------

The *FIRST* Tech Challenge SDK software (as of v10.1) includes some **Color
Processing** features from OpenCV, a popular and powerful open-source library
for vision processing.

Introduced with INTO THE DEEP, these new features will help *FIRST* Tech Challenge teams
**identify colors** and **process color blobs**\ , useful in any game requiring
color and shape recognition.

Here's the outline of this tutorial's main pages:

.. toctree::
   :maxdepth: 1
   :titlesonly:

   color-sensor/color-sensor
   color-blob-concepts/color-blob-concepts
   color-locator-discover/color-locator-discover 
   color-locator-explore/color-locator-explore
   color-locator-challenge/color-locator-challenge
   color-locator-round-blobs/color-locator-round-blobs
   color-spaces/color-spaces

Much credit to developer and :term:`Sample OpMode` author `@gearsincorg <https://github.com/gearsincorg>`_, :term:`EasyOpenCV` developer `@Windwoes <https://github.com/Windwoes>`_, FTC :term:`Blocks` developer `@lizlooney <https://github.com/lizlooney>`_, and the open-source team at `OpenCV <https://opencv.org/>`_.

Compatibility
-------------

This new software includes two Color Processors, each compatible with the FTC
:term:`VisionPortal` introduced in 2023.  These processors can run alongside an
:term:`AprilTag` processor, and replace the :term:`TensorFlow` processor (removed in 2024).

These new processors can be used on the usual FTC cameras:

* any UVC-compatible :term:`webcam <Webcam>`
* the built-in camera of an FTC-supported Android phone (as :term:`Robot Controller`)

This does **not** include vision :term:`sensors <Sensor>` such as HuskyLens and LimeLight 3A,
which do not use the FTC VisionPortal.

Two Processors
--------------

The new software includes these processors:

* **Color Sensor** - detects the color of a specified zone in the camera's
  view
* **Color Locator** - gives detailed info on clusters of a specified color,
  in a specified zone

This tutorial has a :doc:`Color Sensor <color-sensor/color-sensor>` page, showing how
to use the Sample :term:`OpMode` called ``ConceptVisionColorSensor``.

For the **Color Locator** processor, the color "clusters" are called **Blobs**.
As listed above, this tutorial offers one page on Color Blob Concepts, and
four pages covering the Sample OpModes called ``ConceptVisionColorLocator_Rectangle`` 
and ``ConceptVisionColorLocator_Circle``.

The Sample OpModes are available in **FTC Blocks**\ , and in **Java** for use
in :term:`OnBot Java` or :term:`Android Studio`.  Each programming section of this tutorial has
a Blocks tab and a Java tab.

Next Steps
----------

Time to get started!

Following this tutorial in order, first try the Sample OpModes for :doc:`Color
Sensor <color-sensor/color-sensor>`.

Then read about **Color Blob Concepts**\ , and try the **Color Locator** Sample
OpModes.

Soon you'll be ready to add one or both features to your :term:`Autonomous` OpModes --
perhaps even to help automate your :term:`TeleOp <TELEOP>`!

============

Questions, comments and corrections to westsiderobotics@verizon.net


