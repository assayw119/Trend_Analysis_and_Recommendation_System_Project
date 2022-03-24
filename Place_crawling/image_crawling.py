from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
import time


# 일단 음식점 하나만!


def image_crawling(driver, link, cnt):

    img_list = []
    num = 1
    # cnt = int(input("가져오고 싶은 이미지 개수를 입력하세요 : "))
    print("-" * 50)
    name = driver.find_element(
        by=By.XPATH,
        value="/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[1]/div[1]/span[1]",
    )
    print(name.text)

    while num < cnt + 1:

        try:
            path = driver.find_element(
                by=By.XPATH,
                value=f'//*[@id="app-root"]/div/div/div[2]/div[5]/div/div[1]/ul/li[{num}]',
            )
            try:
                image_path = driver.find_element(
                    by=By.XPATH, value=f'//*[@id="visitor_{num}"]'
                )
            except:
                image_path = driver.find_element(
                    by=By.XPATH, value=f'//*[@id="ugc_{num}"]'
                )
            image = image_path.get_attribute("src")
            print("num :", num)
            print(image)
            img_list.append(image)
        except:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            driver.implicitly_wait(5)
        #             time.sleep(5)
        num += 1
        return img_list


def total_img_list_func(url, cnt):
    total_image_list = []

    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")
    driver = webdriver.Chrome("./chromedriver", options=options)

    driver.get(url[:-4] + "photo")

    driver.implicitly_wait(5)

    total_image_list += image_crawling(driver, url, cnt)
    return total_image_list
