from flask import Flask
from flask import request
from flask import Flask, render_template
import pymysql

app = Flask(__name__) ## Flask instance를 만들어주고.

@app.route('/') ## URL, 이 경우 localhost:5000/
def index():
    return 'Hello, Flask'

@app.route('/param', methods=['GET','POST'])
def param():
    if request.method == "POST":
        name = request.form.get("name", "kimchulsu")
    if request.method == "GET":
        name = request.args.get("name", "kimchulsu")
#     name = request.args.get('name',"user01")
#     name = "hahaha"
    return 'param='+name

@app.route('/forward.do') 
def forward():
    title = "Good morning"
    return render_template('foward.html',title=title)

@app.route('/db.do') 
def db():
#     s_code db select -> 화면에 뿌려주기
    conn = pymysql.connect(host='localhost', user='root', passwd='java', db='python', charset='utf8')
    curs = conn.cursor()
    sql = "SELECT s_code, s_name, s_price, in_time FROM stock order by in_time desc"
    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()
    print("조회완료")
    return render_template('foward.html', rows=rows)

if __name__ == "__main__":
    app.run()