#! /bin/bash
#
# This file is intended to be placed inside the container to run the tests.
#

#
# Enable the virtual environment
#
source /venv/bin/activate

#
# Run the tests
#
pytest
