Exposure Control Code Samples
-----------------------------

1. Import the interface. This line is automatically added by OnBot Java
   when the interface is used (coded).

-  ``import org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl;``

2. Declare the ExposureControl object, before ``runOpMode()``.

-  ``ExposureControl myExposureControl;``

3. Assign the Vuforia/TFOD video stream control to your control object,
   in ``runOpMode()``.

-  ``myExposureControl = vuforia.getCamera().getControl(ExposureControl.class);``

4. Set the mode to Manual, for direct control.

-  ``myExposureControl.setMode(ExposureControl.Mode.Manual);``

5. Set the exposure duration, in this case to 30 milliseconds.

-  ``myExposureControl.setExposure(30, TimeUnit.MILLISECONDS);``

See far below for these and other exposure controls illustrated in
`Sample OpModes <#sample-opmodes>`__.