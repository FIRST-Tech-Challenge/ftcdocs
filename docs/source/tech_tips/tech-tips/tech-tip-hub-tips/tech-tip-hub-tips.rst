Control and Expansion Hub Tips
==============================

Started in the 2023-2024 season, Tech Tips are segments released in the
*FIRST* Tech Challenge `Team E-mail Blast
<https://www.firstinspires.org/resource-library/ftc/team-blast-archive>`__.
Sometimes the Tech Tips are included in whole in the email blast, but sometimes
there is more content than is reasonable in the email blast so partial content
is included in the blast with the rest of the content here.

.. _controlhubtips:

Port and Wiring Tips
--------------------

This Tech Tip provides useful tips when using Control and Expansion Hubs.

- The RS485 data cable ports that provide data between Control and Expansion
  Hubs are redundant - you can use two data cables utilizing both ports to
  ensure that if one cable fails communications aren't lost.

- Encoder ports 0 and 3 are hardware-counted, but ports 1 and 2 are
  software-counted. This means higher counts-per-revolution encoders (like
  the REV Through-Bore Encoder) should be placed on Ports 0 or 3 to ensure
  counts aren't missed, and lower counts-per-revolution encoders (like the
  goBILDA Odometry Pods or most motors) can be connected to any port.

- Servo port pairs (0,1), (2, 3), and (4,5) each share a common power
  supply, so if you're using higher-current servos (like a goBILDA torque
  servo) directly on the Control or Expansion Hub you should only use ports
  (0, 2, 4) or (1, 3, 5) in order to maximize the power available to each
  servo. If you need to use more than 3 high-current servos per hub,
  consider using a `REV Servo Power Module
  <https://www.revrobotics.com/rev-11-1144/>`__.

- Each Digital and Analog sensor connector on the Control and Expansion Hub
  each have 2 signal channels. Some REV sensors are only designed to be
  configured and used on the N or N+1 channels. Read the documentation for
  each sensor carefully!

- The USB 2.0 port shares the same USB bus as the internal Control Hub
  radio. ESD or other electrical interference that affects devices (like
  webcams) plugged into that port may cause a loss of communications. When
  using a USB webcam, use the USB 3.0 port first.

- USB C-to-C cables do not work properly with the Control Hub, only USB
  A-to-C cables do.

- If you're utilizing the onboard IMU, Do not plug I2C devices into Port 0
  unless absolutely necessary. Port 0 shares an I2C bus with the IMU, and
  misbehaving devices (or devices that don't "play well with others")
  plugged into Port 0 can cause the IMU to stop communicating.

.. _hardwarediagrams:

Hardware Connection Diagrams
----------------------------

Have you ever asked, "How does that get connected?" when working with
*FIRST* Tech Challenge control system components? Stefen Acepcion of *FIRST*
Robotics Competition Team 3161 has graciously compiled several connection
diagrams that demonstrate different ways that common components can be
connected within the *FIRST* Tech Challenge control system.
:ref:`Driver Station connection diagrams
<control_hard_compon/ds_components/index:Driver Station Overview>` and
:ref:`Robot Controller connection diagrams
<control_hard_compon/rc_components/index:Robot Controller Overview>`
can be found on ftc-docs. Stefen has contributed additional
diagrams, including an `Advanced REV Control Hub connection
diagram
<https://ftc-docs.firstinspires.org/en/latest/_downloads/4b186ff4e86995d4783883bf72a90474/B2.pdf>`__
and an `Advanced Smartphone connection diagram
<https://ftc-docs.firstinspires.org/en/latest/_downloads/27dafd353271695f59d8b103142de605/A2.pdf>`__.
These diagrams are chock full of helpful tips, connection techniques, and
information you otherwise can't find in one place - check them out!

Got any questions about the Control and Expansion Hubs? Come start or join the
conversation on the `FTC Community Forums
<https://ftc-community.firstinspires.org/>`__!
