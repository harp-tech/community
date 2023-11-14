*************************************************
Harp Documentation - DEPRECATED
*************************************************

**This repository is being superseded by a new DocFX website at** `harp-tech/harp-tech.github.io <https://github.com/harp-tech/harp-tech.github.io>`_. **It will be archived and marked as read-only.**

How to edit this documentation
####################################

The documentation files are written in reStructuredText and saved in the 'source' folder. Sphinx is a documentation generator that converts these .rst files to HTML, so that browsers can display them. This sphinx 'build' can be performed locally so that you can preview pages in a browser, or it can be done by github remotely (see below for build instructions).

Sphinx is a Python project, and each site relies on a specific list of python packages. These are listed in the Pipfile so that local or remote builds know which packages to install. This project uses pipenv, allowing the user to create a virtual environment in which the correct version of all required packages is installed (see 'local build').


How to build this documentation
####################################

Building remotely
*************************************************
Pushing to the main branch of the repo triggers GitHub Actions. Gh-actions will generate a virtual environment, build the HTML pages, and then commit and push these to the 'gh-pages' branch, by following the instructions under .github/workflows/sphinx-build. Finally, if under repo settings gh pages is enabled and points to 'gh-pages/docs, the docs site will be generated.

Building locally
*************************************************
Building HTML files locally allows you to preview changes.

With pipenv (recommended)
-------------------------------------------------

Requirements (system)

* make

Requirements (Python 3):

* pipenv (will automatically download all the project requirements from pypi)

Create a virtual environment with pipenv (will use the Pipfile for installing the necessary packages)

.. code:: install

   pipenv install

then you can start a subshell

.. code:: shell

   pipenv shell

and build the documentation

.. code:: build

   make html

all the outputs will be in docs folder (for html: docs/html)


Adding or editing Device Data
####################################

Device data is collected and modified on a Google sheet. The deviceHandle will also be used to search for the device image, so be sure to name images with the devicehandle. There should not be more than one link entered in a cell that points to a repo or software.

To update the documentation with the Google Sheet information, run the script 'harpsheetstopages.py' in the _static/python folder. This will use the card, page, and repo button template in order to generate a page and device card for each added device.


Acknowledgements
####################################

This documentation's source template was taken from the `Spinal HDL <https://github.com/SpinalHDL/SpinalDoc-RTD>`_ project.

The theme is based on the `PyData Sphinx Theme <https://pydata-sphinx-theme.readthedocs.io/en/latest/>`_
