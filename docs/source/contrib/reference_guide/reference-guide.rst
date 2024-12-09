FTC Docs Reference Guide
========================

.. note:: The following is a rough draft, and is not complete.

   The intent of the Reference Guide is to provide detailed information that should not be in a tutorial or a style guide.
   It is also where we might link to external info like the docutils reStructuredText site.
   It may repeat or reinforce information already mentioned in the tutorial or style guide.
   It should explain why the style guide says we should do something a certain way.
   Probably will add an accessibility section.
   
   The intent of all this is that the tutorial should be for new users and gives step by step instructions
   and basic information. It should probably link to the style guide and/or ref guide as needed.
   
   The style guide is where we describe how we do things in FTC Docs,
   like what rst directive to use to include an image and what options to use.
   The style guide is being re-written, but could be loosely based on the FRC Doc style guide.
   It should link to the ref guide.

Images
------

Images usually support the text on a page. They provide visual reinforcement and can break up
large blocks of text. Sometimes an image is the primary source of meaning for the content. 
It's hard to talk about AprilTags without images of what AprilTags look like.

FTC Doc doesn't use decorative images. See `Decorative Images`_ if needed.

Images can be included by the Image Directive if no caption is required,
or using the `Figure Directive`_ if a caption is required or a long description of the image is required.

See `Image Files`_ for file formats, size, and where to place images the FTC Docs folders.

Image Directive
^^^^^^^^^^^^^^^

Use the ``.. image`` directive to include an image that does **not** need a caption.
Determine if the image needs a caption. Photo credits need a caption. Complex images probably need a caption. 
Anything that requires an editorial or illustrative description to tie the image to the content of the page requires a caption. 

If no caption is required then the image directive can be used. 
Add the **alt** option and provide text that describes the image. 
This is all you need for basic images.

.. code:: ReST

   .. image:: images/butterfly.jpg
      :alt: A blue butterfly sitting on an orange flower.

The alt text should have a functional description. A functional description explains exactly what is in an image. 
These descriptions should be thorough but brief, one or two sentences.
If a long description is required, use the ``figure`` directive, see `Complex Images`_.

.. tip:: insert reference to further guidance on alt text writing - or better yet more examples

.. warning:: Sphinx will set alt text set to the path and file name of the image if you don't specify the **:alt:** option.
   The HTML looks like `<img alt="../_images/GoodStuff.png" src="../_images/GoodStuff.png">`.
   A screen reader will read out loud the alt text `../_images/GoodStuff.png`.
   
   This is not good accessibility. If you are editting an existing page that has an **image** or **figure** directive with no **:alt:** option,
   please take a moment to add the **:alt:** option with a functional description of the image.

The ``image`` directive has many options, but we don't recommend most of them for FTC Docs. 
This is new guidance so many existing pages specify **width** and **align**.
It maybe worth removing those if you are changing the content on that page anyway.

Image Options
"""""""""""""

The options supported by the ``image`` directive are:

alt : *text*
   Alternate text: a short description of the image, displayed by applications
   that cannot display images, or spoken by applications for visually impaired
   users
height : *length*
   The desired height of the image. Used to reserve space or scale the image
   vertically. When the "scale" option is also specified, they are combined.
   For example, a height of 200px and a scale of 50 is equivalent to a height
   of 100px with no scale.
scale : *integer percentage (the "%" symbol is optional)*
   The uniform scaling factor of the image. The default is "100 %", i.e. no
   scaling.
width : *length or percentage of the current line width*
   The width of the image. Used to reserve space or scale the image
   horizontally. As with "height" above, when the "scale" option is also
   specified, they are combined. It is often preferable to use *width*
   over *height* or *scale*.
align : "top", "middle", "bottom", "left", "center", or "right"
   The alignment of the image, equivalent to the HTML <img> tag's deprecated
   "align" attribute or the corresponding "vertical-align" and "text-align" CSS
   properties. The values "top", "middle", and "bottom" control an image's
   vertical alignment (relative to the text baseline); they are only useful for
   inline images (substitutions). The values "left", "center", and "right"
   control an image's horizontal alignment, allowing the image to float and
   have the text flow around it. The specific behavior depends upon the browser
   or rendering software used.
