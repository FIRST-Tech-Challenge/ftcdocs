.. meta::
   :title: Optimizing Videos for FTC-ML
   :description: A guide to optimizing the input videos for use in FTC-ML
   :keywords: FTC Docs, FIRST Tech Challenge, FTC, FTC-ML, Tensorflow, TFOD, FMLTC

Optimizing Videos for increased TensorFlow Model Performance
============================================================


Before diving into creating your first videos for TensorFlow training,
it’s important to cover a bunch of topics under the header of, “Things
you should really know about TensorFlow for ftc-ml and were hopefully
probably about to ask anyway”. Here they are, in an order that hopefully
makes some sense. Please read this in its entirety:

1. AI and Machine learning are **incredibly** resource-hungry
   operations.

   -  For high-end performance, machine learning applications can run on
      special Google-designed Artificial Intelligence (AI) accelerator
      hardware chips known as Tensor Processing Units (TPU). These
      advanced chips are specialized for the high-volume low-precision
      computations required for AI processing, and are Google
      proprietary. TPUs generally consume large amounts of power when
      running in the Google datacenters. A TPU designed to consume far
      less power, known as the Pixel Neural Core, was introduced in the
      Pixel 4 smartphone in 2019 for machine learning applications.

   -  For far less performance, machine learning applications can run on
      traditional Graphical Processing Units (GPU) typically found on
      graphics cards or embedded systems. Most modern cell phones
      contain GPUs, such as the Qualcomm Adreno 308 GPU found on the
      Moto E5 phone. However, performance is relative – the performance
      of GPUs found in cell phones is dwarfed by GPUs found in graphics
      cards or desktop systems.

   -  For incredibly unreasonably low performance, machine learning
      applications can run on a general Central Processing Unit (CPU).
      Let’s say no more about this and move along.

2. Building a TensorFlow model from scratch can take months of TPU time
   to train and refine the model properly. However, pre-trained models
   can be used as starting points to relatively quickly add novel (new)
   datasets. Therefore, Google provids a `TensorFlow Detection Model
   Zoo <https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md>`__
   that contains pre-trained models using the `COCO 2017
   dataset <https://cocodataset.org/#home>`__ composed of over
   120,000 images of common everyday objects classified into `81
   different
   labels <https://github.com/tensorflow/models/blob/master/research/object_detection/data/mscoco_complete_label_map.pbtxt>`__.
   The ftc-ml tool uses the SSD MobileNet v2 320x320 model as its
   default starter model from this Zoo – the TensorFlow models released
   in the `FTC 7.0
   SDK <https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases/tag/v7.0>`__
   are based on this model too. Unfortunately due to the way models are
   trained within ftc-ml, those everyday object labels are no longer
   accessible once you train for additional objects. However, by using
   those stock Zoo models (instead of training to add your own objects)
   and adding the proper labels to your Op Mode, your Op Mode could
   recognize 81 categories of objects without training a new model. If
   you have the ability to customize objects, images can be added to
   those objects that the Zoo models recognize – like a picture of a
   cat, a picture of a teddy bear, or even a stop sign (these are 3
   categories of objects that can be recognized using the zoo models
   once the appropriate labels are added to your Op Mode code).

**NOTE:** FTC is working to convert several of these TensorFlow Model
Zoo models from full TensorFlow models (.pb files) to TensorFlow-Lite
models (.tflite files) to be used within FTC Op Modes. It will be
announced on the Help/Feedback forums once these models are available
for use.

3.  The performance of a TensorFlow model using Object Detection, even
    on TPU hardware, is completely dependent upon the core resolution of
    the model it’s working with. The larger the core resolution, the
    more processing the model must perform. As an optimization, the core
    models in the TensorFlow Detection Model Zoo are trained on square
    (meaning equal width and height) resolutions of varying sizes. For
    TensorFlow models designed for Mobile applications, the core
    resolution is intentionally kept small. A 640x640 core model
    requires at least 4x the processing effort of a 320x320 core model;
    not all mobile devices can keep up with even 1-2 frames per second
    (fps) processing rates even on a 320x320 model!

4.  Modern webcams have very high resolutions. The minimum resolution
    for an “acceptable” modern webcam is 720p. When scaling 720p, 1080p,
    or higher resolution images to a core model resolution of 320x320,
    fine details in the image are lost. The 16:9 aspect ratio source
    image is squeezed to a 1:1 aspect ratio image, making wide objects
    narrow (this is part of the reason why a webcam trained in a
    landscape orientation has poorer detection in portrait orientation).
    Small yellow objects in the source image suddenly turn into tiny
    indistinguishable blocky yellow blobs. The effects of the scaling
    process can be brutal.

