import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pymysql

class MyManager:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', passwd='java', db='python', charset='utf8')
        self.curs = self.conn.cursor()
        
    def __del__(self):
        self.conn.close()
    
    def getName(self):
        sql = "SELECT s_name FROM stock groud order by in_time desc"
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        
        
        names = []
        print(rows)
        for row in rows:
            names.append(row[0])
            print(row[0])
        return names
    
    def getPrices(self,s_name):
        sql = "SELECT s_price FROM stock where s_name = '"+s_name+"' order by in_time desc"
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        
        
        prices = []
        print(rows)
        for row in rows:
            prices.append(row[0])
            print(row[0])
        return prices
    
    def getPricesPer(self,s_name):
        sql = "SELECT s_price FROM stock where s_name = '"+s_name+"' order by in_time"
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        
        
        prices = []
        p_intit = 0
        for idx, row in enumerate(rows):
            if idx == 0:
                p_intit = row[0]
            prices.append((row[0]/p_intit)*100)
        return prices
    
    def getCount(self,s_name):
        sql = "SELECT count(s_code) FROM stock where s_name = '"+s_name+"' order by in_time"
        rows = self.curs.execute(sql)
#         rows = self.curs.fetchall()
        return rows
    

mm = MyManager()

fig = plt.figure()
ax = fig.gca(projection='3d')

xindex =[]

for i in range(mm.getCount("삼성전자")):
    xindex = i
print(xindex)
x = np.array(xindex)
y = np.array(xindex)
# y = np.array([0,1,2,3,4,5])
z1 = np.array(mm.getPricesPer("삼성전자"))
# z1 = np.array(mm.getPricesPer("LG"))
# z1 = np.array(mm.getPricesPer("SK"))

ax.plot(x, y, z1)
# ax.plot(x+1, y, z1)
# ax.plot(x+2, y, z1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# plt.show()

