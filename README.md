# Yggtrasil Developer Documentation
The documentation of the development platform **Yggtrasil**. This platform is a versatile embedded development platform manly for Embedded GNU/Linux and Android but not only.
The documentation is based on sphinx and configured in a way that it is easy to automatically deploy its content by build automation systems such as GitLab CI/CD.

## Authors
 * Nikolaij Jurek Andreij SAEGESSER <sagen1@bfh.ch> 
 * Fabian Marc WEBER <webef4@bfh.ch>
 * Martin AEBERSOLD <aom1@bfh.ch>
 * Andreas HABEGGER <andreas.habegger@bfh.ch>
 * Marco BOSS <marco.boss@bfh.ch>

## Build Sphinx Locally
Build the documentation with the following steps:

 * Prepare the python environment
 ```bash
 python3 -m venv venv
 source venv/bin/activate
 pip install -r requirements.txt
 ```
 * Build a local HTML version of the documentation
 ```bash
 make html
 ```
 * Display the HTML documentation with default web browser
 ```bash
 xdg-open _build/html/index.html 
 ```
## Getting Started With Sphinx
[The Sphinx Doc](https://www.sphinx-doc.org/en/master/usage/index.html)
