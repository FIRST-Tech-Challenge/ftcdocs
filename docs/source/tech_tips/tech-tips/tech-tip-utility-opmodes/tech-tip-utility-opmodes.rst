Testing Your Robot with Utility OpModes
=======================================

Started in the 2023-2024 season, Tech Tips are segments released in the
*FIRST* Tech Challenge `Team E-mail Blast
<https://www.firstinspires.org/resources/library/ftc/team-email-blast-archive>`__.
Sometimes the Tech Tips are included in whole in the email blast, but sometimes
there is more content than is reasonable in the email blast so partial content
is included in the blast with the rest of the content here.

.. _utilityopmodes:

Introduction to Utility OpModes
-------------------------------

Starting with version 11.2 of the *FIRST* Tech Challenge :term:`SDK`, a new
kind of :term:`OpMode` is available: 
:doc:`Utility OpModes </utility_opmodes/index>`. Utility OpModes are
designed to help teams test everything connected to their system, from
actuators to :term:`sensors <Sensor>` - including :term:`gamepads <Gamepad>`
connected to the :term:`Driver Station App`. These special OpModes can be 
run directly from the Driver Station App.

Two Utility OpModes are available today:

* **Test Hardware** - lets you cycle through the hardware in your robot
  configuration and set values, so you can verify that everything is working as
  intended. See the
  :doc:`Test Hardware Utility </utility_opmodes/test_hardware/test_hardware_utility>`
  documentation.
* **Test Gamepad** - shows how gamepad inputs are registering in the SDK. See
  the
  :doc:`Test Gamepad Utility </utility_opmodes/test_gamepad/test_gamepad_utility>`
  documentation.

Teams can also create their own Utility OpModes, in Java or in Blocks. The
:doc:`Utility OpModes </utility_opmodes/index>` page has the details.

Why is this important?

Gamepad Utility OpMode
----------------------

In the BIOBUZZ Competition Manual, the rule limiting the gamepads that teams
could use was removed - the rule was never *really* about limiting what gamepads
teams could use, but more about steering teams towards the gamepads that had full
support within the FTC SDK. Gamepads in Android are supported by drivers found 
in one of two places - in the client app, or in the Android Kernel. Gamepad 
support in Android, for the most part, is hit-or-miss - the FTC SDK implemented 
drivers for all of the standard gamepads that have previously been supported, 
because teams found the drivers provided by the Android Kernel to be extremely
buggy and poorly supported. Some of this support has gotten better in newer
Android Kernels, but by and large this has been untested. The REV Driver
Hub uses the Android 10 kernel; newer devices (such as Android Smartphones) may
use newer versions of Android and *possibly* might have better support.

In the :ref:`Gamepad Best Practices <robot_building/best_practices/robot-best-practices:gamepad best practices>` 
section, it describes how to determine whether or not the driver the gamepad
currently plugged in is using a Kernel driver or a Client (FTC SDK) driver (if the
gamepad icon is colored orange, an Android Kernel Driver is being used). That
is, assuming the device is detected at all. This only tells you that the gamepad
might not be fully supported - at least according to the FTC SDK. To determine if 
the driver is *actually* working, you've got to test it yourself. The most common
easy way to determine there might be issues is if the gamepad buttons aren't mapped
properly, meaning when you press the "A" button maybe the "X" button registers as
being pressed, or perhaps no buttons are registered as pressed. You COULD write
a simple OpMode that tests button presses, OR you could just use the "Test Gamepad"
Utility OpMode - that's its intended use. 

The utility can only tell you what's being registered when you press a button; it
cannot remap buttons or swap things around. The Driver Station App cannot be 
modified, so you cannot edit or write your own drivers for the FTC SDK. If the
gamepad you wanted to use doesn't work, then you should consider using one of the 
known good gamepads that the FTC SDK has excellent driver support for. But hopefully
this utility can give you a quick sanity check whether or not your gamepad will
at least register the correct button presses - whether the gamepad will work 
flawlessly over the course of its use in FTC is another thing completely.

Got any questions about Utility OpModes? Come start or join the conversation on
the `FTC Community Forums <https://ftc-community.firstinspires.org/>`__!
