Robot Battery Care, Charging, and Fuses
=======================================

Started in the 2023-2024 season, Tech Tips are segments released in the
*FIRST* Tech Challenge `Team E-mail Blast
<https://www.firstinspires.org/resource-library/ftc/team-blast-archive>`__.
Sometimes the Tech Tips are included in whole in the email blast, but sometimes
there is more content than is reasonable in the email blast so partial content
is included in the blast with the rest of the content here.

.. _batteryCharging:

Battery Charging
----------------

There are :ref:`three robot main batteries
<control_hard_compon/rc_components/power_distr/power-distr:robot main battery>`
that are legal to use in *FIRST* Tech Challenge, and they are all
3000mAh NiMH batteries with an attached 20A fuse. However, the manufacturers
of the batteries have different battery chargers and different recommended
charging settings for the batteries. When charging the `TETRIX MAX 12-Volt
battery
<https://www.pitsco.com/products/TETRIX-12-Volt-Rechargeable-NiMH-Battery-Pack>`__,
on the battery the manufacturer recommends charging at the 0.9A charge rate
(the lowest setting on most selectable battery chargers) using the `Global
NiMH battery pack charger
<https://www.gobilda.com/battery-charger-nicad-nimh-12-1/>`__.  The `Matrix
12-Volt battery
<https://www.gobilda.com/matrix-12v-3000mah-nimh-battery/>`__ with the same
form factor is recommended to be charged with the `goBILDA 12V battery
charger <https://www.gobilda.com/battery-charger-nicad-nimh-12-1/>`__, which
does not have a user-selectable charge rate switch but has a max charge rate
of 1.0A.  However, the `REV 12-Volt Slim Battery
<https://www.revrobotics.com/rev-31-1302/>`__ is recommended to be charged
with the `REV Battery Charger <https://www.revrobotics.com/duo/electronics/power-system/>`__
using the 1.8A charge rate setting. To ensure safety, proper charging, and a
long battery life, make sure you're charging your batteries at the
manufacturer's recommended charge rates!

.. _batterytips1:

Battery Maintenance
-------------------

Nickel-Metal Hydride (NiMH or Ni-MH) batteries, like those used in *FIRST* Tech
Challenge, do require periodic maintenance to keep them healthy! Every day,
NiMH batteries lose on average 1% of their charge capacity at normal room
temperature - at colder temperatures this decline slows a bit but does not stop
it. This means that every 2-3 months it's important to recharge your batteries
to keep them healthy - there is no off-season for batteries! It's also
recommended to mark your batteries with tape and a sharpie to mark (1) Your
team number (never lose a battery at a competition!), (2) What year the battery
was purchased, (3) Give your batteries names so you can differentiate batteries
easily, and (4) optionally provide a tick mark each time the battery is
recharged. NiMH batteries can generally last 200-300 recharge cycles before
their internal resistance declines to the point where it's time to replace
them, and keeping track of charge cycles is an easy way to track how "used"
the battery is before needing to have its internal resistance checked.

.. _batteryfuses:

Battery Fuses
-------------

Every legal Main Robot Battery in *FIRST* Tech Challenge is required to have an
in-line replaceable fuse on the battery, you'll find the fuse housing on the
red (positive) cable on your battery between the battery and the connector
(the top lifts off, exposing the fuse). This fuse helps protect your battery
and your electronics from prolonged or excessive over-current. The fuse used
with all legal batteries is a `20A Automotive-Mini (ATM) blade-style fuse
<https://www.amazon.com/Bussmann-Blade-Fuses-BP-ATM-20-RP/dp/B00JCB4WTS>`__,
and can be found in virtually every auto parts store. It has a yellow-colored
housing which easily identifies it as a 20A fuse. If you find that your
battery's voltage suddenly drops to zero (when tested using a `battery tester
<https://www.andymark.com/products/battery-beak-frc-ftc-usage?Intended%20Use=FTC%20(am-3430)&quantity=1>`__
or multimeter) it's probably because you've blown your battery's in-line
fuse.

A fuse is a short span of specially-designed electrical wire intended to
carry electrical loads up to a very specific amount of current. When the
current loads exceed the rating, the wire within the fuse begins heating up -
the more the load exceeds the rating, the hotter the wire will get.
Eventually the wire will heat up so much it self-destructs and melts or burns
up, breaking the circuit. This fuse-melting condition is often called
"Blowing a Fuse"; the fuse is thus destroyed and is no longer usable, but it
protected the electronics in the circuit as its last selfless act.

How does a battery fuse get blown? These are two of the most common reasons
why a fuse can be blown:

- **Overcurrent Conditions** - The Robot has components (generally actuators,
  like servos and motors) that can pull a combined current that is more than
  the robot's electrical circuit can safely carry. The main electrical power
  wires on a robot are required to be a minimum 18AWG, which can easily
  continuously carry up to 16A of current. When components pull a combined
  current far exceeding this limit, generating unsafe heat in excess of what
  the wires can tolerate (risking melting the wire insulation which could lead
  to short circuits and fire), the fuse blows to protect the circuit. The wire
  size and fuse limit has been carefully selected for the safety of the robot's
  electrical system.

- **Short Circuits** - Usually this happens if unshielded wires of opposite
  polarity touch each other in the robot's electrical system, like when
  performing electrical maintenance on switches or wires (ALWAYS unplug the
  battery before performing any maintenance on a robot!). Other causes can be
  failed electronics and damaged components. This causes an extremely high
  current load to travel through the battery, near-instantly causing the fuse
  to blow. When replacing the connector on a battery, ALWAYS remove the fuse
  prior to performing any work - this protects the person doing the maintenance
  AND protects the fuse!

Always make sure your main battery fuse is replaced with the proper fuse (20A
for *FIRST* Tech Challenge) and make sure you're always following all safety
guidelines when working with your robot's electrical system!

Got any questions about battery care? Come start or join the conversation on
the `FTC Community Forums <https://ftc-community.firstinspires.org/>`__!
