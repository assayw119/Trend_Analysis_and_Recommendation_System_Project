import time
from selenium import webdriver
import pandas as pd
from kakao_search_restaurant_url import kakao_restaurant  # 지역별 음식점의 링크 가져오기
from kakao_inform_restaurant import kakao_inform_restaurant

# 네이버 플레이스에서 음식점에 대한 정보 가져오기

# from image_crawling import total_img_list_func  # 이미지 크롤링 후 리스트 가져오기

if __name__ == "__main__":

    # print(db)
    region_df = pd.read_csv("/Users/seop/Downloads/Report.csv")
    region_df = region_df.drop(index=[0, 1, 2], axis=0)
    for region in region_df["법정동"]:

        urls = kakao_restaurant(region, 15)  # 개수는 15의 배수로 적어주세요
        # df = pd.DataFrame(columns=["이름", "분류", "분위기(테마키워드)", "주요 메뉴", "평균 가격", "평점", "리뷰 수"])
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

        print("region : ", region)
        s = time.time()
        for idx, url in enumerate(urls[:9]):
            print(f"{idx}번째 URL")
            print(url)
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
                "review_list": "/".join(result["review_list"]),
            }

            df = pd.concat([df, pd.DataFrame(info, index=[idx])], ignore_index=False)
        df.to_csv(f"{region}.csv", encoding="utf-8-sig")
        print(df)
        e = time.time()
        print("1 region learning time : ", e - s, "s")
