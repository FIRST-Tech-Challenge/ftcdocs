Gamepad Best Practices
------------------------

While there are no rules around which :term:`gamepads <Gamepad>` teams may use on their :term:`operator console <Operator Console>`,
not all gamepads are supported by the FTC :term:`Driver Station app <Driver Station App>`. The
following gamepads have custom drivers that are included in the FTC :term:`SDK` and are
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
custom drivers for gamepads. Teams are strongly encouraged to use the
:ref:`Test Gamepad Utility <utilityopmodes>` :term:`OpMode` to verify that their
gamepad is registering the inputs correctly.

Special features of some gamepads (Rumble, Lighting) may be programmed and used by teams for notifications and signaling to the drivers of the robot.

If a gamepad is rechargeable, it is highly recommended you charge it fully before a competition and keep it charged throughout the event.
Some gamepads can disconnect from the Driver Station when below 50% charge, some may need even more charge to work properly.
See :ref:`Operator Console Best Practices <robot_building/best_practices/robot-best-practices:operator console best practices>` 
for an operator console that keeps both the REV Driver Hub and gamepads charged by using a USB power bank to supply power to both.

It is also recommended to add a  `ferrite cable clip <https://www.revrobotics.com/rev-39-1224-pk4/>`_
close to the USB connector of the gamepad cable in order to reduce the amount of electrical noise that could create a bad signal to the driver station.

Teams are also encouraged to use a `short USB extension cable <https://www.digikey.com/en/products/detail/startechcom/USB3EXT6INBK/21397568>`_
on the driver station to limit the amount of wear and tear on the USB ports
from frequent plugging and unplugging of the gamepad. The extenders should
always remain plugged into the driver station and, with proper strain relief,
can help protect the port from accidental damage.

