Creating videos of objects to be recognized
============================================

The ftc-ml tool uses videos instead of individual images because videos
are an efficient package for managing potentially hundreds of images of
the same object at slightly different angles/orientations and distances
from the camera (poses). While video capture can be performed with any
camera, it’s recommended that videos have exactly the same resolution as
the camera being used on the robot. Ideally video capture should be done
with the exact camera being used on the robot at the estimated height
from the surface of the floor that the camera will be at. By using the
exact camera on the robot, specific artifacts of the camera used – such
as lens distortion and other optical effects – can be reflected in the
training images which result in a much better overall object detection
rate. Programs such as the Windows 10 Camera Application can be used to
capture video from a webcam while it’s mounted on a robot and plugged
into a laptop. It’s recommended to use the lowest frames per second
(fps) setting possible, only because with a higher framerate the
likelihood of getting multiple frames of the exact same image are
incredibly high, and that’s just wasted frames that you have to label
(or manually discard) and there’s no extra benefit in model training
with duplicate frames (it takes longer to train your model). There are
multiple web-based tools that will allow you to change the frame rate by
removing frames from the video free online. For tips and best practices
for creating the best poses, see Section 7 Optimizing Videos for
increased TensorFlow Model Performance.