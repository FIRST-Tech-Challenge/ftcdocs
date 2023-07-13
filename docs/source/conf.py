# Configuration file for the Sphinx documentation builder.

# -- Project information
import os
import sys
import urllib.parse as urlparse

project = 'FIRST Tech Challenge Docs'
copyright = 'FIRST'
author = 'FIRST Tech Challenge'

release = '0.1'
version = '0.1.0'
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

# Disable xindy support
# See: https://github.com/readthedocs/readthedocs.org/issues/5476
latex_use_xindy = False

latex_elements = {
    "fontpkg": r"""
	\setmainfont{DejaVu Serif}
	\setsansfont{DejaVu Sans}
	\setmonofont{DejaVu Sans Mono}""",
    "preamble": r"""
	\usepackage[titles]{tocloft}
	\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
	\setlength{\cftchapnumwidth}{0.75cm}
	\setlength{\cftsecindent}{\cftchapnumwidth}
	\setlength{\cftsecnumwidth}{1.25cm}
	""",
    "fncychap": r"\usepackage[Bjornstrup]{fncychap}",
    "printindex": r"\footnotesize\raggedright\printindex",
}

suppress_warnings = ["epub.unknown_project_files"]

sphinx_tabs_valid_builders = ["epub", "linkcheck"]

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Specify a standard user agent, as Sphinx default is blocked on some sites
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"

# Add a timeout to linkcheck to prevent check from simply hanging on poor websites

linkcheck_timeout = 30

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
   r'https://www.solidworks.com/',
   r'https://april.eecs.umich.edu/'
]

latex_documents = [
    (master_doc, output_name + '.tex', project, author, "manual"),
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

# Add support for translations
gettext_compact = False
locale_dirs = ["locale/"]
