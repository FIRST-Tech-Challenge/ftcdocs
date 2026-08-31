Managing Electrical Noise and Static
====================================

Started in the 2023-2024 season, Tech Tips are segments released in the
*FIRST* Tech Challenge `Team E-mail Blast
<https://www.firstinspires.org/resource-library/ftc/team-blast-archive>`__.
Sometimes the Tech Tips are included in whole in the email blast, but sometimes
there is more content than is reasonable in the email blast so partial content
is included in the blast with the rest of the content here.

.. _ferritecore:

Signal Filtering with Ferrite Cores
-----------------------------------

For those about to use sensors, we salute you! This section focuses on signal
noise and how to eliminate it with ferrite cores.

When deciding to use a sensor on a robot, we're normally worried about how
accurate the sensor's detection is, how much the sensor costs, or how the
sensor's protocol will interface with the control system. It isn't until the
device is being mounted to the robot before we consider how outside
electrical noise already present on the robot might significantly impact the
performance of the sensor. This electrical noise almost exclusively comes
from the electric motors and other sources of electric fields on a robot,
such as power wires, power supplies, some sensors (especially ultrasonic
sensors and cameras), radio frequency generators (like the Wi-Fi on the
robot), and other places. This electrical noise can generate unwanted
currents through electromagnetic induction in nearby wires, especially sensor
wires, and these unwanted currents can wreak havoc (create "noise") within
the signals from your sensors. The amount of current induced in the wire
depends on several factors including the strength of the magnetic field, the
rate of change of the field, and the orientation of the wire.

Some buses and wiring are more sensitive to electrical noise than others. On
a *FIRST* Tech Challenge robot, long signal-carrying wires (such as Servo wires
or I2C sensor wires) are most susceptible to induced noise. So how can we
eliminate this noise? The easiest way to remove noise is through the use of a
Ferrite Core. Ferrite Cores, also known as Ferrite Beads, are made of a
ceramic material called ferrite that has incredibly useful magnetic
properties. When a Ferrite Core is clipped around a signal-carrying wire, the
induced "noisy" alternating currents in the wire generate electrical fields
in the ferrite that act to oppose those currents - this has the effect of
canceling out or removing the high-frequency noise. It's not typically
required to "loop" the cable around the ferrite core, but doing so could
increase the efficiency of the noise filtering in cases where excessive noise
is being generated. You can find ferrite cores already installed in cables
meant for high-noise environments or highly sensitive devices such as USB
webcam cables and monitor cables. It's best to place ferrite cores on the
wire closest to the connector leading into the Control/Expansion Hub port.

.. _revgroundingstrap:

The REV Resistive Grounding Strap
---------------------------------

The `REV Resistive Grounding Strap
<https://www.revrobotics.com/rev-31-1269/>`__ (RGS) is the only FTC-legal
means of providing a grounding option for your robot frame or connected
structural elements. Static electricity has two basic behaviors depending on
whether it's building up on a conductive or non-conductive surface; on
non-conductive surfaces like polycarbonate or other plastics static
electricity builds up in "pools", on conductive surfaces like most metals
static electricity spreads and distributes across the entire surface of the
material. Aluminum extrusion used on robots typically has a clear
non-conductive anodized layer used to prevent corrosion of the aluminum but
the aluminum under the layer is conductive. When using the RGS, it's important
to connect the RGS to surfaces where you want to mitigate static buildup. If
mounting the RGS to aluminum on your robot, it's recommended to use a
`multimeter
<https://www.amazon.com/KAIWEETS-Multimeter-Resistance-Capacitance-Temperature/dp/B07SHLS639>`__
to test the continuity between the ring terminal on the RGS to different
places on the robot to determine if the static buildup will be mitigated by
the RGS. If testing for resistivity, remember that the REV Grounding Strap
has a 470 Ohm resistor (with a ~5% tolerance) in-line in the strap - if not
using an auto-range multimeter, be sure to select a range above 600 Ohms to
ensure the resistivity is measured properly. It may be necessary to scrape
the aluminum to create a conductive path between multiple segments of
aluminum, just remember that a non-conductive oxide layer will eventually
form on the exposed aluminum. Remember that if you're probing aluminum
extrusion to check for continuity or resistivity, those areas need to be
scraped to expose bare metal in order to ensure electrical connectivity.
"Jumper wires" screwed to aluminum elements can also be added to ensure
conductivity between components.

Got any questions about electrical noise or static? Come start or join the
conversation on the `FTC Community Forums
<https://ftc-community.firstinspires.org/>`__!
