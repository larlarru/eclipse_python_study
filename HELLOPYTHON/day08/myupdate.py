import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='java', db='python', charset='utf8')

cursor = conn.cursor()

sql = "update sample set col01 = 4 where col01 = 1 and col02 = 5"
cursor.execute(sql)

conn.commit()

conn.close()
