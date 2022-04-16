from flask import Flask, render_template, jsonify
import pymysql
import db_connect

app = Flask(__name__)

db = pymysql.connect(host='localhost', user='root', password='qwedsa2249',
                     db='test', charset='utf8')
cursor = db.cursor()
db.commit()

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('01_inflow_page.html')

@app.route('/result')
def reuslt():
   return render_template('02_result_page.html')

@app.route('/db', methods=['GET'])
def select():
   db_class = db_connect.Database()

   sql = 'SELECT name FROM test'
   row = db_class.executeAll(sql)

   print(row)
   return jsonify({'data':row})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5001,debug=True)