VisionPortal Overview
=====================

**FIRST Tech Challenge** introduces **VisionPortal**, a comprehensive new
interface for vision processing.

-  For **FTC Blocks and Java** teams, VisionPortal offers key capabilities of
   **AprilTag** and **EasyOpenCV**, along with **TensorFlow Object Detection
   (TFOD)** – at the same time!

   .. figure:: images/020-dual-detection.png
      :width: 75%
      :align: center
      :alt: Dual Detection

      Dual Preview with both AprilTags and TensorFlow

   |

-  **AprilTag** detections include ID code and **pose**: tag location and
   orientation, relative to the camera.

-  **Camera Controls**, which can improve AprilTag and TFOD performance for
   webcam, are now fully available to **FTC Blocks** users.

-  **Multiple cameras** can operate at the same time – phone camera and/or
   webcam.

   .. figure:: images/030-CH-preview-2-webcams.png
      :width: 75%
      :align: center
      :alt: Dual Camera

      Multiple Camera View

   |

-  **Sample OpModes** and new tools are available to operate and
   customize these features, including the **Builder pattern**.

-  For heavy video processing, many options are available to manage
   **CPU resources** and **USB bandwidth**.

-  DS and RC previews can be **BIG**!

   .. figure:: images/100-DH-DS-CS-BIG-TFOD.png
      :width: 75%
      :align: center
      :alt: Full Screen

      Full Screen Preview

Many other new and improved features `await your discovery
<https://github.com/FIRST-Tech-Challenge/FtcRobotController#release-information>`__
in VisionPortal and beyond.

----

In preparation for the 2023-2024 CENTERSTAGE season, the new Software
Development Kit (SDK) **VisionPortal** includes **built-in support for AprilTag
technology**. Previously, Teams needed to download and incorporate external
libraries, complicating the programming effort.

AprilTag is a popular vision technology for detecting a simple black-and-white
tag, used to estimate **position and orientation**. In the 2022-2023 POWERPLAY
game, many Teams enjoyed AprilTag’s reliable Autonomous performance for
Signal Sleeve recognition.

   .. figure:: images/005-AprilTag-Worlds.png
      :width: 75%
      :align: center
      :alt: Dual Detection

      Photo Credit: Mike Silversides

**All sections of this Guide assume prior reading of the** :doc:`AprilTag
Introduction <../apriltag_intro/apriltag-intro>` **.**
   
The SDK describes AprilTag pose **relative to the camera**, by default.
This computing process is called **pose estimation**, a term that emphasizes
this is an estimate only, based on many factors including **camera
calibration**. You must determine AprilTag’s best use for reaching your 
goals.

.. toctree::
   :maxdepth: 1

   AprilTag Introduction <../apriltag_intro/apriltag-intro>
   Vision Processor Initialization <../vision_processor_init/vision-processor-init>
   VisionPortal Initialization <../visionportal_init/visionportal-init>
   VisionPortal Previews <../visionportal_previews/visionportal-previews>
   AprilTag ID Codes <../apriltag_id_code/apriltag-id-code>
   AprilTag Metadata <../apriltag_metadata/apriltag-metadata>
   AprilTag Reference Frame <../apriltag_reference_frame/apriltag-reference-frame>
   AprilTag Camera Calibration <../apriltag_camera_calibration/apriltag-camera-calibration>
   AprilTag Pose <../apriltag_pose/apriltag-pose>
   AprilTag Library <../apriltag_library/apriltag-library>
   VisionPortal CPU and Bandwidth <../visionportal_cpu_and_bandwidth/visionportal-cpu-and-bandwidth>
   VisionPortal Camera Controls <../visionportal_camera_controls/visionportal-camera-controls>
   Vision Multiportal <../vision_multiportal/vision-multiportal>
   AprilTag Advanced Use <../apriltag_advanced_use/apriltag-advanced-use>

====

Much credit to 

- EasyOpenCV developer `@Windwoes <https://github.com/Windwoes>`__ 
- FTC Blocks developer `@lizlooney <https://github.com/lizlooney>`__ 
- *FIRST* Tech Challenge navigation expert `@gearsincorg <https://github.com/gearsincorg>`__ 
- and the smart people at `UMich/AprilTag <https://april.eecs.umich.edu/software/apriltag>`__.

Questions, comments and corrections to westsiderobotics@verizon.net


