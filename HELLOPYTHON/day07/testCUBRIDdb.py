import CUBRIDdb

conn = CUBRIDdb.connect('CUBRID:localhost:8001:dba::')

cur = conn.cursor()
cur.execute("SELECT * FROM db_user")
conn.commit()
