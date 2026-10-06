.. _apriltag:

AprilTag
========

:term:`AprilTag` is a visual fiducial -- a scanned image similar to a QR Code --
that a robot camera can detect for **identification** and **field localization**.
The AprilTag processor runs inside the :doc:`VisionPortal
<vision_portal/visionportal_overview/visionportal-overview>`, which covers camera
selection, initialization, previews and camera controls.

.. toctree::
   :maxdepth: 1

   AprilTag Introduction <vision_portal/apriltag_intro/apriltag-intro>
   AprilTag ID Codes <vision_portal/apriltag_id_code/apriltag-id-code>
   AprilTag Metadata <vision_portal/apriltag_metadata/apriltag-metadata>
   AprilTag Reference Frame <vision_portal/apriltag_reference_frame/apriltag-reference-frame>
   AprilTag Pose <vision_portal/apriltag_pose/apriltag-pose>
   Understanding AprilTag Values <understanding_apriltag_detection_values/understanding-apriltag-detection-values>
   AprilTag Library <vision_portal/apriltag_library/apriltag-library>
   AprilTag Localization <vision_portal/apriltag_localization/apriltag-localization>
   AprilTag Test Images <opmode_test_images/opmode-test-images>
   AprilTag Advanced Use <vision_portal/apriltag_advanced_use/apriltag-advanced-use>

.. seealso:: SDK 12.0 added AprilTag Clusters, groups of tags detected
   together as one target, and split AprilTag detections into two types. The
   change affects code on several of the pages above. See
   :ref:`AprilTag Clusters <apriltagclusters>`.
