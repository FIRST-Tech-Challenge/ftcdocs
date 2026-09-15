What Makes Battery Voltage Sag?
===============================

Started in the 2023-2024 season, Tech Tips are segments released in the
*FIRST* Tech Challenge `Team E-mail Blast
<https://www.firstinspires.org/resource-library/ftc/team-blast-archive>`__.
Sometimes the Tech Tips are included in whole in the email blast, but sometimes
there is more content than is reasonable in the email blast so partial content
is included in the blast with the rest of the content here.

.. _batteryvoltagesag:

This Tech Tip surrounds a question that we get asked at events all the time -
"What makes battery voltage sag?". As a battery is heavily used, teams will
notice that the voltage of the battery temporarily decreases from its starting
voltage during periods of heavy use, and then generally raises back up once the
heavy use has subsided. So what causes this?

There are LOTS of reasons why battery voltage will sag during use. Below we
cover the major factors: battery chemistry and heavy use, cell health and
battery temperature, and internal resistance.

.. _batteryvoltagesag1:

Battery Chemistry and Heavy Use
-------------------------------

The first thing to remember is that a battery is a chemical reaction factory,
and does not exactly work the same as the typical "gas tank" analogy makes it
seem. The chemical reactions at the electrodes create a potential difference
(voltage) between them. This voltage drives the flow of electrons generated
by hydrogen and hydroxide ion creation and transfer. In NiMH batteries this
reaction is reversible but it takes time and energy. What's important to
understand is that the chemical reaction can happen only at a specific rate
(the rate is based on a number of factors which we'll discuss later); if the
demand exceeds the rate of reaction for the battery, the voltage and current
will drop until the reactions can replenish the battery output (this
temporary drop is known as "sag"). As the materials at the electrodes are
gradually consumed, the overall battery charge will deplete and can no longer
sustain the flow of electrons, and the battery will need to be recharged or
replaced.

So what is the biggest reason why batteries will sag? On a *FIRST* Tech
Challenge robot, this reason is actuator (motor and servo) current draw.
Motors and Servos can pull a considerable amount of current when they're
being used, especially when they're being used in low-torque configurations.
Motors that are geared closer to 1:1 gear ratio can spin faster - they can
propel your robot's drivetrain across the field much faster - but have less
torque because of the lower gear ratio. Motor configurations that have less
torque consume significantly more current to operate (when driving the same
load) than motor configurations with more torque. Systems being driven by
actuators that have more friction or less torque will cause the motors to
consume larger amounts of current, and this can cause even healthy batteries
to have their voltages "sag" during periods of high use. Teams must consider
their power consumption very carefully when optimizing their battery and
motor utilization during a match, even though that's often an afterthought
for most teams.

.. _batteryvoltagesag2:

Cell Health and Battery Temperature
-----------------------------------

Battery cell health is an important factor in the overall health of a
battery. An NiMH battery used in *FIRST* Tech Challenge is a multi-cell
battery, meaning it's composed of individual smaller batteries connected
together. Each cell contributes to the overall power output of the battery.
As a battery ages, individual cells in the battery may age at different rates
- this aging can lead to degradation of cell material, electrolyte breakdown,
and creation of dendrites that can eventually puncture the cell wall from
inside the cell among others. Most often this cell breakdown is accelerated
due to improper storage, overcharging, deep discharging, excessive
temperatures, or physical damage (especially due to dropping). When a cell
fails, it can lead to a reduced capacity of the battery pack, and the
battery will not last as long on a single charge nor will it be able to
provide the peak power output that it previously could. Failed cells can
cause other cells to fail prematurely, primarily due to overcharging and
imbalanced voltage due to the fact that NiMH batteries and chargers for
NiMH batteries do not contain a load-balancing management system for
individual cells. In some cases, failed cells can cause short circuits,
overheating, and increased risk of fire/explosion! If you're suspicious of
a battery, get it tested before using it again.

Battery temperature is also an important consideration. When a battery is
being charged, it will likely become warm and even slightly hot to the touch
- this is expected and natural due to the process of recharging a battery.
NiMH batteries deliver their best performance at moderate temperatures.
When a battery is hot from charging, its internal resistance increases
(covered in the next section) which can lead to reduced power output.
Allowing the battery to cool down before use helps to ensure optimal
performance. This process of allowing the battery to cool down before use can
also prolong the life of the battery. This advice should also be tempered with
the knowledge that most modern NiMH batteries are generally designed to handle
some degree of heat; if you need to use the battery immediately after
charging, it's usually safe to do so as long as the battery is not excessively
hot to the touch. However, understand that it may not provide the maximum
level of power output as it would have if it had cooled first.

.. _batteryvoltagesag3:

Internal Resistance
-------------------

Understanding Internal Resistance (IR) requires talking about the discharge
rate of a battery. The discharge rate is a measure of how quickly the battery
can deliver its stored energy. Most NiMH batteries used in *FIRST* Tech
Challenge are rated at a nominal 12V and a maximum discharge rate of 30A,
though that rate is limited by the 20A fuse. A battery's IR refers to any
opposition to that flow of electric current within the battery itself.
Resistance can come from a number of sources, such as resistance within the
battery's chemistry (such as a breakdown of the conductive electrolyte within
the battery), changes to the resistance of the electrodes (such as a buildup of
crystals around the electrodes), resistance added due to connectors and wiring,
and others. Rising IR affects the battery performance primarily in decreasing
the Voltage and Current that the battery can provide, and causes the battery to
generate excess heat when used. The starting IR of a battery can vary among
different manufacturing processes and batches, so much that batteries should
have their IR measured (using a `CTR Battery Beak
<https://www.andymark.com/products/battery-beak-frc-ftc-usage?Intended%20Use=FTC%20(am-3430)&quantity=1>`__,
`West Mountain Radio CBA <https://www.westmountainradio.com/cba.php>`__, or
similarly capable battery tester) at "birth" (when "new" at time of purchase)
and the IR then should be tracked over time. Once the battery's IR increases by
50% from when it was "born", the battery is universally considered ready for
replacement.

