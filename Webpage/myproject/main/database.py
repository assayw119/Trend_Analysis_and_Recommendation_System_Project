from sqlalchemy import create_engine
import pymysql
import pandas as pd

db = pymysql.connect(host='52.78.234.97', user='root', password='qwedsa2249',
                    db='capston', charset='utf8mb4')
cursor = db.cursor()
db.commit()

data = pd.read_csv('./main/data/data.csv', encoding='utf-8', index_col=0)

engine = create_engine('mysql+pymysql://root:qwedsa2249@52.78.234.97:3306/capston?charset=utf8mb4')
# utf8로 이모티콘 등의 문자 인식되지 않는 것 해결

conn = engine.connect()
data.to_sql(name='data', con=engine, if_exists='replace', index=False)
conn.close()

# sql = 'SELECT * FROM demo'
# cursor.execute(sql)
# data_list = cursor.fetchall()
# print(data_list)

class Database():
    def __init__(self):
        self.db = pymysql.connect(host='52.78.234.97',
                                # host='localhost'
                                user='root',
                                password='qwedsa2249',
                                db='capston',
                                charset='utf8')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()