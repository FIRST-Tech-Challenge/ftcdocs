Evaluating Your Webcam
----------------------

The firmware of a specific webcam may or may not support certain
features described here. The SDK provides some methods to query the
webcam and/or return values that indicate whether a valid response was
available.

Exposure Support
~~~~~~~~~~~~~~~~

Here are two methods to query exposure and a specific exposure mode:

-  isExposureSupported()
-  isModeSupported(ExposureControl.Mode._mode_)

   -  for *mode*, enter the specific mode name you are testing

For the following methods, a field called ``unknownExposure`` of type
long is returned if exposure unavailable: 

-  getExposure(TimeUnit.MILLISECONDS) 
-  getMinExposure(TimeUnit.MILLISECONDS) 
-  getMaxExposure(TimeUnit.MILLISECONDS)

The methods that set the exposure and mode can also return a Boolean,
presumably indicating whether the operation was successful or not. As
optional examples: 

- ``wasExposureSet =  setExposure(25);`` 
- ``wasExposureModeSet = setMode(ExposureControl.Mode.Manual)``

Likewise the AE Priority feature can return a Boolean. For example: 

- ``wasAEPrioritySet =  setAePriority(true);``

Gain Support
~~~~~~~~~~~~

The method that sets the gain can also return a Boolean indicating
whether the operation was successful or not. As an optional example: 

- ``wasGainSet =  setGain(25);``

White Balance Support
~~~~~~~~~~~~~~~~~~~~~

The methods that set temperature and mode can also return a Boolean,
indicating whether the operation was successful or not. As optional
examples:

-  ``wasTemperatureSet = setWhiteBalanceTemperature(3000);``
-  ``wasWhiteBalanceModeSet = setMode(WhiteBalanceControl.Mode.MANUAL);``

Focus Support
~~~~~~~~~~~~~

Here are two methods to query focus and and a specific focus mode: 

- isFocusLengthSupported() 
- isModeSupported(FocusControl.Mode._mode_)

The following methods return a **negative value** if the requested focus
value is unavailable. For example, -1 is returned by the Logitech C270
and the Microsoft LifeCam VX-5000. The Javadoc also mentions a field
``unknownFocusLength`` of type double. 

- getFocusLength() 
- getMinFocusLength() 
- getMaxFocusLength()

The methods that set the focus length and mode can also return a
Boolean, presumably indicating whether the operation was successful or
not. As optional examples: 

- ``wasFocusSet =  setFocusLength(25);`` 
- ``wasFocusModeSet = setMode(FocusControl.Mode.Fixed)``

PTZ Support
~~~~~~~~~~~

The methods that set the pan/tilt pair and zoom value can also return a
Boolean, presumably indicating whether the operation was successful or
not. As optional examples: 

- ``wasPanTiltSet =  setPanTilt(myHolder);``
- ``wasZoomSet = setZoom(3)``

For PTZ get() methods, some webcams simply **return zero** for
unsupported values.

Some Caveats
------------

-  the SDK supports webcams conforming to the `UVC
   standard <https://en.wikipedia.org/wiki/USB_video_device_class>`__

   -  many non-UVC webcams work well in competition, despite lacking UVC
      certification
   -  some non-UVC webcams can be listed in Configure Robot, but crash
      the RC app at runtime

-  webcams may retain an assigned Exposure Mode or Focus Mode, even if
   unplugged

   -  always verify the current mode

-  for a given exposure value, one mode’s preview may look very
   different than another mode’s preview
-  some webcams **accept** / ``set()`` and **confirm** / ``get()`` a
   **non-supported mode**
-  Logitech C270 preview becomes **lighter** up to exposure 655, then
   rolls over to **dark** at 656

   -  this webcam’s Min is 0, Max is 1000.

-  Logitech V-UAX16 preview looks normal at exposure = 0, becomes
   **darker** up to 30-40
-  Logitech C920 **gain** value (0-255) greatly influences preview
   quality, comparable to **exposure** (0-204)
-  restarting the RC app is sometimes needed after a webcam OpMode
   crashes
-  firmware versions may vary among webcams of the same model number

Lastly, some features here may be implemented or enhanced with the help
of an external library such as `OpenCV <https://opencv.org/>`__ or
`EasyOpenCV <https://github.com/OpenFTC/EasyOpenCV>`__. That potential
is not covered in this basic tutorial. A separate tutorial covers the
general use of `External
Libraries <https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/External-Libraries-in-OnBot-Java-and-Blocks>`__
in Blocks and OnBot Java.