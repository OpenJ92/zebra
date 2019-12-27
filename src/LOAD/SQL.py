from snowflake.connector import connect
from pandas import read_sql

class snowflake(object):
    def __init__(self, account, user, password,          \
                     database, warehouse, schema):
        self._conn = connect(account=account, user=user, \
                password=password, database=database,    \
                warehouse=warehouse, schema=schema)

    def __call__(self, sql):
        return read_sql(sql=sql, con=self._conn)
