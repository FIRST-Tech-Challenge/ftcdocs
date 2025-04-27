FTC Docs Style Guide
====================

This guide contains the various reStructuredText (RST) and Sphinx specific guidelines for the FTC Docs project.
reStructuredText is the default plain text markup language used by Sphinx.

.. contents:: Contents
   :local:
   :depth: 1
   :backlinks: none

..  This will be a long page. I think we need in page links. See guidance here: https://www.nngroup.com/articles/formatting-long-form-content/
   In page links are also an accessibility improvement (imagine having to listen to this entire long page to find the one section near the end that you wanted).
   I'll probably add sub-pages for some things (like detailed image guidance).
   
   The goal being that most users should find the style guide sufficient.
   But the sub-pages will have more detail and guidance for complicated directives like image and figure.

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

Please refer to the :doc:`ftc-docs-accessibility-guidelines` section of FTC Docs for how to 
improve the accessibility of content created for FTC Docs.

Plain Language
--------------

Plain language means communicating in a way that’s clear, straightforward, and easy to understand. It helps audiences “get” what you’re saying immediately. 

Writing in plain language ensures that users can:

- Find the information they need
- Understand what they find
- Use the information to fulfill their needs


This article talks about plain language and contains `tips with examples <https://evolvingweb.com/blog/plain-language-guide-how-write-inclusive-digital-content-2024#how>`_.
These are similar to the tips on `Writing for Web Accessibility <https://www.w3.org/WAI/tips/writing/#keep-content-clear-and-concise>`_.
Finally, you can explore the `Federal plain language guidelines <https://www.plainlanguage.gov/guidelines/>`_.

reStructuredText Documents
--------------------------

reStructuredText (RST) is the default plaintext `markup language <https://en.wikipedia.org/wiki/Markup_language>`_ used by Sphinx. 
See the `reStructuredText primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ for a short introduction.
There is also a `RST cheatsheet <https://sphinx-tutorial.readthedocs.io/cheatsheet/>`_ that can be helpful to remind you of the basics.

The following sections illustrate how to write RST for FTC Docs. They are not a tutorial or reference guide for RST. 

Example Document
^^^^^^^^^^^^^^^^

The following example shows how content is mixed with RST markup.
The RST markup indicates titles, paragraphs, code samples, images and document sections.

.. code:: ReST

   Article Title
   =============

   This is an example article.
   A paragraph is a collection of lines. You can have multiple sentances per line.
   
   Leave a blank line to start a new paragraph.
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

.. note:: If you are having issues editing files with the ``.rst`` extension, the recommended text editor is VS Code with the
    `reStructuredText <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_ extension.
    
    However, a plain text editor works just fine. Though you would need to generate the HTML to see what the document will look like.

Document Filenames
^^^^^^^^^^^^^^^^^^

This is for the files that make up the pages of FTC Docs. 
Use only lowercase alphanumeric characters and - (minus) symbol in the file name. Example: ``style-guide.rst``

For documents that will have an identical software/hardware name, append “-hardware” or “-software” to the end of the document name. example: ``ultrasonics-hardware.rst``

Suffix filenames with the ``.rst`` extension.

Titles and Headings
-------------------

Titles and Section Headers are both related, and are treated the exact same way. 

In order to create a new Section, SubSection, SubSubSection, and so on, we just
use a special character that we will define for each level. FTC Docs uses the following:

.. code:: ReST

   Titles
   ====== (Equals)

   Sections
   -------- (Dash)

   SubSection
   ^^^^^^^^^^ (Carrot)

   SubSubSection
   """"""""""""" (Double Quotes)

   SubSubSubSection
   ++++++++++++++++ (Plus Sign)

This is what should be used for different levels of sections.
Please nest the sections in order. For example, use SubSection to add something to a Section (not a SubSubSection).

.. warning:: Titles, Sections, SubSections, etc. must all be uniquely named within the same document.

Text
----

Use the ASCII character set for English text. For special characters (e.g. Greek symbols) use the `standard character entity sets <https://docutils.sourceforge.io/docs/ref/rst/definitions.html#character-entity-sets>`_.

