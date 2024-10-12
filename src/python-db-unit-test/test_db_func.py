from pathlib import Path
import psycopg
from db_functions import db_func
from pytest_postgresql import factories

# Spins up an instance of PostreSQL in the container and connects to it.
postgresql_my_proc = (
    factories.postgresql_proc(executable='/usr/lib/postgresql/17/bin/pg_ctl', host='127.0.0.1',
                              dbname='python_db_unit_test', port='5432',
                              load=[Path('/app/db/seed/100-schema.sql'), Path('/app/db/seed/200-data.sql')]))
postgresql = factories.postgresql('postgresql_my_proc')


# This test will pass.
def test_db_func_returns_correct_number_of_records(postgresql):
    with psycopg.connect(host=postgresql.info.host, dbname=postgresql.info.dbname, user=postgresql.info.user,
                         password=postgresql.info.password) as conn:
        assert db_func(conn) == 2


# This test will fail.
def test_db_func_test_will_fail(postgresql):
    with psycopg.connect(host=postgresql.info.host, dbname=postgresql.info.dbname, user=postgresql.info.user,
                         password=postgresql.info.password) as conn:
        assert db_func(conn) == 3
