import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='java', db='python', charset='utf8')

cursor = conn.cursor()

sql = "insert into sample values(4, 5, 6)"
cnt = cursor.execute(sql)
print(cnt)
conn.commit()

conn.close()
