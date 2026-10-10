VisionPortal Overview
=====================

**FIRST Tech Challenge** introduces **VisionPortal**, a comprehensive new
interface for vision processing.

-  For **FTC Blocks and Java** teams, :term:`VisionPortal` offers key capabilities of
   **AprilTag**, **EasyOpenCV** and the **Color Processors** – at the same
   time!

   .. figure:: images/020-dual-detection.png
      :width: 75%
      :align: center
      :alt: Dual Detection

      Dual Preview, with two Processors running at once

   |

-  **AprilTag** detections include ID code and **pose**: tag location and
   orientation, relative to the camera.

-  **Camera Controls**, which can improve vision processing performance for
   :term:`webcam <Webcam>`, are now fully available to **FTC Blocks** users.

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

**If you are using the AprilTag processor, read the** :doc:`AprilTag
Introduction <../apriltag_intro/apriltag-intro>` **first.**
   
The SDK describes AprilTag pose **relative to the camera**, by default.
This computing process is called **pose estimation**, a term that emphasizes
this is an estimate only, based on many factors including **camera
calibration**. You must determine AprilTag’s best use for reaching your 
goals.

.. toctree::
   :maxdepth: 1

   Webcams for VisionPortal <../visionportal_webcams/visionportal-webcams>
   Vision Processor Initialization <../vision_processor_init/vision-processor-init>
   VisionPortal Initialization <../visionportal_init/visionportal-init>
   VisionPortal Previews <../visionportal_previews/visionportal-previews>
   Camera Calibration </programming_resources/vision/camera_calibration/camera-calibration>
   VisionPortal Camera Controls <../visionportal_camera_controls/index>
   VisionPortal CPU and Bandwidth <../visionportal_cpu_and_bandwidth/visionportal-cpu-and-bandwidth>
   Vision Multiportal <../vision_multiportal/vision-multiportal>

.. seealso:: For the AprilTag processor specifically -- ID codes, pose, tag
   libraries and field localization -- see :doc:`AprilTag
   <../apriltag_intro/apriltag-intro>`. For the color processors, see
   :ref:`Color Processing <color_processing>`.

====

Much credit to 

- EasyOpenCV developer `@Windwoes <https://github.com/Windwoes>`__ 
- FTC Blocks developer `@lizlooney <https://github.com/lizlooney>`__ 
- *FIRST* Tech Challenge navigation expert `@gearsincorg <https://github.com/gearsincorg>`__ 
- and the smart people at `UMich/AprilTag <https://april.eecs.umich.edu/software/apriltag>`__.

Questions, comments and corrections to westsiderobotics@verizon.net


