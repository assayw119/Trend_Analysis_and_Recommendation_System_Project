import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ProcessPoolExecutor
import os
import threading
import pandas as pd
from naver_reviews import naver_reviews_list
from search_restaurant_url import restaurant
from image_crawling import image_crawling
from inform_restaurant import inform_restaurant
import warnings

warnings.filterwarnings("ignore")

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


def fetch_review(url):
    print(f"{os.getpid()} process | {threading.get_ident()} thread, {url}")
    try:
        driver = webdriver.Chrome(
            "/Users/seop/Documents/GitHub/Trend_Analysis_and_Recommendation_System_Project/Place_crawling/chromedriver",
            chrome_options=chrome_options,
        )
        driver.get(url[:-4] + "review/visitor")
    except:
        print(url, "| HTTP Error 500: Internal Server Error")
    return naver_reviews_list(driver, url, 5)


def fetch_image_food(url):
    # print(f"{os.getpid()} process | {threading.get_ident()} thread, {url}")
    try:
        driver = webdriver.Chrome(
            "/Users/seop/Documents/GitHub/Trend_Analysis_and_Recommendation_System_Project/Place_crawling/chromedriver",
            chrome_options=chrome_options,
        )
        driver.get(url[:-4] + "photo?filterType=음식")
    except:
        print(url, "| HTTP Error 500: Internal Server Error")
    return image_crawling(driver, url, 30)


def fetch_image_inner(url):
    # print(f"{os.getpid()} process | {threading.get_ident()} thread, {url}")
    try:
        driver = webdriver.Chrome(
            "/Users/seop/Documents/GitHub/Trend_Analysis_and_Recommendation_System_Project/Place_crawling/chromedriver",
            chrome_options=chrome_options,
        )
        driver.get(url[:-4] + "photo?filterType=내부")
    except:
        print(url, "| HTTP Error 500: Internal Server Error")
    return image_crawling(driver, url, 30)


def main():
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
        ]
    )

    region_df = pd.read_csv("/Users/seop/Downloads/Report.csv")
    region_df = region_df.drop(index=[0, 1, 2], axis=0)

    for region in region_df["법정동"][:1]:

        print("현재 지역 :", region)
        urls = restaurant(region, 3)

        executor = ProcessPoolExecutor(max_workers=10)

        result_rivew = list(executor.map(fetch_review, urls))
        result_food = list(executor.map(fetch_image_food, urls))
        result_inner = list(executor.map(fetch_image_inner, urls))

        for idx, url in enumerate(urls):
            result_df = inform_restaurant(url)
            df = pd.concat(
                [df, pd.DataFrame(result_df, index=[idx])], ignore_index=False
            )

        result = {}
        result["review_list"] = []
        result["img_food"] = []
        result["img_inner"] = []

        for i, j, k in zip(result_rivew, result_food, result_inner):

            result["review_list"].append(i)
            result["img_food"].append(j)
            result["img_inner"].append(k)

        result_selenium = pd.DataFrame(result)
        df = pd.concat([df, result_selenium], axis=1)
        df.to_csv(f"{region}.csv", encoding="utf-8-sig")

    return df, result_selenium


if __name__ == "__main__":

    start = time.time()
    df, result_selenium = main()
    end = time.time()
    print(end - start, " second")

# 60초
