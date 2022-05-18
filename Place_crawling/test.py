import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import ProcessPoolExecutor
import os
import threading
from selenium.webdriver.chrome.options import Options
import pandas as pd
from naver_reviews import naver_reviews_list
from search_restaurant_url import restaurant
from image_crawling import image_crawling

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


def fetch_review(url):
    print(f"{os.getpid()} process | {threading.get_ident()} thread, {url}")
    driver = webdriver.Chrome(
        "/Users/seop/Documents/GitHub/Python-Concurrency-Programming/exercise/chromedriver",
        chrome_options=chrome_options,
    )
    driver.get(url[:-4] + "review/visitor")

    return naver_reviews_list(driver, url, 5)


def fetch_image_food(url):
    print(f"{os.getpid()} process | {threading.get_ident()} thread, {url}")
    driver = webdriver.Chrome(
        "/Users/seop/Documents/GitHub/Python-Concurrency-Programming/exercise/chromedriver",
        chrome_options=chrome_options,
    )
    driver.get(url[:-4] + "photo?filterType=음식")

    return image_crawling(driver, url, 30)


def fetch_image_inner(url):
    print(f"{os.getpid()} process | {threading.get_ident()} thread, {url}")
    driver = webdriver.Chrome(
        "/Users/seop/Documents/GitHub/Python-Concurrency-Programming/exercise/chromedriver",
        chrome_options=chrome_options,
    )
    driver.get(url[:-4] + "photo?filterType=내부")

    return image_crawling(driver, url, 30)


def main():
    executor = ProcessPoolExecutor(max_workers=10)
    urls = restaurant("가락동", 3)

    result_rivew = list(executor.map(fetch_review, urls[:3]))
    result_food = list(executor.map(fetch_image_food, urls[:3]))
    result_inner = list(executor.map(fetch_image_inner, urls[:3]))

    result = {}
    result["review_list"] = []
    result["img_food"] = []
    result["img_inner"] = []

    for i, j, k in zip(result_rivew, result_food, result_inner):
        result["review_list"].append(i)
        result["img_food"].append(j)
        result["img_inner"].append(k)

    return result


if __name__ == "__main__":
    df = pd.DataFrame(columns=["review_list"])
    start = time.time()
    result = pd.DataFrame(main())
    end = time.time()
    print(result.info())
    print(end - start)

# 60초
