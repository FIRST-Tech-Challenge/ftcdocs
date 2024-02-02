AprilTag ID Codes
=================

After the AprilTag Processor and VisionPortal have been **initialized**, your
OpMode can begin tag detection.

Let's start with the simple task of retrieving the **ID code** of a detected
AprilTag.  For tag family 36h11, the numeric ID code ranges from 0 to 586. The
FTC SDK can provide over 30 fields per detected AprilTag, if that tag's size
was provided (thus eligible for pose estimation).  Otherwise only tag ID code
is available.

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      .. figure:: images/070-ID-Block-arrow.png
         :width: 75%
         :align: center
         :alt: AprilTag ID Code

         Highlighting blocks for getting AprilTag ID Code

   .. tab-item:: Java
      :sync: java

      Example of retrieving AprilTag ID

      .. code-block:: java
 
         AprilTagDetection myAprilTagDetection;
         int myAprilTagIdCode = myAprilTagDetection.id;

Since the camera might see multiple AprilTags at once, retrieving any field(s)
is usually done with a **`for() loop`**.  The loop can process each detection,
one at a time:

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      .. figure:: images/080-AprilTag-Blocks-FOR-loop.png
         :width: 75%
         :align: center
         :alt: AprilTag FOR Loop

         All AprilTag Detections being read in a FOR Loop

      This code snippet assumes ``myAprilTagProcessor`` and VisionPortal have been
      initialized, as described at previous pages **Processor Initialization** and
      **VisionPortal Initialization**.

   .. tab-item:: Java
      :sync: java

      Example reading all detected AprilTags in a FOR Loop

      .. code-block:: java
 
         AprilTagProcessor myAprilTagProcessor;
         List<AprilTagDetection> myAprilTagDetections;	// list of all detections
         AprilTagDetection myAprilTagDetection;		// current detection in for() loop
         int myAprilTagIdCode;                           // ID code of current detection, in for() loop

         // Get a list of AprilTag detections.
         myAprilTagDetections = myAprilTagProcessor.getDetections();

         // Cycle through through the list and process each AprilTag.
         for (myAprilTagDetection : myAprilTagDetections) {

              if (myAprilTagDetection.metadata != null) {  // This check for non-null Metadata is not needed for reading only ID code.
                   myAprilTagIdCode = myAprilTagDetection.id;

                   // Now take action based on this tag's ID code, or store info for later action.

              }
         }

      This code snippet assumes ``myAprilTagProcessor`` and VisionPortal have been
      initialized, as described at previous pages **Processor Initialization** and
      **VisionPortal Initialization**.

The OpMode should take the desired action for each AprilTag **inside** the
``for() loop``, or store information for later action.  In the above example,
the variable ``myAprilTagIdCode`` receives the different values of each
detection, ending with only the **last tag's value**.

By default, the FTC SDK recognizes the ID code of **any** 36h11 AprilTag, even
if the OpMode did not place that tag in the AprilTag Library.  Some tags are
placed in the Library automatically by the SDK: for example, ID codes 583-586
used by Sample OpModes.

An OpMode can also place other tags in a Library, to supplement or overwrite
default tags.  This is covered further at the **Library** page.

====

*Questions, comments and corrections to westsiderobotics@verizon.net*

