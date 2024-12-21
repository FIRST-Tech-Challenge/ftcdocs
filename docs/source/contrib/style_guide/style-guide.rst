FTC Docs Style Guide
====================

.. attention:: The following is loosely modeled after the `FRC Docs Style Guide <https://docs.wpilib.org/en/stable/docs/contributing/frc-docs/style-guide.html>`_.
   It's formatted slightly differently, and has a section on accessibility.
   
   All the "Attention" notes will be removed when this is no longer a rough draft.

This guide contains the various reStructuredText (RST) and Sphinx specific guidelines for the FTC Docs project.
reStructuredText is the default plaintext markup language used by Sphinx.
Sphinx is a documentation generator.
Sphinx converts reStructuredText files into HTML web pages. 

In addition to the FTC Docs website, there is a 
PDF version of FTC Docs that can downloaded for viewing when one doesn't have access to the internet.

.. contents:: Contents
   :local:
   :depth: 1
   :backlinks: none

.. attention:: This will be a long page. I think we need in-page links. See guidance here: https://www.nngroup.com/articles/formatting-long-form-content/
   In-page links are also an accessibility improvement (imagine having to listen to this entire long page to find the one section near the end that you wanted).
   I'll probably add sub-pages for some things (like detailed image guidance).
   
   The goal being that most users should find the style guide sufficient.
   But the sub-pages will have more detail and guidance for complicated directives like image and figure.
   
   This note will be removed when this is no longer a rough draft.

Accessibility
-------------

A new emphasis in FTC Docs is to improve the accessibility of FTC Docs. 
The `Americans with Disabilities Act (ADA) <https://www.ada.gov/topics/intro-to-ada/>`_
is a federal civil rights law that prohibits discrimination against people with disabilities in everyday activities.

What is Web Accessibility
^^^^^^^^^^^^^^^^^^^^^^^^^

.. Note:: This section is copied from: https://www.w3.org/WAI/fundamentals/accessibility-intro/.

Web accessibility means that websites, tools, and technologies are designed and developed so that people with disabilities can use them. More specifically, people can:

- perceive, understand, navigate, and interact with the Web
- contribute to the Web

Web accessibility encompasses all disabilities that affect access to the Web, including:

- auditory
- cognitive
- neurological
- physical
- speech
- visual

Web accessibility also benefits people without disabilities, for example:

- people using mobile phones, smart watches, smart TVs, and other devices with small screens, different input modes, etc.
- older people with changing abilities due to aging
- people with “temporary disabilities” such as a broken arm or lost glasses
- people with “situational limitations” such as in bright sunlight or in an environment where they cannot listen to audio
- people using a slow Internet connection, or who have limited or expensive bandwidth

Web Content Accessibility Guidelines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Web Content Accessibility Guidelines (WCAG) are 
a set of recommendations for making Web content more accessible, primarily for people with disabilities.

FTC Docs is not completely compliant with WCAG. 
Our goal to address the Level A success criteria to remove accessibility barriers.
Then move to meet the level AA criteria to improve that accessibility.
See https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2

The `WCAG documents <https://www.w3.org/WAI/standards-guidelines/wcag/>`_
explain how to make web content more accessible to people with disabilities. 
Web 'content' generally refers to the information in a web page or web application,

Please refer to the :doc:`ftc-docs-accessibility-guidelines` section of FTC Docs for how to 
improve the accessibility of content created for FTC Docs.

The following section provide the WCAG principles that the accessibility guidelines are based on.
   
Principle 1 – Perceivable
"""""""""""""""""""""""""

Information and user interface components must be presentable to users in ways they can perceive.
For the vision impaired this includes providing text alternative for non-text content like images.
It could include Closed captioning which is a form of subtitling, a process of displaying text on a television, 
video screen, or other visual display to provide additional or interpretive information, where the viewer is given the choice of whether the text is displayed. 

Create content that can be presented in different ways (for example simpler layout) without losing information or structure.

Make it easier for users to see and hear content including separating foreground from background.

