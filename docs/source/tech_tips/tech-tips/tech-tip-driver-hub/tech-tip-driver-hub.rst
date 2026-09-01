REV Driver Hub Tips
===================

Started in the 2023-2024 season, Tech Tips are segments released in the
*FIRST* Tech Challenge `Team E-mail Blast
<https://www.firstinspires.org/resource-library/ftc/team-blast-archive>`__.
Sometimes the Tech Tips are included in whole in the email blast, but sometimes
there is more content than is reasonable in the email blast so partial content
is included in the blast with the rest of the content here.

.. _revdriverhubtips:

This Tech Tip is a long one, filled with great REV Driver Hub tips. Most
everything here can be found in REV's Driver Hub Troubleshooting tips page,
we've just annotated a few of these for the most common scenarios you'll
potentially experience with the REV Driver Hub. Understand that this Tech Tip
is not meant to disparage the REV Driver Hub in any way - no device is perfect,
but the REV Driver Hub can provide you trouble-free performance if you can
understand its nuances and take a few additional steps to keep it running
optimally.

Ten Driver Hub Tips
-------------------

1. Make sure your REV Driver Hub time/date is set correctly! This is the cause
   of a number of inspection nightmares and Robot Controller log file
   confusion, the first step should always be to check to make sure the
   Date/Time on the Driver Hub is set correctly. This is set through the normal
   Android System Settings by pulling down the Android Quick Settings pull-down
   twice, tapping the Gear Icon, selecting System, and then selecting "Date &
   Time".

2. USB wall chargers are all the same, right? Wrong. A/C-to-USB wall
   chargers can range drastically in power (measured in Watts) - the REV
   Driver Hub comes with an A/C-to-USB wall charger, and that is the
   recommended wall charger to use to charge the REV Driver Hub. Can you
   use another device to charge the REV Driver Hub? Maybe, but it's best
   to stick to either the one that ships with the REV Driver Hub or a
   fully-charged USB Battery Pack like the `Anker 10,000mA Power Bank
   <https://www.amazon.com/Anker-Portable-Charger-PowerIQ-Battery/dp/B0D5CLSMFB>`__
   which can keep a Driver Hub fully charged all day without ever needing
   to put the Driver Hub to sleep.

3. Rechargeable Lithium batteries don't necessarily work the same way that
   other batteries work, they all have a slightly different usable
   Voltage range. The REV Driver Hub needs to calibrate to the Voltage
   range of the internal lithium battery plugged into it, and to do that
   there's a full `calibration process
   <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting/driver-hub-battery-troubleshooting#battery-calibration>`__
   that has to be followed for any new battery, along with a
   `verification step
   <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting/driver-hub-battery-troubleshooting#battery-verification>`__.
   DO NOT simply "replace" a drained battery with a new charged one when
   it gets low, the new battery is NOT guaranteed to have the same
   calibration as the first and it is not guaranteed to perform
   optimally. If you're having problems keeping the REV Driver Hub
   internal battery charged, consider a USB Battery Pack like the `Anker
   10,000mA Power Bank
   <https://www.amazon.com/Anker-Portable-Charger-PowerIQ-Battery/dp/B0D5CLSMFB>`__.

4. Battery safety in any Lithium Battery system is paramount, and the REV
   Driver Hub has battery safety features that most teams will likely run
   into at least once. The most commonly experienced safety feature is
   the `Battery Lockout system
   <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting/driver-hub-battery-troubleshooting#battery-lockout-recovery>`__.
   If a REV Battery depletes to a level below its recommended safe level,
   or the battery is overcharged, the REV Driver Hub will enter lockout
   mode to protect the battery. In this mode, the REV Driver Hub will not
   power on when the battery button is held down.  The process for
   recovering from Battery Lockout can take several minutes, but it's
   better than the alternative. It's not recommended to leave a REV
   Driver Hub on charge unattended for more than 8-10 hours, and
   definitely NOT for multiple days.

5. When a user puts the REV Driver Hub to sleep, or if it goes to sleep on
   its own because the Driver Station App main screen is not actively
   running in the foreground, it goes to sleep pretty easily. However,
   when the REV Driver Hub returns from a sleep state, sometimes the
   Wi-Fi and the gamepads will not reload correctly or automatically;
   this requires you to unplug and replug the gamepads from the REV
   Driver Hub before you can use them again, or perform a hard reboot in
   order to bring Wi-Fi connectivity back. Many veteran teams use a
   fully-charged USB Battery Pack, like the `Anker 10,000mA Power Bank
   <https://www.amazon.com/Anker-Portable-Charger-PowerIQ-Battery/dp/B0D5CLSMFB>`__,
   and leave the Driver Station App main screen running all day without
   putting the device to sleep.

6. Keep the REV Driver Hub safe by using 3M Dual-Lock or hook-and-loop
   fasteners (like those sold by Velcro Brand) to mount the Driver Hub to
   a `Driver Station Carrier
   <https://www.andymark.com/products/18-in-driver-station-tray>`__. This
   prevents your REV Driver Hub from being placed on the floor (where team
   members may step on it) and prevents you from accidentally dropping the
   Driver Hub on the floor - dropping the Driver Hub is the #1 cause of all
   Driver Hub damage! Some teams have designed their own
   `custom <https://www.thingiverse.com/thing:3386378>`__
   `Driver <https://www.thingiverse.com/thing:5439041>`__
   `Carriers <https://jmhannon.myportfolio.com/ftc-driver-station>`__,
   be creative and have fun!

