from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from kakao_search_restaurant_url import kakao_restaurant


urls = kakao_restaurant("충무로", 15)
options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")
driver = webdriver.Chrome("chromedriver", options=options)
# url  url 리스트 안의 원소들
driver.get(urls[0])  # 일단 하나의 사이트에서만
driver.implicitly_wait(5)


name = driver.find_element(
    by=By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/h2"
)
restaurant_name = name.text  # 음식점 명

tag = driver.find_element(
    by=By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/div"
)  # 평점 정보
sort_point, cnt, review = tag.text.split("\n")
sort, _, point = sort_point.split()  # 분류,평점
point = float(point)
cnt = int(cnt.strip(")").strip("(").replace(",", ""))  # 평점을 매긴 사람들의 수
review_count = int(review.split()[1].replace(",", ""))  # 리뷰 수

menus = driver.find_element(
    by=By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[3]/ul"
)

ssum = 0
menu_count = 0
menu_list = menus.text.split("\n")[::2]  # 대표 메뉴 리스트

for i in menus.text.split("\n")[1::2]:
    try:
        ssum += int(i.replace(",", ""))
        menu_count += 1
    except:
        print("가격 오류: ", ssum)
        continue
mean_price = ssum / menu_count  # 평균 가격대


# 여기서부턴 리뷰들

review_list = []
daum_button, no_review = False, False  # 처음에는 2페이지로 가는 파라미터가 1이지만, 한번 다음을 클릭한다면, 2로 바뀐다
next_page = 1
while 1:

    for n in range(1, 5 + 1):
        try:
            review_coment = driver.find_element(
                by=By.XPATH,
                value=f"/html/body/div[2]/div[2]/div[2]/div[6]/div[3]/ul/li[{n}]/div[2]/p",
            ).text
            print(review_coment)
            review_list.append(review_coment)
        except:
            no_review = True
            break
    if no_review:
        break

    next_page_button = driver.find_element(
        by=By.XPATH,
        value=f"/html/body/div[2]/div[2]/div[2]/div[6]/div[3]/div/a[{next_page}]",
    )
    next_page_button.click()
    time.sleep(2)
    next_page += 1

    if next_page == 6:
        next_page_button = driver.find_element(
            by=By.XPATH,
            value=f"/html/body/div[2]/div[2]/div[2]/div[6]/div[3]/div/a[{next_page}]",
        )
        next_page_button.click()
        time.sleep(2)
        next_page = 2

    if next_page == 5 and not daum_button:
        daum_button = True
        next_page_button = driver.find_element(
            by=By.XPATH,
            value=f"/html/body/div[2]/div[2]/div[2]/div[6]/div[3]/div/a[{next_page}]",
        )
        next_page_button.click()
        time.sleep(2)
        next_page = 2
