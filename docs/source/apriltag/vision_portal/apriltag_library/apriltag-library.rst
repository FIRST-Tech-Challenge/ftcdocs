AprilTag Library
================

For a *FIRST* Tech Challenge match, your OpMode has a known set of AprilTags to
detect.  They are preloaded by default or specified by you, with or without
custom tags.

These tags form an **AprilTag Library**. Each Library tag has a set of 4
to 6 properties, described at the **Metadata** page.

This page shows many ways to create an AprilTag Library. The
**Initialization** page explained this is the optional **Step 1** of
preparing to use AprilTags in an OpMode.

**Try these examples in order**, to master the use of AprilTag
Libraries.

The Easy Way
~~~~~~~~~~~~

Let’s start with… no Library! If your OpMode will use only the current 
season defaults, no Library action is needed.

Simply create the AprilTagProcessor as follows:

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      .. figure:: images/010-Blocks-ATprocessor-Easy.png
         :width: 75%
         :align: center
         :alt: Simple AprilTag Processor

         Simple AprilTag Processor

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         AprilTagProcessor myAprilTagProcessor;

         // Create the AprilTag processor and assign it to a variable.
         myAprilTagProcessor = AprilTagProcessor.easyCreateWithDefaults();

Specifying a Library is needed for creating an AprilTag Processor. Even
this “Easy Way” does specify the default Library, behind the scenes.

Default Libraries
~~~~~~~~~~~~~~~~~

The SDK uses two core Libraries of predefined AprilTags:

-  tags used only in Sample OpModes
-  tags used only in the Robot Game (competition)

The first Library, called ``SampleTagLibrary``, is available now with
SDK 8.2. Its basic Metadata values are:

-  ``583, Nemo, 4, DistanceUnit.INCH``
-  ``584, Jonah, 4, DistanceUnit.INCH``
-  ``585, Cousteau, 6, DistanceUnit.INCH``
-  ``586, Ariel, 6, DistanceUnit.INCH``

The second Library, called ``CenterStageTagLibrary``, is planned for
future competition only. It’s available now in SDK 8.2, but currently
holding three “placeholder” tags:

-  ``0, MEOW, 0.166, DistanceUnit.METER``
-  ``1, WOOF, 0.166, DistanceUnit.METER``
-  ``2, OINK, 0.166, DistanceUnit.METER``

After Kickoff in September 2023, these will be replaced (in SDK 9.0)
by the **real tags** for CENTERSTAGE.

For convenience, a third Library contains **both** of these core
Libraries, and nothing else. This is the default, called
``CurrentGameTagLibrary``.

AprilTag Processor
~~~~~~~~~~~~~~~~~~

Specifying **any aspect** of a Processor is done with a **Processor
Builder**, requiring at least 2 commands:

-  create the Builder, using the Java keyword ``new``

-  after specifying/adding features, finalize with a call to the
   ``.build()`` method

In between these actions, your OpMode will add one of the three
Libraries directly to the Processor Builder. It’s easiest to use the
default ``CurrentGameTagLibrary``, containing all of the predefined
tags.

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      First create this expression, drawing the first component from the
      ``AprilTagProcessor.Builder`` toolbox (or palette), and drawing the
      second component from the ``AprilTagLibrary`` toolbox.

      .. figure:: images/020-Blocks-setTagLibrary-CurrentGame.png
         :width: 75%
         :align: center
         :alt: Set Current Game Tag Library

         Setting Current Game Tag Library

      **Around this** (before and after), place one Block to **create** the
      Processor Builder, and another Block to **finalize** the process with
      ``.build()``.

      .. figure:: images/030-Blocks-ATprocessor-CurrentGame.png
         :width: 75%
         :align: center
         :alt: Completing Builder

         Completing Builder 

      These are the first and last Blocks in the ``AprilTagProcessor.Builder``
      toolbox. The remaining Blocks are used to set optional features of the
      Processor. Here we are setting only the Library.

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         AprilTagProcessor.Builder myAprilTagProcessorBuilder;
         AprilTagProcessor myAprilTagProcessor;

         // Create a new AprilTagProcessor.Builder object and assign it to a variable.
         myAprilTagProcessorBuilder = new AprilTagProcessor.Builder();

         // Set the tag library.
         // Get the AprilTagLibrary for the current season.
         myAprilTagProcessorBuilder.setTagLibrary(AprilTagGameDatabase.getCurrentGameTagLibrary());

         // Build the AprilTag processor and assign it to a variable.
         myAprilTagProcessor = myAprilTagProcessorBuilder.build();


Library Variable
~~~~~~~~~~~~~~~~

