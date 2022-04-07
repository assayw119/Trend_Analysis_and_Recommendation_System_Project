import certifi
import time
from selenium import webdriver
from pymongo import MongoClient
import pandas as pd
from config import MONGO_URL
from search_restaurant_url import restaurant  # 지역별 음식점의 링크 가져오기
from inform_restaurant import inform_restaurant  # 네이버 플레이스에서 음식점에 대한 정보 가져오기
from reviews import naver_reviews_list
from image_crawling import image_crawling

if __name__ == "__main__":

    # ca = certifi.where()
    # client = MongoClient(MONGO_URL, tlsCAFile=ca)

    # db = client["test"]
    # print(db)
    urls = restaurant("충무로", 5)  # 지역, 음식점 갯수
df = pd.DataFrame(
    columns=[
        "name",
        "sort",
        "menu",
        "mean_price",
        "score",
        "people_give_score",
        "review_count",
        "reivew_list",
        "img_food",
        "img_inner",
    ]
)
error = []
start = time.time()
for url in urls:

    result = inform_restaurant(url)
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")
    driver1 = webdriver.Chrome(
        "/Users/seop/파이썬/아아아하기싫어/chromedriver_mac64_m1 (4)/chromedriver",
        options=options,
    )
    driver1.get(url[:-4] + "review/visitor")
    driver1.implicitly_wait(5)

    driver2 = webdriver.Chrome(
        "/Users/seop/파이썬/아아아하기싫어/chromedriver_mac64_m1 (4)/chromedriver",
        options=options,
    )
    driver2.get(url[:-4] + "photo?filterType=음식")
    driver2.implicitly_wait(5)

    driver3 = webdriver.Chrome(
        "/Users/seop/파이썬/아아아하기싫어/chromedriver_mac64_m1 (4)/chromedriver",
        options=options,
    )
    driver3.get(url[:-4] + "photo?filterType=내부")
    driver3.implicitly_wait(5)

    review_list = naver_reviews_list(driver1, url, 50)
    result["reivew_list"] = ",".join(review_list)

    img_food = image_crawling(driver2, url, 30)
    #     print('img_food :',img_food)
    result["img_food"] = img_food

    img_inner = image_crawling(driver3, url, 30)
    result["img_inner"] = img_inner

    try:
        df = pd.concat([df, pd.DataFrame(result)], ignore_index=False)
    except:
        error.append(url)

end = time.time()
print("총 러닝 타임 : ", end - start)