Use ``.. math::`` for standalone equations and ``:math:`` for inline equations. 
The ``.. math::`` directive uses Latex markup, see this `LaTeX equation cheat sheet (PDF) <https://www.reed.edu/academic_support/pdfs/qskills/latexcheatsheet.pdf>`_ for more information.

The standard text formatting markup is quite simple - use:

* One Asterisk: \*text\* for emphasis (italics) - like *text*
* Two Asterisks: \*\*text\*\* for strong emphasis (boldface) - like **text**
* Two Backticks: \`\`text\`\` for literals - like ``text``

Use literals for filenames, function, and variable names.

Whitespace
----------

Indentation
^^^^^^^^^^^

Indentation should *always* match the previous level of indentation *unless* you are creating a new content block.

Indentation of content directives as new line ``.. toctree::``  should be `3` spaces.

Blank Lines
^^^^^^^^^^^

There should be one blank line separating basic text blocks and section titles. There should be one blank line separating text blocks and content directives.

Interior Whitespace
^^^^^^^^^^^^^^^^^^^

Use one space between sentences.

Tables
------

There are many ways to create tables, FTC Docs prefers the `list <https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table>`_ 
or `CSV <https://docutils.sourceforge.io/docs/ref/rst/directives.html#csv-table-1>`_ style of RST table. 
Please avoid the ASCII art form of table.

.. code:: ReST

   .. csv-table:: Frozen Delights!
      :header: "Treat", "Quantity", "Description"
      :widths: 15, 10, 30

      "Albatross", 2.99, "On a stick!"
      "Crunchy Frog", 1.49, "If we took the bones out,
      it wouldn't be crunchy, now would it?"
      "Gannet Ripple", 1.99, "On a stick!"
      
Which creates the following:

.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out,
   it wouldn't be crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"

Admonitions
-----------

Admonitions are RST directives that provide special formatting to the admonition text.
In FTC docs admonitions have a color heading, followed by a color shaded block with the admonition text.
The list of admonitions is: "attention", "caution", "danger", "error", "hint", "important", "note", "tip", "warning".
FTC Docs has lots of "note" and "warning" admonitions.

In RST an admonition looks like:

.. code:: ReST

   .. note:: This is a note admonition.
      This is the second line of the first paragraph.

      - The note contains all indented body elements
        following.
      - It includes this bullet list.
   
Which results in the following:

.. note:: This is a note admonition.
   This is the second line of the first paragraph.

   - The note contains all indented body elements
     following.
   - It includes this bullet list.
   
Please use admonitions to highlight important information. 

.. tip:: Admonitions should usually should be short.

Links
-----

Effective link text:

- Avoid link text such as “click here” or "learn more." These call to actions do not provide any relevant information.
- Links should be unique and describe where it takes you. If you have multiple links that look or sound similar (but point to different sections), use different words for each link.
- Links to files (e.g. Microsoft Word, PDF, etc.) should also indicate the file type or destination within the link text.
- Avoid using long URLs as link text. Longer, less intelligible URLs used as link text might be difficult to comprehend with assistive technology.
- Link text should be clear and concise. Avoid linking entire sentences or paragraphs.

.. tip:: See this guide on `writing hyperlinks <https://www.nngroup.com/articles/writing-links/>`_ for more information.
   
Internal Links
^^^^^^^^^^^^^^

Internal Links will be automatically generated based on the ReStructuredText filename and section title.
For example, here are several ways to link to sections and documents.

- Use this format to reference a section of the same document: ```Images`_`` Note the single underscore. This renders to the link `Images`_ which is a section further down in this document.

- Use this format to reference the top level of a document. You can use relative paths ``:doc:`image-and-figure-details``` renders to :doc:`image-and-figure-details`. Or to use absolute paths, put a forward slash at the beginning of the path ``:doc:`/apriltag/vision_portal/visionportal_webcams/visionportal-webcams``` renders to :doc:`/apriltag/vision_portal/visionportal_webcams/visionportal-webcams`. Note that the link text rendered is the main section title of the target page regardless of the target filename.

The general way to reference a section in another document is to add a label in front of the section in that other document.
Note the leading underscore and trailing colon that surround the label. The label must be unique across all of FTC Docs. You can also reference a Figure with the label method.

.. code:: rest

   .. _imu axes def:
   
   Axes Definition
   ---------------

