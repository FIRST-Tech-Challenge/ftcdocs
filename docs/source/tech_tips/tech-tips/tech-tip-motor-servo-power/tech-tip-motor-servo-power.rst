Calculating Motor and Servo Power
=================================

Started in the 2023-2024 season, Tech Tips are segments released in the
*FIRST* Tech Challenge `Team E-mail Blast
<https://www.firstinspires.org/resource-library/ftc/team-blast-archive>`__.
Sometimes the Tech Tips are included in whole in the email blast, but sometimes
there is more content than is reasonable in the email blast so partial content
is included in the blast with the rest of the content here.

.. _motorservopower:

In this Tech Tip we'll be exploring mechanical and electrical
power, why some types of power are calculated differently, and how to use
this calculated power to compare servos. This Tech Tip was written and
fact-checked with the help of Google Gemini 1.5 Flash using Google AI
Studio.

Electrical Power and Mechanical Power
-------------------------------------

The fundamental concept we need to understand is power. We are generally
concerned with two similar but different kinds of power, so let's look at
the two most common types. In a motor, **electrical power** is the energy
supplied by the electrical current flowing through the motor's windings.
This electrical energy is transformed into **mechanical power**, which is
the rate at which the motor performs work by rotating a shaft. Both kinds of
power are measuring different aspects of the motor; electrical power deals
with the movement of electrical charges, and mechanical power deals with the
movement of objects due to forces. Both of these measurements are expressed
in the same unit, Watts (W), because power, in general, is defined as the
rate of energy transfer or work done. No matter the form of energy
(electrical, mechanical, thermal, etc.) the fundamental concept of power
remains the same. Even though these two power measurements carry the same
unit, they are calculated differently and **cannot be used interchangeably
(or together!)**.

Motors and servos are constructed similarly - both are electromechanical
devices that convert electrical energy into mechanical energy - but there
are big differences in how they're used. Motors are often used in
applications requiring continuous power, such as pumps, fans, and conveyor
systems. Motors are typically rated for **continuous power output**, meaning
they can sustain that power level indefinitely without overheating. Servos
are commonly used in robotics and precision positioning systems, where
controlled movement and precise positioning are essential. Servos are
designed for intermittent operation - typically cycling through on/off
periods to control movement - and are often rated for their **stall torque** and
**no-load speed** reflecting their ability to hold a position against a force
and how fast they move when unloaded. While electrical power is calculated
generally the same for both types of devices, these design and use
differences have an impact on how mechanical power is determined.

Both motors and servos calculate **electrical power** the same, using the
standard electrical power formula:

- *Electrical Power(W) = volts(V) x amps(A)*

For example, a typical REV Smart Servo is supplied with 6V when used with a
REV Servo Power Module (SPM) or 5V when used with a Control or Expansion
Hub. Per the servo's specs, at 6V the servo will pull at most 2A at stall
(when the servo cannot physically move to the position it's being commanded
to). This means the maximum electrical power the servo will consume is
12Watts of power when plugged into the REV SPM and being commanded to a
position it cannot reach. The REV SPM supplies 90W of maximum electrical
power, so the maximum number of fully-stalled REV Smart Servos the SPM can
supply full power to is 7 (90W divided by 12W, ignoring the remainder).

Motors and servos also generally calculate mechanical power similarly.

- *Mechanical Power(W) = torque (N-m) x angular speed (rad/s)*

Mechanical Power for a DC motor generally follows a very specific curve,
based on its efficiency, stall current, stall torque, speed, and a bunch of
other factors. The general performance curve of a DC motor can be seen in
Figure 1.

.. figure:: images/dc-motor-curve.*
   :width: 75%
   :align: center
   :alt: DC Motor Performance Curves

   Figure 1: General DC Motor Performance Curve

From this we can see that the Peak Power is found at the intersection of 1/2
Stall Torque and 1/2 Speed. Even though a servo is used different than a
generic motor, this approximation is still good for calculating the maximum
mechanical power of a servo. Simplified, we can use this formula:

- *Servo Max Mechanical Power(W) = 0.25 x stall torque(N-m) x no-load speed(rad/s)*

Using this approximation the REV Smart Servo, when being provided 6V,
produces a maximum Stall Torque of 13.5kg-cm (1.33N-m) and a time of 0.14s
per 60 degrees of travel (7.48rad/s) yielding an approximate max servo
mechanical power of 2.48W.

