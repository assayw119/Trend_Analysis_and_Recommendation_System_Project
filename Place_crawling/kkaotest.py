import time
from selenium import webdriver
import pandas as pd
from kakao_search_restaurant_url import kakao_restaurant  # 지역별 음식점의 링크 가져오기
from kakao_inform_restaurant import kakao_inform_restaurant
import numpy as np
import os
import glob


if __name__ == "__main__":

    road = "/Users/seop/Documents/GitHub/Trend_Analysis_and_Recommendation_System_Project/Region/naver"
    road_2 = "/Users/seop/Documents/GitHub/Trend_Analysis_and_Recommendation_System_Project/Region/new_region/"
    region_df = glob.glob(os.path.join(road, "*.csv"))

    for region in region_df:
        cnt = 1

        dong = region.replace(".csv", "").split("/")[-1]
        region = pd.read_csv(region)
        print(dong)

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
            ]
        )

        s = time.time()

        for re in region["name"]:
            print("cnt", cnt)
            if cnt == 5:
                break
            print(re)
            urls = kakao_restaurant(dong + " " + re, 15)

            for url in urls[:1]:
                print(url)
                result = kakao_inform_restaurant(url)
                if not result["review_list"]:
                    break
                info = {
                    "name": result["name"],
                    "address": result["address"],
                    "sort": result["sort"],
                    "menu": result["main_menu"],
                    "mean_price": result["mean_price"],
                    "score": float(result["score"]),
                    "people_give_score": result["people_give_score"],
                    "review_count": int(result["review_count"]),
                    "review_list": "/".join(result["review_list"]),
                }

                df = pd.concat(
                    [df, pd.DataFrame(info, index=[cnt])], ignore_index=False
                )
                cnt += 1
        df.to_csv(road_2 + f"{dong}_2.csv", encoding="utf-8-sig")

        e = time.time()
        print("1 region learning time : ", e - s, "s")
