VisionPortal CPU and Bandwidth
==============================

Introduction
------------

Vision processing can consume significant **CPU resources** and USB
communications **bandwidth**.  Reaching such limits may affect previews, and
cause an OpMode or Robot Controller to slow down, or freeze, or crash.

Teams can balance the benefits of higher resolution and speed
(frames-per-second) against the risk of overloading CPU and bandwidth
resources.

The 8.2 SDK provides numerous tools to manage this balance:

- disable and enable the RC preview (called LiveView) - "Level 1"
- disable and enable the AprilTag (or TFOD) processor - "Level 2"
- stop and resume the camera stream - "Level 3"
- close VisionPortal - "Level 4"
- monitor frames-per-second (FPS)
- select a compressed video streaming format
- select the camera resolution
- set decimation (down-sampling)
- select a pose solver algorithm
- get all or only fresh detections from the AprilTag Processor
- get all or only fresh recognitions from the TFOD Processor

The first four actions are informally rated for benefit and response:

- **LiveView** "Level 1": some reduction of resources used, resumes very quickly after stopping
- **Processor(s)** "Level 2": more reduction of resources used, resumes quickly after stopping
- **Camera Stream** "Level 3": high reduction of resources used, resumes less quickly after stopping
- **VisionPortal** "Level 4": maximum reduction of resources used, do not resume after stopping

Camera Status
-------------

Before discussing the tools to manage vision processing resources, we should
review again the available **camera states**.  This may help you monitor,
evaluate and troubleshoot your optimization efforts.

Repeated from the **Camera Controls** page, these camera states are now available:

- OPENING_CAMERA_DEVICE - No vision processing is happening.
- CAMERA_DEVICE_READY - Camera is open.  No processing is happening, including
  background processing from EOCV (i.e. pulling frames and performing color
  conversion). Ready to call ``resumeStreaming()``.
- STARTING_STREAM - No processing is happening.
- STREAMING - Frames are available for processing (AprilTag and/or TFOD
  recognitions) and preview (LiveView RC preview and DS Camera Stream).
- STOPPING_STREAM - Processing may or may not be happening.  This status is
  followed by ``CAMERA_DEVICE_READY``.
- CLOSING_CAMERA_DEVICE - No processing is happening.
- CAMERA_DEVICE_CLOSED - Nothing is running, USB comms are closed.  Once
  closed, don't open camera again during this OpMode.
- ERROR

These **enums** are listed in sequence, as if opening a camera (fresh build),
then starting or resuming streaming, then stopping streaming, then closing the
VisionPortal.

All of the above is completely separate from the AprilTag and/or TFOD processor
status.  Those can be enabled or disabled at any time, but naturally require
``STREAMING`` status to actually process camera images.

About Previews
--------------

As noted at the **Previews** page, LiveView refers only to the **Robot
Controller** preview.  It's completely separate from the Driver Station (DS)
**Camera Stream**, which still operates normally even if LiveView is stopped
(manually or automatically).

DS Camera Stream uses its own frame collection process, which naturally still
requires the camera/pipeline status to be ``STREAMING``.

Instructions for viewing DS Camera Stream are shown at `ftc-docs
<https://ftc-docs.firstinspires.org/en/latest/hardware_and_software_configuration/configuring/configuring_external_webcam/configuring-external-webcam.html#image-preview>`__.

DS Camera Stream can display only one camera's image, even under the new
MultiPortal feature.  Teams can create specialty OpModes to see one camera's
image or the other camera's image, if needed for match set-up.

Side Note: For SDK 8.2, "LiveView" became the new universal name for the RC
preview. There remain two instances of old names:

- ``myVisionPortalBuilder.enableCameraMonitoring(true);``, discussed below
- ``VIEWPORT`` appears in the preview status window, when stopped

Pause LiveView - Direct
-----------------------

One way to conserve CPU resources ("Level 1") is **directly pausing** LiveView,
while running an OpMode.  The CPU continues processing camera images for
AprilTag and/or TFOD recognitions, but does not actually generate an RC preview
image (video).  

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      These are found in the ``VisionPortal`` toolbox, or palette, under the
      ``Vision`` category.

      .. figure:: images/050-Blocks-LiveView-toggle.png
         :width: 75%
         :align: center
         :alt: Toggle LiveView

         Examples of Toggling LiveView

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         // Temporarily stop the live view (RC preview).
         myVisionPortal.stopLiveView();

         // Start the live view (RC preview) again.
         myVisionPortal.resumeLiveView();  

Your OpMode will **not** need to work with camera status **enums** here, since
these "stop" and "resume" actions happen quickly.

The above commands toggle only LiveView; the DS Camera Stream preview (touch to
refresh) remains available.

Pause LiveView - Indirect
-------------------------

The SDK also offers an **indirect** control of LiveView, available in Blocks
and Java:

.. code-block:: java

   builder.setAutoStopLiveView(true)

