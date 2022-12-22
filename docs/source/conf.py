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
    'org.firstinspires.ftc.ftccommon': ('https://javadoc.io/static/org.firstinspires.ftc/FtcCommon/7.1.0/', 'javadoc'),
    'org.firstinspires.ftc.hardware': ('https://javadoc.io/static/org.firstinspires.ftc/Hardware/7.1.0/', 'javadoc'),
    'org.firstinspires.ftc.inspection': ('https://javadoc.io/static/org.firstinspires.ftc/Inspection/7.1.0/', 'javadoc'),
    'org.firstinspires.ftc.onbotjava': ('https://javadoc.io/static/org.firstinspires.ftc/OnBotJava/7.1.0/', 'javadoc'),
    'org.firstinspires.ftc.robotcore': ('https://javadoc.io/static/org.firstinspires.ftc/RobotCore/7.1.0/', 'javadoc'),
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
linkcheck_timeout = 15

# Change request header to avoid 403 error because Solidworks is great like that
linkcheck_request_headers = {
    "*": {
        "Accept": "text/html,application/xhtml+xml",
    }
}

# Firstinspires redirects to login and break our link checker :)
# ftc-ml.firstinspires.org does a redirect that linkcheck hates.
# GitHub links with Javascript Anchors cannot be detected by linkcheck
# Solidworks returns 403 errors on too many web pages. Thanks, buddy.
linkcheck_ignore = [
   r'https://my.firstinspires.org/Dashboard/', 
   "https://ftc-ml.firstinspires.org",
   r'https://github.com/.*#',
   r'https://www.solidworks.com/'
]

latex_documents = [
    (master_doc, output_name + '.tex', project, author, "manual"),
]

def setup(app):
    app.add_css_file("css/ftc-rtd.css")
    #app.add_css_file("css/ftc-rtl.css")
    app.add_js_file("js/external-links-new-tab.js")

# Configure for official builds
if(os.environ.get("DOCS_BUILD") == "true"):
    html_context = dict()
    html_context['display_lower_left'] = True

    html_context['current_version'] = version
    html_context['version'] = version

    html_context['downloads'] = list()
    pdfname = str(urlparse.urlparse(os.environ.get("url", default="")).path) + output_name + ".pdf"
    html_context['downloads'].append(('PDF', str(pdfname)))

    html_context['display_github'] = True
    html_context['github_user'] = 'FIRST-Tech-Challenge'
    html_context['github_repo'] = 'ftcdocs'
    html_context['github_version'] = 'main/docs/source/'
    
    # Specify canonical root
    # This tells search engines that this domain is preferred
    html_baseurl = str(os.environ.get("url")).replace("http://", "https://")
    
    # Sets up sitemap and robots.txt    
    if(html_baseurl != ""):
        extensions.append('sphinx_sitemap')
        
        with open('robots.txt', 'w') as robots:
            
            robots.write(f'User-agent: *\n\nSitemap: {html_baseurl}sitemap.xml')
            html_extra_path = ["robots.txt"]
            sitemap_url_scheme = "{link}"


    # Configure Google Analytics
    googleanalytics_id = os.environ.get("GOOGLE_ANALYTICS_ID") 
    googleanalytics_enabled = os.environ.get("GOOGLE_ANALYTICS_ID", default = "") != ""
    cookiebanner_enabled = os.environ.get("COOKIEBANNER", default = "") != ""

# Configure RTD Theme
html_theme_options = {
    'navigation_depth': 5,
}
