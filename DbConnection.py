from sqlalchemy import create_engine
from sqlalchemy.engine.mock import MockConnection

conn = MockConnection
try:
    conn = create_engine('mysql+pymysql://ahmed:123456@localhost/testDb')
    print("MySQL Connection Sucessfull!!!!!!!!!!!")

except Exception as err:

    print("MySQL Connection Failed !!!!!!!!!!!")
    print(err)
