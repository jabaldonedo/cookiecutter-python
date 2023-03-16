Cookiecutter Python
===================

This repository contains a Cookiecutter_ template for creating a basic Python development project structure. It is
based on the cookiecutter-hypermodern-python_ template.

.. _cookiecutter-hypermodern-python: https://github.com/cjolowicz/cookiecutter-hypermodern-python

Usage
-----

In order to instantiate this template you need to have Cookiecutter_ installed. We recommend doing the installation
through pipx_ in order to isolate python applications as much as possible to avoid incompatibilities.

.. code-block:: bash

    pipx install cookiecutter

Then you can instantiate the template by running:

.. code-block:: bash

    cookiecutter https://uri.to.this.repository

This will prompt you for some information about your project and then create a directory with the project structure.


.. _Cookiecutter: https://www.cookiecutter.io/
.. _pipx: https://github.com/pypa/pipx
