Utility OpModes
===============

Starting with version 11.2 of the *FIRST* Tech Challenge :term:`SDK <SDK>`,
Utility :term:`OpModes <OpMode>` are available to help test and troubleshoot
your robot. Utility OpModes can be run from the :term:`Driver Station App`.
This category of OpMode is for OpModes that are not meant for competition,
and thus shouldn't clutter the AUTO or TELEOP menus, but instead are 
OpModes that your team would use for maintenance or "utility" needs.

These OpModes reside in the Settings menu, and are accessed by selecting 
"Utility OpModes" in the menu. There are two built-in Utility OpModes:

* Test Hardware - Test the hardware in your configuration.
* Test Gamepad - Test your gamepad to ensure all buttons, triggers, and
  stick axes work properly.

Teams can also create their own Utility OpModes by using the ``@Utility``
annotation in Java, or by selecting Utility as the OpMode type in Blocks. 

.. code-block:: java
   :caption: Creating a Utility OpMode in Java

   @Utility(name="Cool Utility", description="Brief Description")
   public class MyUtilityOpMode extends OpMode {
       // Your code here
   }

.. figure:: images/utility_creation_blocks.png
   :alt: Top bar of a Blocks Utility OpMode 
   :width: 75%
   :class: no-scaled-link

   Creating a Utility OpMode in Blocks

.. figure:: images/ds_menu.png
   :alt: Driver Station menu where Utility OpModes can be found
   :width: 75%
   :class: no-scaled-link

   Accessing the Utility OpModes via the Settings Menu

.. figure:: images/util_list.png
   :alt: Utility OpMode dialogue in the Driver Station app
   :width: 75%
   :class: no-scaled-link
   
   Accessing the list of Utility OpModes

.. toctree::
   :maxdepth: 1

   test_hardware/test_hardware_utility
   test_gamepad/test_gamepad_utility