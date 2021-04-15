import pymysql
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PyQt5.QtCore import QDate, Qt

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='java', db='python', charset='utf8')
cursor = conn.cursor()

html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php")
bs = BeautifulSoup(html, "html.parser")

tds = bs.select(".st2");
# tds = bs.select(".st2 > td");

for td in tds :
    cnt=""
#     print(i.text)
    s_code = td.find(["a"]).get("title")
    s_name = td.text
    s_price = td.parent.select("td")[1].text
    print("s_code :",s_code, end=" ")
    print("s_name :", s_name, end=" ")
    print("s_price :",s_price)
    now = QDate.currentDate()
    print(now.toString(Qt.ISODate))
    cursor = conn.cursor()
    s_price = s_price.replace(",","")
    print("s_price :",s_price)
    sql = "insert into stock values('"+s_code+"','"+s_name+"','"+s_price+"','"+now.toString(Qt.ISODate)+"')"
#     sql = "insert into stock values(%s,%s,%s,%s)"
#     cnt += cursor.execute(sql,(s_code,s_name,s_price,now.toString(Qt.ISODate)))
    cursor.execute(sql)
    conn.commit()
    
    conn.close()
