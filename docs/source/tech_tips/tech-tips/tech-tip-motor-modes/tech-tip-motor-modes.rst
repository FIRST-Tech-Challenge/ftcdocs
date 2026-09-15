Motor Modes and Encoders
========================

Started in the 2023-2024 season, Tech Tips are segments released in the
*FIRST* Tech Challenge `Team E-mail Blast
<https://www.firstinspires.org/resource-library/ftc/team-blast-archive>`__.
Sometimes the Tech Tips are included in whole in the email blast, but sometimes
there is more content than is reasonable in the email blast so partial content
is included in the blast with the rest of the content here.

.. _encoders101:

Using Encoders
--------------

Encoders are the devices that track how much a motor shaft has rotated, which
the vast majority of motors used in *FIRST* Tech Challenge have built-in. The
encoders on the motors can help track a motor, but they can also be used to
help synchronize and control motors via "Motor Modes" built into the Control
and Expansion Hub firmware. Did you know that most programmers use these motor
modes incorrectly? More on these "Motor Modes" and the correct way to use them
can be found on the `REV Robotics Encoder documentation
<https://docs.revrobotics.com/duo-control/programming/using-encoder-feedback>`__.

.. _motormodes:

Motor Modes
-----------

This section is for all you who love diving deep into the *FIRST* Tech
Challenge SDK and exploring interesting lesser-known behaviors of well-known
interfaces. The `REV Robotics documentation
<https://docs.revrobotics.com/duo-control/programming/using-encoder-feedback>`__
for encoder feedback has a really good description of the four primary run
modes, namely:

- ``DcMotor.RunMode.STOP_AND_RESET_ENCODER`` mode
- ``DcMotor.RunMode.RUN_WITHOUT_ENCODER`` mode
- ``DcMotor.RunMode.RUN_USING_ENCODER`` mode
- ``DcMotor.RunMode.RUN_TO_POSITION`` mode

The first two modes do exactly as their names suggest, and generally no more.
``STOP_AND_RESET_ENCODER`` stops the motors and resets the encoder count to
zero. ``RUN_WITHOUT_ENCODER`` more or less blindly controls the motor power
using a calculated percentage of the available battery power through the
motor's ``.setPower()`` method. There's really no more to see here.

The last two modes are a bit more interesting. These two modes use a feature
of the Control/Expansion hub firmware to externally (from robot code) control
the motors. Using this feature you can do a lot more with the motors such as
set the maximum velocity of the motor (nominally in encoder-ticks-per-second)
using the ``.setVelocity()`` method, and :ref:`change the actual PIDF algorithm
<programming_resources/shared/pidf_coefficients/pidf-coefficients:Changing
PIDF Coefficients>` being used by the motor mode (using the
``.setPIDFCoefficients()`` methods). Because these two motor modes rely on
knowing specific motor characteristics, it's VERY important to set the
correct motor type for the motor in the Robot Configuration!

Finally, one final note about ``RUN_TO_POSITION``. When setting a Power or a
Velocity for the motor in ``RUN_TO_POSITION`` mode, the value is intended to be
unsigned. When using ``RUN_WITHOUT_ENCODER`` and ``RUN_USING_ENCODER`` the sign
of the value of the Power or Velocity denotes direction; positive values mean
run the motor "forwards" and negative values mean run the motor "backwards."
However, with ``RUN_TO_POSITION``, the current encoder value and target encoder
position are already known - and thanks to the motor setting in the Robot
Configuration it knows everything about the motor - therefore the controller
already knows which direction to run the motor and does not need a signed
value indicating direction.

Got any questions about motor modes or encoders? Come start or join the
conversation on the `FTC Community Forums
<https://ftc-community.firstinspires.org/>`__!