5.  To combat the effects of scaling, varying the “pose” of an object
    (orientation, angle, and distance from the camera) is incredibly
    important.

    -  It is vital that the size of the object in the image be as large
       as possible when the camera is at maximum detection distance from
       the object. The larger the object is in the image, the more
       likely that scaling effects will have a lessened impact on the
       scaled image.

    -  TensorFlow models are able to be more generically trained (that’s
       a good thing) when the objects are different sizes in different
       images. For example, including poses with the object at different
       distances from the camera is ideal. Building a labeled dataset
       with the object at different sizes helps the model recognize the
       objects better when they are different sizes.

    -  If the object should still be recognized when it is rotated in
       any way, rotational variations are also important.

    -  I hope you’ve realize this by now, but TensorFlow models follow
       the garbage-in garbage-out concept in model training. The more
       variations in size, rotation, angle, and orientation you can
       supply of the target object the more the model is going to be
       able to recognize/predict that target object.

6.  TensorFlow Object Detection is not the best at recognizing
    geometries. Yes, this might run contrary to conventional wisdom in
    human object detection. Because a machine learning model is usually
    trained to be as general as possible, yellow circles and yellow
    octogons (depending on size) could be difficult to differentiate
    from each other (and from a generic yellow blob) depending on how
    the model is trained. Therefore, don’t expect TensorFlow to be
    really good at recognizing subtle differences in geometry.

7.  Even though TensorFlow isn’t the best at recognizing geometries,
    it’s incredibly good at recognizing textures. No, probably not the
    kinds of textures you’re thinking about – we’re talking visual
    textures like zebra stripes, giraffe spots, neon colors, and so on.
    Colored patterns are TensorFlow’s strength. Careful Team Shipping
    Element design beforehand may yield great benefits later.
8.  When creating videos for TensorFlow training, be very careful about
    the backgrounds being used. Machine Learning involves passing data
    and answers to a model, and letting the model determine the rules
    for detecting objects. If the background of an object is always
    consistent – let’s say the object is a duck on dark gray tiles – the
    model may include in its rules that the object must always be on a
    dark gray background, and will not recognize the duck on light gray
    tiles. In order to create a more generic model, the object would
    need to be found on multiple different backgrounds. “Negative
    Frames”, or frames that have no labels in them and are just of the
    background, can be used to help the model intentionally recognize
    “what is in the background” and that those elements of the
    background should be ignored; TensorFlow does this by adding the
    background patterns to an internal “background” label that is never
    shown to the user. It’s not typically necessary to include “Negative
    Frames”, however, unless there is content in the background that is
    only seen when the object is not present, and you feel it’s
    advantageous to ignore that content. TensorFlow and modern Machine
    Learning algorithms isolate portions of each frame that do not
    include bounding boxes and add those portions of the image to the
    “background” label.

9.  Related to backgrounds, lighting effects can cause issues with
    Object Detection. If the model is only trained with frames with
    objects that are extremely well lit, the model may not be very good
    when the objects are not so well lit. It’s important to get
    videos/frames of different lighting conditions if it’s possible that
    the lighting conditions could differ between training and
    competition venues. One `classical urban legend about tank
    detection <https://www.gwern.net/Tanks>`__ in the early 1990’s gives
    a pretty good warning about dataset bias.

10. If multiple similar-looking objects could possibly be in a frame and
    you only want the model to ever recognize one of them (for example
    you could have Yellow Blocks and Yellow Ducks in the same frame, but
    you ONLY want the model to detect Ducks) it is advised that yellow
    blocks be present but unlabeled in multiple frames. This allows the
    background detector to pick up the yellow blocks as background
    items, and be trained (covertly) to not recognize blocks as ducks by
    accident. There is no need to label objects in a model unless you
    want TensorFlow to specifically learn them.

11. Play like you train, and train like you play. This is just a poor
    way of saying, “try your best to video how your robot will see the
    objects in competition, and try your best in competition to make
    sure that your robot only sees the objects like you trained the
    model”. This has been said in different ways multiple times, but it
    needs to be repeated. The most likely reason a model will have poor
    performance in competition is because something has changed –
    whether that be the lighting is different, more/different objects
    are in the background, the pose of the objects are too different
    from those during training, and so on.

12. This might not need to be said, but avoid “floppy” or “non-rigid”
    objects. For example fabric that can be folded or bunched up,
    flexible objects with joints that can move, or structures that can
    easily bend. Models still might be able to differentiate some of the
    possible variations, but the likelihood that it doesn’t when it
    matters is too great.