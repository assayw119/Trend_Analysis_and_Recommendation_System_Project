from flask import Flask, render_template, jsonify
import pymysql

app = Flask(__name__)


## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('01_inflow_page.html')

@app.route('/result')
def result():
   return render_template('02_result_page.html')

@app.route('/resultdata', methods=['GET'])
def select():

   db = pymysql.connect(host='localhost', user='root', password='qwedsa2249',
                        db='test', charset='utf8')
   cursor = db.cursor()

   sql = 'select * from chungmuro'
   cursor.execute(sql)
   row = cursor.fetchall()
   # print(row)
   return jsonify({'data':row})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5001,debug=True)
