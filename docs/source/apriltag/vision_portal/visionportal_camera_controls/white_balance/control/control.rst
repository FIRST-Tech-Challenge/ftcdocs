White Balance Control
---------------------

:java:extdoc:`org.firstinspires.ftc.robotcore.external.hardware.camera.controls.WhiteBalanceControl`

Continuing with other interfaces, the SDK (new for version 7.1)
provides methods for white balance control.

White balance is a digital camera setting that balances the **color
temperature** in the image. Color temperature is measured in units of
degrees Kelvin (K) and is a physical property of light.

For example, sunlight at noon measures between 5200-6000 K. An
incandescent light bulb (warm/orange) has a color temperature of around
3000 K, while shade (cool/blue) measures around 8000 K.

When performed automatically, white balance adds the opposite color to
the image in an attempt to bring the color temperature back to neutral.
This interface WhiteBalanceControl allows the color temperature to be
directly programmed by a user.

A single value is used here to control white balance temperature, in
units of degrees Kelvin, of Java type integer. Here are the methods:

-  setWhiteBalanceTemperature(int temperature)
-  getWhiteBalanceTemperature()

As with exposure and gain, the webcam may support minimum and maximum
allowed values of white balance temperature. These can be retrieved
with:

-  getMinWhiteBalanceTemperature()
-  getMaxWhiteBalanceTemperature()

There are no ``set()`` methods for min and max temperature values; these
are hard-coded in the webcam’s firmware. Note that firmware settings may
vary among different versions of the same webcam model.

The Logitech C920 webcam has a min value of 2000 and a max value of
6500.