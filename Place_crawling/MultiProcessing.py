import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import ProcessPoolExecutor
import os
import threading
from selenium.webdriver.chrome.options import Options
from naver_reviews import naver_reviews_list
from search_restaurant_url import restaurant

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


def fetch_review(url):
    print(f"{os.getpid()} process | {threading.get_ident()} thread, {url}")
    driver = webdriver.Chrome(
        "/Users/seop/Documents/GitHub/Python-Concurrency-Programming/exercise/chromedriver",
        chrome_options=chrome_options,
    )
    driver.get(url)

    return naver_reviews_list(driver, url, 20)


def main():
    executor = ProcessPoolExecutor(max_workers=10)
    urls = restaurant("가락동", 3)
    result = list(executor.map(fetch_review, urls))

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


if __name__ == "__main__":

    start = time.time()
    main()
    end = time.time()

    print(end - start)

# 60초
