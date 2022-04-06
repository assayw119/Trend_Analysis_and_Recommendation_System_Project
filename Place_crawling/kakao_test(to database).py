import certifi
from selenium import webdriver

# from models.information import Information
from pymongo import MongoClient
from config import MONGO_URL
from kakao_search_restaurant_url import kakao_restaurant  # 지역별 음식점의 링크 가져오기
from kakao_inform_restaurant import (
    kakao_inform_restaurant,
)  # 네이버 플레이스에서 음식점에 대한 정보 가져오기

# from image_crawling import total_img_list_func  # 이미지 크롤링 후 리스트 가져오기

if __name__ == "__main__":

    ca = certifi.where()
    client = MongoClient(MONGO_URL, tlsCAFile=ca)
    # client = MongoClient('localhost', 27017)

    db = client["test"]
    # print(db)
    urls = kakao_restaurant("충무로", 15)  # 개수는 15의 배수로 적어주세요
    # df = pd.DataFrame(columns=["이름", "분류", "분위기(테마키워드)", "주요 메뉴", "평균 가격", "평점", "리뷰 수"])

    for url in urls[:2]:

        result = kakao_inform_restaurant(url)
        info = {
            "name": result["name"],
            "address": result["address"],
            "sort": result["sort"],
            "menu": result["main_menu"],
            "mean_price": result["mean_price"],
            "score": float(result["score"]),
            "people_give_score": result["people_give_score"],
            "review_count": int(result["review_count"]),
            "review_list": result["review_list"],
        }

        dpInsert = db.inform.insert_one(info)  # db에 정보 입력
        # df = pd.concat([df, pd.DataFrame(result)], ignore_index=False)
    print("finish!")
