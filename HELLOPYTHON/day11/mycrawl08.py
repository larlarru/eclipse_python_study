import pymysql
import time
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PyQt5.QtCore import QDate, Qt

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='java', db='python', charset='utf8')
cursor = conn.cursor()


cnt=0
while True:
    
    html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php")
    bs = BeautifulSoup(html, "html.parser")
    tds = bs.select(".st2");
    now = datetime.datetime.now()
    in_time = now.strftime("%Y%m%d,%H%M")
    for td in tds :
        s_code = td.find(["a"]).get("title")
        s_name = td.text
        s_price = td.parent.select("td")[1].text
        cursor = conn.cursor()
        s_price = s_price.replace(",","")
        sql = "insert into stock values('"+s_code+"','"+s_name+"','"+s_price+"','"+in_time+"')"
        cursor.execute(sql)
        
    conn.commit()
    cnt+=1
    time.sleep(60)
    print("ok",cnt)
    if cnt > 5:
        break
    
    
conn.close()
