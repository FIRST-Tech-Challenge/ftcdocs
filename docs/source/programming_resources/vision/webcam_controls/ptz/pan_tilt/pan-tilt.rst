Pan and Tilt
=============

A webcam does not typically express pan and tilt values in *pixels*, the
smallest unit of image capture by the webcam sensor. For example, the
Logitech C920 and the Microsoft LifeCam VX-5000 have a range of
+/-36,000 units, far greater than the pixel count in each axis.

The webcam accepts pan and tilt as a pair of (x, y) values. Thus the 
SDK pan and tilt methods handle these values **only as a pair**, in a
special class named PanTiltHolder. This class has two fields, named pan
and tilt, of type integer.

Here’s an example to illustrate using the basic methods:

.. code:: java

   myHolder.pan = 5;                  // assign the pan field
   myHolder.tilt = 10;                // assign the tilt field
   myPtzControl.setPanTilt(myHolder);         // command the webcam with (x, y) pair

To retrieve values from the webcam:

.. code:: java

   newHolder = myPtzControl.getPanTilt();      // retrieve (x, y) pair from webcam
   int currentPanValue = newHolder.pan;        // access the pan value
   int currentTiltValue = newHolder.tilt;      // access the tilt value

The above examples assume these objects already exist:

.. code:: java

   PtzControl myPtzControl = vuforia.getCamera().getControl(PtzControl.class); // create PTZ webcam control object
   PtzControl.PanTiltHolder myHolder = new PtzControl.PanTiltHolder();         // instantiate input holder object
   PtzControl.PanTiltHolder newHolder;                                 // declare output holder object

The webcam may support minimum and maximum allowed pan/tilt paired
values. Subject to the control object guidelines shown above, these can
be retrieved as follows: 

-  ``minPanTiltHolder = getMinPanTilt();`` 
-  ``maxPanTiltHolder = getMaxPanTilt();``

There are no ``set()`` methods for min and max pan/tilt values; these
are hard-coded in the webcam’s firmware. Note that firmware settings may
vary among different versions of the same webcam model.

These pan and tilt methods are called on a PtzControl object, as
described above for exposure.