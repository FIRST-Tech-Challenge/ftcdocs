Vision Resources: AprilTags, Webcams, and HuskyLens
===================================================

Started in the 2023-2024 season, Tech Tips are segments released in the
*FIRST* Tech Challenge `Team E-mail Blast
<https://www.firstinspires.org/resource-library/ftc/team-blast-archive>`__.
Sometimes the Tech Tips are included in whole in the email blast, but sometimes
there is more content than is reasonable in the email blast so partial content
is included in the blast with the rest of the content here.

.. _apriltaglocalization:

AprilTag Localization
---------------------

How can your robot determine where it is on the field by looking at an
AprilTag? A set of APIs was added in SDK 10.0 to provide just that
information, and it works for any static (immobile) AprilTag on the
competition field. Check out the :ref:`AprilTag Localization
<apriltag/vision_portal/apriltag_localization/apriltag-localization:AprilTag Localization>`
documentation on ftc-docs!

.. _webcams:

Choosing the Right Webcam
-------------------------

When using AprilTags, choosing the right webcam can save you from having to
:ref:`perform your own calibration
<programming_resources/vision/camera_calibration/camera-calibration:Camera
Calibration>` before being able to use it for obtaining
:ref:`AprilTag Pose information
<apriltag/vision_portal/apriltag_pose/apriltag-pose:AprilTag Pose>`.
The :ref:`Webcams for VisionPortal
<apriltag/vision_portal/visionportal_webcams/visionportal-webcams:Webcams
for Vision Portal>` document highlights several commonly used webcams
that have calibration data built-in to the SDK itself. Maximum frame rates,
field of view, and supported resolutions with calibration data are all
covered for each of the most common webcams in *FIRST* Tech Challenge.  Short
on time? Be sure to check out the handy :ref:`quick summary
<apriltag/vision_portal/visionportal_webcams/visionportal-webcams:quick summary>`
at the bottom of the page! Did you calibrate your own camera and
determine lens intrinsics for it? Please check out `this FTC-Community post
<https://ftc-community.firstinspires.org/t/sticky-camera-calibration-crowdsourcing/577>`__
to contribute to the crowd-sourcing effort for calibration data!

.. _huskylensintro:

HuskyLens Intro
---------------

This section comes to us from Chris Johannesen, 2023 *FIRST* Tech Challenge
Volunteer of the Year and author of many ftc-docs tutorials. Have you heard of
the HuskyLens and want to learn how to properly connect one to a Control Hub,
learn how to use it to detect objects, and use the HuskyLens samples included
with SDK 9.0.0 and newer? Chris has this and more in his :ref:`HuskyLens
Tutorial <devices/huskylens/huskylens:HuskyLens Intro for *FIRST* Tech Challenge>`
on ftc-docs, check it out!

Got any questions about vision on your robot? Come start or join the
conversation on the `FTC Community Forums
<https://ftc-community.firstinspires.org/>`__!
