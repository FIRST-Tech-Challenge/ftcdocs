Computer Requirements for *FIRST* Programs
==========================================

*FIRST*\ :sup:`®` programs, such as *FIRST*\ :sup:`®` LEGO\ :sup:`®`
League, *FIRST*\ :sup:`®` Tech Challenge, and *FIRST*\ :sup:`®` Robotics
Competition, are as unique as the teams that participate in them. This
uniqueness is partially due to the wide variety of vendors that provide
technologies to the programs, the hardware and software necessary to
manage each program’s distinctive goals, and the constantly evolving
landscape of tools and techniques that teams find useful to participate
and excel. One commonality between programs is the need for teams to
have a computer platform for software development, design, and
collaboration. This document serves as a recommendation for the hardware
and operating system requirements for that computer system.

Of the many factors that can affect the minimum requirements for a
computer, these are the ones that affect those requirements most
heavily:

-  Any role-specific tasks that the computer may perform in the program

-  Type of Computer-Aided Design (CAD) software that may be used on the
   computer

-  Software development and hardware update requirements

-  Vendor-specific application requirements and limitations

Program-Specific Requirements
-----------------------------

Each program has a unique set of requirements, but each of those
requirements can be met with a minimum computer configuration. This
section attempts to identify the minimum requirements for each program’s
roles. Specific recommended hardware that meets each of the requirements
are listed in the “Recommended Hardware Sets” section.

Recommended Computer Hardware for *FIRST*\ :sup:`®` LEGO\ :sup:`®` League
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*FIRST* LEGO League has two divisions which use programmable platforms:
*FIRST* LEGO League Challenge which uses the `LEGO\ ® Education SPIKE\ ™
Prime <https://education.lego.com/en-us/product-resources/spike-prime/downloads/system-requirements/>`__
platform, and *FIRST* LEGO League Explore which uses the `LEGO\ ®
Education SPIKE\ ™
Essential <https://education.lego.com/en-us/products/lego-education-spike-essential-set/45345/>`__
platform. Both platforms have virtually the same computer requirements,
differences are noted below. These platforms are some of the most
accessible, as they are supported by most computer configurations.

*Recommended for Software Development:*

-  `Windows Standard Laptop`_

Also Supported:

-  `MacOS Standard Laptop`_

-  `Chrome OS Standard Laptop`_

-  `iOS Standard Tablet`_

   -  LEGO\ :sup:`®` Education SPIKE™ Essential hub cannot be updated
      with iPad

-  `Android Standard Tablet`_

   -  LEGO\ :sup:`®` Education SPIKE™ Essential not supported

It is also recommended to have an active internet connection to access
the Google Play Store (for Chromebook Android apps), to download in-app
content, to access teacher support materials, and to use certain
features such as live weather data.

Recommended Computer Hardware for *FIRST*\ :sup:`®` Tech Challenge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The predominant hardware platform used in *FIRST* Tech Challenge is the
`REV Control
Hub <https://docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics>`__
and `REV Driver
Hub <https://docs.revrobotics.com/duo-control/control-system-overview/driver-hub-specifications>`__.
These platforms have unique operating system and application
requirements, though it is possible to perform most of the basic
functions with most hardware platforms (albeit with more manual steps).
Teams in *FIRST* Tech Challenge use computers for two basic purposes –
software development and CAD – and team preference in these two uses
shapes the required hardware.

*Recommended for Software Development and CAD:*

-  `Windows Performance Laptop`_



*Recommended for Software Development Only:*

-  `Windows Standard Laptop`_

   -  Only cloud CAD solutions are recommended

      -  OnShape, SolidWorks 3D Experience, etc.


Also Supported:

-  `MacOS Standard Laptop`_

   -  `REV Hardware
      Client <https://docs.revrobotics.com/rev-hardware-client/>`__ not
      supported

      -  Must update manually using browser-based interface

-  `Chrome OS Standard Laptop`_

   -  `REV Hardware
      Client <https://docs.revrobotics.com/rev-hardware-client/>`__ not
      supported

      -  Must update manually using browser-based interface

   -  `Android Studio <https://developer.android.com/studio>`__ not
      supported

      -  Only Blocks and OnBotJava supported

