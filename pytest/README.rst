pytest-split durations
======================

This directory contains test durations files for
`pytest-split <https://github.com/jerry-git/pytest-split>`_, which is used to
accelerate `pytest <https://github.com/pytest-dev/pytest>`_ runs in scico
project CI.

These files should be updated for both MacOS and Ubuntu test platforms whenever
significant changes are made to the scico test suite. Updates should be
computed using::

    pytest --level=<n> --store-durations --durations-path <path-to-durations-file>

where `n` is 1 for MacOS and 2 for Ubuntu, and then bzipped before being used to
replace existing versions.
