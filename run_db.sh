#! /bin/sh
#
# This file is intended to run the database locally.
#

# Build the Docker image.
docker build -t python-test-db-local:1.0 -f ./db/local.dockerfile .

# Run the database
docker run --rm -d -p 5432:5432 --env POSTGRES_DB=python-test-db-local \
--env POSTGRES_USER=${DB_USER} --env POSTGRES_PASSWORD=${DB_PASSWORD} \
python-test-db-local:1.0