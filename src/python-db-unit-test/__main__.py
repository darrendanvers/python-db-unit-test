import os
import psycopg

from db_functions import db_func


def main():
    """
    Prints the number of records in the test_table table.
    :return: void
    """
    with psycopg.connect(host='localhost', dbname='python-test-db-local', user=os.environ['DB_USER'],
                         password=os.environ['DB_PASSWORD']) as conn:
        print(db_func(conn))


if __name__ == "__main__":
    main()
