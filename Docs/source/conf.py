# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os
import pathlib 

sys.path.insert(0,os.path.abspath("../../src"))
sys.path.insert(1,os.path.abspath("/home/lukab/.cache/pypoetry/virtualenvs/proj-h402-promethee-gamma-gui-o5_ldxpO-py3.11/lib/python3.11/site-packages"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PROMETHEE Gamma GUI app'
copyright = '2023, Luka BONHEURE'
author = 'Luka BONHEURE'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.viewcode', 
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',]

templates_path = ['_templates']
exclude_patterns = []

intersphinx_mapping = {'python': ('https://docs.python.org/3', None),
                    'matplotlib': ('https://matplotlib.org/', None),
                    'numpy': ('http://docs.scipy.org/doc/numpy/', None)}



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