target : *text (URI or reference name)*
   Makes the image into a hyperlink reference ("clickable"). The option
   argument may be a URI (relative or absolute), or a reference name with
   underscore suffix (e.g. \`a name`_).

The new guidance related to images comes from improving website accessibility.
We recommending avoiding the following options.


align : 
   The accessibility problem comes because the image can float to the new position with text reflowing around it.
   This can float the image out of context with its surrounding text. A big accessibility issue as images should relate to the text.
   Images can float to the next page in the PDF version, sometimes the image is there all alone on an otherwise blank page.

width : height, scale
   Width is usually used to force the image to not fill the width of the page which usually looks ok in HTML and PDF. 
   However, when viewing in a mobile browser the image can be too small to see easily.
   For example, a width of 50% will look fine when viewed on a big screen, but in portrait mode in a mobile browser the image will be half the width of the screen.
   However, on mobile you can usually just use two fingers to zoom the image (as long as you don't have a physical disability with your fingers). 
   
   The bigger accessibility problem is that it also causes Sphinx to insert a link to the image. 
   This is an accessibility issue as the link ltself has no title. It does not read well in a screen reader.
   If a visually impaired person followed the link they end up on a page with no text content and no alt text either.
   
   The AprilTag test images have both height and width specified as 5in which looks ok on the desktop or in a PDF,
   but ends up with a squished aspect ratio if viewed in a mobile browswer.
   We'd be better off not specifying that for HTML and the PDF version of FTC docs, and rely on a separate PDF download that they can print.
   
   If you want to keep the **width** option (perhaps the image size is too big for the page), then for accessibility we recommend you add the **class** option with **no-scaled-link**.
   This tells Sphinx to not create the link, but the images will have the width you want.
   Though a better option might be to change the resolution of the image.

External Images
"""""""""""""""

It is possible to include images that are external to FTC Docs, but we don't recommend that.
There is no way to know if the image will still be there in the future.
There is also the issue that external images may be copyrighted so we would not have permission to use.

Including an external image using a web address:

.. code:: ReST

   .. image:: https://m.media-amazon.com/images/I/51-2PZby7KL.jpg
      :alt: Logitech gamepad


Decorative Images
"""""""""""""""""

A wavy line image that is used to separate blocks of content is a decorative image.
A photo of persons shaking hands on a page about negotiating contracts might be decorative if it was placed to look pretty.
If the image is not directly related to the content and is ony there for visual appeal then it is a decorative image.

.. note:: FTC Docs does not use decorative images. Do not add an image because it looks nice.
   This is not a marketing web site or a visual design website.

Decorative images are also an accessibilty problem. The screen reader has to process them.
If the image has alt text it is not likely related to the content so it may just cause confusion.

If you really need a decorative image, use the **.. image** directive and include the **:alt:** option with blank text.  
Blank alt text will cause screen readers to ignore the image, which is appropriate when the image is just there for visual presentation.

Example

.. code:: ReST

   .. image:: images/handshake.jpg
      :alt: 

Figure Directive
^^^^^^^^^^^^^^^^

Use the ``.. figure`` directive when the image requires a visible text caption or a long description.

Photo credits are an example of whe you need a caption. 
You should also use a caption when you need editorial or illustrative text to highlight something 
about the image to the reader or to connect the image to the surrounding text content.

If a caption is not required, just use the `Image Directive`_.

Please create alt text for screen readers even though there is a caption. 
The alt text and caption should be different because a screen reader will read both.
One way to think about this is the alt text should be functional and the caption editorial or illustrative.
In the following example, the alt text describes the image, and the caption serves to connect the image
with a travel article about Machu Picchu.

.. code:: ReST

   .. figure:: images/martha.jpg
      :alt: A closeup of a llama's face looking off to the side on a mountain.
      
      Martha is one of the many domesticated llamas that roam freely around the grounds of Machu Picchu.

Note that the ``:alt:`` line and caption are both indented 3 spaces after the directive.
A blank line is required between the ``:alt:`` and the caption.

We don't want the ``:alt:`` line to be blank. 
A screen reader will have probably spoken that there is a figure, without alt text the screen reader will skip over announcing the image and read the caption
leaving the user wondering what the caption is referring to.

The **figure** directive supports all options of the **image** directive. These options (except align) are passed on to the contained image.

* **:align:**  "left", "center", or "right". 
   The horizontal alignment of the figure, allowing the image to float and have the text flow around it. The specific behaviour depends upon the browser or rendering software used.
   
   Avoid using **align**. In PDF it tends to float the figure to another area of the page,
   sometimes to the next page where the image is no longer in context.

There is an optional legend that can be included after the caption. This might be useful for charts and maps and other complex imagery.
The legend paragraph is a good place for a long description of the image to go.

Legends looks like:

.. code:: ReST

   .. figure:: map.png
      :alt: map to buried treasure

      This is the caption of the figure (a simple paragraph).

      The legend consists of all elements after the caption.  In this
      case, the legend consists of this paragraph and the following
      table:

      +-----------------------+-----------------------+
      | Symbol                | Meaning               |
      +=======================+=======================+
      | .. image:: tent.png   | Campground            |
      +-----------------------+-----------------------+
      | .. image:: waves.png  | Lake                  |
      +-----------------------+-----------------------+
      | .. image:: peak.png   | Mountain              |
      +-----------------------+-----------------------+

There must be blank lines before the caption paragraph and before the legend. 
To specify a legend without a caption, use an empty comment ("..") in place of the caption.
The table would be useful for charts or complex images that might need descriptions, 
like green lines on a diagram versus red lines when the color has meaning.
      
Complex Images
""""""""""""""

To make images accessible for the visually impaired, we need to provide a text description of the image.
For complex images, you might need a whole paragraph to describe the image.

The FTC Docs guidance is to use the legend of a **figure** when a long description is required.
This paragraph should be placed after after the captione, leaving a single blank line in between.

Here's what the complete **figure** looks like with a long description.

.. code:: ReST

   .. figure:: images/image3.jpg
      :alt: A square field with X, Y and Z axes shown
   
      The Cascade Effect game field
      
      In a square field configuration the two Alliances face each other across the field.
      The field is oriented such that the Red Wall is on the right as seen
      from the audience, and the blue wall will be on the left.
      The Y axis points across the field from the Red Wall to the blue wall.
      The X axis points away from the audience to the rear of the field.

Note there are blank lines before and after the caption. 
The paragraph after the caption is known as the legend of the figure.
The caption and legend are indented the same as the alt option.

This will generate the following HTML.

.. code:: HTML

   <figure class="align-default" id="id2">
     <img alt="A square field with X, Y and Z axes shown" class="no-scaled-link" src="../../_images/image3.jpg" style="width: 25%;">
     <figcaption>
       <p><span class="caption-text">The Cascade Effect game field</span><a class="headerlink" href="#id2" title="Permalink to this image"></a></p>
       <div class="legend">
         <p>In a square field configuration the two Alliances face each other across the field.
         The field is oriented such that the Red Wall is on the right as seen
         from the audience, and the blue wall will be on the left.
         The Y axis points across the field from the Red Wall to the blue wall.
         The X axis points away from the audience to the rear of the field.</p>
       </div>
     </figcaption>
   </figure>

The above HTML is good for accessibility because the caption and long description are in the `<figcaption>` tag, which is inside the `<figure>` tag.
This clearly associates the text with the image for screen readers.

Image Files
-----------

Image files should be stored in an ``images`` subdirectory in the folder of the current document. 
This allows the document to reference the image as follows: ``.. image:: images/my-image.png``.

Example: The document **field-coordinate-system.rst** is in the **game_specific_resources\\field_coordinate_system** folder.
The images for that page are stored in the folder **game_specific_resources\\field_coordinate_system\\images**.

Image file names should follow the naming scheme of **short-description.ext**, where the name of the image is a short description of what the image shows. 
This should be less than 24 characters. 
File name extensions shoud be **png** or **jpg**.

Image file formats should be Portable Network Graphics(PNG) or Joint Photographic Experts Group(JPEG).

.. warning:: Images with the extension .gif and .svg are not supported in PDF format. 

Images (including vector graphics) should be less than 500 kilobytes in size and no more than 1000 pixels in width. 
Please make use of a smaller resolution and more efficient compression algorithms.
This facilitates reasonable web page loading for those with slow internet connections.
Our HTML documents have a maximun width of 1000 pixels for desktop browsing so image width should be 1000 pixels or less.