Then you reference the label by using ``:ref:`` and surrounding the label with back ticks as follows:

.. code:: rest

   partial sentence including :ref:`imu axes def`
   
   another reference to :ref:`IMU or robot axes <imu axes def>`

The second ``:ref:`` shows a format that lets you specify the link text, otherwise the section heading is used for the link text. This looks like the following:

.. list-table:: 

   * - partial sentence including :ref:`imu axes def`
     - This shows the section heading.
   * - another reference to :ref:`IMU or robot axes <imu axes def>`
     - This shows custom link text.

When using ``:ref:`` or ``:doc:`` you may customize the displayed text by surrounding the actual link with angle brackets ``<>`` and adding the custom text between the first back tick ````` and the first angle bracket ``<``, leaving a space between the text and bracket. 
For example ``:ref:`RC Overview <control_hard_compon/rc_components/index:Robot Controller Overview>``` renders to :ref:`RC Overview <control_hard_compon/rc_components/index:Robot Controller Overview>`.
This is a link to the Robot Controller Overview section of the index in the rc_components folder.

External Links
^^^^^^^^^^^^^^

Links to other websites and even to the main *FIRST* Inspires site are call *external links*.
It's possible to create a link by entering the URL in the text https://www.firstinspires.org/resource-library/ftc/game-and-season-info.
Sphinx will build a link when it encounters a URL. But that is not the preferred approach.

Use descriptive link text rather than just embedding a URL.
Use the following RST syntax:

.. code:: rest

   `Game and Season Materials <https://www.firstinspires.org/resource-library/ftc/game-and-season-info>`_

Which looks like: `Game and Season Materials <https://www.firstinspires.org/resource-library/ftc/game-and-season-info>`_

FTC Docs has chosen to open links to external sites in new tabs. This is done with JavaScript.
We mitigate this somewhat by adding an icon that indicates the link is to an external site and add screen reader only text.

Links to Files
^^^^^^^^^^^^^^
   
You can directly link to files such as a PDF, but that is an accessibility problem. 
The issue is the context switch from web browsing to suddenly having to deal with a PDF that has probably opened in a new tab/window without any warning.
FTC Docs contains quite a few links to PDFs that should be make more accessible.

The recommended approach to linking to files is to include in the link a warning that the link is actually a file, the file type, and if possible the file size.
Ideally that information is in text and included in the link text portion of the link so that a screen reader would read that information and let the user decide if they want to follow the link.

Simple example of a link to a PDF. 

RST Code:

.. code:: rest
   
   `Field Setup Guide (PDF, 4.5 MB) <https://ftc-resources.firstinspires.org/file/ftc/game/fieldguide>`__

Which looks like:

.. list-table:: 

   * - `Field Setup Guide (PDF, 4.5 MB) <https://ftc-resources.firstinspires.org/file/ftc/game/fieldguide>`__

Generally in FTC Docs we link to file to enable them to be downloaded for printing or offline viewing. 
In that case, the user is downloading the file, which is an action, so a button is appropriate.
Buttons are appropriate user interface components for user actions.
Using a button as a link will visually distinguish a file link from a regular link.

The following RST example show a sentence that precedes the button to give context.
We include the document name as screen readers and keyboard only users might tab to the link
so we need to indicate in the link what file will be downloadable.

.. code:: rest

   Use the following button link to download a PDF of the Field Setup Guide from the *FIRST* Website:
   
   .. button-link:: https://ftc-resources.firstinspires.org/file/ftc/game/fieldguide
      :color: primary

      Download Field Setup Guide PDF, 4.5 MB

This looks like:

.. list-table:: 

   * - Use the following button link to download a PDF of the Field Setup Guide from the *FIRST* Website:
   
       .. button-link:: https://ftc-resources.firstinspires.org/file/ftc/game/fieldguide
          :color: primary

          Download Field Setup Guide PDF, 4.5 MB

The preferred approach when linking to files is to create what is called a gateway page.
The gateway page would describes the file, perhaps giving a summary of the content. 
This lets the reader decide if it's worth taking the trouble to view or download the file.
Ideally, all references to the file elsewhere on the website link to the gateway page which then links to the file. 

External reference: https://www.nngroup.com/articles/gateway-pages-prevent-pdf-shock/

