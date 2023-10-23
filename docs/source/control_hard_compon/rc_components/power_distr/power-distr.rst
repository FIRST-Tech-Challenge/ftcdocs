Power Distribution
===================

Robot Main Battery
----------------------

.. grid:: 1 2 2 3
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      TETRIX 12V Battery

      ^^^

      .. figure:: images/W39057.jpg
         :align: center
         :alt: W39057
         :width: 50 %

      +++

      TETRIX (W39057, formally 739023)

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      MATRIX 12V Battery

      ^^^

      .. figure:: images/14-0014-FTCLegal__75264.jpg
         :align: center
         :alt: 14-0014
         :width: 50 %

      +++

      Modern Robotics/MATRIX (14-0014)

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      REV 12V Battery

      ^^^

      .. figure:: images/am-4649.jpg
         :align: center
         :alt: REV-31-1302
         :width: 50 %

      +++

      REV Robotics (REV-31-1302)

The main power of a robot comes from one 12v battery. The battery may be one of
the batteries shown above. Refer to section ``<RE03>`` in the 
:ref:`Game Manual Part 1<manuals/game_manuals/game_manuals:game manuals>` 
for exact information on allowed batteries. Note that it is typically allowed
by ``<RE15>`` to replace the connector on the batteries, provided the in-line
fuse on the battery is preserved.

.. warning:: 
   Be sure to remove the 20A fuse from the in-line fuse holder prior to cutting
   any wires/connectors if/when replacing the factory default battery connector.

Main Power Switch
----------------------

