import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import ProcessPoolExecutor
import os
import threading
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


def naver_reviews_list(driver, url, cnt):
    driver.implicitly_wait(10)

    scroll_repeat = (cnt - 10) // 10

    for i in range(scroll_repeat):
        try:
            button = driver.find_element(
                by=By.XPATH,
                value="/html/body/div[3]/div/div/div[2]/div[5]/div[4]/div[3]/div[2]/a",
            )

            button.click()
            time.sleep(6)
        except:
            print(url)
            break

    time.sleep(3)
    res = driver.find_elements(by=By.CLASS_NAME, value="WoYOw")

    reviews_list = []
    for i in res:
        try:
            i.click()
            driver.implicitly_wait(5)
            reviews_list.append(i.text.replace("\n", ""))
        except:
            reviews_list.append(i.text.replace("\n", ""))

    return reviews_list


def fetch(url):
    print(f"{os.getpid()} process | {threading.get_ident()} thread, {url}")
    driver = webdriver.Chrome(
        "/Users/seop/Documents/GitHub/Python-Concurrency-Programming/exercise/chromedriver",
        chrome_options=chrome_options,
    )
    driver.get(url)

    return naver_reviews_list(driver, url, 20)


def main():
    executor = ProcessPoolExecutor(max_workers=10)
    urls = [
        "https://m.place.naver.com/restaurant/1835052467/home",
        "https://m.place.naver.com/restaurant/11678488/home",
        "https://m.place.naver.com/restaurant/11679353/home",
        "https://m.place.naver.com/restaurant/1799596430/home",
        "https://m.place.naver.com/restaurant/11720161/home",
        "https://m.place.naver.com/restaurant/1865094857/home",
        "https://m.place.naver.com/restaurant/1323525758/home",
        "https://m.place.naver.com/restaurant/1444910504/home",
        "https://m.place.naver.com/restaurant/19866570/home",
    ]

    result = list(executor.map(fetch, urls))
    result = [i for i in result if i]
    print(result)
    print(len(result))


if __name__ == "__main__":

    start = time.time()
    main()
    end = time.time()

    print(end - start)

# 60초
