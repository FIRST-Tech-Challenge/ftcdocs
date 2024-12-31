FTC Docs Workflows
===================
.. note::
    Please note that this flowchart is meant only for refernce for 
    *maintainers* of the FTC Docs repository. For those looking 
    only to contribute to the FTC Docs documents please refer to 
    the :doc:`Contributing to FTC Docs </contrib/tutorials/index>` document.

Overview
--------
.. mermaid::

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
