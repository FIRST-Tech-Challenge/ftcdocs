Battery Ports
--------------

.. danger:: 
   **Never** connect a battery charger directly to the battery port. This will
   void your warranty and fry your hub.

These `XT-30 <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/xt-30-power-cable>`_ 
connectors are used to power your REV Hub as well as all the devices connected to it. 
As the connector is known for its fragility it is highly recommended you be careful when using it.
It is also recommended that you expand your connector prongs periodically. For more information on this 
process please watch this `video <https://www.youtube.com/watch?v=UYXTiSeVmB0>`_. While this video features an XT60, a larger version 
of the XT-30, and a drone the advice is much the same. This port may also be used 
to connect a grounding strap. For more information on legal grounding straps see ``<RE15>``, 
:ref:`Game Manual Part 1 <manuals/game_manuals/game_manuals:game manuals>`. For more information on this port please see 
`REV Documentation <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#input-power-specifications>`_.

Motor Ports
-------------

These `JST-VH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-vh-motor-power>`_ 
style connectors are used to power your motors. There are 4 of these ports 
per hub and they are numbered from 0-3. As you are able to use 8 motors per robot you may 
want to control more than these hubs allow. In that case it is possible for you to use 
an :ref:`additional hub<hardware_and_software_configuration/configuring/configuring_dual_hubs/configuring-dual-hubs:using two expansion hubs>` 
or to use a `REV SPARKmini Motor Controller <https://www.revrobotics.com/rev-31-1230/>`_ 
(REV-31-1230) to power more motors. For more information on this port please see 
`REV Motor Port Documentation <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#motor-port-specifications>`_.


Encoder Ports
--------------

These 4-pin `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`_ 
style connectors are used for your quadrature encoders. There are 4 of these
ports on each hub and they can be used in tandem with the motor they are
adjacent to. However, it is also possible to use this port to connect to a
standalone incremental encoder. To connect to more than 4 encoders it is
currently necessary to connect an additional hub. For more information on this
port please see 
`REV Encoder Port Documentation <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#encoder-port-specifications>`_.

Servo Ports
------------

These 0.1” Header pins are used to power and control your servos. There are 6 ports on each hub and they are numbered from 0-5. 
Be mindful of matching the polarity of the device attached to this port as it is possible to flip the connector. 
For increasing the power supplied to these servos it is possible to use a Servo Power Module that is in compliance with 
``<RE05>``, :ref:`Game Manual Part 1 <manuals/game_manuals/game_manuals:game manuals>`. For more information on this port 
please see `REV Servo Port Documentation <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#servo-port-specifications>`_.

+5V Power Ports
---------------

These 0.1” Header pins are used to power and control various appliances. There
are two ports on each hub. These connectors can be used for a limited range of
applications in FIRST Tech Challenge, such as powering powered USB hubs. For more
information on this port please see 
`REV +5V Power Port Documentation <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#+5v-power-port-specifications>`_ and 
:ref:`Game Manual Part 1 <manuals/game_manuals/game_manuals:game manuals>`.

Analog Ports
--------------

These 4-pin `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`_ 
style connectors are used for your analog inputs. There are 2 of these ports on each hub. These ports 
have 4 channels labeled from 0-4. This port can be used to connect to a standalone analog sensor. A common example of an 
analog sensor is a `potentiometer <https://www.revrobotics.com/rev-31-1155/>`_. An analog sensor is one that outputs a range 
of values rather than digital which alternates between one of two states. For more information on this port please see 
`REV Analog Port Documentation <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#analog-port-specifications>`_.

Digital Ports
---------------

These 4-pin `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`_ 
style connectors are used for your digital inputs. There are 4 of these ports on each hub with a total of 8 channels labeled from `0-7`. 
A device attached to a digital port alternates between one of two states (e.g., on and off). One such device would be a button. It is important
to note that each port has two channels and devices such as the `REV Touch Sensor <https://www.revrobotics.com/rev-31-1425/>`_ will only operate on one channel (N+1).


I2C Ports
---------

.. todo::
   TODO [uvidyadharan]
   Add reference to I2C Driver creation tutorial once migrated

These 4-pin `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`_ 
style connectors are used for connecting I2C sensors. Each port is a single I2C bus where multiple sensors can be 
attached. Using sensors with identical addresses on the same bus can cause problems. The range of I2C sensors that can be connected is limited 
by :ref:`Game Manual Part 1 <manuals/game_manuals/game_manuals:game manuals>`. While it is possible to use a large range of 
sensors, the vast majority of I2C sensors do not have drivers built into the SDK. It is possible to use community drivers 
or create your own. For more information on this port please see 
`REV I2C Port Documentation <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics#i2c-port-specifications>`_.


RS485
-----

These 3-pin `JST-PH <https://docs.revrobotics.com/duo-control/control-system-overview/cables-and-connectors/jst-ph-sensors-and-rs485>`_ 
style connectors are used for serial communication between REV Hubs. You would use this port if you wished to use a second REV Hub 
as described :ref:`in this tutorial <hardware_and_software_configuration/configuring/configuring_dual_hubs/configuring-dual-hubs:using two expansion hubs>`. 
Both RS485 ports can be used to add redundancy by using two cables connecting both ports between the REV Hubs.

UART
-----

This connector is used only for **Developer** (non end user) debugging. Its use is not supported 
by FIRST.

