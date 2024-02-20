# Configuration file for the Sphinx documentation builder.

# -- Project information
import os
import sys
import urllib.parse as urlparse
import gitinfo

project = 'FIRST Tech Challenge Docs'
copyright = 'FIRST'
author = 'FIRST Tech Challenge'
license = 'BSD 3-Clause'

release = '0.2'
version = '0.2.0'
# -- General configuration

extensions = [
    'javasphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.duration',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx_design',
    'sphinx_rtd_dark_mode',
    'sphinxcontrib.googleanalytics',
    'sphinxcontrib.cookiebanner',
    'sphinxcontrib.mermaid',
]

autosectionlabel_prefix_document = True
default_dark_mode = False
todo_include_todos = False

# Configure Google Analytics, Disabled by default
googleanalytics_enabled = False

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

javadoc_url_map = {
    'org.firstinspires.ftc.ftccommon': ('https://javadoc.io/static/org.firstinspires.ftc/FtcCommon/8.2.0/', 'javadoc'),
    'org.firstinspires.ftc.hardware': ('https://javadoc.io/static/org.firstinspires.ftc/Hardware/8.2.0/', 'javadoc'),
    'org.firstinspires.ftc.inspection': ('https://javadoc.io/static/org.firstinspires.ftc/Inspection/8.2.0/', 'javadoc'),
    'org.firstinspires.ftc.onbotjava': ('https://javadoc.io/static/org.firstinspires.ftc/OnBotJava/8.2.0/', 'javadoc'),
    'org.firstinspires.ftc.robotcore': ('https://javadoc.io/static/org.firstinspires.ftc/RobotCore/8.2.0/', 'javadoc'),
    'org.firstinspires.ftc.vision': ('https://javadoc.io/static/org.firstinspires.ftc/Vision/8.2.0/', 'javadoc'),
}

templates_path = ['_templates']

# Image Checker Configuration

IMAGE_SIZE_EXCLUSIONS = ["source/control_hard_compon/rc_components/images/A1.svg",
                        "source/control_hard_compon/rc_components/images/B1.svg",
                        "source/control_hard_compon/rc_components/images/A2.svg",
                        "source/control_hard_compon/rc_components/images/B2.svg",
                        "source/control_hard_compon/ds_components/images/C1.svg",]

# Specify the master doc file, AKA our homepage
master_doc = "index"

output_name = 'ftcdocs'

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Sidebar logo
html_logo = "assets/FIRSTTech_iconHorz_RGB_reverse.png"

# URL favicon
html_favicon = "assets/FIRSTicon_RGB_withTM.ico"


# Credit: https://github.com/wpilibsuite/frc-docs/blob/main/source/conf.py
# -- Options for latex generation --------------------------------------------

latex_engine = "xelatex"

latex_logo = "assets/Latex_Logo_FTC.png"

latex_additional_files = ["assets/Latex_Footer_FTC.png", "_static/RTX.png", 'assets/FTC_Center_Stage_Title.pdf']

# Disable xindy support
# See: https://github.com/readthedocs/readthedocs.org/issues/5476
latex_use_xindy = False

gitInfo = gitinfo.get_git_info(dir="../../.")
gitInfo = {'commit': "N/A", 'refs': 'N/A', 'author_date': 'N/A', 'author': 'N/A'} if gitInfo==None else gitInfo

