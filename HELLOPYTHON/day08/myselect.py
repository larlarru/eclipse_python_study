import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='java', db='python', charset='utf8')

cursor = conn.cursor()

sql = "SELECT * FROM sample"
cursor.execute(sql)

result = cursor.fetchall()

print(result)

conn.close()
