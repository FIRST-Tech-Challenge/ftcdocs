Gain Control
------------

:java:extdoc:`org.firstinspires.ftc.robotcore.external.hardware.camera.controls`

Gain is a digital camera setting that controls the amplification of the
signal from the webcam sensor. This amplifies the whole signal,
including any associated background noise.

Gain can be managed in coordination with exposure. Raising exposure and
keeping gain low, can provide a bright image and low noise. On the other
hand, longer exposure can cause motion blur, which may affect target
tracking performance. In some cases, reducing exposure duration and
increasing gain may provide a sharper image, although with more noise.

The interface GainControl uses a single value to control gain. It’s
used for amplification, and thus has no units – it’s just a number of
type integer. Its methods are: 

- setGain(int gain) 
- getGain()

As with exposure, the webcam may support minimum and maximum allowed
values of gain. These can be retrieved with: 

- getMinGain() 
- getMaxGain()

There are no ``set()`` methods for min and max gain; these are
hard-coded in the webcam’s firmware. Note that firmware settings may
vary among different versions of the same webcam model.

These and other gain methods are called on a GainControl object, as
described above for exposure.