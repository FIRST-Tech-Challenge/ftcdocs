Exposure Control Mode
---------------------

:java:extdoc:`org.firstinspires.ftc.robotcore.external.hardware.camera.controls`


A webcam may operate in one of various exposure modes.

Many common webcams offer only some of these modes. To directly
control the exposure, set the webcam to Manual mode.

The SDK supports these values of ExposureControl.Mode: 

- `AperturePriority`
- `Auto` 
- `ContinuousAuto`
- `Manual` 
- `ShutterPriority` 
- `Unknown`

Mode is managed with these ExposureControl methods: 

- setMode(ExposureControl.Mode._mode_) 
- getMode()

The Logitech C920 and C270 models offer two exposure modes:
AperturePriority and Manual.