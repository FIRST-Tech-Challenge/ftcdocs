Focus Control
-------------

:java:extdoc:`org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl`

At a distance called “focus length”, a subject’s image (light rays)
converge from the lens to form a clear image on the webcam sensor.

If supported by the webcam, focus can be managed with these FocusControl
methods: 

-  setFocusLength(double focusLength) 
-  getFocusLength()

Distance units are not specified here; they may be undimensioned values
within an allowed range. For example, the Logitech C920 allows values
from 0 to 250, with **higher** values focusing on **closer** objects.

The webcam may support minimum and maximum allowed values of focus
length. These can be retrieved with: 

-  getMinFocusLength() 
-  getMaxFocusLength()

There are no ``set()`` methods for min and max focus length; these are
hard-coded in the webcam’s firmware. Note that firmware settings may
vary among different versions of the same webcam model.

These and other focus methods are called on a FocusControl object, as
described above for exposure.