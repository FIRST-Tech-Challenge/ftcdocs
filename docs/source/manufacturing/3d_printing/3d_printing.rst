3D Printing
===========


Many parts in FTC need to be a special/unique shape and size, one that isn't sold or available from a vendor.
Sometimes, teams need a part that is impossible to machine or cut out, or needs to be lightweight. Other times,
teams may want to test and iterate the design of a part rapidly and cheaply. 3D printing is a great solution to
all of these problems.

3D Printing Methods
-------------------

There are numerous kinds of 3D printing, but for FTC there are only a few that are practical. The most common is
Fused Deposition Modeling (FDM). FDM printers melt a plastic filament
and extrude it through a nozzle, which moves around to create the part. FDM printers are the most common
type of printer used, so this guide will focus on them. Other types of printers include SLA (Stereolithography)
and SLS (Selective Laser Sintering), however these are often more expensive, difficult to use, and have less
use in FTC.

3D Printing Pros
----------------

* 3D printed parts can be infinitely customized and optimized for a specific purpose. This can be used to create
  pulleys or gears with a specific number of teeth, or a part that fits perfectly in a specific place.
* 3D printing can be used to create parts that adapt between different build systems or standards. Many build systems
  contain their own standards for mounting holes, shaft sizes, or other dimensions. 3D printing can be used to create
  parts that adapt between these standards.
* 3D printing can be used to make parts relatively quickly and cheaply. This is especially useful for prototyping
  new designs, or iterating on a design to make it better at little cost and in a short amount of time.

3D Printing Cons
----------------

* 3D printed parts are often not as strong as machined or cut parts. This is especially true for FDM printers, which
  have a layer-by-layer structure that can be a weak point if the part is loaded in a certain way. If consideration
  is given to this weakness when designing the part, however, the result can be made very strong.
* Depending on the material, 3D printed parts can be weak to shock loads, such as impacts.
* A 3D printed part can only be as large as the print bed it is printed on. This means that large parts may need to
  be printed in multiple pieces and assembled later.
* 3D printing can be slow, especially for large parts. Longer prints can take hours or even days to complete, raising
  the risk of a print failing and wasting time and material.
* 3D printing can be expensive. The cost of a printer, filament, and other materials can add up quickly. However,
  the cost of a 3D printer has been decreasing rapidly, and filament is relatively cheap.


Common 3D Printing Filaments
----------------------------

There are many different materials that can be used for 3D printing, but for FTC there are only a few that are
of practical use for most teams. This page will go through the most common filaments and their properties. While
each filament has advantages and disadvantages, **most teams will find that PLA (Polylactic Acid) or
PETG (Polyethylene Terephthalate Glycol) will be the best choice for strength, durability, and aesthetics.**
These filaments are the easiest to print with, and are available from many different manufacturers at a low cost.
Many other filaments that will be discussed add some specific property (ex: TPU/TPE for flexibility), but are
more difficult to print with, and are often more expensive.

.. warning:: If your printer's hotend (the part that melts the filament) has a PTFE (Teflon) lining where the
    PTFE tube goes all the way down to the heat block (common in lower price printers like the Ender 3 and its variants),
    then you **should not be printing at or above 250° C**. Doing so will cause the PTFE tube to degrade and melt,
    releasing toxic fumes. If you need to print at these temperatures and you have a PTFE lined hotend, you can look
    at upgrading to an all-metal hotend.


PLA (Polylactic Acid)
^^^^^^^^^^^^^^^^^^^^

Polylactic Acid, or PLA, is the most common 3D printing filament used today. It is made from biological sources such
as corn starch or sugar cane. PLA is easy to print with, and is usually the best choice for most robot parts. It
prints at a low temperature, and tends to warp very little. PLA is very stiff, but can be brittle, especially under
shock loads (impacts), and parts should be designed with this in mind.

- PLA hotend temperatures: 190-230° C
- PLA bed temperatures:20-60° C; PLA does not require a heated bed, but it is recommended.

.. tip:: Due to the relatively low melting point of PLA, it is not advisable to leave PLA parts in locations such
    as a hot car, as this can produce severe warping in those parts.

PLA is sold in a massive number of variations from different manufacturers, like PLA+ or PLA Pro. These filaments
contain different additives to improve the properties of the filament, such as increased strength or better
printability. While more expensive, these filaments can be a great option that make PLA much more capable.

PETG (Polyethylene Terephthalate Glycol)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PETG is another very common filament that can be considered as an upgrade to PLA. While not difficult to print with,
PETG often has more stringing and other artifacts on parts. PETG's tensile strength is a technically lower than that of PLA,
however it is much more flexible and less brittle. Because of this, PETG is more resistant to shock loads
than PLA, and is a good choice for parts that may be impacted. PETG is also more resistant to heat than PLA, and
is unlikely to warp when left in a hot location.

.. warning:: PETG is well known for bonding extremely well to print beds, **especially those made out of glass and
    PEI**, to the point of tearing chunks out of the bed. If you are printing with PETG, it may be a good idea to
    apply some glue stick or hairspray to the surface to prevent this.

* PETG hotend temperatures: 230-250° C
* PETG bed temperatures: 60-80° C


Less Common 3D Printing Filaments
---------------------------------

These filaments are less common than those above, but can be useful for specific applications in FTC, often due
to specific material properties like ductility or flexibility. These filaments are more difficult to print with,
coming with significant challenges that prevent some printers from being able to print them out of the box, in
addition to being much more expensive.


ABS (Acrylonitrile Butadiene Styrene)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before PLA became readily available, ABS was the most common filament used for 3D printing. ABS is very strong,
having a high ductility and able to withstand shock loads well. These strengths come with major difficulties,
however, as an enclosure is often needed to increase the ambient temperature in order to prevent severe
part warping. Due to these challenges, the strength of ABS parts is often not worth the effort required to print
them, and PETG is a better choice for most applications. Despite this, ABS can be inexpensive and often found
near the same price as PLA.

* ABS hotend temperatures: 230-250° C
* ABS bed temperatures: 100-120° C
* Enclosure highly recommended to prevent warping

Due to the difficulties presented by ABS, some teams may want to look at a similar material known as ASA, which
is easier to print with and has similar properties to ABS, but is more expensive.


TPU/TPE (Thermoplastic Polyurethane/Elastomer)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TPU and TPE are flexible filaments that can be used to create parts that are flexible and can bend. These filaments
are sold under a variety of different durometers (a measure of a material's hardness). TPU/TPE's flexibility grants
it an extremely high impact resistance, making it very durable as well. In FTC, TPU/TPE is often used to make
flexible components such as intake rollers, wheel bumpers, and occasionally low-load toothed belts.

.. tip:: Since TPU/TPE is very flexible, printers with a Bowden extrusion system, where the extruder motor and gear
is not located near the hotend, will have a very difficult time printing with it.

* TPU/TPE hotend temperatures: 210-250° C
* TPU/TPE does not usually need a heated bed, but if one is used care should be taken to not allow the bed to
  exceed 60° C, as this can cause the filament to fuse to the bed.
* TPU/TPE is quite hydrophilic, and will absorb moisture from the air, which will likely require drying before and
  possibly during printing.
* Direct drive extrusion system highly recommended
