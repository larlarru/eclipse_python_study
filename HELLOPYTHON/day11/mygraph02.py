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


mm = MyManager()

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.array([0,1,2,3,4,5])
y = np.array([0,1,2,3,4,5])
z1 = np.array(mm.getPrices("삼성전자"))
z1 = np.array(mm.getPrices("LG"))
z1 = np.array(mm.getPrices("SK"))

ax.plot(x, y, z1)
ax.plot(x+1, y, z1)
ax.plot(x+2, y, z1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

print("x :",x)
print("y :",y)
print("z1 :",z1)

plt.show()

