from selenium import webdriver
from selenium.webdriver.common.by import By
from search_restaurant_url import restaurant


def naver_reviews_list(url, cnt):

    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")
    driver = webdriver.Chrome("chromedriver", options=options)
    driver.get(url[:-4] + "review/visitor")
    driver.implicitly_wait(5)

    scroll_repeat = (cnt - 10) // 10

    for i in range(scroll_repeat):

        button = driver.find_element(
            by=By.XPATH,
            value="/html/body/div[3]/div/div/div[2]/div[5]/div[4]/div[3]/div[2]/a",
        )
        button.click()
        driver.implicitly_wait(5)

    res = driver.find_elements(By.CLASS_NAME, "WoYOw")
    reviews_list = []
    for i in res:
        try:
            i.click()
            driver.implicitly_wait(5)
            reviews_list.append(i.text.replace("\n", ""))
        except:
            reviews_list.append(i.text.replace("\n", ""))

    return reviews_list


def total_reviews_list(url, cnt):
    total_reviews_list = []
    total_reviews_list += naver_reviews_list(url, cnt)
    return total_reviews_list


if __name__ == "__main__":

    urls = restaurant("충무로", 1)
    for url in urls:
        review = {}

        review_list = total_reviews_list(url)
        review["review_list"] = review_list
