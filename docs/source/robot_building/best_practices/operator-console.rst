Operator Console Best Practices
-------------------------------

An operator console is the set of components and mechanisms used by the drive team
to relay commands to the robot.

At a minimum this includes:

- A driver station consisting of a REV Driver Hub (or Android Device) running the Driver Station App.
- One or two gamepads with a wired USB connection connected to the driver station.

See section 12.9 Operator Console in the Robot Construction Rules chapter of the Competition Manual for relevant rules.
There are other rules in the competition manual related to using an operator console at the field.
This includes, but is not limited to:

- Bring your operator console to Inspection, it must comply with safety and fair play rules.
- The driver station touch screen must be visible and able to be touched.
- The only permitted wireless connection from an operator console is from the driver station to the robot.

Additional console components can include:

- An actual tray or similar item that holds the other components.
- Fasteners are allowed so that the components can't move around or fall off.
- Decorations such a team name, team number, and team branding.
- A USB power bank and a USB cable that connects the power bank to the USB-C port of the REV Driver Hub. 
  the REV Driver Hub can kept fully charged even with gamepads connected. 
- Short USB extension cables. These can reduce wear and tear on the REV Driver Hub USB ports.
  Securing the extension cables and cable strain relief also reduces the likelihood of USB disconnects.
- A `ferrite cable clip <https://www.revrobotics.com/rev-39-1224-pk4/>`_ attached near the connector of the gamepad USB cable will 
  reduce electrical signal interference from the gamepad that may cause the Driver Station to receive incorrect gamepad inputs. 
  Most likely this would be due to static electricity coming from the field.
- For driver stations using an Android device, a :term:`OTG adapter <OTG Adapter>` is required to connect one gamepad.
  Add a :term:`USB hub <USB Hub>` in order to connect two gamepads (or use a USB hub with OTG included). The hub may also be powered by a USB power bank.

A physical operator console can also provide the following benefits.

- It allows the team to store, organize and transport the Driver Station to and from the competition field.
- By keeping all the driver station components in something, there is less chance of forgetting something when showing up at the field for a match, and setup at the field should be faster.
- Having the REV Driver Hub secured to the console may protect the hub from physical damage. 
  Hubs can be accidentally dropped during transport, or pulled off of a competition-provided stand onto the floor during match play.
 
Here are some examples of operator consoles.

.. grid:: 1 1 1 2
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      Simple Tray

      ^^^

      .. figure:: images/20240309_171518.jpg
         :align: center
         :alt: a simple operator console tray
         :width: 75 %

      +++

      A simple tray can help carry things to the field, but it provides no organization or protection.
      
   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      A Custom Tray

      ^^^

      .. figure:: images/20260124_084705.jpg
         :align: center
         :alt: a custom tray
         :width: 75 %

      +++

      This operator console has handles and holders for a USB power bank, the REV Driver Hub and a gamepad.

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      Operator Console for a Phone

      ^^^

      .. figure:: images/20181216_224531.jpg
         :align: center
         :alt: an operator console for a phone
         :width: 75 %

      +++

      This operator console secures an Android phone and provides a way to secure and organize the gamepad cables.

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      Operator Console for a Driver Hub

      ^^^

      .. figure:: images/20230218_113211.jpg
         :align: center
         :alt: an operator console for a driver hub
         :width: 75 %

      +++

      This operator console secures a driver hub. A USB power bank was added.   

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      An Advanced Tray

      ^^^

      .. figure:: images/20260208_135847.jpg
         :align: center
         :alt: an advanced operator console tray
         :width: 75 %

      +++

      This operator console uses the REV UltraUSB Hub to connect two gamepads. 
      A second USB hub connects a USB power bank to the REV Driver Hub and UltraUSB Hub.
      Cables are strain relieved by securing them to the tray. 

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      Budget Operator Console

      ^^^

      .. figure:: images/PXL_20261022_203650783.jpg
         :align: center
         :alt: a budget operator console
         :width: 75 %

      +++

      This is a tray from a 24 pack of pop cans. The REV Driver Hub is secured to the tray via a M3 screw and washer from the underside of the tray.
      Short USB extensions are also secured to the tray. A USB power bank is secured with a reusable cable tie.

.. tip:: None of the above examples show `ferrite cable clips <https://www.revrobotics.com/rev-39-1224-pk4/>`_ on the USB gamepad cables. 
   However these are still recommended as they would reduce electrical noise from static electricity buildup on the field that might interfere with gamepad inputs.

You can find design files suitable for :doc:`/manufacturing/3d_printing/index` on Thingiverse.
Component holders for driver station components and even this
`Driver Station Carrier <https://www.thingiverse.com/thing:3386378>`_.

