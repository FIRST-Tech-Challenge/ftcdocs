ReStructured Text Overview
==========================

This overview serves to describe the overall purpose and functionality of 
reStructured Text (rST) files.

Overview
--------

From the outset, let me say that "reStructured Text" is probably a bit of a
misnomer. It's more like "Text" that uses certain consistent patterns (also
known as *markup*) in order to instruct a tool on how that text should
ultimately look or feel - for example, whether or not a passage should be
*italicized*, **bolded**, or if an image should be displayed in that location in the
final document. ReStructured Text is used to generate *minimally-interactive
web pages*, PDF documents, and other forms of output in such a way that no
actual web programming or PDF publishing experience is necessary AND is still
human-readable. In this way, reStructured Text can literally be written once
and then exported to lots of different formats and platforms. Comprable web
programming and PDF authoring tools are not, in the opinion of this author,
readable by the average person and cannot be easily translated between output
formats whereas "reStructured Text" is. 

History
-------

Now a very brief history lesson: In the early 1990's the first "Structured
Text" markup languages were developed - these languages were used to help
develop different kinds of program documentation for the quickly developing
software industry. This created a universal standard for adding symbols and
directives to plain text so that it could be processed by generic tools. This
way the documentation could be read and formatted any way a user or company
wanted - it could be converted into printer commands for printing onto paper,
it could be rendered onto a screen, it could be read aloud by a text-to-voice
system, or it could be used in lots of other ways. Unfortunately, as is
usual in this business, the tools quickly became too complicated or not
flexible enough for the needs of its users. In the early 2000's, elements of
"Structured Text" were "revised, reworked, and reinterpreted" into a new
format, which ultimately became called "reStructured Text" (rST).

Example
-------

As a quick example, consider the following text::

   The quick brown fox jumped over the lazy dog.

Let's assume we want to **bold** the nouns in the sentence, so in rST format 
we would add two asterisks (**) to the front and end of each word to make them
**bold**. Let's do that by modifying the text to show the following::

   The quick brown **fox** jumped over the lazy **dog**.

This would ultimately output text that looks like:

   The quick brown **fox** jumped over the lazy **dog**.

Now let's make the word ``quick`` be *italicized*. In rST format, we *italicize*
words or sections by adding a single asterisk (*) to the front and end of each 
section we want to *italicize*. It would now look like so::

   The *quick* brown **fox** jumped over the lazy **dog**.

This would output text that looks like:

   The *quick* brown **fox** jumped over the lazy **dog**.

And finally, let's add a link on the word "over" to the `dictionary.com 
reference of the word over <https://www.dictionary.com/browse/over>`_. To do this,
we use a slightly more complex piece of markup that includes "back ticks" (`) and
ends in an underscore (_), like this::

   The *quick* brown **fox** jumped `over <https://www.dictionary.com/browse/over>`_ the lazy **dog**.

And this sentence with several different kinds of *markup* finally would be displayed as:

   The *quick* brown **fox** jumped `over <https://www.dictionary.com/browse/over>`_ the lazy **dog**.

This was just a quick example of what can be done with rST and how it is 
accomplished. Move on to the other elements of this tutorial to learn 
more about rST.