This setting causes LiveView to stop **automatically** if both processors
(AprilTag and TFOD) are disabled.  Being part of the Builder pattern, this
feature cannot be directly toggled ``true`` and ``false`` during the OpMode.

This setting is triggered when **both** processors are disabled.  When set to
``false``, by default, the monitor continues showing the camera's view without
annotations.  If set to ``true``, the monitor is Auto Paused, showing a solid
orange screen if no processors are enabled.  Thus the preview **can**
effectively be toggled off and on, using this AutoPause feature.

When one or both processors are re-enabled, LiveView resumes.  This setting
affects only LiveView; the Driver Station Camera Stream preview remains
available.

Disable LiveView
----------------

The SDK also contains a different Builder setting that allows (or disallows)
LiveView **in general**, available in Blocks and Java:

.. code-block:: java

   builder.enableCameraMonitoring(true);

Sample OpModes set this Builder field to ``true`` by default.

This could be set to ``false``, if the OpMode will not need the LiveView
preview at all.  Being part of the Builder pattern, this feature cannot be
directly toggled ``true`` and ``false`` during the OpMode.

Toggle Processors
-----------------

Another way to conserve CPU resources ("Level 2") is **disabling an AprilTag or
TFOD Processor**, while running an OpMode.  

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      These are found in the ``VisionPortal`` toolbox, or palette, under the
      ``Vision`` category.

      .. figure:: images/060-Blocks-Processor-toggle.png
         :width: 75%
         :align: center
         :alt: Toggle Processor

         Examples of Toggling Processors

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         // Enable or disable the AprilTag processor.
         myVisionPortal.setProcessorEnabled(myAprilTagProcessor, true);

         // Enable or disable the TensorFlow Object Detection processor.
         myVisionPortal.setProcessorEnabled(myTfodProcessor, true);

Disabling a Processor does not close LiveView, with its own controls described
above.  Any annotations will stop appearing in the preview.

Disabling and re-enabling processors is very fast, and saves CPU resources.
But EOCV frame pulling and color conversion continue running in the background.

Toggle Camera Stream
--------------------

A more active way to conserve CPU resources ("Level 3") is **stopping the
camera stream**, while running an OpMode.  Naturally this also achieves Levels
1 and 2: stopping LiveView and preventing operation of the AprilTag and TFOD
Processors. DS Camera Stream provides no new snapshots.

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      These are found in the ``VisionPortal`` toolbox, or palette, under the
      ``Vision`` category.

      .. figure:: images/080-Blocks-Streaming-toggle.png
         :width: 75%
         :align: center
         :alt: Toggle Camera Stream

         Examples of Toggling Camera Stream

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         // Temporarily stop the streaming session. This can save CPU
         // resources, with the ability to resume quickly when needed.
         myVisionPortal.stopStreaming();

         // Resume the streaming session if previously stopped.
         myVisionPortal.resumeStreaming();

Stopping (and later resuming) the stream is slightly risky, can take about 1
second, and stops all background processing.  This is what happens when
switching cameras, in the Sample OpModes called ``SwitchableCameras``.  One
stream stops, and the other stream starts.

Close VisionPortal
------------------

Closing the portal with ``close()`` stops all background processing permanently ("Level 4"), and closes USB communication with the camera.  

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      These are found in the ``VisionPortal`` toolbox, or palette, under the
      ``Vision`` category.

      .. figure:: images/100-Blocks-close-VisionPortal.png
         :width: 75%
         :align: center
         :alt: Close VisionPortal

         Close VisionPortal Example

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         // Save computing resources by closing VisionPortal at any time, if no
         // longer needed.  
         myVisionPortal.close();

The ``close()`` process is a "teardown" of all camera processing.  It is not
recommended to "re-open" the camera within the same OpMode, by building another
VisionPortal.  This is risky and might take several seconds.

Accordingly, the SDK offers no corresponding ``reopen()`` or ``resume()``
method.

The ``close()`` process happens automatically at the end of any OpMode.  

Calling ``stopStreaming()`` before calling ``close()`` is allowed (for
clarity), but not required, since ``close()`` internally calls
``stopStreaming()`` if applicable.

Rapid Toggling
--------------

Your OpMode (or manual testing) should avoid or handle rapid stacking of the
"on" and "off" actions described above.

It's legal to call ``resumeStreaming()`` while the status is ``STOPPING_STREAM``.
But the program will be **blocked** until the stopping operation is done.

**Blocking** means the latest function doesn't return immediately.  So the code
is temporarily "stuck" there, as if executing a ``sleep()`` command.

The same applies if calling ``stopStreaming()`` while the status is
``STARTING_STREAM``.  It's allowed, but your code may have to wait.

To avoid blocking, it's best to check the relevant **status enum** to make sure
the previous operation is complete.  This can be done with an empty ``while()``
loop, in a linear OpMode.

CPU Management Choices
----------------------

So far, there are **10 possible configurations** to evaluate CPU performance,
using only the vision process controls discussed above:

- VisionPortal closed
- VisionPortal open, Streaming off