Principle 2 – Operable
""""""""""""""""""""""

User interface components and navigation must be operable.
Make all functionality available from a keyboard.
Provide users enough time to read and use content.
Do not design content in a way that is known to cause seizures or physical reactions. Example: flashing content.
Provide ways to help users navigate, find content, and determine where they are.

Make it easier for users to operate functionality through various inputs beyond keyboard.

Principle 3 – Understandable
""""""""""""""""""""""""""""

Information and the operation of the user interface must be understandable.
Make text content readable and understandable.
Make Web pages appear and operate in predictable ways.

Principle 4 – Robust
""""""""""""""""""""

Content must be robust enough that it can be interpreted by a wide variety of user agents, including assistive technologies.
Help users avoid and correct mistakes.

This success criterion is primarily for Web authors who develop or script their own user interface components. For example, standard HTML controls already meet this success criterion when used according to specification.

reStructuredText Documents
--------------------------

.. attention:: talk about RST documents, directives, and general structure issues.

Example Document
^^^^^^^^^^^^^^^^

.. code:: ReST

   Title
   =====

   This is an example article.
   This is a paragraph.

   Here is some code:

   .. code:: java

      System.out.println("Hello World");

   This is how to include an image:

   .. image:: images/BlocksPicture1.jpg
      :alt: Blocks Programming Tool showing a graphical Blocks program.
 
   This is how to include an image with caption:
   
   .. figure:: images/examplemulticolorplates.png  
      :alt: 6 multicolor square 3d printed logos. 

      This FTC Team printed their sponsors logos in multiple colors to represent them!  
   
   Section
   -------

   This is a section!
   
   Sub-section
   ^^^^^^^^^^^
   
   This is a sub-section!

.. note:: If you are having issues editing files with the ``.rst`` extension, the recommended text editor is VS Code with the [reStructuredText extension](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext).

Document Filenames
^^^^^^^^^^^^^^^^^^

This is for the files that make up the pages of FTC Docs. 
Use only lowercase alphanumeric characters and - (minus) symbol in the file name. Example: ``style-guide.rst``

For documents that will have an identical software/hardware name, append “-hardware” or “-software” to the end of the document name. example: ``ultrasonics-hardware.rst``

Suffix filenames with the ``.rst`` extension.


Titles and Headings
-------------------

.. attention:: talk about things related to document structure and how we want FTC Docs headings.

Text
----

.. attention:: talk about FTC Docs text, paragraphs, lists, tables, admonitions etc.

   This is where we just have guidelines and don't repeat info in the tutorials or reference guide.

   Example: we can encourage use of the list style of RST table and avoid the ascii box style of table.
   
   Also talk about plain language: https://evolvingweb.com/blog/plain-language-guide-how-write-inclusive-digital-content-2024

Links
-----

.. attention:: talk about links in FTC Docs. In page links, links between docs, links to sections, etc. Links to labels??

   Probably want to add how to improve the accessibility of links.
   Examples: warning if the link opens in a new tab, or will download a file, or goes to an external site.

Images
------

Images usually support the text on a page. They provide visual reinforcement.
Sometimes an image is the primary source of meaning for the content. 
It's hard to talk about AprilTags without images of what an AprilTag looks like.

For FTC Docs, please don't add :ref:`decorative-images-label` that are just for visual presentation.
Images should relate to the content of the page.

See `Image Files`_ for file formats, size, and where to place images the FTC Docs folders.

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
For assistance with alt text descriptions, see :ref:`alt-text-label`.

The description should be functional. Describe the image for someone who cannot see it.
If you need more than a sentence or two to describe the image, see `Complex Images`_.

Here's what the web page for an image looks like (but reduced in size for this example).
The image is a screen shot of the Blocks programming tool on a page that talks about the various programming tools available.

.. list-table:: 

   * - .. image:: ../../programming_resources/shared/choosing_program_lang/images/BlocksPicture1.jpg
          :alt: Blocks Programming Tool showing a graphical Blocks program.
          :width: 40%
          :class: no-scaled-link  

The alt text reads ``Blocks Programming Tool showing a graphical Blocks program.``

The alt text is not visible in HTML or PDF, but would be displayed in the browser if the image failed to load 
or the user had selected to not load images (perhaps they are on a low bandwidth internet connection).

