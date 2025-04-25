FTC Docs Accessibility Guidelines
=================================

The Web Content Accessibility Guidelines (WCAG) are part of a series of web accessibility guidelines published by the Web Accessibility Initiative (WAI) of the World Wide Web Consortium (W3C), the main international standards organization for the Internet. They are a set of recommendations for making Web content more accessible, primarily for people with disabilities — but also for all user agents, including highly limited devices, such as mobile phones. 
See the `WCAG overview <https://www.w3.org/WAI/standards-guidelines/wcag/>`_
for more information about the WCAG standard.

Our goal to address the WCAG Level A success criteria to remove accessibility barriers.
Then move to meet the level AA criteria to improve that accessibility.
See the `How to Meet WCAG Quick Reference <https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2>`_ for more information.

.. Note:: 
   This page attempts to document from the WCAG perspective what is important and relate that to FTC Docs.
   This page is primarily for content authors. Accessibility issues due to Sphinx or Read the Docs will be dealt with in GitHub issues.

.. contents:: Contents
   :local:
   :depth: 3
   :backlinks: none

Principles
----------

The following are WCAG principles that the accessibility guidelines are based on.
   
- **Perceivable** - Information and user interface components must be presentable to users in ways they can perceive.

- **Operable** - User interface components and navigation must be operable.

- **Understandable** - Information and the operation of the user interface must be understandable.

- **Robust** - Content must be robust enough that it can be interpreted by a wide variety of user agents, including assistive technologies.


Principle 1 – Perceivable
^^^^^^^^^^^^^^^^^^^^^^^^^

Information and user interface components must be presentable to users in ways they can perceive.
For the vision impaired this includes providing text alternative for non-text content like images.
It could include Closed Captioning which is a form of subtitling, a process of displaying text on a television, 
video screen, or other visual display to provide additional or interpretive information, where the viewer is given the choice of whether the text is displayed. 

Create content that can be presented in different ways (for example simpler layout) without losing information or structure.

Make it easier for users to see and hear content including separating foreground from background.

.. Note:: FTC Docs mostly consists of web pages with text and images. It should be feasible to make most FTC Docs content perceivable to most users. 

Guideline 1.1 – Text Alternatives
"""""""""""""""""""""""""""""""""

Provide text alternatives for any non-text content so that it can be changed into other forms people need, such as large print, braille, speech, symbols or simpler language.

Success Criterion 1.1.1 Non-text Content - Level A
++++++++++++++++++++++++++++++++++++++++++++++++++

All non-text content that is presented to the user has a text alternative that serves the equivalent purpose.

- FTC Docs labels some images with Alt Text, but many images have nothing and some Alt Text labels are not proper descriptions.

**FTC Docs To Do**

- FTC Docs has begun setting or updating Alt Text for images. This will likely be a gradual and ongoing process as time permits. 
  See :ref:`contrib/style_guide/style-guide:Images` in the Style Guidelines for how to provide text alternatives for images.
- See also :doc:`image-and-figure-details`.

Success Criterion 1.3.3 - Sensory Characteristics - Level A
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Instructions provided for understanding and operating content do not rely solely on sensory characteristics of components such as shape, color, size, visual location, orientation, or sound.

**FTC Docs To Do**

- People who are blind and people who have low vision may not be able to understand instructions if they rely only on a description of the shape and/or location of content. Providing additional information in any instructions other than shape and/or location will allow users to understand the instructions even if they cannot perceive shape and/or location.

Principle 2 – Operable
^^^^^^^^^^^^^^^^^^^^^^

User interface components and navigation must be operable.

.. Note:: FTC Docs has some operable issues to be resolved in Sphinx or the Read the Docs theme. 

Guideline 2.4 – Navigable
"""""""""""""""""""""""""
Provide ways to help users navigate, find content, and determine where they are.	

Success Criterion 2.4.4 Link Purpose (In Context) - Level A
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The purpose of each link can be determined from the link text alone or from the link text together with its programmatically determined link context, except where the purpose of the link would be ambiguous to users in general.

- FTC Docs has intentionally chosen to open links to external sites in new tabs. This is done with JavaScript.

  This does preserve your current location in FTC Docs and may be convenient for sighted users who can easily close the new tab.
  This is an accessibility issue related to unexpected context switching, it also creates a new browser tab that some users might have trouble noticing or closing.
  It also prevents the *back* browser command from working.
  
- There is a FTC Docs Pull Request to add an external link icon and screen reader text to external links.
   
  We can mitigate the accessibility problem of creating new browser tabs somewhat by adding an icon that indicates the link is to an external site.
  That can be styled with CSS and a span is added with text that is only for screen readers to say "external". 
  We also add screen reader only text that says "link opens in a new tab" to warn screen reader users that the link will open a new tab.

**FTC Docs To Do**

- We link to some files like a PDF without warning the user. PDFs often result in a context switch to a PDF viewer.
- I have been surprised a few times when links I thought would be a FTC Docs page actually took me to a PDF or to *FIRST* Inspires web page.
  The Persona Pages are bad for this. There are grid button links that sometimes take you to a ftc-docs page but often take you to another site with no warning.
  Ideally all Persona pages should link to FTC Docs pages, some of which might be Gateway Pages to the main *FIRST* site.
- See the :ref:`contrib/style_guide/style-guide:links` section of the Style Guide.
  There is information about how to create links in RST content including good link text which helps users decide whether they want to follow the link.

Guideline 2.5 – Input Modalities
""""""""""""""""""""""""""""""""

Make it easier for users to operate functionality through various inputs beyond keyboard.	

**FTC Docs To Do**

- We might want to enhance functionality for mobile users and other forms of input.
  But we need to be careful not to introduce problems. 
  For example, important content in a tooltip that only shows with mouse hover and is not keyboard accessible or accessible on a mobile device.

Principle 3 – Understandable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Information and the operation of the user interface must be understandable.

Guideline 3.1 – Readable
""""""""""""""""""""""""

Make text content readable and understandable.	

**FTC Docs To Do**

- Plain language means communicating in a way that’s clear, straightforward, and easy to understand. It helps audiences “get” what you’re saying immediately. See https://evolvingweb.com/blog/plain-language-guide-how-write-inclusive-digital-content-2024.
- Some FTC Docs pages have acronyms and excess punctuation that screen readers had trouble with. Revising the text to make it more accessible would make it more readable and understandable for all users.
- It's OK to discuss a complex subject, but given the wide audience for FTC Docs content authors should consider perhaps a simplified introduction or summary that builds in complexity and/or add links to background information.

Principle 4 – Robust
^^^^^^^^^^^^^^^^^^^^

Content must be robust enough that it can be interpreted by a wide variety of user agents, including assistive technologies.

.. Note:: This success criterion is primarily for Web authors who develop or script their own user interface components. For example, standard HTML controls already meet this success criterion when used according to specification.

  Counter example: use of Sphinx primary grids is a problem because they create ‘fake’ buttons that screen readers have problems with.

**FTC Docs To Do**

- Content authors may wish to take care not to use Sphinx or Read the Docs feature that result in accessibility problems.

- They should also review their changes in desktop and mobile views and the generated PDFs of FTC Docs content.

