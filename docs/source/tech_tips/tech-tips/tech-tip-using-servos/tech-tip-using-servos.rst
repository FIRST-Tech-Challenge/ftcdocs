Using Servos on Your Robot
==========================

Started in the 2023-2024 season, Tech Tips are segments released in the
*FIRST* Tech Challenge `Team E-mail Blast
<https://www.firstinspires.org/resource-library/ftc/team-blast-archive>`__.
Sometimes the Tech Tips are included in whole in the email blast, but sometimes
there is more content than is reasonable in the email blast so partial content
is included in the blast with the rest of the content here.

.. _servooncontrolhub:

Servos on the Control and Expansion Hubs
----------------------------------------

There was a fantastic `question on the FTC-QA
<https://ftc-qa.firstinspires.org/qa/229>`__ that prompted an in-depth
discussion about servos in *FIRST* Tech Challenge - the question was in regard
to servo compatibility and operation/performance on a REV Control Hub, REV
Expansion Hub, and REV Servo Power Module. While the full explanation was
too much for a Q&A answer, the complete answer was provided on the
`FTC-Community forums
<https://ftc-community.firstinspires.org/t/rev-control-hub-servo-port-compatibility/858>`__.
If you are using servos (or want to use servos) on your robot, the full
answer contains an explanation of how servos are managed on a Control and
Expansion Hub that you cannot get anywhere else!

.. _servopowerinjectors:

Servo Power Injectors
---------------------

Servo Power Injectors have been used in *FIRST* Tech Challenge
for several years now, but do you really understand what they are and how they
work? What is a Servo Power Injector and how might servos behave differently
when used with one?

A servo connection is a 3-wire combination that combines power, ground, and
a signal. The actual command signal for the servo travels on the signal wire,
and the power used to power the servo travels on the other two wires. A servo
power injector is a device that removes the power provided by the servo controller
(REV Control Hub or REV Expansion Hub for FTC) and provides a new, usually higher
wattage power source. Both the REV Servo Power Module and Studica Servo Power Block
replace the 5V/10W power provided by the REV Control/Expansion Hubs with a 6V power
source with a higher maximum wattage.

So what does higher voltage do for a servo? Servos operate on a power range; the
more power they get, the faster and stronger they can become, up to a certain limit.
Servos operating at 5V get a noticeable boost in speed and output power when used
at 6V. The same servos may seem superhuman at higher voltages!

The downside of servo power injectors is that teams are now responsible for
managing their own power usage. On the REV Control Hub, for instance, each servo
port pair is limited in how much power it can draw (at least there's a limit on
how long it can draw high loads). When using a servo power injector, the pool of
power for a servo is much larger and less restricted since it pulls its power
directly from the robot battery - using power injectors means you could consume
all of the power on the robot just from the servos alone! This will result in the
robot power system browning out (resulting in loss of communications or loss of
power to the control system) or even blowing the 20A battery fuse.

Using a servo power injector can also expose different behaviors in servos that
were not present when using the REV Control/Expansion Hub directly. The biggest
behavior is the "Lost Signal" behavior. When an OpMode ends, the REV
Control/Expansion hubs stop the signal and also cut power to the servo ports -
this leads to the servos "going limp" as they lose power. With a servo power
injector, the servos never lose power, and so "lost signal" behaviors will often
then take over which may cause the servo to move to a "default" position (which
is virtually never advantageous for robots but definitely advantageous for R/C
planes for example). The Axon MAX+ servo and several higher-power HiTec servos
have this behavior, the Axon MAX+ behavior is at least configurable with a servo
programmer.

Finally, when using a servo power injector it's of VITAL importance that you
cover unused ports with tape or other debris-limiting measures to protect the
ports. It's very easy to get metal swarf in open servo ports, and that metal
can short out the power output pins - especially lower-cost power injectors
cannot tell when they're being used, or don't have protections against short
circuits, but they still have all output pins powered. This can quickly turn
your servo power injector into an expensive paperweight when the power
regulator overloads and burns out.

.. tip::
   Wondering how to compare one servo against another? See
   :ref:`Calculating Motor and Servo Power
   <tech_tips/tech-tips/tech-tip-motor-servo-power/tech-tip-motor-servo-power:Calculating Motor and Servo Power>`.

Got any questions about servos? Come start or join the conversation on the
`FTC Community Forums <https://ftc-community.firstinspires.org/>`__!
