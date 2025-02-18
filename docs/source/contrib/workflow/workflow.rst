FTC Docs Workflows
===================
.. note::
    Please note that this flowchart is meant only for reference for 
    *maintainers* of the FTC Docs repository. For those looking 
    only to contribute to the FTC Docs documents please refer to 
    the :doc:`Contributing to FTC Docs </contrib/tutorials/index>` document.

Overview
--------

The following diagram shows the various GitHub repositories and the actions and flow between them and the build artifacts.
Pull Requests to the FTC Docs repository result in GitHub actions that build HTML pages and PDF files.
The HTML pages ultimately end up on the ftc-docs.firstinspires.org website and the PDF files in AWS S3 file storage.

In a web browser this diagram can be zoomed and panned by using a mouse. 
Use the scroll wheel to zoom in and out. Right click and hold then drag to pan.
The diagram is not keyboard accessible.
A screen reader will read the various nodes and actions in the diagram and starts in the Translation section of the diagram.

.. mermaid::
   :zoom:

    flowchart LR
        private[Private Github Repo]
        source[FTC Docs Github Repo]
        translation-repo[FTC Docs Translation Repo]
        transifex[Transifex]
        aws-s3[AWS S3]
        booklets[Booklet Builder]
        site[ftc-docs.firstinspires.org]
        cdn[ftc-docs-cdn.ftclive.org]
        contributors[Contributors]


        rtd-ftcdocs-en[RTD FTC Docs]
        rtd-ftcdocs-es[RTD FTC Docs Spanish]
        rtd-ftcdocs-fr[RTD FTC Docs French]

        private-->|Release Content|source
        contributors-->|Pull Request|source
        source-->|GitHub Action|translation-repo

        subgraph Translation
        direction BT
        transifex-->|.po files|translation-repo
        translation-repo-->|.pot files|transifex
        end
        
        source-->|GitHub Action|booklets
        booklets-->|Booklets in all languages|aws-s3
        aws-s3 --> cdn
        translation-repo-->booklets

        source-->|reST|rtd-ftcdocs-en
        translation-repo-->|Webhook|rtd-ftcdocs-es
        translation-repo-->|Webhook|rtd-ftcdocs-fr

        rtd-ftcdocs-en -->|HTML and Main PDF|site
        rtd-ftcdocs-es -->|HTML and Main PDF|site
        rtd-ftcdocs-fr -->|HTML and Main PDF|site
