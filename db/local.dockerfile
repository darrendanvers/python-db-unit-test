# PostreSQL database
FROM postgres:latest

# Copy the files that PostgreSQL will run
# to create the schema and load sample data.
COPY db/seed/* /docker-entrypoint-initdb.d/