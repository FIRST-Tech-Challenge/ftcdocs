Sample OpModes
--------------

The intent of this tutorial is to describe the available webcam
controls, allowing programmers to **develop their own solutions** guided
by the SDK API (Javadoc).

Rather than reproduce sample code here, this page points to the OpModes in
the `FtcRobotController repository
<https://github.com/FIRST-Tech-Challenge/FtcRobotController/tree/master/FtcRobotController/src/main/java/org/firstinspires/ftc/robotcontroller/external/samples>`__,
which are maintained alongside the SDK and updated each season. The same
samples are available in Android Studio and OnBot Java, under
``FtcRobotController/external/samples``.

Exposure and Gain
~~~~~~~~~~~~~~~~~

`ConceptAprilTagOptimizeExposure.java
<https://github.com/FIRST-Tech-Challenge/FtcRobotController/blob/master/FtcRobotController/src/main/java/org/firstinspires/ftc/robotcontroller/external/samples/ConceptAprilTagOptimizeExposure.java>`__
is the SDK's camera controls sample. It builds a VisionPortal with an
AprilTag Processor, then asks the Portal for its control objects:

.. code:: java

   ExposureControl myExposureControl = visionPortal.getCameraControl(ExposureControl.class);
   GainControl myGainControl = visionPortal.getCameraControl(GainControl.class);

The gamepad bumpers and triggers raise and lower exposure and gain, while
telemetry reports the tags currently detected. Its goal is to find the
**shortest exposure** that still gives reliable detection, since a short
exposure reduces motion blur while the robot is driving.

That sample is also a reasonable starting point for the other controls
described in this tutorial. ``FocusControl``, ``WhiteBalanceControl`` and
``PtzControl`` are all requested from the Portal in exactly the same way.

Focus, White Balance and PTZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SDK does not ship a sample for these three controls. The
:ref:`VisionPortal Camera Controls
<apriltag/vision_portal/visionportal_camera_controls/visionportal-camera-controls:other test opmodes>`
page links Blocks test OpModes covering Focus, Pan/Tilt/Zoom and White
Balance. For Java versions, click ``Export to Java`` in the Blocks editing
interface.
