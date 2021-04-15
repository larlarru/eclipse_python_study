import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='java', db='python', charset='utf8')

cursor = conn.cursor()

sql = "SELECT s_name, s_price FROM stock where s_name = '삼성전자' order by in_time desc"
cursor.execute(sql)
cursor.execute(sql)
rows = cursor.fetchall()


names = []
prices = []
print(rows)
for row in rows:
    names.append(row[0])
    print(row[0])
    prices.append(row[1])
    print(row[1])
print("names : ",names)
print("prices : ",prices)
conn.close()