Here's a gateway page example for the Field Setup Guide PDF.

.. list-table:: 

   * - The Field Setup Guide has the official instructions for assembling and setting up a *FIRST* Tech Challenge field.
       Typically there are assembly instructions that build structures that then have setup instructions for placing on the field.
       There are also tear down instructions that indicate how to take apart the field for storage or transport.

       The guide typically has the following sections:

       - A list of all tools required for assembly and setup, some tools are only for assembly or for setup.
       - A list all the game elements and scoring elements with the quantity of each.
       - Instructions for setup of the field perimeter and field tiles.
       - Step by step instructions for assembling parts and setting them on the field.
       - Most games have tape lines on the field to mark locations or areas of the game. There are also taped areas outside the field for the Alliances, and sometimes for game areas.
       - Most games have AprilTags placed around the field that can be used for robot navigation.
       - Finally, there are tear down instructions that indicate how to take the field down for storage or transport.

       Use the following button link to download a PDF of the Field Setup Guide from the *FIRST* Website:

       .. button-link:: https://ftc-resources.firstinspires.org/file/ftc/game/fieldguide
          :color: primary

          Download Field Setup Guide PDF, 4.5 MB

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

Use the following ``.. image`` directive when the image does not require a visible text caption.
For accessibility, please add an ``:alt:`` option to the image directive with a functional description of the image.
This description will not be visible on a web page or PDF, but will be spoken out loud by 
screen reader software. 

.. code:: ReST

   .. image:: images/BlocksPicture1.jpg
      :alt: Blocks Programming Tool showing a graphical Blocks program.
      
The ``:alt:`` line is indented three spaces. 

The description should be functional. Describe the image for someone who cannot see it.

Here's what the web page for an image looks like (but reduced in size for this example).
The image is a screen shot of the Blocks programming tool on a page that talks about the various programming tools available.

.. list-table:: 

   * - .. image:: ../../programming_resources/shared/choosing_program_lang/images/BlocksPicture1.jpg
          :alt: Blocks Programming Tool showing a graphical Blocks program.
          :width: 40%
          :class: no-scaled-link  

The alt text reads *Blocks Programming Tool showing a graphical Blocks program.*
The alt text is not visible in HTML or PDF, but would be spoken aloud by screen reading software.
Alt text is displayed in the browser if the image failed to load or the user had selected to not load images
because they are on a low bandwidth internet connection.

FTC Docs has many diagrams. Some are simple like this one for a control system diagram on a page that introduces the control system. 

.. list-table::

   * - .. image:: ../../programming_resources/shared/control_system_intro/images/PointToPointControl.jpg
          :alt: Two gamepads are connected to a Rev Driver Hub, which is connected by WiFi to a Rev Control Hub on the robot.
          :width: 40%
          :class: no-scaled-link

The alt text reads *Two gamepads are connected to a Rev Driver Hub, which is connected by WiFi to a Rev Control Hub on the robot.*

FTC Docs also has photographs. These also need alt text to describe the image.

Alt Text Guidelines
"""""""""""""""""""

- Keep it short. Alt text shouldn’t be much longer than around 150 characters. 

- Do not include words like ‘image’ or ‘photo’ at the beginning. 

- End alt text with a period, even if it isn’t a full sentence. The period ensures that the screen reader pauses after reading the alt text.

- Front load alt text with the most important words, to help users make a quick and informed decision about whether it’s worth listening to the rest of the alt text before moving on.

- Always include an alt attribute. Otherwise, screen readers might announce the image file name.

- Avoid technical jargon and abbreviations unless users are certain to understand them.

If you need more than a sentence or two to describe the image, see `Complex Images`_.

.. tip:: For assistance with alt text descriptions, see :ref:`alt-text-label`.

.. important:: If you are editting an existing page that has an ``.. image`` or ``.. figure`` directive with no ``:alt:`` option,
   please take a moment to add the ``:alt:`` option with a functional description of the image.

Images With Captions
^^^^^^^^^^^^^^^^^^^^

Use the ``..figure`` directive when the image requires a visible text caption. 
Sphinx place the caption text below the image. The caption text is in italic font.

