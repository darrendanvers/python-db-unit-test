# Python unit tests that use a PostgreSQL database

This is an experiment in creating unit tests in Python against a [PostgreSQL](https://www.postgresql.org) database without mocking. 
It takes advantage of the [pytest-postgresql](https://pypi.org/project/pytest-postgresql/) package.

It creates a container based on the [PostgreSQL base container](https://hub.docker.com/_/postgres) with all
the files need to run the unit test for a simple application.

I am not experienced with Python, so anyone seeing this will need to forgive any stylistic mistakes and take this
for what it is, me playing around.

## Setup

You will need to have [Docker](https://www.docker.com) installed.

In addition, the code relies on setting two environment variables:

- DB_USER: the user ID to use to connect to the PostgreSQL database.
- DB_PASSWORD: the password of the user who will connect to the PostgreSQL database.

To simplify this example, I use the default PostreSQL admin user.

## Running

This setup allows for supporting multiple modes of development.

### Local development

For local development where you want to spin up the application and run it, there is a script to build a PostgreSQL container and
seed it with tables and data. To run this, type:

```shell
./run_db.sh
```

### Local Pytest

You can run Pytest tests locally against this database by running the command:

```shell
./run_tests.sh -e local
```

This will create a temporary schema in the DB, use the same seed scripts mentioned above, run your tests against the new schema,
and tear the schema down.

### CI/CD Pytest

The final mode is meant to emulate running your tests in a CI/CD pipeline. It constructs a new image with
PostgreSQL and Python installed, starts the container with the repository as a mount, and runs the tests against
a PostgreSQL instance in the container. To run this, type:

```shell
./run_tests.sh -e ci
```

## References

- [https://pypi.org/project/pytest-postgresql/](https://pypi.org/project/pytest-postgresql/)
- [https://www.psycopg.org/psycopg3/docs/](https://www.psycopg.org/psycopg3/docs/)
- [https://docs.pytest.org/en/stable/how-to/fixtures.html](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [https://mingzhi2.medium.com/how-to-create-a-test-database-pytest-pytest-postgresql-sqlalchemy-77f814b57b10](https://mingzhi2.medium.com/how-to-create-a-test-database-pytest-pytest-postgresql-sqlalchemy-77f814b57b10)
- [https://pytest-with-eric.com/pytest-advanced/pytest-addoption/](https://pytest-with-eric.com/pytest-advanced/pytest-addoption/)
- [https://stackoverflow.com/questions/43172467/pytest-how-to-access-command-line-arguments-outside-of-a-test](https://stackoverflow.com/questions/43172467/pytest-how-to-access-command-line-arguments-outside-of-a-test)