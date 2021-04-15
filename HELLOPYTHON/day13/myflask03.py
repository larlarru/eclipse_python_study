from flask import Flask, Response, jsonify, render_template
from flask import request, json
import pymysql
import logging

mylogger = logging.getLogger("my")
mylogger.setLevel(logging.DEBUG)
    
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
stream_hander = logging.StreamHandler()
stream_hander.setFormatter(formatter)
mylogger.addHandler(stream_hander)
    
file_handler = logging.FileHandler('my.log')
file_handler.setFormatter(formatter)
mylogger.addHandler(file_handler)


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask"

@app.route("/param", methods=['GET','POST'])
def param():
    mylogger.debug("param 진입")
    if request.method == "POST":
        name = request.form.get('name', "kimchulsu")
        mylogger.debug("param POST")
    if request.method == "GET":
        mylogger.debug("param GET")
        name = request.args.get('name', "kimchulsu")  
    return "param="+name

@app.route("/forward.do")
def forward():
    mylogger.debug("forward 진입")
    title = "Good Morning"
    return render_template('forward.html',title=title)

@app.route("/db.do")
def db():
    mylogger.debug("db 진입")
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    curs.execute("select emp_id,emp_name,nickname from emp")
    mylogger.debug("db 실행")
    rows = curs.fetchall()
    conn.close()
    mylogger.debug("db 실행 종료")
    print(rows)
    mylogger.debug("db 값 return")
    return render_template('db.html',title="good",list=[1,2,3],db_list=rows)

@app.route('/upd.ajax')
def ajax_upd():
    mylogger.debug("ajax_upd 진입")
    emp_id      = request.args.get('emp_id') 
    emp_name    = request.args.get('emp_name')  
    nickname    = request.args.get('nickname')   
    print("emp_id",emp_id)
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    mylogger.debug("db 진입")
    curs = conn.cursor()
    cnt = curs.execute("update emp set emp_name='"+emp_name+"', nickname='"+nickname+"' where emp_id='"+emp_id+"'")
    mylogger.debug("db 실행")
    conn.commit()
    conn.close()
    mylogger.debug("db 종료")
    obj = {'cnt':cnt}
    json_return=json.dumps(obj)
    return jsonify(json_return)

@app.route('/del.ajax')
def ajax_del():
    mylogger.debug("ajax_del 진입")
    emp_id      = request.args.get('emp_id') 
    print("emp_id",emp_id)
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    mylogger.debug("ajax_del db 진입")
    cnt = curs.execute("DELETE FROM emp WHERE emp_id='"+emp_id+"'")
    mylogger.debug("ajax_del db 실행")
    conn.commit()
    conn.close()
    mylogger.debug("ajax_del db 종료")
    obj = {'cnt':cnt}
    json_return=json.dumps(obj)
    return jsonify(json_return)

@app.route('/ins.ajax')
def ajax_ins():
    mylogger.debug("ajax_ins 진입")
    emp_name    = request.args.get('emp_name')  
    nickname    = request.args.get('nickname')   
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    mylogger.debug("ajax_ins db 진입")
    curs = conn.cursor()
    cnt = curs.execute("INSERT INTO emp(emp_name,nickname) VALUES('"+emp_name+"','"+nickname+"')")
    mylogger.debug("ajax_ins db 실행")
    conn.commit()
    conn.close()
    mylogger.debug("ajax_ins db 종료")
    obj = {'cnt':cnt}
    json_return=json.dumps(obj)
    return jsonify(json_return)


if __name__ == "__main__":
    app.run()