FTC Docs has many diagrams. Some are simple like this one for a control system diagram on a page that introduces the control system. 

.. list-table::

   * - .. image:: ../../programming_resources/shared/control_system_intro/images/PointToPointControl.jpg
          :alt: Two gamepads are connected to a phone, the phone is connected by WiFi Direct to another phone on the robot.
          :width: 40%
          :class: no-scaled-link

The alt text reads ``Two gamepads are connected to a phone, the phone is connected by WiFi Direct to another phone on the robot.``

FTC Docs also has photographs. These also need alt text to describe the image.
This next example is on a page discussing hardware tradeoffs including stiff and flexible printer beds.

.. list-table::

   * - .. image:: ../../manufacturing/3d_printing/general_knowledge/hardware_tradeoffs/images/flexiblebeds.png
          :alt: An image showing how flexible beds peel off of the bed.
          :width: 40%
          :class: no-scaled-link

The alt text reads ``An image showing how flexible beds peel off of the bed.``

Alt Text Guidelines
"""""""""""""""""""

- Keep it short. Alt text shouldn’t be much longer than around 150 characters. 

- Do not include words like ‘image’ or ‘photo’ at the beginning. 

- End alt text with a period, even if it isn’t a full sentence. The period ensures that the screen reader pauses after reading the alt text.

- Front load alt text with the most important words, to help users make a quick and informed decision about whether it’s worth listening to the rest of the alt text before moving on.

- Always include an alt attribute. Otherwise, screen readers might announce the image file name.

- Avoid technical jargon and abbreviations unless users are certain to understand them.

.. tip:: For assistance with alt text descriptions, see :ref:`alt-text-label`.

.. important:: If you are editting an existing page that has an **image** or **figure** directive with no **:alt:** option,
   please take a moment to add the **:alt:** option with a functional description of the image.

Images With Captions
^^^^^^^^^^^^^^^^^^^^

Use the **figure** directive when the image requires a visible text caption. 
Sphinx place the caption text below the image. The caption text is in italic font.

Photo credits are an example of when you need a caption. 
You should also use a caption when you need editorial or illustrative text to highlight something 
about the image to the reader or to connect the image to the surrounding text content.
You might draw the readers attention to some detail of the image, or what is important in the image.
Captions can be longer than one line if needed, but like alt text probably should be no more than one sentence.

Please create alt text even though there is a caption. 
The alt text and caption should be different because a screen reader will read both.
One way to think about this is the alt text should be functional and the caption should editorial or illustrative.
If you need more than a sentence or two to describe the image, see `Complex Images`_.

Do not add the word "Figure" to the caption, or Figure 1, 2 etc. 
The PDF writer will automatically add "Fig." and a number to all captions.

If you need to reference the figure in the text of the page, use the leading text of the caption if possible, or
some unique short identifier or description of the image.
Try not to reference the figure by position (such as "see the image above") as visually impaired persons cannot see the position.
Also, the PDF writer might move the figure out of context with the surrounding text.

If the caption is just a functional description of the image, maybe you don't need a caption and can use the **image** directive instead.
The following example is on a page about 3D printed parts in a section about Robot Aesthetics.

.. code:: ReST

   .. figure:: images/examplemulticolorplates.png  
      :alt: 6 multicolor square 3d printed logos. 

      This FTC Team printed their sponsors logos in multiple colors to represent them!   

Note that **:alt:** and caption are both indented 3 spaces.
A blank line is required between **:alt:** and the caption.

Here's what this looks like (with image reduced in size for this example).

.. list-table:: 

   * - .. figure:: ../../manufacturing/3d_printing/3d_printed_parts/images/examplemulticolorplates.png
          :alt: 6 multicolor square 3d printed logos. 
          :width: 40%
          :class: no-scaled-link
          
          This FTC Team printed their sponsors logos in multiple colors to represent them!
          
The alt text for the image reads ``6 multicolor square 3d printed logos.``

This is a good example of a functional alt text description for a screen reader followed by
an editorial caption that is visible.

.. attention:: we need more examples of alt text with captions. I'm not sure this is trivial, so more examples would be nice.
   or maybe link to the detailed style-guide-images page with more examples there.
   This page has more info: https://thoughtbot.com/blog/alt-vs-figcaption

