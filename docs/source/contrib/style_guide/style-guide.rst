FTC Docs Style Guide
====================

.. note:: The following is modeled after the `FRC Docs Style Guide <https://docs.wpilib.org/en/stable/docs/contributing/frc-docs/style-guide.html>`_.

Document Filenames
------------------

This is for the files that make up the pages of FTC Docs. 

Use only lowercase alphanumeric characters and - (minus) symbol.

For documents that will have an identical software/hardware name, append “-hardware” or “-software” to the end of the document name. IE, ultrasonics-hardware.rst

Suffix filenames with the ``.rst`` extension.

Images
------

Images usually support the text on a page. They provide visual reinforcement and can break up
large blocks of text. Sometimes an image is the primary source of meaning for the content. 
It's hard to talk about AprilTags without images of what AprilTags look like.
Don't add decorative images.

See Image Files **[to do: add link to ref doc section]** for file formats, size, and where to place images the FTC Docs folders.

Simple Images
^^^^^^^^^^^^^

Use the following **image** directive when the image does not require a visible text caption. 
For accessibility, please add an **:alt:** option to the **image** directive with a description of the image.
This description will not be visible on a web page or PDF, but will be spoken out loud by 
screen reader software.

.. code:: ReST

   .. image:: images/BlocksPicture1.jpg
      :alt: Blocks Programming Tool showing a graphical Blocks program.
      
The **:alt:** line is indented three spaces. 

The description should be functional. Describe the image for someone who cannot see it.
If you need more than a sentance or two to describe the image, see `Complex Images`_.
For assistance in alt text descriptions, see **[insert link to that section of ref guide]**.

Here's what that looks like (but reduced in size for this example).
The alt text is not visible in HTML or PDF.

+----------------------------------------------------------------------------------------------+
|.. image:: ../../programming_resources/shared/choosing_program_lang/images/BlocksPicture1.jpg |
|   :alt: Blocks Programming Tool showing a graphical Blocks program.                          |
|   :width: 40%                                                                                |
|   :class: no-scaled-link                                                                     |
+----------------------------------------------------------------------------------------------+

The alt text is normally for screen readers only, but it will displayed if the image fails to load in a browser.

.. warning:: Sphinx will set alt text set to the path and file name of the image if you don't specify the **:alt:** option.
   
   This is not good accessibility. If you are editting an existing page that has an **image** or **figure** directive with no **:alt:** option,
   please take a moment to add the **:alt:** option with a functional description of the image.

Images With Captions
^^^^^^^^^^^^^^^^^^^^

Use the **figure** directive when the image requires a visible text caption. 
Photo credits are an example of when you need a caption. 
You should use a caption when you need editorial or illustrative text to highlight something 
about the image to the reader or to connect the image to the surrounding text content. 

Please create alt text even though there is a caption. 
The alt text and caption should be different because a screen reader will read both.
One way to think about this is the alt text should be functional and the caption should editorial or illustrative.
If you need more than a sentence or two to describe the image, see `Complex Images`_.

If the caption is just a functional description of the image, maybe you don't need a caption and can use the **image** directive instead.

.. code:: ReST

   .. figure:: images/examplemulticolorplates.png  
      :alt: 6 multicolor square 3d printed logos. 

      This FTC Team printed their sponsors logos in multiple colors to represent them!   

Note that **:alt:** and caption are both indented 3 spaces.
A blank line is required between **:alt:** and the caption.

Here's what this looks like (with image reduced in size for this example).

+-------------------------------------------------------------------------------------------------+
|.. figure:: ../../manufacturing/3d_printing/3d_printed_parts/images/examplemulticolorplates.png  |
|   :alt: 6 multicolor square 3d printed logos.                                                   |
|   :width: 40%                                                                                   |
|   :class: no-scaled-link                                                                        |
|                                                                                                 |
|   This FTC Team printed their sponsors logos in multiple colors to represent them!              |
+-------------------------------------------------------------------------------------------------+
   
The alt text for the image reads **6 multicolor square 3d printed logos.**
This is a good example of a functional alt text description for a screen reader followed by
an editorial caption that is visible.

.. tip:: we need more examples of alt text with captions

Complex Images
^^^^^^^^^^^^^^

To make images accessible for the visually impaired, we need to provide a text description of the image.
For complex images, you might need a whole paragraph to describe the image.
Add that paragraph after the caption in the **figure** directive.
You will also need alt text and a caption.

A complete text description is also important for those persons who have trouble processing or understanding visual information.

In the following reStructuredText source example the **figure** directive has alt text, followed by a one line caption.
A descriptive paragraph is added after the caption. It is indented the same as the caption.
There is a blank line before and after the caption.

.. code:: ReST

   .. figure:: images/image3.jpg
      :alt: A square field with X, Y and Z axes shown
   
      The Cascade Effect game field
      
      In a square field configuration the two Alliances face each other across the field.
      The field is oriented such that the Red Wall is on the right as seen
      from the audience, and the blue wall will be on the left.
      The Y axis points across the field from the Red Wall to the blue wall.
      The X axis points away from the audience to the rear of the field.

Here's what a complex image looks like (with image reduced in size for this example).

+--------------------------------------------------------------------------------------+
|.. figure:: ../../game_specific_resources/field_coordinate_system/images/image3.jpg   |
|   :alt: A square field with X, Y and Z axes shown                                    |
|   :width: 25%                                                                        |
|   :class: no-scaled-link                                                             |
|                                                                                      |
|   The Cascade Effect game field                                                      |
|                                                                                      |
|   In a square field configuration the two Alliances face each other across the field.|
|   The field is oriented such that the Red Wall is on the right as seen               |
|   from the audience, and the blue wall will be on the left.                          |
|   The Y axis points across the field from the Red Wall to the blue wall.             |
|   The X axis points away from the audience to the rear of the field.                 |
+--------------------------------------------------------------------------------------+

The alt text for the example image reads **A square field with X, Y and Z axes shown**.