latex_elements = {
    "papersize": "letterpaper",
    'classoptions':',openany',
    "fontpkg": r"""
        \setmainfont{Roboto}
        \setsansfont{Roboto}
        \setmonofont{DejaVu Sans Mono}
    """,
    'passoptionstopackages': r"""
        \PassOptionsToPackage{letterpaper,portrait,includehead=true,includefoot=true,left=0.5in,right=0.5in,top=0.9in,bottom=3in,footskip=12.4pt,headsep=25pt,}{geometry}
        \usepackage{titling}
        """,
    "preamble": r"""
        \usepackage{fancyhdr}
        \usepackage{color}
        \usepackage{eso-pic}
        \usepackage{titlesec}
        \usepackage[datesep=/,style=ddmmyyyy]{datetime2}

        \titleformat
            {\chapter} % command
            [display] % shape
            {\bfseries\Large\itshape} % format
            {Chapter \thechapter} % label
            {0ex} % sep
            {
                \vspace*{-1ex}
                \textcolor[rgb]{.96, .49, .15}{\rule{\textwidth}{3pt}}
                \vspace{1ex}
            } % before-code
            [
            ] % after-code

        \addtolength{\topmargin}{-23.80643pt}
        \setlength{\footskip}{36pt}
        \makeatletter
            \fancypagestyle{normal}{
                \fancyhf{}
                \fancyfoot[LE]{{
                        \vspace{-5mm}
                        \includegraphics[scale=0.75]{Latex_Footer_FTC.png}
                }}
                \fancyfoot[RE]{
                    \py@HeaderFamily \py@release \hspace{4mm} \today
                    }
                \fancyfoot[LO]{\py@HeaderFamily \textbf{Gracious Professionalism®} - \textcolor[rgb]{.96, .49, .15}{“Doing your best work while treating others with respect and kindness - It’s what makes FIRST, first.”}}
                \fancyhead[R]{{\vspace{5mm} \py@HeaderFamily \@title, \thepage}}
                \fancyhead[L]{{\vspace{5mm} FTC Docs}}
                \fancyhead[C]{{\vspace{5mm} \begin{center}\py@HeaderFamily \thechapter \end{center}}}

            }
            \fancypagestyle{plain}{
                \fancyhf{}
                \fancyfoot[LE]{{
                        \vspace{-5mm}
                        \includegraphics[scale=0.75]{Latex_Footer_FTC.png}
                }}
                \fancyfoot[RE]{
                    \py@HeaderFamily \py@release \hspace{4mm} \today
                    }
                \fancyfoot[LO]{\py@HeaderFamily \textbf{Gracious Professionalism®} - \textcolor[rgb]{.96, .49, .15}{“Doing your best work while treating others with respect and kindness - It’s what makes FIRST, first.”}}
                \fancyhead[R]{{\vspace{5mm} \py@HeaderFamily \@title, \thepage}}
                \fancyhead[L]{{\vspace{5mm} FTC Docs}}
                \fancyhead[C]{{\vspace{5mm} \begin{center}\py@HeaderFamily \thechapter \end{center}}}
            }

        \makeatother
	""",
    "maketitle": r"""
        \newgeometry{left=0.5in,
            right=0.5in,
            top=0.5in,
            bottom=0.5in}
        \pagenumbering{Roman}
        \begin{titlepage}

            \AddToShipoutPictureBG*{\includegraphics[width=\paperwidth,height=\paperheight]{FTC_Center_Stage_Title.pdf}}
            \vspace*{113mm}
            \begin{flushright}
                \begin{center}
                    \textbf{\Large {2023-2024 \emph{FIRST} Tech Challenge}}
                    \\
                    \vspace{4mm}
                    \textbf{\Huge {\thetitle}}
                    \\
                    \vspace*{\fill}
                    \textbf{\Large {\emph{FIRST} Tech Challenge Documentation}}
                \end{center}
            \end{flushright}
        \end{titlepage}
	
        \newpage
        \vspace*{5mm}
        \textbf{\Large{Sponsor Thank You}}
        \indent Thank you to our generous sponsors for your continued support of the \emph{FIRST} Tech Challenge! 
        \vspace{50mm}
        \begin{figure}[!h]
            \begin{center}
                \includegraphics[scale=0.8]{RTX.png}
            \end{center}
        \end{figure}
        \restoregeometry
        \newgeometry{left=0.5in,
            right=0.5in,
            top=0.6in,
            bottom=1in}
    """,
    'atendofbody': rf"""
            \newpage
            \chapter{{Version Information}}
            \section{{Document Information}}
            \large \textbf{{Author:}} \theauthor
            \\
            \large \textbf{{Version:}} {release}
            \\
            \large \textbf{{Release Date:}} \today
            \\
            \large \textbf{{Generation Time:}} \DTMcurrenttime
            \\
            \section{{Git Information}}
            \large \textbf{{Git Hash: }} {gitInfo['commit']}
            \\
            \large \textbf{{Git Branch: }} {gitInfo['refs']}
            \\
            \large \textbf{{Git Commit Date: }} {gitInfo['author_date']}
            \\
            \large \textbf{{Git Commit Author:}} {gitInfo['author']}
            \section{{Document License}}
            \large \textbf{{License:}} {license}
        """,
    "printindex": r"\footnotesize\raggedright\printindex",
}

suppress_warnings = ["epub.unknown_project_files"]

sphinx_tabs_valid_builders = ["epub", "linkcheck"]

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Specify a standard user agent, as Sphinx default is blocked on some sites
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"

# Add a timeout to linkcheck to prevent check from simply hanging on poor websites

linkcheck_timeout = 60

# Change request header to avoid timeout errors with SOLIDWORKS/Autodesk because they are great like that

