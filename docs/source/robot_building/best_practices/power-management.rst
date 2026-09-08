Power Management Best Practices
-------------------------------

Given the extensive amount of motors and servos allowed on a ROBOT, teams are
encouraged to consider the total power available from the ROBOT battery during
the design and build of the ROBOT. Drawing large amounts of current from many
motors and/or servos at the same time could lead to drops in ROBOT battery
voltage that may result in exceeding the battery fuse limits or browning out
the control system leading to power loss or communications loss. It is
suggested that teams measure their power draw and ensure that they are staying
below the 20A fuse limit. This is an incomplete list of devices and systems
that can draw significant amounts of current from the ROBOT battery:
- Flywheels
- Servo Power Injectors
- LED systems on a ROBOT
- Cameras (It is recommended to only power 2 cameras directly off USB, and to use a powered USB hub)

See the :doc:`Power Distribution <../../control_hard_compon/rc_components/power_distr/power-distr>` page for background on power ports.
