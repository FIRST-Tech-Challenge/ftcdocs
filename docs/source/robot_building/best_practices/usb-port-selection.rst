USB Port Selection Best Practices
---------------------------------

The :term:`Control Hub` has two USB Type-A ports, one USB 2.0 and one USB 3.0.
They are not interchangeable. The USB 2.0 port shares a bus with the Control
Hub's internal Wi-Fi radio, so an :term:`electrostatic discharge (ESD) <ESD>`
event or other electrical interference on a device plugged into that port can
knock out the radio and disconnect the :term:`Driver Station`. Plugging a
:term:`webcam <Webcam>` into the USB 2.0 port is a common cause of
hard-to-diagnose disconnects during matches.

- Plug :term:`webcams <Webcam>` and other USB devices into the **USB 3.0 port**
  first.
- To connect more than one device, add a powered :term:`USB hub <USB Hub>` to
  the USB 3.0 port instead of using the USB 2.0 port. Make sure to read the
  :term:`Competition Manual` rules about USB power.
- Use USB Type-A-to-C cables with the Control Hub. USB C-to-C cables do not
  work properly with it.
- Strain relieve every USB cable so that a jostled connector cannot generate an
  ESD event or intermittent connection. See
  :ref:`Robot Wiring Best Practices <robot_building/best_practices/robot-best-practices:robot wiring best practices>`.

A powered hub keeps every camera off the radio's bus, and it powers the cameras
instead of the Control Hub. The cost is that the cameras now share one bus.
Lower the resolution or frame rate if they run out of bandwidth. See
:doc:`Managing CPU and Bandwidth <../../apriltag/vision_portal/visionportal_cpu_and_bandwidth/visionportal-cpu-and-bandwidth>`
for measured bandwidth data.

See the :doc:`Control Hub Ports <../../control_hard_compon/rc_components/hub/ports/ch-ports>`
page for a description of all four Control Hub USB ports, and
:doc:`Managing ESD Effects <../../hardware_and_software_configuration/configuring/managing_esd/managing-esd>`
for ESD mitigation.
