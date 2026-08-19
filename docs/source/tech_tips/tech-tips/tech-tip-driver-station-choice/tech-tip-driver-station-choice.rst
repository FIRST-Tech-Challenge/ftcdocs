Driver Hub or Smartphone?
=========================

Started in the 2023-2024 season, Tech Tips are segments released in the
*FIRST* Tech Challenge `Team E-mail Blast
<https://www.firstinspires.org/resource-library/ftc/team-blast-archive>`__.
Sometimes the Tech Tips are included in whole in the email blast, but sometimes
there is more content than is reasonable in the email blast so partial content
is included in the blast with the rest of the content here.

.. _huborphone:

This Tech Tip briefly discusses the pros and cons of Smartphones versus the
Driver Hub. Which one should you use? Are there hidden benefits or perils for
using one over the other?

.. important:: Only the REV Driver Hub is officially supported as a Driver
   Station. A SmartPhone is legal to use in competition, but it is not
   supported - teams who use one are responsible for all of their own
   testing and troubleshooting.

The REV Driver Hub
------------------

The REV Driver Hub is the standard *FIRST* Tech Challenge Driver Station
hardware device. It boasts three USB-A ports for plugging in gamepads,
a USB-C port used for communication and charging, a large touch screen,
and an unused Ethernet port (for future-proofing). This device runs the
Android operating system, maintained by REV Robotics, and uses Wi-Fi
to communicate with the REV Control Hub.

**Driver Hub Pros**

- Driver Hub and Control Hub combo use 802.11w for communications.
  SmartPhones do not support 802.11w communications.

  - 802.11w offers encryption of control packets, which prevents many
    Wi-Fi attacks by remote routers/devices.

- Driver Hub is a "standard" *FIRST* Tech Challenge Driver Station device,
  which provides long-term support for *FIRST* Tech Challenge. The average
  SmartPhone is deprecated within 2 years after being released, but the
  Driver Hub has long-term support in *FIRST* Tech Challenge.

- Driver Hub has a USB-C port, which allows for charging while it's being
  used.

  - USB-C port allows use of external battery packs, which are necessary
    for sustained use of PS4 and PS5 gamepads which leech power from the
    Driver Station to charge their own internal batteries.

  - A single 10,000mAh External battery pack allows Control Hub to be
    used non-stop over the course of an entire day.

- Driver Hub has 3 USB-A ports, so no external USB hubs and additional
  cables are required for using multiple USB gamepads. This makes the
  Driver Hub very compact and easy to manage.

**Driver Hub Cons**

- Driver Hub still has Power Management issues

  - Driver Hub needs battery compartment tweak to ensure internal battery
    makes good connection. Foam insert in battery compartment helps, but
    doesn't always perfectly fix the problem.

  - Driver Hub cannot boot if the internal battery is too low, even if
    plugged into external battery. If battery dies, troubleshooting
    requires removal of battery to power device.

  - Power Management bugs can drain battery while charging.

- Driver Hub USB ports are fragile

  - Teams carrying their Driver Hubs around without a Driver Station tray
    (NOT RECOMMENDED) have dropped their Driver Hubs with gamepads plugged
    in, and impact can damage USB-A ports.

- Display screen ribbon cable comes loose

  - If the screen stops working, opening the back of the device and
    re-seating the screen ribbon cable can sometimes fix screen issues.

- Turning off the display unloads gamepad drivers, but turning the display
  back on does not reload them. USB devices must be re-plugged in order to
  trigger USB driver loading.

- USB-C to USB-C cables do not work with Driver Hub. USB-A to USB-C cables
  are required in order to use the USB-C port.

SmartPhones
-----------

On the other hand, off-the-shelf SmartPhones can also be used. These
devices, like the REV Driver Hub, run the Android mobile operating system
and use Wi-Fi to talk to the REV Control Hub (therefore no SIM card or cell
plan is required). SmartPhones use USB-OTG to interface with gamepads and
external USB hubs necessary for operating multiple gamepads.

**SmartPhone Pros**

- SmartPhones are typically cheaper than Driver Hubs, and generally survive
  being dropped better.

- SmartPhones don't have the same power management issues that Driver Hubs
  are known to have.

- Some teams report having better Wi-Fi consistency with SmartPhones than
  Driver Hubs, though that has not been verified or debunked in any way.

**SmartPhone Cons**

- SmartPhones are not officially supported in *FIRST* Tech Challenge.
  Teams who use one are on their own for testing and troubleshooting.

- Older SmartPhones are often no longer supported by the manufacturers
  of the phones.

  - SmartPhones are deprecated typically within 2 years after being
    released. Security updates and OS updates are not guaranteed.

  - Once a model is discontinued, replacements become increasingly
    difficult to obtain.

- Android is not a consistent platform in the Mobile Phone industry. Each
  manufacturer, and sometimes even within product families, will produce
  their own "flavor" of Android which has different software requirements
  and behaviors. Supporting the different manufacturers in the changing
  Android landscape is near impossible.

  - There is very little consistency between smartphones of the same
    model sold in different countries - each will have their own
    firmware with their own quirks, often impossible to debug or avoid.

  - *FIRST* Tech Challenge is not enough of a volume consumer to be able to
    set requirements or have partnerships with SmartPhone manufacturers.

- SmartPhones cannot use 802.11w for encryption of Wi-Fi control packets,
  which makes the connection between devices vulnerable. Rogue Access Point
  Detection and Quarantine features within venue network security systems
  (like within schools and other venues) can interrupt these communications
  seemingly randomly, making connections difficult to maintain.

- SmartPhones cannot be used at the same time they're being charged, so
  teams frequently run down the internal batteries on the phones during the
  course of an event. Careful battery management is required.

  - PS4 and PS5 gamepads with internal batteries will further drain the
    SmartPhone batteries, as they leech power from the Driver Station in
    order to maintain a full charge level for their own batteries.

- SmartPhones require USB-OTG cables and external USB Hubs are also
  required in order to use multiple gamepads, and each cable/connection
  and device is a potential source of failure. Extreme care must be taken
  to ensure the connections remain solid.

Got any questions about choosing a Driver Station device? Come start or join
the conversation on the `FTC Community Forums
<https://ftc-community.firstinspires.org/>`__!