Photo credits are an example of when you need a caption. 
You should also use a caption when you need editorial or illustrative text to highlight something 
about the image to the reader or to connect the image to the surrounding text content.
This could include the who, what, when, where, and/or why of an image.
You might draw the readers attention to some detail of the image, or what is important in the image.
Captions can be longer than one line if needed, but should generally be kept short.

Please create alt text even though there is a caption. 
The alt text and caption should be different because a screen reader will read both.
One way to think about this is the alt text should be functional and the caption should editorial or illustrative.

Do not add the word "Figure" to the caption, or "Figure 1", etc. 
The PDF writer will automatically add "Fig." and a number to all captions.

If you need to reference the figure in the text of the page, use the leading text of the caption if possible, or
some unique short identifier or description of the image.
Try not to reference the figure by position (such as "see the image above") as visually impaired persons cannot see the position.
Also, the PDF writer might move the figure out of context with the surrounding text.

The following example is on a page about 3D printed parts in a section about Robot Aesthetics.

.. code:: ReST

   .. figure:: images/examplemulticolorplates.png  
      :alt: 6 multicolor square 3d printed logos. 

      This FTC Team printed their sponsors logos in multiple colors to represent them!   

Note that ``:alt:`` and caption are both indented 3 spaces.
A blank line is required between ``:alt:`` and the caption.

Here's what this looks like (with image reduced in size for this example).

.. list-table:: 

   * - .. figure:: ../../manufacturing/3d_printing/3d_printed_parts/images/examplemulticolorplates.png
          :alt: 6 multicolor square 3d printed logos. 
          :width: 40%
          :class: no-scaled-link
          
          This FTC Team printed their sponsors logos in multiple colors to represent them!
          
The alt text for the image reads *6 multicolor square 3d printed logos.*

This is a good example of a functional alt text description for a screen reader followed by
an editorial caption that is visible.

Complex Images
^^^^^^^^^^^^^^

To make images accessible for the visually impaired, we need to provide a text description of the image.
For complex images, you might need a whole paragraph to describe the image.
Alt text is not supposed to be more than a sentence or two, we need to provide something short in the alt text knowing that a long description follows.

To include a complex image use the figure directive.
Set the ``:alt:`` text to a short functional description, perhaps a summary of the long description.
Set the caption to be an editorial or illustrative comment on the image.
See the guidance about alt text and captions in the preceding section.
The long description is then added as a paragraph after the caption in the figure directive.

Try to adjust the alt text, caption, and long description so that the text flows such
that it would make sense if read aloud by a screen reader.

In the following reStructuredText source example the figure directive has alt text, followed by a one line caption.
A descriptive paragraph is added after the caption. It is indented the same as the caption.
There is a blank line before and after the caption.

.. code:: ReST

   .. figure:: images/into-the-deep-field.png
      :alt: A square field with X, Y and Z axes shown.
   
      The Into The Deep game field
      
      In a square field configuration the two Alliances face each other across the field.
      The field is oriented such that the Red Wall is on the right as seen
      from the audience, and the blue wall will be on the left.
      The Y axis points across the field from the Red Wall to the blue wall.
      The X axis points away from the audience to the rear of the field.

Here's what a complex image looks like (with image reduced in size for this example).

.. list-table:: 

   * - .. figure:: /game_specific_resources/field_coordinate_system/images/into-the-deep-field.png
          :alt: A square field with X, Y and Z axes shown. 
          :width: 25%
          :class: no-scaled-link
          
          The Into The Deep game field

          In a square field configuration the two Alliances face each other across the field.
          The field is oriented such that the Red Wall is on the right as seen
          from the audience, and the blue wall will be on the left.
          The Y axis points across the field from the Red Wall to the blue wall.
          The X axis points away from the audience to the rear of the field. 

The alt text for the example image reads *A square field with X, Y and Z axes shown.*
This is a short functional description that a screen reader would say.

The caption is an editorial comment that this field is from the Cascade Effect game.
It is not the same as the alt text.

The paragraph after the caption completely describes the image for those who cannot see it.
A complete text description is also important for those persons who have trouble processing or understanding visual information.
It can help them understand the image they are seeing.

For another example of a complex image see :ref:`complex-image-label`.

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
Those diagrams are over 2500 pixels wide and greater than 500 KB in size.
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

