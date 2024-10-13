import psycopg

from db_functions import db_func
from pytest_postgresql import factories

# Construct a feature that allows connecting to PostgreSQL.
# postgresql_host is defined in confgest.py
posgresql_conn = factories.postgresql('postgresql_host')


# This test will pass.
def test_db_func_returns_correct_number_of_records(posgresql_conn):
    with psycopg.connect(host=posgresql_conn.info.host, dbname=posgresql_conn.info.dbname,
                         user=posgresql_conn.info.user,
                         password=posgresql_conn.info.password) as conn:
        assert db_func(conn) == 2


# This test will fail.
def test_db_func_test_will_fail(posgresql_conn):
    with psycopg.connect(host=posgresql_conn.info.host, dbname=posgresql_conn.info.dbname,
                         user=posgresql_conn.info.user,
                         password=posgresql_conn.info.password) as conn:
        assert db_func(conn) == 3