.. danger::

  You cannot measure the internal resistance of a battery directly with a
  multimeter. Please do not even try. Doing so will certainly blow your
  multimeter's fuse, and may even damage the multimeter. Please do not
  attempt.  Internal resistance can only be measured indirectly using a
  load-measuring device like a `CTR Battery Beak
  <https://www.andymark.com/products/battery-beak-frc-ftc-usage?Intended%20Use=FTC%20(am-3430)&quantity=1>`__.

What can teams do to slow the increase in a battery's IR? Naturally the
battery's IR will change as the battery ages, increasing due to chemical
changes and wear and tear. The temperature of the battery can also have a
negative effect on IR, higher temperatures cause higher resistance (so keep
your batteries cool!). It's also important to note that the state of charge
of a battery can change the IR, battery IR should always be measured fully
charged. But the most important ways to keep your battery healthy are to
avoid deep discharges (avoid letting your batteries drain below 10V
steady-state, definitely never below 9V!), use a high-quality charger that
prevents batteries from overcharging, follow the battery manufacturer's
recommended charging procedures, and use low-resistance connections (thick
wires and clean connectors!).

Finally, the IR of NiMH batteries can also sometimes be decreased through a
process known as "battery conditioning" (also referred to as "charge
cycling"). If IR within a battery is raised due to crystal formations inside
the battery, this process of conditioning can help break down those crystal
formations and improve Voltage and the flow of current in a battery. Some
chargers have automatic conditioning modes, but always refer to your
manufacturer's recommended procedure for charge cycling your NiMH batteries.

Got any questions about battery voltage sag? Come start or join the
conversation on the `FTC Community Forums
<https://ftc-community.firstinspires.org/>`__!
