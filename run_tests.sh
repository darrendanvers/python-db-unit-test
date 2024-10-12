#! /bin/sh
#
# This file is intended to run outside the container to build it and kick off the tests.
#

# Build the Docker image.
docker build -t python-test-db:1.0 -f ./db/Dockerfile .

# Run the tests
docker run --rm python-test-db:1.0