import pandas as pd
from sqlalchemy import create_engine
import pymysql

db = pymysql.connect(host='localhost', user='root', password='qwedsa2249',
                     db='test', charset='utf8mb4')
cursor = db.cursor()
db.commit()

data = pd.read_csv('./data/충무로.csv', encoding='utf-8', index_col=0)
# name = data['name']
# address = data['address']
# sort = data['sort']
# menu = data['menu']
# mean_price = data['mean_price']
# score = data['score']
# people_give_score = data['people_give_score']
# review_count = data['review_count']
# review_list = data['review_list']
# img_food = data['img_food']
# img_inner = data['img_inner']

engine = create_engine('mysql+pymysql://root:qwedsa2249@localhost:3306/test?charset=utf8mb4')
# utf8로 이모티콘 등의 문자 인식되지 않는 것 해결 필요

conn = engine.connect()
data.to_sql(name='chungmuro', con=engine, if_exists='replace', index=False)
conn.close()

# sql = 'select * from chungmuro limit 5'
# sql_test = pd.read_sql(sql, db)
# print(sql_test)

sql = 'SELECT * FROM chungmuro'
cursor.execute(sql)
data_list = cursor.fetchall()
print(data_list)

# for i in data_list:
#     print(i[0])