Then 4 with Streaming on, Preview off:

- only AprilTag processor enabled
- only TFOD processor enabled
- both enabled
- both disabled

Then 4 with Streaming on, Preview on:

- only AprilTag processor enabled
- only TFOD processor enabled
- both enabled
- both disabled

This gives Teams ample opportunity to evaluate and manage CPU performance
and USB Bandwidth.  Many other tools remain:

- monitor frames-per-second (FPS)
- select a compressed video streaming format
- select the camera resolution
- set decimation (down-sampling)
- select a pose solver algorithm
- get all or only fresh detections from the AprilTag Processor
- get all or only fresh recognitions from the TFOD Processor

Frame Rate
----------

The VisionPortal **automatically optimizes** for maximum frame rate, the number
of processed frames per second (FPS).  Presuming this optimization is based on
**CPU resources**, measuring effects on **frame rate** could indirectly reflect
CPU resource status/consumption/capacity.

Frame rate is reported visually in the LiveView status window.  It's also
available for your OpMode to track, record and evaluate, in Blocks and Java:

.. code-block:: java

   float myFPS = myVisionPortal.getFps();

Teams can collect FPS data to illustrate the general effects of, for
example, (a) resolution and (b) processors running, on CPU performance.
Results will depend on many team-specific factors such as webcams, codebase
(other processing), vision targets (number, type, distance), etc.

Learn more about such studies at this `Datalogging tutorial
<https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/Datalogging>`__.

Dual Webcams
------------

Before discussing Streaming Formats, we should mention that **USB Bandwidth**
can be a concern for **dual webcams**.

.. note::
   Internal phone cameras have an independent high-speed interconnect (not
   USB), unaffected by an added USB webcam.

The two webcams do *not* need to use the same format or resolution.

For dual webcams **plugged directly into the Control Hub**, the USB 2.0 and USB
3.0 ports are on different buses.  This reduces the concern about bandwidth
capacity, although higher resolution can cause the auto-optimized frame rate to
reduce.

Using the Control Hub's two USB ports, the choice of stream format has little
impact.  But the USB 2.0 bus also carries the Control Hub's **WiFi radio**;
adding a webcam may affect its reliability.

On the other hand, both webcams on an **external USB Hub** (plugged into the CH
3.0 port) can reach **bandwidth limits**, causing preview failures and OpMode
crashes.  This can be managed by factors discussed already, and by the choice
of **streaming format**.

Streaming Formats
-----------------

Under the legacy **YUY2 format**, one webcam or the other (on a shared hub) may
stop streaming above roughly 640x360 resolution.  This is **below the default**
resolution of 640x480.

Bandwidth problems are often indicated by **no detections**, and a blue screen
in LiveView.  A team using default resolutions may quickly conclude
(incorrectly) that dual webcams **does not work**.

The SDK now offers a compressed **MJPEG format**.  This can significantly
reduce USB bandwidth issues, but must be evaluated also for speed and quality
of recognitions.

Under the MJPEG format, resolutions under roughly 432x240 may degrade the image
to prevent AprilTag detection on at least 1 webcam, while higher resolutions
may occasionally stop the RC app or crash the Control Hub.

For both formats, higher resolution can reduce frame rate.

These factors offer much opportunity for experimentation and Datalogging, to
help optimize your VisionPortal performance.

Camera Resolution
-----------------

Some teams believe "higher resolution is better", when purchasing webcams and
specifying resolution for AprilTag and TFOD use.

As indicated in the previous sections here, it's more useful to consider a
"suitable resolution" that satisfies multiple goals and challenges:

- quick and reliable AprilTag detections
- quick and reliable TFOD recognitions, including object tracking
- accurate AprilTag pose estimates
- smooth, accurate navigation while driving (higher FPS)
- avoid CPU overload
- avoid USB bandwidth limits
- resolution (or aspect ratio) for which calibration values exist
- accommodates lighting conditions and any Camera Controls applied

You might end up preferring the **lowest resolution** that meets your needs.

It's easy to find out which resolutions are supported by your camera. Just try
to run any VisionPortal OpMode with an **incorrect (fake) resolution**; the error
message will tell you the supported resolutions. Write these down for future
reference.

Other Tools
-----------

This topic continues at the **AprilTag Advanced Use** page, to discuss advanced
tools for managing CPU usage. It includes a Test OpMode in Blocks and Java.

For now, these are left for interested users to research and investigate:

- set decimation (down-sampling)
- select a pose solver algorithm
- get all or only fresh detections from the AprilTag Processor
- get all or only fresh recognitions from the TFOD Processor

All of the above features are easily found in the **FTC Blocks** toolboxes, or
palettes, under Vision category.

**Java** users should review the VisionPortal interface at the SDK
`Javadocs <https://javadoc.io/doc/org.firstinspires.ftc/RobotCore/latest/overview-summary.html>`__
site.  Click **FRAMES** for easy navigation.

====

*Questions, comments and corrections to westsiderobotics@verizon.net*

