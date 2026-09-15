Gamepad Calibration and Drift
=============================

Started in the 2023-2024 season, Tech Tips are segments released in the
*FIRST* Tech Challenge `Team E-mail Blast
<https://www.firstinspires.org/resource-library/ftc/team-blast-archive>`__.
Sometimes the Tech Tips are included in whole in the email blast, but sometimes
there is more content than is reasonable in the email blast so partial content
is included in the blast with the rest of the content here.

.. _gamepadcalibrationanddrift:

We had an abnormally large number of questions regarding gamepad calibration
hit our support lines, both at *FIRST* and at REV Robotics, though question
submitters had no idea that gamepad calibration was the issue - so let's cover
the topic!

How does a joystick know where "center" is on a gamepad? On virtually all
gamepads the analog joysticks have an electrical device (usually a
potentiometer) that electrically measures the motion of the stick. If the
electrical device's value at "center" does not coincide with the value the
gamepad thinks should be center, the stick will have a non-zero value at its
center position; this is called drift. In a video game, drift is what causes
your character to walk left (or right, etc) even though you're not moving
the joystick. For a robot, this can cause ghost turning or unwanted motor or
servo motion. So how is this "center" value determined?

Some gamepads, like the Logitech F310 gamepads, simply read the value of the
analog joystick when it's first powered on and assumes the sticks are always
"centered" at that time. If the analog stick is NOT centered when powered
on, for example if it's upside down on a table or otherwise resting against
something that is deflecting the analog stick, the "center" value will
include some amount of drift. In order to correct this, ensure the gamepad
analog sticks are centered and simply unplug and replug the joystick. When
replugged, the gamepad will again read the current analog stick value as
"center" and correct the drift.

Other gamepads, like the Sony DualShock 4 (PS4) or Sony DualSense (PS5),
can be calibrated using online tools such as https://dualshock-tools.github.io/
(this is not an official Sony calibration method).

Got any questions about gamepad drift? Come start or join the conversation on
the `FTC Community Forums <https://ftc-community.firstinspires.org/>`__!
