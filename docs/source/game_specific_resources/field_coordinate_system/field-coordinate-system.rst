Field Coordinate System Definition
==================================

Scope
-----

  
This document defines the Field Coordinate System 
for a *FIRST* Tech Challenge playing Field. This definition can be
used for consistent field-centric navigation, target localization and path
planning.

The Field Coordinate System is a 
`three-dimensional Cartesian coordinate system 
<https://en.wikipedia.org/wiki/Cartesian_coordinate_system#Three_dimensions>`__ 
which means that the three axes are at right angles to each other. 
The X and Y axes will refer to a position on the Field and Z axis a height above the Field. 

Reference Frame
---------------

The reference frame for this definition is the Field perimeter wall, adjacent
to the red Alliance Area, known here after as the Red Wall.  The definition is
from the perspective of a person, standing outside the Field, in the center of
Red Wall, looking towards the center of the Field.

.. note::
   If the red Alliance Area is ever adjacent to two perimeter walls,
   the Red Wall will be the one with *most* contact with the Alliance Area. If
   the red Alliance Area is ever adjacent to two perimeter walls *equally*, then
   the most clockwise of the two walls will be considered to be the Red Wall.

Origin
^^^^^^

The 0,0,0 origin of the *FIRST* Tech Challenge coordinate system is the point
in the center of the Field, equidistant from all 4 perimeter walls (where the
four center tiles meet). The origin point rests on the top surface of the floor
mat.

X Axis
^^^^^^

Looking at the origin from the Red Wall, the X axis extends through the origin
point and runs to the right and left, parallel with the Red Wall. The X axis
values increase to the right.

Y Axis
^^^^^^

Looking at the origin from the Red Wall, the Y axis extends through the origin
point and runs out and in, perpendicular to the Red Wall. Increasing Y values
run out (away) from the Red Wall.

Z Axis
^^^^^^

Looking at the origin from the Red Wall, the Z axis extends through the origin
point and runs up and down in a vertical line. Increasing Z values extend
upwards.

Rotation About Axes
^^^^^^^^^^^^^^^^^^^

When considering rotations about an axis, consider yourself looking down the
axis from the positive end towards the origin. Positive
rotations are then counterclockwise and negative rotations clockwise.
This rotation convention comes from the 
`right hand rule <https://en.wikipedia.org/wiki/Right-hand_rule>`__ of classic geometry.

.. figure:: images/image1.jpg
   :width: 35%
   :align: center
   :class: no-scaled-link
   :alt: illustration 
   
   showing the counterclockwise rotations about each axis.
   
A rotation example: consider looking down the positive Z axis towards the origin. 
This would be like standing in the middle of the Field
looking down at the intersection of the tiles in the very center of the Field.
A positive rotation about the Z axis is then counterclockwise.
Example: a robot spinning clockwise on the Field is making a negative rotation about the Z axis. 

Field Configuration Examples
----------------------------

Below are two examples illustrating the Field Coordinate System for different
*FIRST* Tech Challenge Field configurations.

In a diamond Field configuration the two Alliance walls are adjacent. 
The Field is rotated 45 degrees such that both Alliance Areas face the audience.
From the audience perspective the Field forms a diamond shape.
The Red Wall will be on the right as seen from the audience,
and the blue wall will be on the left.
The Y axis points across the Field as seen from the Red Wall. 
The X axis points to the blue wall.

.. figure:: images/image2.jpg
   :width: 75%
   :align: center
   :class: no-scaled-link
   :alt: a diamond Field
   
   from the *FIRST* RES-Q game 

In a square Field configuration the two Alliances face each other across the Field.
The Field is oriented such that the Red Wall is on the right as seen from the audience,
and the blue wall will be on the left.
The Y axis points across the Field from the Red Wall to the blue wall.
The X axis points away from the audience to the rear of the Field.

.. figure:: images/image3.jpg
   :width: 75%
   :align: center
   :class: no-scaled-link
   :alt: a square Field
   
   from the Cascade Effect game

.. note::
   In both Field configurations the red Alliance is facing out along the positive Y axis,
   and the Z axis points up from the center of the Field.

   In the diamond Field configuration the X axis is pointing
   towards the blue Alliance. In the square Field configuration
   the Y axis is pointing towards the blue Alliance.

Measured Values
---------------

The following values have been measured from a 2016 competition Field. They are
representative only, and should not be assumed to be exact, or guaranteed.

-  Distance between opposite inside faces of panels: 3580 mm,
   (if the Field is assembled well: the straps give some adjustment tolerance)
-  Polycarbonate transparencies have a visible opening height of 255 mm
-  The top edge of transparencies is 30 mm from the top of the perimeter
-  Total perimeter height is 313 mm
-  Tiles are 13 mm thick

So, for a diamond Field configuration, the corner of the Field closest to the
audience, at a height equal to the top of the perimeter wall, would have a
coordinate position of: (-1790, 1790, 300).

Glossary
--------

.. glossary::

   Alliance
      An Alliance is a cooperative of two *FIRST* Tech Challenge teams. 
      An Alliance in the red Alliance Area is known as the red Alliance,
      and an Alliance in the blue Alliance Area is known as the blue Alliance.
      
   Alliance Area
      A 120 inch (~304.8 cm) wide by 42 inch (~106.7 cm) deep by infinitely tall volume formed
      by placing Alliance colored tape onto the flooring surface outside of the Field.
      The Alliance Area includes the taped lines.
      The red Alliance Area will have red tape, the blue Alliance Area will have blue tape.
      
   Field
      An approximately 12 foot (3.66m) by 12 foot (3.66m) Area bounded by the
      outside edge of the extrusion that frames the walls of the Field perimeter.
      The flooring surface of the Field is made of 36 (nominal size) 24 inch by 24 inch by 5/8 inch interlocking soft foam tiles. 