It is also recommended to have an active internet connection during
software development. Access to https://github.com is required by the
REV Hardware Client to download and install required season software
updates and is required for Android Studio users to download software
templates.

Recommended Computer Hardware for *FIRST*\ :sup:`®` Robotics Competition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The predominant hardware platform used in *FIRST* Robotics Competition
is the `NI
roboRIO <https://www.ni.com/docs/en-US/bundle/roborio-20-specs/page/specs.html>`__.
This platform has a unique set of requirements for computer hardware in
competition that may be different than requirements for software
development depending on the programming environment. Like *FIRST* Tech
Challenge, teams in *FIRST* Robotics Competition use software
development computers for two basic purposes – software development and
CAD – and team preferences in these two uses shape the required
hardware. However, in *FIRST* Robotics Competition there are two roles
that computers can serve, such as Software and Design Development
platforms and/or Driver Station platforms, and those roles also shape
the requirements of the computer hardware.

It is recommended to have two separate computers, one to use for the
Driver Station platform and another for Software and Design Development,
though one laptop can be used for both purposes if necessary.

Driver Station
^^^^^^^^^^^^^^

The driver station computer is used as the primary interface to the
robot, is used to interface with the Field Management System (FMS) at an
event and is limited by the software tools used to communicate with the
hardware and software platform on the robot. Teams find it advantageous
to have separate computers for the Driver Station role and for the
Software and Design Development role to enable them to segregate the
duties and physical demands of the systems at an event. Budget-conscious
teams can certainly use a single computer for both roles if that
computer at least meets the minimum requirements of the Driver Station
role. Note that the Driver Station role requires a Windows operating
system, as the applications required to perform the role's duties are
Windows-only applications.

*Recommended for the Driver Station role:*

-  `Windows Standard Laptop`_


Also Supported:

-  `Windows Performance Laptop`_

Software Development and Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Like *FIRST* Tech Challenge, *FIRST* Robotics Competition teams use
Software Development and Design laptops for Software Development and
CAD, and depending on the use of CAD the hardware requirements are
slightly different:

*Recommended for the Software and Design Development role with CAD:*

-  `Windows Performance Laptop`_


*Recommended for Software Development Only:*

-  `Windows Standard Laptop`_

   -  Only cloud CAD solutions are recommended

      -  OnShape, SolidWorks 3D Experience, etc.


Also Supported:

-  `MacOS Standard Laptop`_

   -  `REV Hardware
      Client <https://docs.revrobotics.com/rev-hardware-client/>`__ not
      supported

   -  `LabVIEW <https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/labview-setup.html>`__
      software not supported

It is also recommended to have an active internet connection during
software development. Access to https://github.com is required by the
REV Hardware Client to download and install required season software and
firmware updates. Additional software may have similar requirements.

Recommended Hardware Sets
-------------------------

These are the Recommended Hardware sets referenced by the
Program-Specific Requirements. There are a few extra requirements and
recommendations for all hardware platforms, such as:

*Windows Operating System*

-  Support for Windows 10 is ending in mid-2025, so purchasing a Windows
   system that supports Windows 11 is highly recommended. While not all
   software is specifically labeled as being supported by Windows 11,
   virtually all the required software has been tested to work with
   Windows 11.


*USB Ports*

-  Laptops should have at least 2 available physical USB-A ports.

-  For *FIRST* Tech Challenge, USB-C ports on laptops are not able to
   work properly with the REV Control Hub nor REV Driver Hub, so it is
   important to have USB-A ports also available.


*Bluetooth*

-  For *FIRST* LEGO League, it is important that laptops and tablets
   support Bluetooth 4.0 or above.


*Physical Ethernet Ports*

-  While most features of hardware and software can be easily supported
   by Wi-Fi, in some situations (such as the Driver Station for *FIRST*
   Robotics Competition) having a physical RJ-45 ethernet port on the
   system is a huge benefit.


*SSD Hard Drive*

