#! /bin/bash
#
# This file is intended to run outside the container to build it and kick off the tests.
#

USAGE="${0} [-e ci|local]\n\
e  environment: Environment must be ci or local. Default is local.\n\
h: Print this message and quit."

ENVIRONMENT=local

while getopts ':e:h' opt; do
  case "${opt}" in
    e)
      ENVIRONMENT=${OPTARG}
      ;;
    h)
      echo -e ${USAGE}
      exit 0
      ;;
    :|?)
      echo -e ${USAGE}
      exit 1
      ;;
  esac
done

if [ "${ENVIRONMENT}" != "local" ] && [ "${ENVIRONMENT}" != "ci" ]; then
  echo -e $USAGE
  exit 1
fi


# Run the tests as though it were a CI/CD pipeline
if [ "${ENVIRONMENT}" == "ci" ]; then

  # Build the Docker image.
  docker build -t python-test-db:1.0 -f ./db/ci.dockerfile .

  # Run the tests
  docker run --rm -v $(pwd):/app python-test-db:1.0 /app/_run_tests.sh
else
  if [ "${DB_PASSWORD}" == "" ]; then
    echo "The environment variable DB_PASSWORD is undefined. This may cause errors."
  fi

  # Run the tests
  pytest --local-db --postgresql-password=${DB_PASSWORD}
fi