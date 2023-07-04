Exposure Control
----------------

Exposure is the amount of light that reaches the webcam sensor. It is an
important part of how bright or dark your image appears.

Exposure varies directly with the amount of time that the shutter is
open, allowing light to enter and reach the sensor. So, the 
interface ExposureControl uses a single value of **duration**, in units
of time that you specify, typically ``TimeUnit.MILLISECONDS``.

For example, at a frame rate of 60 frames per second (fps), exposure
duration is 1/60 of a second, or 1/60 x 1000 = 16 milliseconds. This
basic tutorial does not address frame rate.

Here are the methods to manage exposure: 

- setExposure() has two parameters: duration and time unit 
- getExposure() has one parameter: time unit

The webcam may support minimum and maximum allowed values of exposure.
These can be retrieved with: 

- getMinExposure(TimeUnit.MILLISECONDS) 
- getMaxExposure(TimeUnit.MILLISECONDS)

There are no ``set()`` methods for min and max exposure; these are
hard-coded in the webcam’s firmware. Note that firmware settings may
vary among different versions of the same webcam model.

These and other exposure methods are called on an ExposureControl
object; sample code is shown below, after Exposure Control Mode.