-  While not specifically required, hard drives that use SSD technology
   (versus spinning disk technology) boot up faster and are less likely
   to be damaged when carrying while powered on or experiences
   “unexpected bumps” as is common for a *FIRST* Robotics Competition
   Driver Station computer.

**Windows Performance Laptop**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A laptop designed for high graphics performance containing a high-end
processor, like a `Dell
G16 <https://www.dell.com/en-us/shop/dell-laptops/g16-gaming-laptop/spd/g-series-16-7630-laptop>`__
or `HP
Omen <https://www.hp.com/us-en/shop/pdp/omen-gaming-laptop-16-xf0087nr>`__,
with the following recommended specs:

-  Processor: Intel Core i7, AMD Ryzen 7, or better

-  Graphics: NVIDIA GeForce RTX 4050 or better

-  Memory: 16GB RAM or more, 32GB preferred

-  Storage: 512 GB SSD or greater, 1TB SSD preferred

-  Ethernet: RJ-45 Ethernet Port preferred

-  Ports: 2 or more USB type A ports preferred

-  Bluetooth: Bluetooth 4.0 or better

-  Wi-Fi: Integrated Wi-Fi, Wi-Fi 6E or better preferred

-  Operating System: Windows 10 or better, Windows 11 preferred

**Windows Standard Laptop**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A standard Windows laptop, like a `Dell Inspiron
15 <https://www.dell.com/en-us/shop/dell-laptops/inspiron-15-laptop/spd/inspiron-15-3530-laptop>`__
or `HP Pavilion
Laptop <https://www.hp.com/us-en/shop/mdp/laptops/pavilion-15-344522--1>`__,
designed for smooth performance and everyday tasks,

-  Processor: Intel Core i5, AMD Ryzen 5, or better

-  Graphics: Intel or AMD embedded graphics adapter or better

-  Memory: 8GB RAM or more, 16GB preferred

-  Storage: 256GB or greater, 512 GB SSD preferred

-  Ethernet: RJ-45 Ethernet Port preferred

-  Ports: 2 or more USB type A ports preferred

-  Bluetooth: Bluetooth 4.0 or better

-  Wi-Fi: Integrated Wi-Fi, Wi-Fi 6E or better preferred

-  Operating System: Windows 10 or better, Windows 11 preferred

**MacOS Standard Laptop**
~~~~~~~~~~~~~~~~~~~~~~~~~

A standard MacOS laptop, like a `MacBook
Air <https://www.apple.com/shop/buy-mac/macbook-air>`__ or `MacBook
Pro <https://www.apple.com/shop/buy-mac/macbook-pro>`__,
designed for smooth performance and everyday tasks.

-  Processor: Apple M1 or better, Apple M2 preferred

-  Memory: 4GB RAM or more

-  Storage: 2GB available storage space or better

-  Bluetooth: Bluetooth 4.0 or better

-  Operating System: MacOS Mojave 10.14 or newer

**iOS Standard Tablet**
~~~~~~~~~~~~~~~~~~~~~~~

A standard iOS tablet, such as an iPad Air 2 or iPad Mini 4 or newer.

-  Operating System: iOS 13 or newer

**Chrome OS Standard Laptop**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A standard Chromebook, such as the `Samsung Galaxy Chromebook
2 <https://www.google.com/chromebook/discover/pdp-samsung-galaxy-chromebook-2/sku-samsung-galaxy-chromebook-2-8gb-128gb/>`__,
or similar.

-  Processor: 1.40 GHz Intel Celeron 2955U dual-core processor or better

-  Memory: 4GB RAM or better

-  Storage: 3GB available storage space or better

-  Bluetooth: Bluetooth 4.0 or above

-  Operating System: Android 7.0 or newer

**Android Standard Tablet**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A standard Android Tablet, such as the `Samsung Galaxy Tab A7
Lite <https://www.samsung.com/us/tablets/galaxy-tab-a/galaxy-tab-a7-10-4-inch-gray-64gb-wi-fi-sm-t500nzaexar/>`__,
or similar.

-  8” display or larger

-  Memory: 3GB RAM or better

-  Storage: 3GB available storage space or better

-  Bluetooth: Bluetooth 4.0 or above

-  Operating System: Android 7.0 or newer
