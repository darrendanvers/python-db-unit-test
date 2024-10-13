# PostreSQL database
FROM postgres:latest

#
# Install Python
#
RUN apt-get update && apt-get install -y python3 python3.11-venv python3-pip

# Dependencies
COPY requirements.txt /requirements.txt

#
# Need to be in Bash to run source.
#
SHELL ["/bin/bash", "-c"]

#
# Configure the Python environment
#
RUN python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

#
# Cannot be root to run PostgreSQL
#
USER postgres

WORKDIR /app
