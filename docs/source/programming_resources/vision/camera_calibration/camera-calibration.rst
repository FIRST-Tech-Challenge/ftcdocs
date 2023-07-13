Camera Calibration for *FIRST* Tech Challenge
=============================================

What is a camera calibration and why is it needed?
--------------------------------------------------

Cameras are composed of many different components that can introduce variability
in the actual image that a camera ultimately "sees". Camera calibration is a
process that mathematically models how a camera & lens combination ultimately 
sees the world, for example how wide the field of view is. Calibrating your camera
is a must if you desire to use it for high-precision tasks, such as performing
precision measurements using the camera or obtaining accurate 6DOF pose data from 
fiducial marker systems like AprilTags. It's important to note that calibrations 
are not only specific to the camera and lens, but also specific to the resolution 
used on a particular camera as well!

.. warning:: 
   Due to the differences in refractive index, calibrations performed in air and 
   in liquids (for example, in water) are not transferrable. Calibrations must be 
   performed within the medium that the camera will be operating in. 

Camera Calibration Methods
--------------------------

There are many methods to calibrate cameras, including OpenCV, MATLAB, MRCAL
etc. 

-  For advanced teams, using `MRCAL <http://mrcal.secretsauce.net/>`__ is
   likely the best option - it is a tool developed by NASA JPL that provides
   extensive data on how good your calibration is and what goes into the numerical
   optimization to arrive at the optimal parameters. 
-  For the rest of us, here we explain how to calibrate your camera using `3DF Zephyr
   <https://www.3dflow.net/3df-zephyr-free/>`__, which is
   extremely easy to use and can provide reasonable results.

Calibrating with 3DF Zephyr
---------------------------

1. Download and install `3DF Zephyr Free Edition <https://www.3dflow.net/3df-zephyr-free/>`__.
2. Copy the sample ``UtilityCameraFrameCapture`` OpMode to your teamcode folder,
   and modify the parameters at the top according to your needs. It's important
   to note that this Sample is only written in Java.
3. In 3DF Zephyr, go to:

   - Utilities --> Images --> Camera Calibration 

   and follow the instructions. Use the frame capture OpMode to take the pictures.
4. Connect your Robot Controller device to your computer with a USB cable and
   copy the captured frames to your computer. They will be located in the root
   of the USB storage, with names prefixed by ``VisionPortal-``.
5. Press the *Add Images* button in 3DF Zephyr and point it to the images you
   just copied to your computer.
6. Run the calibration target analysis in 3DF Zephyr; when it is complete, it
   will provide you with ``fx, fy, cx, cy`` which are the needed calibration
   parameters to be applied to your ``AprilTagProcessor``.


