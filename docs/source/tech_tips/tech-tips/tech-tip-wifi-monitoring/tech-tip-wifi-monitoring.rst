Monitoring Your Robot's Wi-Fi Connection
========================================

Started in the 2023-2024 season, Tech Tips are segments released in the
*FIRST* Tech Challenge `Team E-mail Blast
<https://www.firstinspires.org/resource-library/ftc/team-blast-archive>`__.
Sometimes the Tech Tips are included in whole in the email blast, but sometimes
there is more content than is reasonable in the email blast so partial content
is included in the blast with the rest of the content here.

.. _wifimonitoring:

One common question we get is how to determine the Wi-Fi signal strength
between the Driver Station and the Robot. Because there are a lot of factors
that can play into your robot performance on the field, it's important to know
that your robot is getting the strongest Wi-Fi signal possible. The
:ref:`FTC Driver Station App
<ftc_sdk/updating/ds_app/Updating-the-DS-App:Updating the Driver Station App>`
reports three related pieces of information: Signal Strength, Link Speed, and
the Signal Bar Graph.

.. _wifisignalstrength:

Wi-Fi Signal Strength
---------------------

Wi-Fi signal strength is measured in dBm (decibel-milliWatts) and is always
negative. Typically the range for Wi-Fi is -30dBm to -90dBm; -30dBm is the
maximum possible signal strength, and -90dBm is considered too weak of a
signal to support Wi-Fi communications. dBm is measured on a logarithmic
scale, so comparing dBm values differs from what you would normally consider
on a linear scale. Increments of 3dBm indicate doubling/halving signal
strength, and increments of 10dBm indicate 10x change in signal strength.
For example, a signal strength of -40dBm is twice as strong as a signal
strength of -43dBm, and a signal strength of -67dBm is one-tenth the signal
strength of -57dBm. Signal strengths around -40dBm are Amazing, but rarely
achievable in match play. A strength of -60dBm is still considered Very
Good. -67dBm is considered Good. -70dBm is considered Okay. Anything less
than -80dBm is considered unusable.

To see the Signal Strength between your Driver Station and the Robot
Controller, first ensure that the robot is connected within the Driver
Station App. At the top of the Driver Station App is a readout that shows
the connected network name, and under it are Ping times and the Channel
number of the Wi-Fi connection. Tap that area of the app, and the display
will change and instead show the signal strength under the connected network
name. Tap again to swap back.

Knowing your Signal Strength can help you understand how metal on your robot
might be affecting your Wi-Fi connection, understand how your robot's signal
may vary depending on the orientation of the robot to the Driver Station,
and how external factors (like placing your Driver Station on a metal music
stand) can degrade the signal strength. Remember that ensuring a strong
Wi-Fi signal strength is just one factor in maintaining optimal robot
health.

.. _wifilinkspeed:

Link Speed and the Signal Bar Graph
-----------------------------------

Link Speed is the speed (in Mbps) at which a Wi-Fi connection can
communicate, and it generally ranges from a snail-like 1Mbps through about
100Mbps, which is the maximum practical rate for an 802.11ac/b/g/n/w Wi-Fi
network (when using a Control Hub and Driver Hub). It's important to
understand the difference between Signal Strength and Link Speed. Signal
Strength is often used to describe how "loud" a connection is, and Link
Speed is used to describe how "fast" a connection can communicate. Link
Speed can also be a secondary indicator of how much "noise" or
"interference" a communication channel has; the "louder" the signal and
"clearer" the communication channel, the "faster" the devices can generally
communicate. Wi-Fi link speeds are automatically renegotiated periodically
and they're most often affected by noise, channel congestion (too much
happening at once), and distance.

A Wi-Fi channel is like a room where only one person/device is ever allowed
to talk at a time. If each person/device can talk in short, fast bursts
(fast link speed) then everyone has an opportunity to speak within a short
duration of when they want to speak. However, if one or more devices are
speaking slowly (slow link speed) then all devices have to wait for them to
finish before they can talk REGARDLESS of their own link speeds - this
invariably introduces communications lag. This example highlights the fact
that even though it's important for a given device to have a strong signal
and a fast link speed, it's important for ALL devices communicating on a
channel to have a strong signal and fast link speed. As the idiom goes, it
only takes one rotten apple to spoil the whole bunch.

Finally the Signal "Bar" Graph attempts to combine the Signal Strength and
Link Speed into an easy to understand graphical meter. The more bars, the
stronger and clearer the signal and the faster the communications.

.. note::
   The `Driver Hub <https://www.revrobotics.com/rev-31-1596/>`__ has
   a known bug where the Link Speed indicator only shows the initially
   negotiated link speed, and the link speed indicated does not change when the
   Wi-Fi device renegotiates different link speeds. This means the Link Speed
   indicator and the Bar graph are not represented accurately on Driver Hubs,
   but are represented accurately on smartphones.

Got any questions about monitoring your robot's Wi-Fi? Come start or join the
conversation on the `FTC Community Forums
<https://ftc-community.firstinspires.org/>`__!
