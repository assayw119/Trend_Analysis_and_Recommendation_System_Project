import certifi
import time
from selenium import webdriver
from pymongo import MongoClient
import pandas as pd
from config import MONGO_URL
from search_restaurant_url import restaurant  # 지역별 음식점의 링크 가져오기
from inform_restaurant import inform_restaurant  # 네이버 플레이스에서 음식점에 대한 정보 가져오기
from reviews import naver_reviews_list
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
import time

import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

executor = ThreadPoolExecutor(10)


def scrape(url, *, loop):
    loop.run_in_executor(executor, scraper, url)


def scraper(url, cnt):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        "/Users/seop/파이썬/아아아하기싫어/chromedriver_mac64_m1 (4)/chromedriver",
        options=options,
    )
    driver.get(url)
    driver.implicitly_wait(10)
    print(1)
    scroll_repeat = (20 - 10) // 10

    for i in range(scroll_repeat):
        try:
            button = driver.find_element(
                by=By.XPATH,
                value="/html/body/div[3]/div/div/div[2]/div[5]/div[4]/div[3]/div[2]/a",
            )

            button.click()
            driver.implicitly_wait(5)
        except:
            break
    time.sleep(3)
    res = driver.find_elements(by=By.CLASS_NAME, value="WoYOw")
    print(len(res))
    reviews_list = []
    for i in res:
        try:
            i.click()
            driver.implicitly_wait(5)
            reviews_list.append(i.text.replace("\n", ""))
        except:
            reviews_list.append(i.text.replace("\n", ""))


loop = asyncio.get_event_loop()
urls = restaurant("충무로", 1)
for url in urls:
    scrape(url, loop=loop)
    print(1)
loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))