7. When the REV Driver Hub is not in use (not at competitions, not in use
   during practices) it should be turned OFF and have all sources of
   power disconnected. Do not put the Driver Hub to sleep, but actually
   turn it off - press the power button for 1-2 seconds and then use the
   drop-down menu to turn off the device. The Driver Hub uses power even
   in sleep mode, and that can lead to a dead battery and you may have to
   perform `Battery Lockout Recovery
   <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting/driver-hub-battery-troubleshooting#battery-lockout-recovery>`__
   before you can turn it back on.

8. Sometimes teams may experience "random power loss" on the REV Driver
   Hub. This is usually due to a battery fitment issue within the battery
   box on the device (the battery momentarily stops making a connection
   with the power pins on the device), and can be mitigated using
   `techniques
   <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting#option-1-tape-quick-fix>`__
   from the REV Troubleshooting tips. Some teams have been known to operate
   their REV Driver Hubs without a battery inserted at all, and simply run
   the Driver Hub using a fully-charged USB Battery Pack, like the `Anker
   10,000mA Power Bank
   <https://www.amazon.com/Anker-Portable-Charger-PowerIQ-Battery/dp/B0D5CLSMFB>`__.
   The jury is still out on whether that's a good idea, but worth
   considering if you're having problems that you're desperate to solve and
   REV Support is unable to help you resolve (because of time pressures)
   before your big event.

9. Ensure your REV Driver Hub is fully updated. Firmware 1.2.0 solves a
   host of REV Driver Hub issues, and it makes sense to use the on-board
   updater (once connected to Wi-Fi) to perform all updates on the Driver
   Hub.

10. This isn't specifically a REV Driver Hub tip, but it's a question we get
    asked all the time. Did you know that the Robot Wi-Fi network name
    (Robot Controller Name) and the Wi-Fi passwords can be managed
    straight from within the Driver Station app? With the Driver Station
    App connected via Wi-Fi to the Robot Controller, click on the three
    dots menu on the upper-right and select "Program and Manage", then
    use the hamburger menu on the upper-left and select "Manage". On this
    page you'll find all of the same settings as you'd find on the
    webpage by logging in to the controller on a laptop!

.. _driverhubbatteries:

Why Driver Hub Batteries Aren't Interchangeable
-----------------------------------------------

The tips above cover the REV Driver Hub broadly, but we never really covered
the batteries used in the Driver Hub themselves - and, of course, this topic
was brought up in a team question. The question was, "Why aren't
batteries for the REV Driver Hub interchangeable?"

Well, that wasn't the actual question, as the team didn't know the question
they SHOULD have been asking, but that was the root of the issue. The team
in question had purchased an extra REV Driver Hub battery, charged it, and
was using it as a spare. We've also heard anecdotes from teams who attended
events where FTAs would also purchase spare batteries (or pull batteries
from spare Driver Hubs)  and let teams with depleted batteries use their
charged batteries. However, in each case the teams noted that the spare
battery never lasted as long as their "regular" batteries, often
significantly shorter (half or less). The issue is actually not specific to
the REV Driver Hub, but in the batteries themselves.

I noticed the same thing a few years ago when I owned a smartphone that had
user-replaceable batteries. My phone battery stopped holding a charge, so I
bought a battery online to replace it. However, I noticed that the
replacement battery had a significantly lower "lifespan", meaning it would
go from full charge to near-dead in a shorter period of time versus the
original battery. Over time the battery seemed to "last longer", until after
about a dozen charge cycles it was very close to the original battery's
performance. Did the battery get better, or did my phone adapt to the
battery?

What I didn't know was that minor variances in how batteries are
manufactured, especially in lower-voltage Li-Ion batteries, can affect the
voltage stability of the battery as it depletes (how the voltage of a
battery changes as it's used). In order to know how much battery power is
left, the device needs to know the "charged" voltage, the "depleted"
voltage, and generally needs to understand how the battery voltage changes
from one extreme to the other. Unfortunately this isn't linear, and
differences in a battery's specific internal resistance and other factors
will cause each battery to have different behavior (this occurs in all
batteries, but higher capacity batteries with low internal resistance tend
to show this difference less). The REV Driver Hub performs a
`calibration <https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting/driver-hub-battery-troubleshooting#battery-calibration>`__
phase as it charges a battery, and stores the battery charge characteristics
- that helps it know how the battery should behave when it's being depleted.
In this way the Driver Hub "learns" how to interpret the battery it's
charging so that it can create an accurate charge profile for the battery
as it's used by the device.

When a team replaces the primary battery with a spare, the Driver Hub
doesn't necessarily know that this has happened, and can only apply the
stored discharge characteristics for the primary battery to the new battery.
Unfortunately this often leads to the device misinterpreting the battery and
shutting down before the battery has fully depleted, or thinking there's
more battery left when there really isn't. If the new battery is then
charged, the Driver Hub will calibrate to the new battery, and changing the
battery again will cause the Driver Hub to mischaracterize the original
battery if replaced.

It is highly recommended that all teams use an
`external USB Battery Pack <https://www.amazon.com/Anker-Portable-Charger-Charging-Battery/dp/B0CXDXP8VR>`__
connected to the USB-C port on the Driver Hub to provide consistent power
(use USB-A to USB-C cables only). The battery pack will sustain your Driver
Hub and keep it from being additionally depleted by any high-power-drain
gamepads (such as the Sony DualShock and Sony DualSense gamepads) that your
team may be using.

Got any questions about the REV Driver Hub? Come start or join the
conversation on the `FTC Community Forums
<https://ftc-community.firstinspires.org/>`__!
