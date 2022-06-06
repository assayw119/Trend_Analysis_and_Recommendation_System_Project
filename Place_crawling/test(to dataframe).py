import time
from selenium import webdriver
import pandas as pd
from search_restaurant_url import restaurant  # 지역별 음식점의 링크 가져오기
from inform_restaurant import inform_restaurant  # 네이버 플레이스에서 음식점에 대한 정보 가져오기
from naver_reviews import naver_reviews_list  # 네이버 플레이스에서 음식점에 대한 리뷰 가져오기
from image_crawling import image_crawling  # 네이버 플레이스에서 음식점에 대한 이미지 가져오기
import warnings

warnings.filterwarnings("ignore")


def crawling(df, urls, region):

    for idx, url in enumerate(urls):
        # print(url)

        # print(f"{idx}번째 URL")
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
        result["img_food"] = ",".join(img_food)

        img_inner = image_crawling(driver3, url, 5)
        result["img_inner"] = ",".join(img_inner)

        try:
            df = pd.concat([df, pd.DataFrame(result, index=[idx])], ignore_index=False)
        except:
            pass
        e = time.time()
        # print("time for each loop : ", e - s, "s")

    df.to_csv(f"{region}.csv", encoding="utf-8-sig")


def start_crawling(region_df):
    for region in region_df["법정동"]:

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

        crawling(df, urls, region)


def main():

    region_df = pd.read_csv("/Users/seop/Downloads/Report.csv")
    region_df = region_df.drop(index=[0, 1, 2], axis=0)
    start_crawling(region_df[:1])


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start, " second")
