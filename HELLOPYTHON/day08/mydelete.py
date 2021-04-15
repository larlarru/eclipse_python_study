import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='java', db='python', charset='utf8')

cursor = conn.cursor()

# sql = "delete from sample where col01 = 1"
sql = "delete from sample"
cnt = cursor.execute(sql)
print("cnt :", cnt)

conn.commit()

conn.close()
