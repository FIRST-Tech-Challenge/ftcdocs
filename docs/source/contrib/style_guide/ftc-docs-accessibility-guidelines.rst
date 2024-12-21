FTC Docs Accessibility Guidelines
=================================

The Web Content Accessibility Guidelines (WCAG) are part of a series of web accessibility guidelines published by the Web Accessibility Initiative (WAI) of the World Wide Web Consortium (W3C), the main international standards organization for the Internet. They are a set of recommendations for making Web content more accessible, primarily for people with disabilities—but also for all user agents, including highly limited devices, such as mobile phones.

As of December 2024, FTC Docs meets some of the WCAG success criteria, but fails at others.
We have good page titles and make use of section headers to organize our content.
We fail at accessible site navigation: we don't have a skip to main content link among other problems.

.. attention:: I think This will be a long page. It's a rough draft.
   The idea is to document from the WCAG perspective what is important and relate that to FTC Docs.
   The following sections are just outlines that will get filled in.

   See `<https://docs.google.com/document/d/1_-seP4lzyWeXwlTSd1wlaon35Zm-YqKZUro3rni0Ap4/edit?usp=sharing>`_
   for an ADA Compliance review (which is primarily a WCAG review).
   
   See https://docs.google.com/spreadsheets/d/1Z_i5QImEdU5CA1j-hBAnpV2jqXNBhC-Rx-bLb0uJnAM/edit?usp=sharing
   for a more detailed WCAG analysis of the 30 level A success criteria.

   See https://docs.google.com/document/d/1b4BjhLhSdbSScADhpJgLYIyqK69RHIxxOdXWzczOBUw/edit?usp=sharing
   for a proposed plan to address FTC Docs accessibility.

.. See `https://docs.google.com/document/d/1_-seP4lzyWeXwlTSd1wlaon35Zm-YqKZUro3rni0Ap4/edit?usp=sharing`_

.. contents:: Contents
   :local:
   :depth: 2
   :backlinks: none

Principle 1 – Perceivable
^^^^^^^^^^^^^^^^^^^^^^^^^

Information and user interface components must be presentable to users in ways they can perceive.

FTC Docs mostly consists of web pages with text and images. 
It should be feasible to make most FTC Docs content perceivable to most users. 

Guideline 1.1 – Text Alternatives
"""""""""""""""""""""""""""""""""

Provide text alternatives for any non-text content so that it can be changed into other forms people need, such as large print, braille, speech, symbols or simpler language.

For FTC Docs this should be all content images, plus any user interface images (such as the dark-light theme switcher icon).

**FTC Docs To Do**

- All content images require Alt text. Some pages do not have alt text for images.  For those page switch alt text the text should be reviewed as the alt text for many is not appropriate. For Example, a single word is not a description.
- FTC Docs needs to provide text alternatives to the theme switch icon. 
- We need to fix the alt text link to the FTC Logo, it should read "FTC Docs Home" as it is a functional link to take users back to the home page. 
- We need to fix the Read the Docs icon.

Guideline 1.2 – Time-based Media
""""""""""""""""""""""""""""""""

Provide alternatives for time-based media.

FTC Docs (and the *FIRST* Inspires site) make use of videos hosted on YouTube.
Those videos have Closed Captioning which is good for those persons who cannot hear the persons speaking in the videos.

**FTC Docs To Do**

- We do not have a a Described Video narrator which would would describe the action in our videos for the visually impaired. This is more of a main FIRST Inspires website issue.

Guideline 1.3 – Adaptable
"""""""""""""""""""""""""

Create content that can be presented in different ways (for example simpler layout) without losing information or structure.

FTC Docs mostly does this already. An example of this is that we have a desktop and mobile version of the web site.
We also publish a PDF version of FTC Docs.

**FTC Docs To Do**

- We have some icons (like the theme switcher) that probably should have a visible text description. Icons alone are not good accessible user interface.

Guideline 1.4 – Distinguishable
"""""""""""""""""""""""""""""""

Make it easier for users to see and hear content including separating foreground from background.

**FTC Docs To Do**

- FTC Docs uses color alone to mark links, it really needs to underline links, and provide for all the link features like Hover and Visited.
- For FTC Docs we need to review our use of color for both the light and dark themes. 
  Grey text on dark or light backgrounds may not be of sufficient contrast for those person with vision problems.
  Admonitions like Notes also have this issue.
- The footer (as of Dec. 2024) also has a problem with contrast.

Principle 2 – Operable
^^^^^^^^^^^^^^^^^^^^^^
User interface components and navigation must be operable.

This may be hard to fix in FTC Docs without changing the Sphinx or Read the Docs templates, perhaps even requiring changes to how they work.
Sphinx and Read the Docs are not designed for accessibility.

Some things like link spacing and how we link to things are under our control. 

**FTC Docs To Do**

- The Read the Docs overlay needs to be keyboard accessible.
- Do not make use of Access Keys, or make them adjustable. FTC Docs sets Next and Previous keys. We have N=next and P=prev accesskey shortcuts that can't be modified and are active when the next previous buttons DO NOT have focus.
- The footer links are too close together, making them a touch target problem (making it more likely a person would press the wrong link by accident).
- We do not have a skip-to-main-content link. Or a way to skip or bypass the sidebar nav links.
- We link to some PDF's without warning the user. We might need to warn/indicate links external to ftc-docs. I have been surprised a few times when links I thought would be an ftcdocs page actually took me to a PDF or to the FIRST Inspires main site.

Principle 3 – Understandable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Information and the operation of the user interface must be understandable.

Make text content readable and understandable.

- Insert something about plain language. See https://evolvingweb.com/blog/plain-language-guide-how-write-inclusive-digital-content-2024.

Make Web pages appear and operate in predictable ways.

**FTC Docs To Do**

- Some pages (like the old Field Coordinate System page) had acronyms and excess punctuation that screen readers had trouble with. Revising the text to make it more accessible would make it more readable and understandable for all users. See the Plain Language guide.
- The sidebar is not predicable to an inexperienced user or a visually impaired person. When a link is clicked the sidebar redraws itself and grabs focus. The focus should be on the content of the link destination.
- FTC Docs should not open external links in new tabs by default. This is an unexpected context switch that a user cannot recover from by just using the back feature of a browser. If we really want an external link to open in a new tab, there should be text like "(opens in a new tab)" in the link text to tell users it will open in a new tab before it is clicked.
- We also have a weird CAPTCHA that pops up unexpectedly and with a complete context switch. I've noticed it in the search box. There is also a CAPTCHA related to the submit feedback form.

Principle 4 – Robust
^^^^^^^^^^^^^^^^^^^^

Content must be robust enough that it can be interpreted by a wide variety of user agents, including assistive technologies.
Help users avoid and correct mistakes.

This success criterion is primarily for Web authors who develop or script their own user interface components. For example, standard HTML controls already meet this success criterion when used according to specification.

**FTC Docs To Do**

- We probably need to change the fake buttons used in the persona grid pages to real buttons.

