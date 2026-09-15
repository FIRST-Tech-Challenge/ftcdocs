Gamepad Best Practices
------------------------

While there are no rules around which gamepads teams may use on their OPERATOR
CONSOLE, not all gamepads are supported by the FTC Driver Station app. The
following gamepads have custom drivers that are included in the FTC SDK and are
known to work with the FTC Driver Station app:

- Logitech F310
- Xbox 360 Controller for Windows
- Sony DualShock 4 Wireless Controller for PS4
- Sony DualSense Wireless Controller for PS5
- Etpark Wired Controller for PS4
- REV Robotics USB PS4 Compatible Gamepad
- Quadstick game controller in Xbox 360 Emulation Mode

Starting with FTC SDK version 12.0, the gamepad indicators on the top right of
the Driver Station App will be orange if the assigned gamepad is not recognized
and thus is using a built-in Android gamepad driver instead of a known FTC SDK
gamepad driver. In this case, the built-in Android driver might work, but it's
possible the device input (button/stick) mappings might be incorrect. Teams are
not allowed to modify the Driver Station app in any way, which includes adding
custom drivers for gamepads. Teams are strongly encouraged to use the Test
Gamepads Utility OpMode to verify that their gamepad is registering the inputs
correctly.

It is recommended to add a  `ferrite cable clip <https://www.revrobotics.com/rev-39-1224-pk4/>`_
close to the USB connector in order to reduce the amount of electrical noise.
Teams are also encouraged to use a `short USB extension cable <https://www.digikey.com/en/products/detail/startechcom/USB3EXT6INBK/21397568>`_
on the DRIVER STATION to limit the amount of wear and tear on the USB ports
from frequent plugging and unplugging of the gamepad. The extenders should
always remain plugged into the DRIVER STATION and, with proper strain relief,
can help protect the port from accidental damage.