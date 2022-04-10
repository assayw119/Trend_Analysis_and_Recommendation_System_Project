from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
import time


# 일단 음식점 하나만!

cnt = 1


def image_crawling(driver, link, cnt):
    scroll_repeat = cnt // 30
    for i in range(scroll_repeat):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        driver.implicitly_wait(5)
    img_list = []
    num = 1

    name = driver.find_element(
        by=By.XPATH,
        value="/html/body/div[3]/div/div/div[2]/div[1]/div[1]/div[1]/span[1]",
    )

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
