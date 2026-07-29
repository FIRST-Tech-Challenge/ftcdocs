VisionPortal Camera Controls
============================

Clearer camera images can improve :term:`AprilTag` and Color Processing results. The
SDK offers eight **camera controls** (Exposure, Gain, White Balance, Focus and
Pan/Tilt/Zoom), available in Blocks, OnBot Java and Android Studio. These
controls can be applied under various lighting conditions.

The :term:`webcam <Webcam>` itself is opened by a :ref:`VisionPortal
<apriltag/vision_portal/visionportal_overview/visionportal-overview:visionportal overview>`,
which also provides the control objects described here.

Hats off to `rgatkinson <https://github.com/rgatkinson>`__ and
`Windwoes <https://github.com/Windwoes>`__ who developed these
camera controls.

.. toctree::
   :maxdepth: 1

   overview/overview
   webcam_states/webcam-states
   exposure/index
   gain/index
   white_balance/index
   focus/index
   ptz/index
   blocks/blocks
   observing/observing
   eval/eval
   samples/samples


Summary
-------

Camera controls in the SDK could potentially improve AprilTag detections and
Color Processor results. Exposure, gain and other values could be
pre-programmed in team autonomous :term:`OpModes <OpMode>`. It's also possible to
manually enter such values before a :term:`match <Match>` begins, based on anticipated lighting,
starting position and other game-time factors.

You are encouraged to submit other webcam reports and examples that
worked for you.

====================================================================

Questions, comments and corrections to westsiderobotics@verizon.net
