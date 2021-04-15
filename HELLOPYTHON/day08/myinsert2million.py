import pymysql
import time

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='java', db='python', charset='utf8')

cursor = conn.cursor()

start = time.time()

cnt = 0 
for i in range(100000):
    sql = 'insert into sample values(%s,%s,%s)'
    cnt += cursor.execute(sql,(i,i,i))
    print("cnt :",cnt)
    
conn.commit()

conn.close()
end = time.time()
print("cnt :",cnt)
print("start :",start)
print("end :",end)
print("end - start :",end - start)
