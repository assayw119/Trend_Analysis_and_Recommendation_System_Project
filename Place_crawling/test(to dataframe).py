
import certifi

from pymongo import MongoClient
import pandas as pd
from config import MONGO_URL
from search_restaurant_url import restaurant # 지역별 음식점의 링크 가져오기 
from inform_restaurant import inform_restaurant #네이버 플레이스에서 음식점에 대한 정보 가져오기 

if __name__ == "__main__":

    ca = certifi.where()
    client = MongoClient(MONGO_URL, tlsCAFile=ca)

    db = client["test"]
    # print(db)
    urls = restaurant("충무로", 1)  # 3*n개의 url이 나옴
    df = pd.DataFrame(columns=["이름", "분류", "분위기(테마키워드)", "주요 메뉴", "평균 가격", "평점", "리뷰 수"])
    for url in urls:

        result = inform_restaurant(url)


        df = pd.concat([df, pd.DataFrame(result)], ignore_index=False)
    print(df)
    print("finish!")
 
