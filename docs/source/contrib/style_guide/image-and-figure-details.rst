Image and Figure Details
========================

This section has detailed information about images and figures and more advice about how to handle them in FTC Docs.

.. contents:: Contents
   :local:
   :depth: 2
   :backlinks: none

.. _decorative-images-label:

Decorative Images
-----------------

A wavy line image that is used to separate blocks of content is a decorative image.
A photo of persons shaking hands on a page about negotiating contracts might be decorative if it was placed to look pretty.
If the image is not directly related to the content and is only there for visual appeal then it is a decorative image.

.. note:: FTC Docs does not use decorative images. Do not add an image because it looks nice.
   This is not a marketing web site or a visual design website.

Decorative images are also an accessibility problem. The screen reader has to process them.
If the image has alt text it is not likely related to the content so it may just cause confusion.

If you really need a decorative image, use the **.. image** directive and include the **:alt:** option with blank text.  
Blank alt text will cause screen readers to ignore the image, which is appropriate when the image is just there for visual presentation.

Example

.. code:: ReST

   .. image:: images/handshake.jpg
      :alt: 

Image Directive
---------------

Use the ``.. image`` directive to include an image that does **not** need a caption.
Determine if the image needs a caption. Photo credits need a caption. Complex images probably need a caption. 
Anything that requires an editorial or illustrative description to tie the image to the content of the page requires a caption. 

If no caption is required then the ``.. image`` directive can be used. 
Add the **alt** option and provide text that describes the image. 
This is all you need for basic images.

.. code:: ReST

   .. image:: images/butterfly.jpg
      :alt: A blue butterfly sitting on an orange flower.

The alt text should have a functional description. A functional description explains exactly what is in an image. 
These descriptions should be thorough but brief, one or two sentences.
If a long description is required, use the `figure directive`_ and provide a long description.

.. tip:: insert reference to further guidance on alt text writing - or better yet more examples

.. warning:: Sphinx will set alt text set to the path and file name of the image if you don't specify the **:alt:** option.
   The HTML looks like `<img alt="../_images/GoodStuff.png" src="../_images/GoodStuff.png">`.
   A screen reader will read out loud the alt text `../_images/GoodStuff.png`.
   
   This is not good accessibility. If you are editting an existing page that has an **image** or **figure** directive with no **:alt:** option,
   please take a moment to add the **:alt:** option with a functional description of the image.

The ``image`` directive has many options, but we don't recommend most of them for FTC Docs. 
This is new guidance, many existing pages specify **width** and **align**.
It maybe worth removing those if you are changing the content on that page anyway.

Image Options
^^^^^^^^^^^^^

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


align 
   The accessibility problem comes because the image can float to the new position with text re-flowing around it.
   This can float the image out of context with its surrounding text. That is a big accessibility issue as images should relate to the text near them.
   Images can float to the next page in the PDF version, sometimes the image is there all alone on an otherwise blank page.

