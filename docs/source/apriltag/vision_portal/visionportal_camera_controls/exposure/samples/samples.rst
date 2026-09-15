Exposure Control Code Samples
-----------------------------

1. Import the interface. This line is automatically added by :term:`OnBot Java`
   when the interface is used (coded).

-  ``import org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl;``

2. Declare the ExposureControl object, before ``runOpMode()``.

-  ``ExposureControl myExposureControl;``

3. Assign the :term:`VisionPortal`'s camera control to your control object, in
   ``runOpMode()``. Wait until the Portal reports ``STREAMING`` before doing
   this; the control is not available until the camera is actually open.

-  ``myExposureControl = visionPortal.getCameraControl(ExposureControl.class);``

4. Set the mode to Manual, for direct control.

-  ``myExposureControl.setMode(ExposureControl.Mode.Manual);``

5. Set the exposure duration, in this case to 30 milliseconds.

-  ``myExposureControl.setExposure(30, TimeUnit.MILLISECONDS);``

See these and other exposure controls illustrated in the :doc:`Sample OpModes
</apriltag/vision_portal/visionportal_camera_controls/samples/samples>`.