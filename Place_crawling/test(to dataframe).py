import time
from selenium import webdriver
import logging
from selenium.webdriver.remote.remote_connection import LOGGER

import pandas as pd
from config import MONGO_URL
from search_restaurant_url import restaurant  # 지역별 음식점의 링크 가져오기
from inform_restaurant import inform_restaurant  # 네이버 플레이스에서 음식점에 대한 정보 가져오기
from naver_reviews import naver_reviews_list
from image_crawling import image_crawling
import warnings

warnings.filterwarnings("ignore")
if __name__ == "__main__":
    region_df = pd.read_csv("/Users/seop/Downloads/Report.csv")

    region_df = region_df.drop(0, axis=0)
    region_df = region_df.drop(1, axis=0)
    region_df = region_df.drop(2, axis=0)

    i = 0
    start = time.time()
    for region in region_df["법정동"][393:]:

        s2 = time.time()
        print("현재 지역 :", region)
        urls = restaurant(region, 3)  # 지역, 음식점 갯수
        df = pd.DataFrame(
            columns=[
                "name",
                "address",
                "sort",
                "menu",
                "mean_price",
                "score",
                "people_give_score",
                "review_count",
                "review_list",
                "img_food",
                "img_inner",
            ]
        )
        error = []
        dong = []
        for idx, url in enumerate(urls):

            print(f"{idx}번째 URL")
            s = time.time()
            result = inform_restaurant(url)
            options = webdriver.ChromeOptions()

            # 창 숨기는 옵션 추가
            options.add_argument("headless")

            driver1 = webdriver.Chrome(
                "/Users/seop/Documents/GitHub/Trend_Analysis_and_Recommendation_System_Project/Place_crawling/chromedriver",
                options=options,
            )
            driver1.get(url[:-4] + "review/visitor")
            driver1.implicitly_wait(10)

            driver2 = webdriver.Chrome(
                "/Users/seop/Documents/GitHub/Trend_Analysis_and_Recommendation_System_Project/Place_crawling/chromedriver",
                options=options,
            )
            driver2.get(url[:-4] + "photo?filterType=음식")
            driver2.implicitly_wait(10)

            driver3 = webdriver.Chrome(
                "/Users/seop/Documents/GitHub/Trend_Analysis_and_Recommendation_System_Project/Place_crawling/chromedriver",
                options=options,
            )
            driver3.get(url[:-4] + "photo?filterType=내부")
            driver3.implicitly_wait(10)

            review_list = naver_reviews_list(driver1, url, 50)
            result["review_list"] = "/".join(review_list)

            img_food = image_crawling(driver2, url, 5)
            #     print('img_food :',img_food)
            result["img_food"] = ",".join(img_food)

            img_inner = image_crawling(driver3, url, 5)
            result["img_inner"] = ",".join(img_inner)

            try:

                df = pd.concat(
                    [df, pd.DataFrame(result, index=[idx])], ignore_index=False
                )
            except:
                error.append(url)
            e = time.time()
            print("time for each loop : ", e - s, "s")

        e2 = time.time()

        df.to_csv(f"{region}.csv", encoding="utf-8-sig")

    end = time.time()
    print("total running time :", end - start, "sec")
