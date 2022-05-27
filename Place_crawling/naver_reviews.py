from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
import time


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
            reviews_list.append(i.text.replace("\n", "") + "/")
        except:
            reviews_list.append(i.text.replace("\n", "") + "/")

    return reviews_list
