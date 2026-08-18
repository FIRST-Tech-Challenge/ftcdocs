.. meta::
   :title: Updating Components of the FTC Control System
   :description: A comprehensive guide to updating key components of the FIRST Tech Challenge Control System
   :keywords: FTC Docs, FIRST Tech Challenge, FTC, Control System, update

Updating Components of the Control System
=========================================

Components of the *FIRST* Tech Challenge Control System will
periodically receive updates.  
It is recommended teams update each component of the Control System
to the latest released version of firmware, operating system and applications.

The Robot Controller App and the Driver Station App have an update schedule based on the game season.
The season Kickoff SDK Release each year will include new game specific assets such as 
:doc:`AprilTags </apriltag/vision_portal/apriltag_intro/apriltag-intro>`. 

It is recommended to use the 
`REV Hardware Client <https://docs.revrobotics.com/rev-hardware-client/>`__
to update devices if a Windows computer is available. 
Alternate methods can be used to update devices, see the detailed 
instructions linked to below.

.. note::
   The most recent versions of FTC software have the
   latest bugfixes and updates. Teams are encouraged to update their
   software to the most recent version. FIELD STAFF at an FTC Event may not be able to
   provide comprehensive support to teams using older software.

The following table lists the most recent and recommended firmware and operating
system (OS) versions for each core control system module.

.. list-table:: Recommended Versions
   :widths: 50 50
   :header-rows: 1
   
   * - Device
     - Software Version
   * - REV Control Hub
     - Hub Firmware 1.8.2 and Control Hub OS 1.1.2
   * - REV Driver Hub
     - Driver Hub OS 1.2.0
   * - REV Expansion Hub
     - Hub Firmware 1.8.2
   * - REV Servo Hub
     - REV Servo Hub Firmware 25.0.2

A **Robot Controller** should be using the most recent Robot Controller App.
At the start of a new FTC season this should be the Kickoff SDK Release
which normally comes out a few weeks after kickoff.

A **Driver Station** should be using the most recent Driver Station App, 

Regardless of the App versions selected, it is highly recommended that the installed
Robot Controller App and Driver Station App versions match major and minor values
to ensure compatibility as not all software versions are compatible with each other.
e.g. if the Robot Controller App is version 11.1, the the Driver Hub should be
using Driver Station App 11.1.

Teams may choose to run older versions of software without affecting their
robot inspection status at an event. This is not recommended, but allowed.

Teams may also use Android phones as their Robot Controller or Driver Station.
Please see the Competition Manual for permitted devices and the procedure for requesting exceptions.

.. caution::
   Due to unpredictable variations in Android software across different
   manufacturers and updates, the REV Control Hub is the only officially supported
   Robot Controller.
   
   The REV Driver Hub is the only officially supported Driver Station device. 
   Not all phones have hardware driver support for the gamepads that are used in a driver station.
   
   Teams choosing to use an Android phone are responsible for testing and verifying its
   compatibility, functionality, and performance.
   
Update Instructions
-------------------

.. toctree::
    :maxdepth: 1
    
    Updating REV Hardware Client <hardware_client/Updating-REV-Hardware-Client>
    Updating Driver Station App <ds_app/Updating-the-DS-App>
    Updating Robot Controller App <rc_app/Updating-the-RC-App>
    Updating Driver Hub OS <driverhub_os/Updating-the-Driver-Hub-OS>
    Updating Control Hub OS <controlhub_os/Updating-the-Control-Hub-OS>
    Updating Hub Firmware <hub_firmware/Updating-Hub-Firmware>
    
The REV Servo Hub (REV-11-1855) also has firmware that can be 
`updated <https://docs.revrobotics.com/rev-hardware-client/crossover/servo-hub#update-tab>`__
using the REV Hardware Client. Instructions at the REV website.