As an alternate, you could first store the Library in your own Variable
name. Then specify that name for the AprilTag Processor. Here we use
``myAprilTagLibrary`` (any other name is fine).

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      First create this expression, drawing the first component from the
      ``AprilTagLibrary`` toolbox, and drawing the second component from
      the ``AprilTagProcessor.Builder`` toolbox.

      .. figure:: images/040-Blocks-ATProcessor-Variable.png
         :width: 75%
         :align: center
         :alt: Set Tag Library

         Set the Tag Library

      As before, **around this** (before and after), place one Block to
      **create** the Processor Builder, and another Block to **finalize** the
      process with ``.build()``.

      .. figure:: images/050-Blocks-ATprocessor-CurrentGame-Variable.png
         :width: 75%
         :align: center
         :alt: Build the AprilTag Processor

         Build the AprilTag Processor

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         AprilTagProcessor.Builder myAprilTagProcessorBuilder;
         AprilTagProcessor myAprilTagProcessor;
         AprilTagLibrary myAprilTagLibrary;

         // Create a new AprilTagProcessor.Builder object and assign it to a variable.
         myAprilTagProcessorBuilder = new AprilTagProcessor.Builder();

         // Get the AprilTagLibrary for the current season.
         myAprilTagLibrary = AprilTagGameDatabase.getCurrentGameTagLibrary();

         // Set the tag library.
         myAprilTagProcessorBuilder.setTagLibrary(myAprilTagLibrary);

         // Build the AprilTag processor and assign it to a variable.
         myAprilTagProcessor = myAprilTagProcessorBuilder.build();


Library Builder, with Defaults
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next we try the Builder pattern, to create a Library containing only
predefined AprilTags. It’s not needed (nothing new to Build!), but it’s
an easy introduction.

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      -  Create a Library Builder, not the same as a Processor Builder.
      -  Then use the ``addTags`` Block – note the plural “tags”, not
         “tag”.
      -  Finalize the process with the ``.build`` command.

      The built Library is assigned or saved to your Variable, here called
      ``myAprilTagLibrary``.

      .. figure:: images/060-Blocks-LibraryBuilder-CurrentGame.png
         :width: 75%
         :align: center
         :alt: Build the Tag Library

         Build the Tag Library

      Next comes the familiar steps:

      -  Create a Processor Builder.
      -  Then set, or add, the Library built and saved in the previous
         sequence.
      -  Finalize the process with the ``.build`` command.

      .. figure:: images/070-Blocks-Processor-Variable.png
         :width: 75%
         :align: center
         :alt: Build the Tag Processor

         Build the Tag Processor

      The final result is the same as the previous examples, but now you see
      how to use a Library Builder.

   .. tab-item:: Java
      :sync: java

      .. code-block:: java

         AprilTagLibrary.Builder myAprilTagLibraryBuilder;
         AprilTagProcessor.Builder myAprilTagProcessorBuilder;
         AprilTagLibrary myAprilTagLibrary;
         AprilTagProcessor myAprilTagProcessor;

         // Create a new AprilTagLibrary.Builder object and assigns it to a variable.
         myAprilTagLibraryBuilder = new AprilTagLibrary.Builder();

         // Add all the tags from the given AprilTagLibrary to the AprilTagLibrary.Builder.
         // Get the AprilTagLibrary for the current season.
         myAprilTagLibraryBuilder.addTags(AprilTagGameDatabase.getCurrentGameTagLibrary());

         // Build the AprilTag library and assign it to a variable.
         myAprilTagLibrary = myAprilTagLibraryBuilder.build();

         // Create a new AprilTagProcessor.Builder object and assign it to a variable.
         myAprilTagProcessorBuilder = new AprilTagProcessor.Builder();

         // Set the tag library.
         myAprilTagProcessorBuilder.setTagLibrary(myAprilTagLibrary);

         // Build the AprilTag processor and assign it to a variable.
         myAprilTagProcessor = myAprilTagProcessorBuilder.build();


Custom Tag - Direct
~~~~~~~~~~~~~~~~~~~

Finally, we are ready to add custom tags to a Library.

