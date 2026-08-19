Servo Power Usage Best Practices
---------------------------------
There are many best practices that teams should keep in mind regarding servo usage.

Voltage Compatibility
^^^^^^^^^^^^^^^^^^^^^
It is important to make sure that the servo you are using is compatible with
the port you are plugging it into. Most servos are designed to accept a range
of voltages which you can find in the spec sheet from the manufacturer. The REV
Control Hub and the REV Expansion Hub both provide 5V to servos, while the
goBILDA Servo Power Injector, REV Servo Power Module, Studica Servo Power
Block, and REV Servo Hub all provide 6V.

Current Draw Limits
^^^^^^^^^^^^^^^^^^^
Each pair of servo ports on the REV Control Hub and REV Expansion Hub is
limited to 2A. Additionally, the 6 servo ports and +5V auxiliary part have a
maximum of 5A total. Therefore, it is recommended to only place servos on ODD
or EVEN ports, and not both, which means only placing up to 3 servos on each
Control or Expansion hub. Teams should also be mindful of the 20A fuse on the
which limits the full electrical system.

Power Source
^^^^^^^^^^^^
The power from each servo port is only for powering servos connected to that
port, and servos should only be powered for the servo port they are connected
to. The Competition Manual prohibits teams from mixing power between devices.

See the :doc:`Servos <../../control_hard_compon/rc_components/servos/servos>` page for background on servo ports and power.
