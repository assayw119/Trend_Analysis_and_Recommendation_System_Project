# 이미지 및 텍스트 마이닝을 통한 사용자 분석과 장소 추천 서비스 (Trend Analysis and Recommendation System based on Image and TextMining)
## Project
2022-1 데이터사이언스 캡스톤디자인

## Packages
1. Selenium
2. BeautifulSoup
3. konlpy
4. pandas
5. numpy
6. captum
7. 


## WebPage Dev.

### 실행
1. 경로 설정
```
cd Webpage
```

2. 가상환경 접속
```
pipenv shell
```

3. 라이브러리 설치
```
pip install -r requirements.txt
```

4. 프로젝트 경로 이동
```
cd myproject
```

5. database 설정

- 기본 세팅
https://heroeswillnotdie.tistory.com/16

- myproject/main/database.py 생성 (중괄호 부분 수정할 것)
```Python
## database.py
from sqlalchemy import create_engine
import pymysql
import pandas as pd

db = pymysql.connect(host='{퍼블릭 IPv4 주소}', user='root', password='{password}',
                    db='{DB명}', charset='utf8mb4')

# localhost에 적용할 경우
# db = pymysql.connect(host='localhost', user='root', password='{password}',
#                     db='{DB명}', charset='utf8mb4')

cursor = db.cursor()
db.commit()

data = pd.read_csv('./main/data/data.csv', encoding='utf-8', index_col=0)

# utfmb48로 이모티콘 등의 문자 인식되지 않는 것 해결
engine = create_engine('mysql+pymysql://root:{password}@{퍼블릭 IPv4 주소}:3306/{DB명}?charset=utf8mb4')
# engine = create_engine('mysql+pymysql://root:{password}@localhost:3306/{DB명}?charset=utf8mb4')

conn = engine.connect()
data.to_sql(name='data', con=engine, if_exists='replace', index=False)
conn.close()

class Database():
    def __init__(self):
        self.db = pymysql.connect(
                                host='{퍼블릭 IPv4 주소}',
                                # host='localhost'
                                user='root',
                                password='{password}',
                                db='{DB명}',
                                charset='utf8'
                                )
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
```

6. migrate
```
python manage.py makemigrations
python manage.py migrate
```

7. runserver
```
python manage.py runserver
```

### 결과

- AWS EC2 배포 결과 : http://mudsil.com/

<img width="1375" alt="image" src="https://user-images.githubusercontent.com/87521259/180601272-94f6b0eb-198a-45aa-943c-1d17c6562f4a.png">
<img width="1372" alt="스크린샷 2022-07-23 오후 7 24 57" src="https://user-images.githubusercontent.com/87521259/180601288-82a6820b-76e5-4419-87e6-ac6e194cde07.png">
<img width="1368" alt="스크린샷 2022-07-23 오후 7 25 20" src="https://user-images.githubusercontent.com/87521259/180601296-1dfb975d-9e8f-411b-b5ab-142019d37bd4.png">

- 2022 데이터사이언스 캡스톤디자인 1등
