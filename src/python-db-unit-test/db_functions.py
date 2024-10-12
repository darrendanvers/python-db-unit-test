def db_func(db_connection):
    """
    Returns a count of the number of records in the test_table table.
    :param db_connection: The connection to the database.
    :return: The number of rows in the test_table table.
    """
    with db_connection.cursor() as cur:
        cur.execute('SELECT count(*) from test_table')
        return cur.fetchone()[0]
