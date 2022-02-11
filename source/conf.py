# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Typed Ansible"
copyright = "2022, valbendan"
author = "valbendan"

# 版本配置
version = "v22.2.11"
# The full version, including alpha/beta/rc tags
release = "2022.2.11"

# -- General configuration ---------------------------------------------------

# for sitemap remove lang and version
# ta for Typed Ansible
html_baseurl = "https://ta.2cc.net"
sitemap_url_scheme = "{link}"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_sitemap",
    "sphinx_rtd_theme",
    "notfound.extension",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# https://sphinx-notfound-page.readthedocs.io/en/latest/configuration.html
notfound_no_urls_prefix = True

# sphinx.ext.todo
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#confval-todo_includ
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"
# html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# 不允许查看源代码
html_show_sourcelink = False
