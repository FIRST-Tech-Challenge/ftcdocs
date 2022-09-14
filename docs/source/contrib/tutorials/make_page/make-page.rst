Creating a new page in FTC Docs
============================

When do you make a new page
------------------------------

Often times when adding new content to FTC Docs you will be tasked between the choice of creating a 
new page or adding content to an existing page. This decision is not always easy to make, but there 
are a few things to consider when making this decision. Each page should be a "bite-sized" chunk of 
information; users should not see a wall of text. At the same time content that goes together very 
tightly should be on the same page. Often times the key factor in this decision is the impact on the 
length of the page. Sphinx allows a high level of integration between pages so breaking up content into 
multiple pages is not a huge problem.

Where do you add a new page
------------------------------

Docs is organized into many different sections and subsections. To decide where to add a new page a 
good practice is to think where you would expect that page to be if it was already there. After figuring 
this out you have to figure out your insertion point. This is the page that will link to your new page. 
In Sphinx, this is done by appending your new page to the end of the 
`toctree <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`_ 
directive in the parent index page. 

FTC Docs Hierarchy Explained
------------------------------

Every single page in FTC Docs is a child of the main page (index.rst). This is the root of the project. 
FTC Docs uses a system whereby each page that is a leaf node, or a page that does not have any children, 
is has a directory entirely to itself. This is done to make it easier to find pages and to make it easier. 
There is only ever one rst file per directory and layer. For non leaf nodes instead use an index.rst file. 
Each index will have a `toctree <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`_ 
and no non indexes will have a toctree. This also does not mean that an index file cannot itself have content on it. 
Lead node directies are named after the title of the page they are the index for. For example, the index for the 
"Hardware" section is named "hardware" and the index for the "Hardware" page is named "hardware.rst". Directories use 
``_`` to separate words and files use ``-`` to separate words. 


Steps to create a new page
-----------------------------


Local
~~~~~~~




GH Pages
~~~~~~~~~~