.. meta::
   :title: Control System Troubleshooting Guide
   :description: A guide to diagnosing and resolving problems with the FIRST Tech Challenge wireless Control System, for teams and technical volunteers.
   :keywords: FTC Control System, Wi-Fi, troubleshooting, FTA, CSA, WTA, Driver Station, Robot Controller

Control System Troubleshooting Guide
=====================================

*FIRST* Tech Challenge uses an Android-based Control System for its robot
competition. Teams are responsible for bringing, maintaining, and
troubleshooting their own wireless Control System, but at an event they may
need help from a FIRST Technical Advisor (FTA), Control System Advisor (CSA),
and/or Wi-Fi Technical Advisor (WTA). This guide provides tips and procedures
for avoiding, diagnosing, and resolving common problems with the wireless
Control System, both for teams and for the technical volunteers who support
them at events.

This guide assumes you already have a basic understanding of the Control
System's components. For an introduction to the Driver Station, Robot
Controller, Control Hub, and Driver Hub, see
:doc:`/programming_resources/shared/control_system_intro/The-FTC-Control-System`.

.. toctree::
   :maxdepth: 1

   wifi_technology/wifi-technology
   monitoring_wireless_environment/monitoring-wireless-environment
   troubleshooting_wireless_at_events/troubleshooting-wireless-at-events
   wifi_channel_planning/wifi-channel-planning
   troubleshooting_common_issues/troubleshooting-common-issues
   wireshark_packet_capture/wireshark-packet-capture
   using_log_files/using-log-files

Mitigating Disruptions Due to Electrostatic Shocks
---------------------------------------------------

Electrostatic discharge (ESD) events have the potential to disrupt the
normal operation of a competition robot. The
:doc:`/hardware_and_software_configuration/configuring/managing_esd/managing-esd`
article provides a comprehensive discussion of this topic. Key takeaways
include:

- ESD is bad for robots.
- To mitigate the risks:

  - Treat tile floors with anti-static spray or water.
  - Use ferrite chokes to dampen ESD effects.
  - Electrically isolate electronics from the metal frame of the robot.
  - Ground electronics to the metal frame using approved grounding cables.

Getting Additional Help
------------------------

If you have questions about the *FIRST* Tech Challenge Control System, visit
the `FIRST Tech Challenge community forum <https://ftc-community.firstinspires.org/>`__
and search for related posts or post your own questions.

There is also a *FIRST* Tech Challenge Technology Slack Workspace reserved
for *FIRST* Tech Challenge technical volunteers (FTAs, CSAs, and WTAs) where
these volunteers can ask questions and exchange information with other
volunteers and with *FIRST* Tech Challenge staff. Prior to an event,
technical volunteers should visit this workspace to get any last-minute
information from other volunteers and from *FIRST* regarding event support
and technical troubleshooting tips.