.. grid:: 1 2 2 3
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      REV Power Switch 

      ^^^

      .. figure:: images/REV-31-1387.png
         :align: center
         :alt: REV-31-1387
         :width: 50 %

      +++

      REV (REV-31-1387)

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      TETRIX Power Switch 

      ^^^

      .. figure:: images/W39129.jpg
         :align: center
         :alt: REV-31-1387
         :width: 50 %

      +++

      TETRIX (part # W39129)

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      MATRIX Power Switch 

      ^^^

      .. figure:: images/50-0030.jpeg
         :align: center
         :alt: REV-31-1387
         :width: 50 %

      +++

      MATRIX (part #50-0030)

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      AndyMark Power Switch 

      ^^^

      .. figure:: images/am-4969.jpg
         :align: center
         :alt: AM-4969 Switch
         :width: 50 %

      +++

      AndyMark (part #am-4969)



One Main Power Switch must control all power provided by the Main Battery. It
along with its label should be placed in accordance to 
:ref:`Game Manual Part 1<manuals/game_manuals/game_manuals:game manuals>`. 
The legal power switches are shown above. ``<RE01>``

:download:`Power Switch Label <https://www.firstinspires.org/sites/default/files/uploads/resource_library/ftc/power-button-labels.pdf>`

Power Distribution Block
-------------------------

.. grid:: 1 2 2 3
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      REV XT30 Power Distribution Block

      ^^^

      .. figure:: images/XT30_Power_Distribution_Block.png
         :align: center
         :alt: REV-31-1293
         :width: 50 %

      +++

      REV (REV-31-1293)

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      goBILDA XT30 Power Distribution Block
   

      ^^^

      .. figure:: images/goBILDApdb.jpg
         :align: center
         :alt: goBildaPDB
         :width: 50 %

      +++

      goBILDA (SKU: 3108-2833-0801)

Power Distribution Blocks help to distribute the power to devices such as
Control Hubs, SPARKminis, and more.  
See :ref:`Game Manual Part 1<manuals/game_manuals/game_manuals:game manuals>` 
for a description of legal Power Distribution methods. The Power
Distribution Blocks shown are not the only legal devices for power distribution.

REV Servo Power Module
----------------------

.. grid:: 1 2 2 3
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      REV Servo Power Module

      ^^^

      .. figure:: images/REV-11-1144.png
         :align: center
         :alt: REV-31-1144
         :width: 50 %

      +++

      REV (REV-11-1144)

This is an electronic device that boosts the power supplied to 3-wire servos. A REV
Servo Power Module has 6 input servo ports and 6 matching output ports. It
draws power from a 12V source and provides 6V power to each output servo port.
A REV Servo Power Module can provide up to 15A of current across all output
servo ports for a total of 90 Watts of power per module.

COTS USB Battery Pack
---------------------

.. grid:: 1 2 2 3
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      USB Battery Pack

      ^^^

      .. figure:: images/ankerbattery.png
         :align: center
         :alt: Anker Pack
         :width: 50 %

      +++

      Anker Battery Pack

A Commercial Off The Shelf (COTS) USB battery pack is an auxiliary power source
that can be used in specific situations in accordance with the :ref:`Game
Manuals<manuals/game_manuals/game_manuals:game manuals>`. In the 2023-2024
season, these batteries were deemed permissible to power LEDs (per
``<RE12>f.ii``) and, by extension, COTS light controller sources like the `REV
Blinkin <https://www.revrobotics.com/rev-11-1105/>`__ (per ``<RE12>e``).
However, having a COTS USB External Battery on the Robot carries additional
considerations.  All teams must ensure their COTS USB Battery Pack:

- Is manufactured by a reputable brand.
- Is within standard Watt-hour capacity limits.
- Includes standard safety features.
- Is secured on the Robot.
- Has unused ports covered.
- Is always charged properly.
- Does not show any signs of distress.

The following sections are intended to help clarify the list above.

Reputable Brands
~~~~~~~~~~~~~~~~

Far and above, the most important factor regarding the safety of COTS USB
Battery Packs is ensuring that the battery pack was manufactured by a reputable
brand. International testing of COTS USB Battery Packs has concluded that
unbranded batteries, or batteries manufactured by little-known companies, tend
to fail more often than batteries from reputable brands. How do you know what
brands are reputable and which ones are not? That's not always an easy thing to
determine, however brands such as 
`Anker <https://www.anker.com/collections/power-banks>`__, 
`Belkin <https://www.belkin.com/products/chargers/portable-chargers-power-banks/>`__,
`Otterbox <https://www.otterbox.com/en-us/power-packs>`__, and 
`BioLite <https://www.bioliteenergy.com/collections/usb-battery-banks>`__ 
are among the most-used brands in the world. *FIRST* Tech Challenge recommends
choosing an internationally reputable brand, even if the brand is more
expensive than a lesser-known brand, as these batteries will be more apt to
follow safety and performance guidelines. NEVER choose a COTS USB Battery
Pack based on its (low) price alone!

Capacity Limits
~~~~~~~~~~~~~~~

The recurring theme in most discussions of COTS USB Battery Packs is safety.
The United States Transportation Safety Administration (TSA) has strict
limitations on COTS USB Battery Packs on-board planes, and *FIRST* Tech
Challenge has adopted the capacity limit restriction. **Batteries are limited
to 100 Watt-Hours (Wh) or less**. 

How do you calculate Watt-hours? To calculate Watt-hours of a battery, multiply
the Voltage (V) of the battery by its capacity measured in Amp-Hours (Ah). For
example, a 12V battery with 3,000mAh capacity has a 36Wh capacity - when
capacity is measured in milli-Amp Hours (mAh), divide the capacity by 1000 to
get Ah and them multiply by Voltage.  However, for COTS USB Battery Packs, the
Voltage cells predominantly used in the packs is **3.7V**, regardless of the
ultimate Voltage provided by the USB ports. Therefore to calculate Wh for a
COTS USB Battery Pack, multiply **3.7V** by the **Ah rating** of the pack. A 25,000mAh
COTS USB Battery Pack has a rating of 92.5Wh. Using this formula, the maximum
capacity COTS USB Battery Pack that is allowed is a **27,000mAh** pack.

Standard Safety Features
~~~~~~~~~~~~~~~~~~~~~~~~

The major benefit of using a reputable COTS USB Battery Pack brand is the
guarantee that the battery pack includes standard safety features, including
but not limited to:

- Reverse Polarity Protection
- Short-Circuit Protection
- Over-Charge Protection
- Over-Temperature or Over-Heat Protection
- Over-Current Protection

You should perform a good-faith effort to determine if your Battery Pack 
contains these safety features. Often within the documentation provided with
your pack it will list the protections offered by the pack. Remember that the
Battery Pack contains Lithium-Ion or Lithium Polymer batteries often will
explode or catch fire when they fail, and these protections are vital to 
ensuring that the batteries do not fail prematurely. It is not recommended 
to use COTS USB Battery Packs without these protections.

Securing the Battery Pack to the Robot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The leading cause of battery failure is physical damage to the battery. For
COTS USB Battery Packs this is usually attributed to dropping the battery pack,
applying excessive force on the Battery Pack, and subjecting the pack to excessive
shock (which might also damage internal components). In order to prevent damage, 
the Battery Pack should be properly secured within the robot. Tips for securing
the battery are:

- Use Hook and Loop or 3M DualLock fasteners to secure the battery, **OR**
- Store the battery in a tight-fitting or custom-fit enclosure within the robot
  that allows the battery to be exposed to air (for cooling), **AND**
- Protect the battery from contact from other robots, game pieces, or field
  elements that might breach the perimeter of the robot.

If utilizing a COTS USB Battery Pack, it is of utmost importance to ensure
that the battery is secured, protected, and ventilated. All batteries (both
main batteries and COTS USB Battery Packs) should be easily accessible and be 
able to be quickly removed from the robot in case of an emergency.

Cover Unused Ports
~~~~~~~~~~~~~~~~~~

Some COTS USB Battery Packs contain multiple ports, and it is often that not
all ports are in-use while securely mounted to the robot. For example, the 
COTS USB Battery Pack may have multiple USB ports, a dedicated charging port,
and other ports as necessary. Any ports that are not in-use (meaning don't have 
a USB connector inserted in them) are at great risk of short-circuiting. The
most common reason for short-circuiting is metal fragments that may make their
way into the ports, especially swarf due to metal rubbing together, gears wearing,
or robot maintenance performed while electronics are present. Any unused ports
should be covered using electrical tape, Gaffers Tape, or any other means of
preventing debris from entering the ports. Short circuits may present risks of 
excessive heat, fire, or explosion and all reasonable efforts should be taken 
to prevent them.

.. warning::
   Never get a COTS USB Battery Pack wet. If it gets wet, follow the manufacturer's
   recommended procedure to clean and dry the battery before continuing use.

Charge COTS USB Battery Packs properly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The owners/instruction manual provided with the COTS USB Battery Pack often 
contains instructions for the proper care and maintenance of the battery pack,
including proper charging. Always follow the manufacturer's recommendations.
In addition, these are common best practices for charging your Batteries:

- Avoid charging the power bank on places that build up heat, such as on your 
  bed or within a bag.
- Unless it's a solar power bank, NEVER leave your battery in the sun!
- Follow the manufacturer's guidelines on the time required to fully charge
  your COTS USB Battery Pack.
- Avoid leaving your COTS USB Battery Pack on prolonged chage as this may 
  cause it to overheat.
- If the COTS USB Battery Pack becomes excessively hot during charging or 
  discharging, unplug it from the power source or powered device immediately
  and allow it to cool before doing anything else with the battery.

Checking for signs of distress
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most COTS USB Battery Packs are contained within a hard plastic shell in order
to protect and package the battery cell(s) within. Therefore it can be
difficult to determine if the battery is showing signs of failure and distress.
Here are several tips for identifying a failing battery:

- Check for Leaking Power Cells. Similar to an acid leak in an alkaline battery,
  check to see if there are any signs of corrosion or acid leak from the 
  battery pack. This might be difficult to determine, so stay vigilent. If signs
  of acid or corrosion are present, dispose of the battery per the manufacturer's
  recommendations immediately with extreme prejudice.
- Look for bulging within the battery casing. When Lithium batteries fail, often 
  they will begin to bulge like a balloon. If the case of the battery shows any
  signs of pressure from within, dispose of the battery per the manufacturer's 
  recommendations immediately with extreme prejudice.
- Test the battery pack for any non-functional ports. Sometimes non-functional
  ports can be an early sign of internal damage. DO NOT use batteries that 
  are suspected of being damaged - dispose of the battery per the manufacturer's
  recommendations immediately.


