General Design for 3d Printed Parts
===================================

Gradually as you 3d print more you will acquire a general design sense. You will have a good sense of what you should and shouldn't print, 
know what your printer is capable of, and know what won't break. A lot of this comes with experience, but there are some general tips that 
can be given.

Large Prints
------------
If you're using your entire build plate, you generally should not be printing that part continuously. Design the part to be connected in 
various places with hardware, or even better, design it to have metal reinforcement and use 3d prints for only the unique/specific geometry.

|

The reason this is said is due to problems with unitization (a practice of combining or splitting multiple parts into smaller or larger objects).
If your part takes a whole print plate, and breaks while on the robot, you have to painfully run a very long print again. Segmented parts can be 
more easily replaced if part of it breaks. Keep your parts small and easy to run replacement prints for.

Avoiding Fine Details
---------------------
3D Printers can achieve a fairly high level of detail but functional parts of a part should be kept to be large geometry as smaller geometry often 
fails easier. For example, when printing something like gears, it's advised to do a large module such as 1-2mm, because standard 3D printers just 
can't print smaller teeth with accuracy and strength. You should make sure all parts of a print are at least 2-3x your nozzle width, to make sure 
that sufficient strength can be achieved. For a standard 0.4mm nozzle, 1.2mm is really the thinnest any part of your design should be.