.. tip::

   It's important to point out that a high speed motor or servo that is
   loaded past its maximum power point will actually do worse than a
   slower motor or servo with the same load. It's all about getting the
   maximum mechanical power by operating the motor at the max power
   point.

.. _servopowercalculator:

Servo Mechanical Power Calculator
---------------------------------

One of the most difficult parts of calculating Servo Mechanical Power is
working with unit conversions, especially since servo manufacturers use lots
of different units. In order to calculate servo mechanical power correctly
the speed unit MUST be converted to radians-per-second and the max stall
torque unit MUST be converted to Newton-meters. Below is a handy calculator
that you can use to automatically perform the necessary conversions and
calculate Servo Mechanical Power (*Thank you to Orion DeYoe for providing
this tool*).

.. raw:: html

   <head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
        
        body {
            background-color: white;
            margin: 0px;
        }
        
        .ODToolContainer {
            display: flex;
            width: 100%;
            height: 100%;
            justify-content: center;
            align-content: center;
        }

        .ODToolCard {
            width: 400px;
            display: inline-block;
            margin: auto;
        }

        .ODUnitControl label {
            display: block;
            color: white;
            /*background-color: #121969;/*#eb532b;*/
            background-image: linear-gradient(to right, #121969, #2c38c7);
            font-family: 'Roboto', sans-serif;
            font-size: 20px;
            padding: 5px;
            margin: 5px;
        }

        .ODUnitControl input {
            display: inline-block;
            font-family: 'Roboto', sans-serif;
            font-size: 12px;
            padding: 5px;
            margin: 5px 3px 5px 10px;
        }

        .ODUnitControl select {
            display: inline-block;
            font-family: 'Roboto', sans-serif;
            font-size: 12px;
            padding: 5px;
            margin: 5px 5px 5px 3px;
        }

        .ODUnitDisplay label {
            display: block;
            color: white;
            background-color: black;
            font-family: 'Roboto', sans-serif;
            font-size: 20px;
            padding: 5px;
            margin: 5px;
        }

        .ODUnitDisplay input {
            display: inline-block;
            font-family: 'Roboto', sans-serif;
            font-size: 12px;
            padding: 5px;
            margin: 5px 3px 5px 10px;
        }

        .ODUnitDisplay select {
            display: inline-block;
            font-family: 'Roboto', sans-serif;
            font-size: 12px;
            padding: 5px;
            margin: 5px 5px 5px 3px;
        }

        .ODInsetUnitLabel {
            display: block !important;
            color: black !important;
            background-color: none !important;
            background-image: none !important;
            font-family: 'Roboto', sans-serif !important;
            font-size: 14px !important;
            padding: 5px !important;
            margin: 0px 5px 0px 5px !important;
        }

        .ODRadioButton {
            display: inline-block;
        }

        .ODRadioOption {
            display: inline-block;
            margin-bottom: 5px;
        }

        .ODSectionDivider {
            display: block;
            color: white;
            /*background-color: #121969;/*#eb532b;*/
            background-image: linear-gradient(to right, #121969, #2c38c7);
            font-family: 'Roboto', sans-serif;
            font-size: 20px;
            padding: 5px;
            margin: 5px;
        }
    </style>
    
    <script type="application/javascript">
        function onLoad() {
            calculate();
        }

        function calculate() {
            var time_base = getBaseUnit("timeUnitControl");
            var ang_vel_base = getBaseUnit("velocityUnitControl");
            var torque_base = getBaseUnit("torqueUnitControl");
            
            var power = 0.0;

            var time_selected = document.getElementById('choice1').checked;
            
            if (time_selected) {
                if (time_base != 0.0) {
                    var time_ang_vel = (Math.PI / 3.0) / time_base;
                    power = time_ang_vel * torque_base * 0.25;
                }
            }
            else {
                power = ang_vel_base * torque_base * 0.25;
            }
            
            setBaseUnit("powerUnitDisplay", power);
        }

        function getBaseUnit(unit_control_id) { //use for getting input from a unit control
            var raw_value = parseFloat(document.querySelector(
                "#"+unit_control_id+" > * > input:first-of-type").value);
            var conversion = parseFloat(document.querySelector(
                "#"+unit_control_id+" > * > select:first-of-type").value);
            return raw_value * conversion;
        }

        function setBaseUnit(unit_display_id, base_unit_value) { //use for setting output to a unit display
            var output_field = document.querySelector(
                "#"+unit_display_id+" > * > input:first-of-type");
            var output_conversion = parseFloat(document.querySelector(
                "#"+unit_display_id+" > * > select:first-of-type").value);
            output_field.value = base_unit_value * output_conversion;
        }
    </script>

   </head>

   <body onload="onLoad()">

       <div class="ODToolContainer">
           <div class="ODToolCard">
               <label class="ODSectionDivider">Speed</label>
               <input type="radio" class="ODRadioButton" name="SpeedSelector" id="choice1" value="time" onchange="calculate()" checked>
               <div class="ODRadioOption">
                   <div class="ODUnitControl" id="timeUnitControl" >
                       <label class="ODInsetUnitLabel">Time per 60°</label>
                       <div class="ODUnitControlValueLine">
                           <input type="number" value="1.0" onchange="calculate()">
                           <select onchange="calculate()">
                               <option value="1.0" selected="selected">sec</option><!--base unit-->
                               <option value="60.0">min</option>
                               <option value="3600.0">hr</option>
                               <option value="0.001">msec</option>
                           </select>
                       </div>
                   </div>
               </div><br>
               

               <input type="radio" class="ODRadioButton" name="SpeedSelector" id="choice2" value="velocity" onchange="calculate()">
               <div class="ODRadioOption">
                   <div class="ODUnitControl" id="velocityUnitControl">
                       <label class="ODInsetUnitLabel">Angular Velocity</label>
                       <div class="ODUnitControlValueLine">
                           <input type="number" value="1.0" placeholder="Angular Velocity" onchange="calculate()">
                           <select onchange="calculate()">
                               <option value="0.1047197551">rev/min</option>
                               <option value="6.2831853072">rev/sec</option>
                               <option value="0.0174532925">deg/sec</option>
                               <option value="1.0" selected="selected">rad/sec</option><!--default unit-->
                           </select>
                       </div>
                   </div>
               </div><br>
               
               
               <div class="ODUnitControl" id="torqueUnitControl">
                   <label>Stall Torque</label>
                   <div class="ODUnitControlValueLine">
                       <input type="number" value="0.0" onchange="calculate()">
                       <select onchange="calculate()">
                           <option value="1.0" selected="selected">N*m</option><!--default unit-->
                           <option value="0.01">N*cm</option>
                           <option value="0.001">N*mm</option>
                           <option value="9.80665">kg*m</option>
                           <option value="0.0980665">kg*cm</option>
                           <option value="0.00980665">kg*mm</option>
                           <option value="1.35581795">lb*ft</option>
                           <option value="0.11298483">lb*in</option>
                           <option value="0.00706155">oz*in</option>
                       </select>
                   </div>
               </div>
           
               <div class="ODUnitDisplay" id="powerUnitDisplay">
                   <label>Power</label>
                   <div class="ODUnitDisplayValueLine">
                       <input disabled id="powerOutput" value="0.0">
                       <select onchange="calculate()">
                           <option value="1.0" selected="selected">W</option><!--default unit-->
                           <option value="0.001">kW</option>
                           <option value="0.00134102">hp</option>
                       </select>
                   </div>
               </div>
           </div>
           
       </div>
       <br>
   </body>

.. tip::

   - For Speed, use the radio button to choose the unit type that the
     manufacturer has provided - for most servos this will be listed in a
     period of time per 60 degrees (such as with the REV Smart Servo
     example) or perhaps the manufacturer may provide an angular velocity,
     such as rotations-per-minute (RPM). Enter the no-load speed value and
     unit as the manufacturer has provided.

   - For stall torque, provide the value and select the unit as specified by
     the manufacturer. If the manufacturer merely provides kg, assume kg*cm.

   The calculator automatically recalculates on any
   changes, there is no button to press in order to trigger a calculation.

Common Servo Mechanical Power Values
------------------------------------

Here is a handy table of some common servo mechanical power values:

.. list-table:: Common Servo Mechanical Power Values ( @6V )
   :widths: 50 20 20 20 20 20
   :header-rows: 1
   :align: center

   * - Description
     - Speed
     - Torque
     - Stall Current
     - Max Power
     - Cost ($USD)
   * - `Tetrix MAX Standard (HiTec HS-485HB) <https://www.pitsco.com/products/tetrix-max-standard-scale-servo-motor>`__
     - 0.18 s/60°
     - 6 kg-cm
     - 1.2 A
     - 0.86 W
     - $29.50
   * - `REV Smart Servo <https://www.revrobotics.com/rev-41-1097/>`__
     - 0.14 s/60°
     - 13.5 kg-cm
     - 2.0 A
     - 2.48 W
     - $30.00
   * - `goBILDA 2000 Series Speed Servo <https://www.gobilda.com/2000-series-dual-mode-servo-25-3-speed/>`__
     - 0.09 s/60°
     - 9.3 kg-cm
     - 2.5 A
     - 2.65 W
     - $33.99
   * - `Axon Robotics Micro+ <https://axon-robotics.com/products/micro>`__
     - 0.075 s/60°
     - 7.8 kg-cm
     - 2.2 A
     - 2.67 W
     - $63.79
   * - `goBILDA 2000 Series Torque Servo <https://www.gobilda.com/2000-series-dual-mode-servo-25-2-torque/>`__
     - 0.20 s/60°
     - 300 oz-in
     - 2.5 A
     - 2.77 W
     - $33.99
   * - `Studica Multi-Mode Smart Servo 200 <https://www.studica.com/studica-robotics-brand/multi-mode-smart-servo-200>`__
     - 0.046 s/60°
     - 5 kg-cm
     - 2.7 A
     - 2.79 W
     - $24.99
   * - `goBILDA 2000 Series Super Speed Servo <https://www.gobilda.com/2000-series-dual-mode-servo-25-4-super-speed/>`__
     - 0.043 s/60°
     - 4.7 kg-cm
     - 2.5 A
     - 2.81 W
     - $33.99
   * - `AndyMark am-4954 High Torque Servos <https://www.andymark.com/products/programmable-servos>`__
     - 0.20 s/60°
     - 22 kg-cm
     - 1.7 A
     - 2.82 W
     - $34.00
   * - `Studica Multi-Mode Smart Servo <https://www.studica.com/studica-robotics-brand/multi-mode-smart-servo>`__
     - 62 RPM
     - 20 kg-cm
     - 1.8 A
     - 3.18 W
     - $23.99
   * - `AndyMark am-4955 High Speed Servos <https://www.andymark.com/products/programmable-servos>`__
     - 0.05 s/60°
     - 7 kg-cm
     - 2.7 A
     - 3.59 W
     - $30.00
   * - `FeeTech FT5335M-FB <https://www.pololu.com/product/3446>`__
     - 0.20 s/60°
     - 35 kg-cm
     - 4.0 A
     - 4.49 W
     - $52.95
   * - `HiTec HS-805BB <https://www.servocity.com/hs-805bb-servo/>`__
     - 0.14 s/60°
     - 24.7 kg-cm
     - 6.0 A
     - 4.53 W
     - $49.99
   * - `HiTec HSR-M9382TH <https://www.servocity.com/hsr-m9382th-servo/>`__
     - 0.17 s/60°
     - 34 kg-cm
     - 2.7 A
     - 5.13 W
     - $199.99
   * - `Power HD GTS3 <https://www.rcmart.com/power-hd-30kg-gts-series-brushless-high-voltage-servo-for-1-10-1-8-rc-car-gts3-00126675>`__
     - 0.083 s/60°
     - 20 kg-cm
     - 4.0 A
     - 6.19 W
     - $120.00
   * - `Axon Robotics MINI+ <https://axon-robotics.com/products/mini>`__
     - 0.09 s/60°
     - 25 kg-cm
     - 3.8 A
     - 7.13 W
     - $79.99
   * - `Axon Robotics MAX+ <https://axon-robotics.com/products/max>`__
     - 0.115 s/60°
     - 34 kg-cm
     - 4.0 A
     - 7.59 W
     - $79.99

Got any questions about calculating motor and servo power? Come start or join
the conversation on the `FTC Community Forums
<https://ftc-community.firstinspires.org/>`__!
