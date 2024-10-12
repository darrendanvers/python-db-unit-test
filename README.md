# Python unit tests that use a PostgreSQL database

This is an experiment in creating unit tests in Python against a [PostgreSQL](https://www.postgresql.org) database without mocking. 
It takes advantage of the [pytest-postgresql](https://pypi.org/project/pytest-postgresql/) package.

It creates a container based on the [PostgreSQL base container](https://hub.docker.com/_/postgres) with all
the files need to run the unit test for a simple application.

I am not experienced with Python, so anyone seeing this will need to forgive any stylistic mistakes and take this
for what it is, me playing around.

## Setup

You will need to have [Docker](https://www.docker.com) installed.

## Running

```shell
./run_tests.sh
```
## References

- [https://pypi.org/project/pytest-postgresql/](https://pypi.org/project/pytest-postgresql/)
- [https://www.psycopg.org/psycopg3/docs/](https://www.psycopg.org/psycopg3/docs/)
- [https://docs.pytest.org/en/stable/how-to/fixtures.html](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [https://mingzhi2.medium.com/how-to-create-a-test-database-pytest-pytest-postgresql-sqlalchemy-77f814b57b10](https://mingzhi2.medium.com/how-to-create-a-test-database-pytest-pytest-postgresql-sqlalchemy-77f814b57b10)