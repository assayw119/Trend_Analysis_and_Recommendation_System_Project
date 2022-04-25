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
def result():
   return render_template('02_result_page.html')

@app.route('/resultdata', methods=['GET'])
def select():
   # db_class = db_connect.Database()
   #
   # sql = 'SELECT name FROM test'
   # row = db_class.executeAll(sql)

   db = pymysql.connect(host='localhost', user='root', password='qwedsa2249',
                        db='test', charset='utf8')
   cursor = db.cursor()
   # db.commit()
   # engine = create_engine('mysql+pymysql://root:qwedsa2249@localhost:3306/test?charset=utf8', encoding='utf-8')
   # utf8로 이모티콘 등의 문자 인식되지 않는 것 해결 필요

   # conn = engine.connect()
   # df_name.to_sql(name='chungmuro', con=engine, if_exists='replace', index=False)
   # conn.close()

   sql = 'select * from chungmuro'
   # row = pd.read_sql(sql, db)
   cursor.execute(sql)
   row = cursor.fetchall()
   # print(row)
   return jsonify({'data':row})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5001,debug=True)