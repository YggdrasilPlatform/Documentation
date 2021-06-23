# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#import os
#import sys
#sys.path.insert(0, os.path.abspath('.'))

import furo
import datetime
from pygments.formatters import HtmlFormatter
from recommonmark.transform import AutoStructify

# -- Project information -----------------------------------------------------

project = 'Yggdrasil'
author = 'Sägesser Nikolaij, Weber Fabian'
copyright = str(datetime.datetime.now().year) + ' | ' + author + ' | ' + 'Bern University of Applied Sciences'

# The full version, including alpha/beta/rc tags
#release = '1.0.0'


# -- General configuration ---------------------------------------------------

html_show_sourcelink = False
html_show_sphinx = False
html_copy_source = False
## To deactivate update time-stamp comment the variable
html_last_updated_fmt = ''

sphinx_tabs_disable_tab_closing = True

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # https://sphinx-copybutton.readthedocs.io/en/latest/
    'sphinx_copybutton',
#    'recommonmark',
    # Auto-generate section labels.
#    'sphinx.ext.autosectionlabel',
    # To embed youtube videos
#    'sphinxcontrib.yt',
    # https://www.sphinx-doc.org/en/master/usage/extensions/todo.html
    'sphinx.ext.todo',    
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_tabs.tabs'
]

todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv', 'README.md','.git', '.gitignore', 'requirements.txt', '*~']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
html_title = "Yggdrasil Developer Guide"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#html_logo = '_static/logos/yggdrasil-logo.svg'
html_favicon = '_static/logos/favicon.ico'
html_theme_options = {
    "announcement": "<em>Important</em> announcement!",
# 'sidebar_hide_name' : 'True',
#    https://pradyunsg.me/furo/customisation/logo/
#    "light_logo": "/_static/logos/logo-light-mode.png",
#    "dark_logo": "/_static/logos/logo-dark-mode.png",
}

# some customizations on styles - relative path to _static
html_css_files = [
    'css/tabs.css',
    'css/custom.css',
#    'css/beta_banner.css',
]


html_context = {
#    'current_version': version,
    'display_gitlab': True,
    'gitlab_host': 'gitlab.ti.bfh.ch',
    'gitlab_group': 'yggdrasil',
    'conf_py_path': '/',
    'show_source': False
}

html_scaled_image_link = False

#Internationalization https://www.sphinx-doc.org/en/master/usage/advanced/intl.html
# make german transliation with make -e SPHINXOPTS="-D language='de'" html
locale_dirs = ['locale/']
gettext_compact = False

def setup(app):
    app.add_config_value('recommonmark_config', {
            'enable_eval_rst': True,
            'enable_auto_toc_tree': True,
            }, True)
    app.add_transform(AutoStructify)
