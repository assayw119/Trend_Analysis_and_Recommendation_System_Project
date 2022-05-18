from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
import time


# 일단 음식점 하나만!


def image_crawling(driver, link, cnt):
    driver.implicitly_wait(10)

    scroll_repeat = cnt // 30
    for i in range(scroll_repeat):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        driver.implicitly_wait(5)
    img_list = []
    num = 1
    time.sleep(2)

    image_path = driver.find_elements(
        by=By.CLASS_NAME,
        value="_img",
    )

    for image in image_path:
        img = image.get_attribute("src")

        img_list.append(img)

    return img_list


# options = webdriver.ChromeOptions()
# # 창 숨기는 옵션 추가
# options.add_argument("headless")
# driver = webdriver.Chrome("/Users/seop/파이썬/아아아하기싫어/chromedriver_mac64_m1 (4)/chromedriver", options=options)
