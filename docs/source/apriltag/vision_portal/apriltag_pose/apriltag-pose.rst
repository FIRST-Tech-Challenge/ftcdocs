AprilTag Pose
=============

The SDK can evaluate a **flat AprilTag** (not curved) to estimate **pose**, the
combination of:

- relative position **from the camera lens center to the AprilTag center**, and
- orientation of the AprilTag **in the camera's reference frame**

As described at the previous page **FTC Reference Frame**, position is
expressed as (X, Y, Z).  Orientation is expressed as rotation about (X, Y, Z),
called Pitch, Roll and Yaw respectively.

The tag must be in the Library, which ensures that tag size (with units) is
defined.  Estimating pose requires knowing the tag size.

As demonstrated in the Sample OpModes, here are ways to retrieve the estimated
pose values.

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      .. figure:: images/Blocks-pose-oval.png
         :width: 75%
         :align: center
         :alt: AprilTag Pose Blocks

         AprilTag Pose Blocks

      Use each of these green Blocks to pass a Pose value to a Telemetry Block, or to a Variable:

   .. tab-item:: Java
      :sync: java

      Use these `ftcPose` fields for Telemetry, or assign to a Variable:

      .. code-block:: java

         AprilTagDetection myAprilTagDetection;
         double myTagPoseX = myAprilTagDetection.ftcPose.x;
         double myTagPoseY = myAprilTagDetection.ftcPose.y;
         double myTagPoseZ = myAprilTagDetection.ftcPose.z;
         double myTagPosePitch = myAprilTagDetection.ftcPose.pitch;
         double myTagPoseRoll = myAprilTagDetection.ftcPose.roll;
         double myTagPoseYaw = myAprilTagDetection.ftcPose.yaw;

*The SDK terms for Pitch, Roll and Yaw are* **not the same** *as the native
AprilTag terms, due to the FTC reference frame.*

Teams may find it helpful to use a **calculated extension** of the basic pose,
with these terms:

- **Range**, direct (point-to-point) distance to the tag center
- **Bearing**, the angle the camera must turn (left/right) to point directly at the tag center
- **Elevation**, the angle the camera must tilt (up/down) to point directly at the tag center

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      Here each green Block assigns its value to a Variable:

      .. figure:: images/Blocks-RBE.png
         :width: 75%
         :align: center
         :alt: AprilTag RBE Blocks

         AprilTag Range, Bearing, Elevation Blocks

   .. tab-item:: Java
      :sync: java

      Use these `ftcPose` fields for Telemetry, or assign to a Variable:

      .. code-block:: java

         AprilTagDetection myAprilTagDetection;
         double myTagPoseRange = myAprilTagDetection.ftcPose.range;
         double myTagPoseBearing = myAprilTagDetection.ftcPose.bearing;
         double myTagPoseElevation = myAprilTagDetection.ftcPose.elevation;

Here, the terms do agree with the SDK method names, because they are
calculated within the SDK from the native AprilTag pose values shown above
(XYZ distances and PRY rotations).

As with tag ID code, pose data is usually retrieved inside a ``for() loop``,
for immediate processing or stored for later use.  See the **Initialization**
page for sample ``for() loop`` code.

Unlike tag ID code, a detected AprilTag might provide **no pose data** -- if it
was not placed into the Library by default or with the custom Builder pattern.
Namely, the tag might lack Metadata including **tag size**, required for pose
estimation.

To avoid logic errors, an OpMode can check the Metadata for a **null**
condition before attempting to process pose data.  This is illustrated in these
Sample OpModes: 

- Blocks: `ConceptAprilTag`
- Java: `ConceptAprilTag.java`

More discussion of AprilTag pose data is available here:

- https://ftc-docs.firstinspires.org/apriltag-detection-values

====

*Questions, comments and corrections to westsiderobotics@verizon.net*