linkcheck_request_headers = {
    "https://www.autodesk.com/": {
        "Origin": "https://www.autodesk.com",
        "Referer": "https://www.autodesk.com/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Accept-Language": "en-us,en;q=0.5",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
    },
    "https://www.hp.com/": {
        "Origin": "https://www.hp.com",
        "Referer": "https://www.hp.com/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Accept-Language": "en-us,en;q=0.5",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
    },
    "https://stackoverflow.com/": {
        "Origin": "https://stackoverflow.com",
        "Referer": "https://stackoverflow.com/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept-Language": "en-us,en;q=0.5",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
    },
    "*": {
        "Accept": "text/html,application/xhtml+xml",
    },
}

# Firstinspires redirects to login and break our link checker :)
# ftc-ml.firstinspires.org does a redirect that linkcheck hates.
# GitHub links with Javascript Anchors cannot be detected by linkcheck
# Solidworks returns 403 errors on too many web pages. Thanks, buddy.
# As of 7/13/23, april.eecs.umich.edu has an expired certificate
linkcheck_ignore = [
   r'https://my.firstinspires.org/Dashboard/', 
   "https://ftc-ml.firstinspires.org",
   r'https://github.com/.*#',
   r'https://wiki.dfrobot.com/.*#',
   r'https://www.solidworks.com/',
   r'https://sketchup.com/',
   r'https://april.eecs.umich.edu/',
   r'https://www.autodesk.com/',
   r'https://knowledge.autodesk.com/',
   r'https://www.3dflow.net/',
]

latex_documents = [
    (master_doc, output_name + '.tex', project, author, "manual"),
]

if(os.environ.get("BOOKLETS_BUILD") == "true"):
    print('Building booklets')
    latex_documents = [
	('ftc_ml/index', "ftc_ml.tex", "FTC Machine Learning", author, "manual"), # FTC ML
        ('programming_resources/index', "prgrm_res.tex", "FTC Programming Resources", author, "manual"), # Programming Resources
        ('programming_resources/android_studio_java/Android-Studio-Tutorial', 'android_studios.tex', 'Android Studio Guide', author, "manual"), # Android Studio
        ('programming_resources/onbot_java/OnBot-Java-Tutorial', "onbot_java.tex", 'OnBot Java Guide', author, "manual"), # OnBot Java
        ('programming_resources/blocks/Blocks-Tutorial', "blocks.tex", 'Blocks Guide', author, "manual"), # Blocks
        ('booklets/apriltags', "april_tags.tex", 'April Tags Guide', author, "manual"), # April Tags
        ('booklets/control_system', "control_system.tex", 'Control System Guide', author, "manual"), # Control System
        ('booklets/advanced', "advanced.tex", 'Advanced Topics, Programming Resources', author, "manual"), # Advanced Topics
        ('booklets/sdk', "sdk.tex", 'SDK Guide', author, "manual"), # SDK
        ('robot_building/rev/PowerPlay/part1/index', "rob_building_rev_p1.tex", 'Part 1 - Basic \'Bot Guide for REV', author, "manual"), # REV Bot Building Power Play P1
        ('manufacturing/3d_printing/index', '3d_printing.tex', '3D Printing Guide', author, "manual"), # 3D Printing
    ]
        

def setup(app):
    app.add_css_file("css/ftc-rtd.css")
    #app.add_css_file("css/ftc-rtl.css")
    app.add_js_file("js/external-links-new-tab.js")

# Set Cookie Banner to disabled by default
cookiebanner_enabled = False

# Configure for local official-esque builds
if(os.environ.get("LOCAL_DOCS_BUILD") == "true"):
    html_context = dict()
    html_context['display_lower_left'] = True

    html_context['current_version'] = version
    html_context['version'] = version

    html_context['downloads'] = list()
    pdfname = str(urlparse.urlparse(os.environ.get("FTCDOCS_URL", default="")).path) + output_name + ".pdf"
    html_context['downloads'].append(('PDF', str(pdfname)))

    html_context['display_github'] = True
    html_context['github_user'] = 'FIRST-Tech-Challenge'
    html_context['github_repo'] = 'ftcdocs'
    html_context['github_version'] = 'main/docs/source/'
    cookiebanner_enabled = True


if(os.environ.get("RTD_DOCS_BUILD") == "true"):
    cookiebanner_enabled = True
    extensions.append('sphinx_sitemap')
    html_baseurl = os.environ.get("FTCDOCS_URL", default="")

# Configure RTD Theme
html_theme_options = {
    'navigation_depth': 5,
}

# Avoid duplicate labels
autosectionlabel_maxdepth = 2

# Add support for translations
gettext_compact = False
locale_dirs = ["locale/"]
