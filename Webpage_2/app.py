from flask import Flask, render_template, jsonify, request, url_for
import pymysql
import pandas as pd
from flask_paginate import Pagination, get_page_args

app = Flask(__name__)

db = pymysql.connect(host='localhost', user='root', password='qwedsa2249',
                        db='test', charset='utf8')
cursor = db.cursor(pymysql.cursors.DictCursor)

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('01_inflow_page.html')

@app.route('/result/')
def result():
   page = request.args.get('page', 1, type=int)

   limit = 10
   sql = 'select * from chungmuro;'
   cursor.execute(sql)
   datas_dict = cursor.fetchall()

   datas = pd.DataFrame(datas_dict)

   total_cnt = len(datas)
   total_page = round(total_cnt / limit)

   block_size = 5
   block_num = int((page-1) / block_size)
   block_start = (block_size * block_num) + 1
   block_end = block_start + (block_size - 1)
   print(block_start, block_end)

   return render_template('02_result_page.html',
                          datas = datas,
                          limit = limit,
                          page = page,
                          block_start = block_start,
                          block_end = block_end,
                          total_page = total_page,)

@app.route('/detail/<address>/<cluster>/<type>')
def search(address, cluster, food_type):
   return render_template('03_detail_page.html', address=address, cluster=cluster, food_type=food_type)

@app.route('/detail')
def detail():
   return render_template('03_detail_page.html')


@app.route('/resultdata', methods=['GET'])
def select():


   # count_sql = 'select count(*) from chungmuro'
   # cursor.execute(count_sql)
   # total_cnt = cursor.fetchall()
   # print(total_cnt[0][0])
   # total_page = round(total_cnt / per_page)

   sql2 = 'select * from chungmuro;'
   cursor.execute(sql2)
   row2 = cursor.fetchall()


   # print(row)
   return jsonify({'data':row2})

# @app.route('/resultdata', method=['POST'])
# Default setting
# pageLimit = 10



if __name__ == '__main__':
   app.run('0.0.0.0',port=5001,debug=True)
