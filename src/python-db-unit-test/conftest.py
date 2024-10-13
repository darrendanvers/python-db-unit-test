from pytest_postgresql import factories
from pathlib import Path


# Add a Pytest command-line option that indicates if the database is running on the local machine. If not,
# then the application assumes the code is running in the same machine as the PostgreSQL installation and
# will start it directly.
def pytest_addoption(parser):
    parser.addoption('--local-db', action='store_true', default=False,
                     help='Set to true when running tests against a running instance of PostgreSQL.')


# Configure how to connect to PostgreSQL. I attempted to do this without a global variable, but
# could not get access to the command line option outside a test or fixture config. I also attempted
# to use a fixture, but could not delegate to the pytest-postgresql fixtures from inside my fixture.
postgresql_host = None


def pytest_configure(config):
    global postgresql_host
    pytest_use_local_db = config.getoption('--local-db')
    if pytest_use_local_db:
        # Using a locally running DB.
        postgresql_host = factories.postgresql_noproc(host='127.0.0.1',
                                                      dbname='python_db_unit_test',
                                                      port='5432',
                                                      load=[Path('./db/seed/100-schema.sql'),
                                                            Path('./db/seed/200-data.sql')])
    else:
        # Start up a DB in the same container the tests are running in.
        postgresql_host = factories.postgresql_proc(executable='/usr/lib/postgresql/17/bin/pg_ctl',
                                                    host='127.0.0.1',
                                                    dbname='python_db_unit_test',
                                                    port='5432',
                                                    load=[Path('/app/db/seed/100-schema.sql'),
                                                          Path('/app/db/seed/200-data.sql')])
