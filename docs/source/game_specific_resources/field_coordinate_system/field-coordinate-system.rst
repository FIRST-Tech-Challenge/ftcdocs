Field Coordinate System Definition
==================================

Scope
-----

This document defines the Field Coordinate System 
for a *FIRST* Tech Challenge playing field. This definition can be
used for consistent field-centric navigation, target localization and path
planning.

The Field Coordinate System is a 
`three-dimensional Cartesian coordinate system 
<https://en.wikipedia.org/wiki/Cartesian_coordinate_system#Three_dimensions>`__ 
which means that the three axes are at right angles to each other. 
The X and Y axes will refer to a position on the field and Z axis a height above the field. 

Reference Frame
---------------

The reference frame for this definition is the field perimeter wall, adjacent
to the RED Alliance Station (known here as the: RED WALL).  The definition is
from the perspective of a person, standing outside the field, in the center of
RED WALL, looking towards the center of the field.

Caveat: If the Red Alliance Station is ever adjacent to two perimeter walls,
the RED WALL will be the one with *most* contact with the Alliance Station. If
the red Alliance Station is ever adjacent to two perimeter walls EQUALLY, then
the most clockwise of the two walls will be considered to be the RED WALL.

Origin
^^^^^^

The 0,0,0 origin of the *FIRST* Tech Challenge coordinate system is the point
in the center of the field, equidistant from all 4 perimeter walls (where the
four center tiles meet). The origin point rests on the top surface of the floor
mat.

X Axis
^^^^^^

Looking at the origin from the RED WALL, the X axis extends through the origin
point and runs to the right and left, parallel with the RED WALL. The X axis
values increase to the right.

Y Axis
^^^^^^

Looking at the origin from the RED WALL, the Y axis extends through the origin
point and runs out and in, perpendicular to the RED WALL.  Increasing Y values
run out (away) from the RED WALL.

Z Axis
^^^^^^

Looking at the origin from the RED WALL, the Z axis extends through the origin
point and runs up and down in a vertical line. Increasing Z values extend
upwards.

Rotation About Axes
^^^^^^^^^^^^^^^^^^^

When considering rotations about an axis, consider yourself looking down the
axis from the positive end towards the origin. Positive
rotations are then counterclockwise and negative rotations clockwise.
This rotation convention comes from the `right hand rule <https://en.wikipedia.org/wiki/Right-hand_rule>`__ of classic geometry.

.. figure:: images/image1.jpg
   :width: 35%
   :align: center
   :class: no-scaled-link
   :alt: illustration 
   
   showing the counterclockwise rotations about each axis.
   
A rotation example: consider looking down the positive Z axis towards the origin. 
This would be like standing in the middle of the field
looking down at the intersection of the tiles in the very center of the field.
A positive rotation about the Z axis is then counterclockwise.
Example: a robot spinning clockwise on the field is making a negative rotation about the Z axis. 

Field Configuration Examples
----------------------------

Below are two examples illustrating the Field Coordinate System for different
*FIRST* Tech Challenge field configurations.

In a diamond field configuration the two alliance walls are adjacent. 
The field is rotated 45 degrees such that both alliances face the audience.
The red alliance will be on the right as seen from the audience.
The Y axis points across the field from the RED WALL and the X axis points to 
the Blue Alliance on the right side of the field.

.. figure:: images/image2.jpg
   :width: 75%
   :align: center
   :class: no-scaled-link
   :alt: a diamond field
   
   from the FIRST RES-Q game 

In a square field configuration the two alliances face each other across the field.
The field is oriented such that the red alliance is on the right as seen from the audience.
The Y axis points across the field to the Blue Alliance and the X axis points 
to the right side of the field, away from the audience.

.. figure:: images/image3.jpg
   :width: 75%
   :align: center
   :class: no-scaled-link
   :alt: a square field
   
   from the Cascade Effect game

.. note::
   In both field configurations the Red Alliance team members are facing out along the positive Y axis
   and the Z axis points up from the center of the field.

   In the diamond field configuration, the X axis is pointing
   towards the Blue Alliance, but in the square field configuration
   the Y axis is pointing towards the Blue Alliance.

Measured Values
---------------

The following values have been measured from a 2016 competition field. They are
representative only, and should not be assumed to be exact, or guaranteed.

-  Distance between opposite inside faces of panels: 3580 mm
   (if field assembled well: the straps give some adjustment tolerance)
-  Polycarbonate transparencies have a visible opening height of 255 mm
-  The top edge of transparencies is 30 mm from the top of the perimeter
-  Total perimeter height is 313 mm
-  Tiles are 13 mm thick

So, for a diamond field configuration, the corner of the field closest to the
audience, at a height equal to the top of the perimeter wall, would have a
coordinate position of: (-1790, 1790, 300).