Complex Images
^^^^^^^^^^^^^^

To make images accessible for the visually impaired, we need to provide a text description of the image.
For complex images, you might need a whole paragraph to describe the image.
Alt text is not supposed to be more than a sentence or two, we need to provide something short in the alt text knowing that a long description follows.

To include a complex image use the **figure** directive.
Set the **alt** text to a short functional description, perhaps a summary of the long description.
Set the caption to be an editorial or illustrative comment on the image.
See the guidance about alt text and captions in the preceding section.
The long description is then added as a paragraph after the caption in the **figure** directive.

Try to adjust the alt text, caption, and long description so that the text flows such
that it would make sense if read aloud by a screen reader.

In the following reStructuredText source example the **figure** directive has alt text, followed by a one line caption.
A descriptive paragraph is added after the caption. It is indented the same as the caption.
There is a blank line before and after the caption.

.. code:: ReST

   .. figure:: images/image3.jpg
      :alt: A square field with X, Y and Z axes shown.
   
      The Cascade Effect game field
      
      In a square field configuration the two Alliances face each other across the field.
      The field is oriented such that the Red Wall is on the right as seen
      from the audience, and the blue wall will be on the left.
      The Y axis points across the field from the Red Wall to the blue wall.
      The X axis points away from the audience to the rear of the field.

Here's what a complex image looks like (with image reduced in size for this example).

.. list-table:: 

   * - .. figure:: ../../game_specific_resources/field_coordinate_system/images/image3.jpg
          :alt: A square field with X, Y and Z axes shown. 
          :width: 25%
          :class: no-scaled-link
          
          The Cascade Effect game field

          In a square field configuration the two Alliances face each other across the field.
          The field is oriented such that the Red Wall is on the right as seen
          from the audience, and the blue wall will be on the left.
          The Y axis points across the field from the Red Wall to the blue wall.
          The X axis points away from the audience to the rear of the field. 

The alt text for the example image reads ``A square field with X, Y and Z axes shown.``
This is a short functional description that a screen reader would say.

The caption is an editorial comment that this field is from the Cascade Effect game.
It is not the same as the alt text.

The paragraph after the caption completely describes the image for those who cannot see it.
A complete text description is also important for those persons who have trouble processing or understanding visual information.
It can help them understand the image they are seeing.

Image Files
^^^^^^^^^^^

Image files should be stored in an ``images`` sub directory in the folder of the current document. 
This allows the document to reference the image as follows: ``.. image:: images/my-image.png``.

Example: The document **field-coordinate-system.rst** is in the **game_specific_resources\\field_coordinate_system** folder.
The images for that page are stored in the folder **game_specific_resources\\field_coordinate_system\\images**.

Image file names should follow the naming scheme of **short-description.ext**, where the name of the image is a short description of what the image shows. 
This should be less than 24 characters. 
File name extensions should be **.png** or **.jpg**.

Image file formats should be Portable Network Graphics(PNG) or Joint Photographic Experts Group(JPEG).

.. warning:: Images with the extension .gif and .svg are not supported in PDF format. 

Images (including vector graphics) should be less than 500 kilobytes in size and no more than 1000 pixels in width. 
Please make use of a smaller resolution and more efficient compression algorithms.
This facilitates reasonable web page loading for those with slow internet connections.
Our HTML documents have a maximum width of 1000 pixels for desktop browsing so image width should be 1000 pixels or less.

An exception to image size is images like the control system diagrams in the 
:ref:`Robot Controller Overview <control_hard_compon/rc_components/index:Robot Controller Overview>`. 
Those diagrams are over 2500 pixels wide and greater than 500kb in size.
However, that extra resolution is required to properly view the details of all the components and the connections.
If those were reduced in resolution, or too heavily compressed as a jpg, relevant details might be lost or hard to see.

More Information
----------------

- :doc:`ftc-docs-accessibility-guidelines`
- :doc:`image-and-figure-details`

.. toctree::
   :hidden:
   :maxdepth: 1
   
   ftc-docs-accessibility-guidelines
   image-and-figure-details