Each tag needs Metadata. You can enter Metadata values directly to a new
tag, as follows.

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      The third Block adds the custom tag to the Library. All other Blocks are
      the same as the previous example.

      .. figure:: images/080-Blocks-addTag.png
         :width: 75%
         :align: center
         :alt: Custom Tag Library

         Add custom tags to Tag Library

   .. tab-item:: Java
      :sync: java

      The custom tag is added with **one new line** of code, otherwise the
      same as the previous example.

      .. code-block:: java

         AprilTagLibrary.Builder myAprilTagLibraryBuilder;
         AprilTagProcessor.Builder myAprilTagProcessorBuilder;
         AprilTagLibrary myAprilTagLibrary;
         AprilTagProcessor myAprilTagProcessor;

         // Create a new AprilTagLibrary.Builder object and assigns it to a variable.
         myAprilTagLibraryBuilder = new AprilTagLibrary.Builder();

         // Add all the tags from the given AprilTagLibrary to the AprilTagLibrary.Builder.
         // Get the AprilTagLibrary for the current season.
         myAprilTagLibraryBuilder.addTags(AprilTagGameDatabase.getCurrentGameTagLibrary());

         // Add a tag, without pose information, to the AprilTagLibrary.Builder.
         myAprilTagLibraryBuilder.addTag(55, "Our Awesome Team Tag", 3.5, DistanceUnit.INCH);

         // Build the AprilTag library and assign it to a variable.
         myAprilTagLibrary = myAprilTagLibraryBuilder.build();

         // Create a new AprilTagProcessor.Builder object and assign it to a variable.
         myAprilTagProcessorBuilder = new AprilTagProcessor.Builder();

         // Set the tag library.
         myAprilTagProcessorBuilder.setTagLibrary(myAprilTagLibrary);

         // Build the AprilTag processor and assign it to a variable.
         myAprilTagProcessor = myAprilTagProcessorBuilder.build();


Custom Tag - Variable
~~~~~~~~~~~~~~~~~~~~~

As an alternate, you can assign Metadata to a Variable, then use that
Variable to create a new AprilTag.

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      These two Blocks could replace the single new Block in the previous
      example.

      .. figure:: images/090-Blocks-add-Metadata.png
         :width: 75%
         :align: center
         :alt: Variable Metadata

         Setting Metadata with Variable

      These Blocks are separated, to illustrate that the Metadata Variable can
      be initialized/assigned anywhere before being added with the Library
      Builder. It doesn’t have to appear immediately before use.

   .. tab-item:: Java
      :sync: java

      The custom tag is added with **two lines** of code, replacing the **one
      new line** in the previous example.

      .. code-block:: java

         AprilTagMetadata myAprilTagMetadata;
         AprilTagLibrary.Builder myAprilTagLibraryBuilder;
         AprilTagProcessor.Builder myAprilTagProcessorBuilder;
         AprilTagLibrary myAprilTagLibrary;
         AprilTagProcessor myAprilTagProcessor;

         // Create a new AprilTagLibrary.Builder object and assigns it to a variable.
         myAprilTagLibraryBuilder = new AprilTagLibrary.Builder();

         // Add all the tags from the given AprilTagLibrary to the AprilTagLibrary.Builder.
         // Get the AprilTagLibrary for the current season.
         myAprilTagLibraryBuilder.addTags(AprilTagGameDatabase.getCurrentGameTagLibrary());

         // Create a new AprilTagMetdata object and assign it to a variable.
         myAprilTagMetadata = new AprilTagMetdata(55, "Our Awesome Team Tag", 3.5, DistanceUnit.INCH);

         // Add a tag to the AprilTagLibrary.Builder.
         myAprilTagLibraryBuilder.addTag(myAprilTagMetadata);

         // Build the AprilTag library and assign it to a variable.
         myAprilTagLibrary = myAprilTagLibraryBuilder.build();

         // Create a new AprilTagProcessor.Builder object and assign it to a variable.
         myAprilTagProcessorBuilder = new AprilTagProcessor.Builder();

         // Set the tag library.
         myAprilTagProcessorBuilder.setTagLibrary(myAprilTagLibrary);

         // Build the AprilTag processor and assign it to a variable.
         myAprilTagProcessor = myAprilTagProcessorBuilder.build();

For Blocks or Java, multiple tags could be added with multiple
(shorter!) Variable names, such as ``myTag1``, ``myTag2``, etc.

Overwriting
~~~~~~~~~~~

You might create a custom AprilTag with the **same ID code** as a tag
already in the Library. This is **overwriting**, which you can allow or
not allow.

If ``setAllowOverwrite()`` is set to ``false`` (the default) and
overwrite is attempted, the OpMode will crash with a suitable error
message.

If set to ``true``, the custom tag will replace the existing tag.

Why might you do this? Suppose a tag size is not quite correct. You
could enter a new tag with the same Metadata, but with a corrected tag
size.

Or you might prefer to use your own tag names, or distance units.

Advanced users might want to specify the **location** of a predefined
tag **on the game field**. This can be done with the optional Vector
and Quaternion fields.

====

*Questions, comments and corrections to westsiderobotics@verizon.net*

