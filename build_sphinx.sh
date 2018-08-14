#!/bin/bash -x
sphinx-apidoc `pwd` --ext-autodoc -F -o sphinx_doc
cd sphinx_doc
make html
