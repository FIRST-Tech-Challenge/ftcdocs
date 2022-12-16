.. meta::
   :title: FIRST Machine Learning Toolchain
   :description: The official FIRST Machine Learning Toolchain (FTC-ML) manual
   :keywords: FTC-ML, FTC ML, FIRST Machine Learning Toolchain, FMLTC, FTC, Tensorflow, Object Detection

*FIRST* Machine Learning Toolchain
==================================

.. warning::
   Please be aware, TensorFlow has multiple "tasks" that it can perform - among these are "Object Detection", 
   "Image Classification", "Speech Recognition", "Segmentation", "Natural Language Question Answering", 
   "Audio Classification", "Optical Character Recognition", and more. In *FIRST* Tech Challenge only the
   "Object Detection" task is supported - that allows for detecting multiple objects in an image along with
   bounding boxes to help identify where in the image the objects are found. Many online tools, such as 
   Google Teachable Machines, use the "Image Classification" task - that allows for detecting a single object
   without a bounding box. These may seem similar, but they are not interchangeable. The *FIRST* Tech 
   Challenge TensorFlow SDK **ONLY** supports the use of "TensorFlow Object Detection (TFOD)". ftc-ml is 
   a tool that is supported by *FIRST* Tech Challenge - using outside tools, even those designed for TFOD, 
   are not supported by *FIRST* Tech Challenge; because of the "research" classification of TensorFlow 
   breaking changes are inevitable and maintenance of projects in the TensorFlow community is abysmal. **NO** 
   support will be provided for outside model trainers.

This tool, the *FIRST* Tech Challenge Machine Learning toolchain **(FTC-ML)**, allows *FIRST* Tech Challenge 
teams to create custom TensorFlow models for use in the game challenge. Learn how to train TensorFlow to 
recognize your Custom Signal Sleeve images and more using this tool, and download 
models that you can use in your autonomous and driver-controlled Op Modes. 

.. toctree::
   :maxdepth: 2

   intro/intro
   logging_on/logging-on
   managing_tool/index
   implement/index
   optimize_videos/optimize-videos
   faq/faq


Volunteer Special Thanks
-------------------------

The *FIRST* Tech Challenge staff would like to extend a special thanks
to the following volunteers for their hard work and dedication toward
this project:

-  Liz Looney, Google – FIRST Machine Learning Toolchain lead developer

-  Mr. Phil Malone – Model designer and platform tester

-  Uday Vidyadharan, Team 7350 – Platform tester and Contributor

-  Jacob Burroughs – Platform configuration and SSO

-  Richard Lester – Platform UI improvements

