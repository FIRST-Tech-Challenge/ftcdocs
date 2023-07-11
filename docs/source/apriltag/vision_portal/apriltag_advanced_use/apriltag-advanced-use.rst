AprilTag Advanced Use
=====================

Overview
--------

This page will offer tips for FTC teams seeking more info about
specialized features of the new VisionPortal.

Optional Metadata
-----------------

An AprilTag Library tag can store two optional **Metadata** fields (of
these Blocks/Java types): 

- ``fieldPosition``: tag location on the game field (``VectorF``) 
- ``fieldOrientation``: tag orientation on the game field (``Quaternion``)

The reference frame is the FTC **Field Coordinate System**, provided here:

- https://ftc-docs.firstinspires.org/en/latest/field-coordinate-system

Here is a simple graphic showing the FTC global axes that apply to
**every game, every season**:

.. figure:: images/FTC-Global-Coordinates.png
   :width: 75%
   :align: center
   :alt: Field Coordinates

   Image Credit: Phil Malone

With a tag’s **field position** and **orientation** specified in advance
as Metadata, the tag’s pose data could be used by an advanced OpMode to
calculate the robot’s position on the field. This conversion math, an
exercise for the FTC team, can allow a robot to use the tag’s pose data
in real-time to navigate to the desired location on the field.

Raw Pose Values
---------------

The frame of reference described at the **AprilTag Reference Frame**
page is provided **by default** in the new 8.2 SDK.

Advanced teams may prefer to perform their own pose calculations, based
on **raw values** from the AprilTag/EasyOpenCV pipeline.

Those raw values are available to Java and Blocks programmers. The Java
version is shown here:

.. code:: java

   for (AprilTagDetection detection : aprilTag.getDetections())  {

        Orientation rot = Orientation.getOrientation(detection.rawPose.R, AxesReference.INTRINSIC, AxesOrder.XYZ, AngleUnit.DEGREES);

        // Original source data
        double poseX = detection.rawPose.x;
        double poseY = detection.rawPose.y;
        double poseZ = detection.rawPose.z;

        double poseAX = rot.firstAngle;
        double poseAY = rot.secondAngle;
        double poseAZ = rot.thirdAngle;
        }

These raw values are converted by the SDK to the default interface, as
follows:

.. code:: java

   if (detection.rawPose != null)   {
        detection.ftcPose = new AprilTagPoseFtc();

        detection.ftcPose.x =  detection.rawPose.x;
        detection.ftcPose.y =  detection.rawPose.z;
        detection.ftcPose.z = -detection.rawPose.y;

        Orientation rot = Orientation.getOrientation(detection.rawPose.R, AxesReference.INTRINSIC, AxesOrder.YXZ, outputUnitsAngle);
        detection.ftcPose.yaw = -rot.firstAngle;
        detection.ftcPose.roll = rot.thirdAngle;
        detection.ftcPose.pitch = rot.secondAngle;

        detection.ftcPose.range = Math.hypot(detection.ftcPose.x, detection.ftcPose.y);
        detection.ftcPose.bearing = outputUnitsAngle.fromUnit(AngleUnit.RADIANS, Math.atan2(-detection.ftcPose.x, detection.ftcPose.y));
        detection.ftcPose.elevation = outputUnitsAngle.fromUnit(AngleUnit.RADIANS, Math.atan2(detection.ftcPose.z, detection.ftcPose.y));
        }

Further discussion is provided here:

- https://ftc-docs.firstinspires.org/apriltag-detection-values

====

*Questions, comments and corrections to westsiderobotics@verizon.net*

