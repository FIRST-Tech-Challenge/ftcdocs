AprilTag Metadata
=================

Introduction
------------

A Library tag stores **Metadata**, a collection of at least 4 fields (of these
:term:`Blocks`/Java types):

- ID code (number/``int``)
- tag name (text/``String``)
- tag size (number/``double``)
- unit for tag size and estimated position (``DistanceUnit INCH, MM, CM, METER``)

Two optional Metadata fields are described at the **Advanced Use** page.

Cluster Metadata
^^^^^^^^^^^^^^^^

Starting with SDK 12.0, an AprilTag Cluster has its own Metadata, of Java type
``AprilTagClusterMetadata``. This is a different type from the single-tag
``AprilTagMetadata`` above, and it holds different fields:

- cluster name (text/``String``)
- short name (text/``String``)
- unit for estimated position (``DistanceUnit``)
- field position (``VectorF``, optional)
- field orientation (``Quaternion``, optional)

A Cluster has no ID code and no tag size of its own, because it is made up of
several member tags. Each member has its own
``AprilTagClusterMemberMetadata``, holding that member's ``id``, ``tagsize``,
and position within the cluster. A Cluster is identified by name, not by ID
code.

See :ref:`AprilTag Clusters <apriltagclusters>` for how Clusters are detected
and targeted.

The full use of Metadata Blocks and Java methods is covered at the **Library**
page.  For now it's enough to know the 4 basic elements of Metadata.

Tag Contents
------------

The SDK 8.2 :term:`Sample OpModes <Sample OpMode>` use :term:`AprilTags <AprilTag>` with these Metadata values:

- ``583, Nemo, 4, DistanceUnit.INCH``
- ``584, Jonah, 4, DistanceUnit.INCH``
- ``585, Cousteau, 6, DistanceUnit.INCH``
- ``586, Ariel, 6, DistanceUnit.INCH``

These four are available with the ``getSampleTagLibrary()`` Block or Java
method.

Past and present game Libraries are available from ``AprilTagGameDatabase``:

- ``getCenterStageTagLibrary()``
- ``getIntoTheDeepTagLibrary()``
- ``getDecodeTagLibrary()``
- ``getBioBuzzTagLibrary()``

A call to ``getCurrentGameTagLibrary()`` provides the current season's game
tags and the Sample OpMode tags.

From SDK 12.0 onward, a game Library may contain AprilTag Clusters as well as
single tags. These Libraries are discussed further at the **Library** page.

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

         AprilTagSingleDetection myAprilTagDetection;
         String myAprilTagName;
         myAprilTagName = myAprilTagDetection.metadata.name;

      A Cluster detection also has a ``.metadata.name``, reached through the
      other subclass:

      .. code-block:: java

         AprilTagClusterDetection myAprilTagClusterDetection;
         String myClusterName;
         myClusterName = myAprilTagClusterDetection.metadata.name;

      In both cases the declared type must be the subclass. The abstract parent
      ``AprilTagDetection`` does not declare ``.metadata``, because the two
      subclasses hold different Metadata types.

As with tag ID code, the tag name is usually retrieved inside a ``for()`` loop,
for immediate processing or stored for later use.  See the **Initialization**
page for sample ``for()`` loop code.

Unlike tag ID code, a detected single AprilTag might have **no tag name** -- if
it was not placed into the Library by default or with the custom Builder
pattern.

To avoid logic errors, an :term:`OpMode` can check the Metadata for a **null**
condition before attempting to process a tag name.  This is illustrated in
these Sample OpModes:

- Blocks: ``ConceptAprilTag``
- Java: ``ConceptAprilTag.java``

A Cluster detection needs no such check. The SDK produces one only for a
Cluster it already knows about, so the Metadata is always present.

====

*Questions, comments and corrections to westsiderobotics@verizon.net*