width, height, scale
   Width is usually used to force the image to not fill the width of the page which usually looks OK in HTML and PDF. 
   However, when viewing in a mobile browser the image can be too small to see easily.
   For example, a width of 50% will look fine when viewed on a big screen, but in portrait mode in a mobile browser the image will be half the width of the screen.
   However, on mobile you can usually just use two fingers to zoom the image (as long as you don't have a physical disability with your fingers). 
   
   The bigger accessibility problem with these options is that that Sphinx will insert a link to the image. 
   The idea is that you can click the link to see the full size image.
   This is an accessibility issue as the link itself has no title. It does not read well in a screen reader.
   If a visually impaired person followed the link they end up on a page with no text content and no alt text either.
   
   Sighted persons who want to see the full size image have the option to right click the image and open it in a new tab or window.
   
   The AprilTag test images have both height and width specified as 5 inches which looks OK on the desktop or in a PDF,
   but ends up with a squished aspect ratio if viewed in a mobile browser.
   We'd be better off not specifying set sizes for the HTML and the PDF version of FTC docs.
   Then provide a separate PDF download that they can print to get accurately sized AprilTags.
   
   If you want to keep the **width** option (perhaps the image size is too big for the page), 
   then for accessibility we recommend you add the **class** option with **no-scaled-link**.
   This tells Sphinx to not create the link, but the images will have the width you want.
   Though a better option might be to change the resolution of the image if relevant detail can be preserved.

External Images
^^^^^^^^^^^^^^^

It is possible to include images that are external to FTC Docs, but we don't recommend that.
There is no way to know if the image will still be there in the future.
There is also the issue that external images may be copyrighted so we would not have permission to use.

Including an external image using a web address:

.. code:: ReST

   .. image:: https://m.media-amazon.com/images/I/51-2PZby7KL.jpg
      :alt: Logitech gamepad

.. _alt-text-label:

Alt Text
--------

Images must have text alternatives that describe the information or function represented by them. This ensures that images can be used by people with various disabilities. 

Why is this important?
^^^^^^^^^^^^^^^^^^^^^^

Images and graphics make content more pleasant and easier to understand for many people, and in particular for those with cognitive and learning disabilities. They serve as cues that are used by people with visual impairments, including people with low vision, to orient themselves in the content.

However, images are used extensively on websites and can create major barriers when they are not accessible. Accessible images are beneficial in many situations, such as:

- People using screen readers: The text alternative can be read aloud or rendered as Braille
- People using speech input software: Users can put the focus onto a button or linked image with a single voice command
- People browsing speech-enabled websites: The text alternative can be read aloud
- Mobile web users: Images can be turned off, especially for data-roaming
- Search engine optimization: Images become indexable by search engines

Alt Text Guidelines
^^^^^^^^^^^^^^^^^^^

The following guidelines are from: https://www.nngroup.com/articles/write-alt-text/

- Keep it short. Alt text shouldn’t be much longer than around 150 characters. Users can’t pause and resume the screen reader in the middle of alt text without going back to the beginning. People also can’t hold very much information in their working memory. Users will skip alt text if it doesn’t immediately seem like it will help them with their task.
- Do not include words like ‘image’ or ‘photo’ at the beginning. Screen readers already identify images as images when they encounter them because they are contained within the <img> HTML tag. Identifying an image as a certain type (e.g., infographic, chart, illustration) is appropriate if it will help the user understand the other alt text.
- End alt text with a period, even if it isn’t a full sentence. The period ensures that the screen reader pauses after reading the alt text.
- Frontload alt text with the most important words, to help users make a quick and informed decision about whether it’s worth listening to the rest of the alt text before moving on.
- Always include an alt attribute (alt=””), even if it will be empty. Otherwise, screen readers might announce the image file name.
- Avoid technical jargon and abbreviations unless users are certain to understand them.
- Never reuse alt text for the same image without reanalyzing the context in which the image is placed.
- Mention identity only if it’s relevant. If the race, ethnicity, gender, religion, or cultural identifiers of the people pictured aren’t part of the reason the image was included, don’t mention them.

The following examples are taken from: https://www.w3.org/WAI/tutorials/images/

Example: Images used to supplement other information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following image shows a dog wearing a bell. It supplements the adjacent text that explains the purpose of this bell. A short text alternative is sufficient to describe the information that is displayed visually but is not explained in the text; in this case, the text alternative is “Dog with a bell attached to its collar.”.

.. list-table:: 

   * - .. image:: https://www.w3.org/WAI/content-images/tutorials/images/dog.jpg
          :alt: Dog with a bell attached to its collar.
     - Off-duty guide dogs often wear a bell. Its ring helps the blind owner keep track of the dog’s location

The alt text is added to the HTML img tag.

.. code:: html

   <img alt="Dog with a bell attached to its collar." src="https://www.w3.org/WAI/content-images/tutorials/images/dog.jpg">

.. Note:: If the text included an explanation of how the dog wears a bell, the image might be considered redundant and therefore decorative.
   As this isn’t mentioned in the text, the image is deemed to be informative.

Example: Images conveying succinct information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This simple diagram illustrates a counterclockwise direction for unscrewing a bottle top or cap. The information can be described in a short sentence, so the text alternative “Push the cap down and turn it counterclockwise (from right to left)” is given in the alt attribute.

.. list-table:: 

   * - .. image:: https://www.w3.org/WAI/content-images/tutorials/images/counter-clockwise.jpg
          :alt: Push the cap down and turn it counterclockwise (from right to left)

The alt text is added to the HTML img tag.

.. code:: html

   <img alt="Push the cap down and turn it counterclockwise (from right to left)" src="https://www.w3.org/WAI/content-images/tutorials/images/counter-clockwise.jpg">

.. Note::
   1. An alternative technique would be to provide the instructions within the main content rather than as a text alternative to the image. This technique makes all information available in text for everyone while providing an illustration for people who prefer to view the information visually.

   2. If more information than that of the diagram is intended to be conveyed by the image, it may be better to follow one of the approaches described in `Complex Images`_. For example, if the fact that this diagram appears on a bottle or if the shape and size of the bottle were relevant pieces of information, use a more detailed alternative text.

Alt Text and Captions
^^^^^^^^^^^^^^^^^^^^^

The previous examples did not require captions. 
If you also require a caption use the RST figure directive with a caption and alt text.
Ensure the caption does not repeat the alt text.
That's because a screen reader will read both.

While both the alt attribute and the figcaption element provide a way to describe images, the way we write for them is different. 
   - alt descriptions should be functional; 
   - figcaption descriptions should be editorial or illustrative.

external reference: https://thoughtbot.com/blog/alt-vs-figcaption


Figure Directive
----------------

Use the ``.. figure`` directive when the image requires a visible text caption or a long description.

Photo credits are an example of when you need a caption. 
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
   The horizontal alignment of the figure, allowing the image to float and have the text flow around it. The specific behavior depends upon the browser or rendering software used.
   
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

A table might be useful for charts or complex images that might need descriptions of various parts of the image. 
Note: we do not recommend using the ascii art form of a table as shown above, use a list style table instead.
      
Complex Images
^^^^^^^^^^^^^^

FTC Docs has some images that are very complex. Usually there is some surrounding text that relates to the image.
However, we usually don't actually describe the image as we assume the reader is not impaired visually.

If you are editing an existing page, you may need to adjust what text surrounds the image, and what text describes the image.
If the surrounding text describes part of the image, it should probably be moved into the long description of the image.

The FTC Docs guidance is to use the legend of a **figure** directive when a long description is required.
This paragraph should be placed after after the caption, leaving a single blank line in between.
Instead of a paragraph, you can include a table or list if that would better describe the image.

The following example is how we might describe a complex diagram.
We use a **figure** directive with alt text, caption and long description.
This diagram is located on the Control System Introduction page.

.. code:: ReST

   .. figure:: images/REVExpansionHubLayout.jpg
      :alt: Rev expansion hub with various devices connected.
   
      Expansion Hub and Phone
      
      The Expansion Hub has the following devices connected.
      
      - a Robot Controller phone via a USB connection;
      - A 12 volt battery with on/off switch;
      - A three wire servo connects to one of six servo ports;
      - An analog sensor connects to one of two analog sensor ports;
      - An I2C sensor connects to one of four I2C ports;
      - Two motors are connected to the Expansion hub. Each motor has a power connection and an encoder connection. There are four motor ports on the Expansion Hub.
          
The alt text is a summary of the functional description of the image (which follows the caption).
The caption indicates that this is an example of an Expansion Hub and phone and relates to the prior paragraphs 
on the Control System Introduction page which talk about possible configurations of the Expansion Hub.
In this case the long description is basically a listing of the devices connected to the Expansion Hub.
          
.. list-table:: 

   * - .. figure:: ../../programming_resources/shared/control_system_intro/images/REVExpansionHubLayout.jpg
          :alt: Rev expansion hub with various devices connected.
          :width: 25%
          :class: no-scaled-link
          
          Expansion Hub and Phone
          
          The Expansion Hub has the following devices connected.
          
          - a Robot Controller phone via a USB connection;
          - A 12 volt battery with on/off switch;
          - A three wire servo connects to one of six servo ports;
          - An analog sensor connects to one of two analog sensor ports;
          - An I2C sensor connects to one of four I2C ports;
          - Two motors are connected to the Expansion hub. Each motor has a power connection and an encoder connection. There are four motor ports on the Expansion Hub.      

Using a Figure with Caption and Legend is good for accessibility because Sphinx will generate a HTML Figure tag and Figcaption tag.
This clearly associates the text with the image for screen readers.

This HTML is from the square field image of the Field Coordinate System page.

.. code:: HTML

   <figure class="align-default" id="id2">
     <img alt="A square field with X, Y and Z axes shown" src="../../_images/image3.jpg">
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

A screen reader encountering the HTML above will normally announce that there is a **figure**. It would then speak the alt text and indicate there was an **image**.
It would continue by reading the caption followed by the long description. Finally the screen reader would announce **end figure**.

Using the **figure** directive for complex images nicely surrounds the image with a complete text description that is useful for all users as we clearly 
indicate what the image is about and what is important.
   
.. note:: if you ever find that you need a long description, but the image really does not need a visible text caption, you can enter a blank comment as the caption.
   This looks like two periods .. placed where the caption would be and at the same indent as the long description. 
    
   .. code:: rest
   
      .. figure:: images/image3.jpg
         :alt: A square field with X, Y and Z axes shown.
   
         ..
      
         In a square field configuration ...

