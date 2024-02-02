AprilTag Metadata
=================

Introduction
------------

A Library tag stores **Metadata**, a collection of at least 4 fields (of these
Blocks/Java types):

- ID code (number/``int``)
- tag name (text/``String``)
- tag size (number/``double``)
- unit for tag size and estimated position (``DistanceUnit INCH, MM, CM, METER``)

Two optional Metadata fields are described at the **Advanced Use** page.

The full use of Metadata Blocks and Java methods is covered at the **Library**
page.  For now it's enough to know the 4 basic elements of Metadata.

Tag Contents
------------

The SDK 8.2 Sample OpModes use AprilTags with these Metadata values:

- ``583, Nemo, 4, DistanceUnit.INCH``
- ``584, Jonah, 4, DistanceUnit.INCH``
- ``585, Cousteau, 6, DistanceUnit.INCH``
- ``586, Ariel, 6, DistanceUnit.INCH``

These four are available with the ``getSampleTagLibrary()`` Block or Java
method.

After Kickoff in September 2023, the CENTERSTAGE game tags will be available
with ``getCenterStageTagLibrary()``.  That Library currently contains 3
placeholder tags: MEOW (ID 0), WOOF (ID 1) and OINK (ID 2).

Before and after Kickoff, a call to ``getCurrentGameTagLibrary()`` will provide
**both sets** of tags.

These three Libraries are discussed further at the **Library** page.

Tag Names
---------

A tag name, whether default or custom, can be retrieved as follows:

.. tab-set::
   .. tab-item:: Blocks
      :sync: blocks

      .. figure:: images/100-tag-name-Blocks.png
         :width: 75%
         :align: center
         :alt: Tag Names

         Example of Reading AprilTag Names

   .. tab-item:: Java
      :sync: java

      Example of retrieving AprilTag Name

      .. code-block:: java
 
         AprilTagDetection myAprilTagDetection;
         String myAprilTagName;
         myAprilTagName = myAprilTagDetection.metadata.name;

As with tag ID code, the tag name is usually retrieved inside a ``for()`` loop,
for immediate processing or stored for later use.  See the **Initialization**
page for sample ``for()`` loop code.

Unlike tag ID code, a detected AprilTag might have **no tag name** -- if it was
not placed into the Library by default or with the custom Builder pattern.

To avoid logic errors, an OpMode can check the Metadata for a **null**
condition before attempting to process a tag name.  This is illustrated in
these Sample OpModes: 

- Blocks: ``ConceptAprilTag``
- Java: ``ConceptAprilTag.java``

====

*Questions, comments and corrections to westsiderobotics@verizon.net*

