from selenium import webdriver

from selenium.webdriver.common.by import By
import time


def kakao_inform_restaurant(url):
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")
    driver = webdriver.Chrome(
        "/Users/seop/Documents/GitHub/Trend_Analysis_and_Recommendation_System_Project/Place_crawling/chromedriver",
        options=options,
    )
    # url  url 리스트 안의 원소들
    driver.get(url)  # 일단 하나의 사이트에서만
    driver.implicitly_wait(10)

    name = driver.find_element(
        by=By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/h2"
    )
    restaurant_name = name.text  # 음식점 명
    address = driver.find_element(
        by=By.XPATH,
        value="/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/span[1]",
    )
    address_name = address.text
    tag = driver.find_element(
        by=By.XPATH,
        value="/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/div",
    )  # 평점 정보
    sort_point, cnt, review = tag.text.split("\n")
    sort, _, point = sort_point.split()  # 분류,평점
    point = float(point)
    cnt = int(cnt.strip(")").strip("(").replace(",", ""))  # 평점을 매긴 사람들의 수
    review_count = int(review.split()[1].replace(",", ""))  # 리뷰 수
    try:
        try:

            menus = driver.find_element(
                by=By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[3]/ul"
            )

        except:
            pass

        ssum = 0
        menu_count = 0
        menu_list = menus.text.split("\n")[::2]  # 대표 메뉴 리스트

        for i in menus.text.split("\n")[1::2]:
            try:
                ssum += int(i.replace(",", ""))
                menu_count += 1
            except:
                continue
        mean_price = ssum // menu_count  # 평균 가격대
    except:
        menu_list = ["표기안함"]
        mean_price = "표기안함"
        pass
    # 여기서부턴 리뷰들

    review_list = []
    daum_button, no_review = (
        False,
        False,
    )  # 처음에는 2페이지로 가는 파라미터가 1이지만, 한번 다음을 클릭한다면, 2로 바뀐다
    next_page = 1
    while 1:

        if len(review_list) >= 30:
            print("break")
            break
        for n in range(1, 5 + 1):

            try:
                review_coment = driver.find_element(
                    by=By.XPATH,
                    value=f"/html/body/div[2]/div[2]/div[2]/div[6]/div[3]/ul/li[{n}]/div[2]/p",
                ).text
                if review_coment != "":
                    review_list.append(review_coment)

            except:
                no_review = True
                break
        if no_review:
            break
        try:
            next_page_button = driver.find_element(
                by=By.XPATH,
                value=f"/html/body/div[2]/div[2]/div[2]/div[6]/div[3]/div/a[{next_page}]",
            )
            next_page_button.click()
            time.sleep(3)
            next_page += 1
        except:
            break
        try:
            if next_page == 6:
                next_page_button = driver.find_element(
                    by=By.XPATH,
                    value=f"/html/body/div[2]/div[2]/div[2]/div[6]/div[3]/div/a[{next_page}]",
                )
                next_page_button.click()
                time.sleep(2)
                next_page = 2
        except:
            pass
        try:
            if next_page == 5 and not daum_button:
                daum_button = True
                next_page_button = driver.find_element(
                    by=By.XPATH,
                    value=f"/html/body/div[2]/div[2]/div[2]/div[6]/div[3]/div/a[{next_page}]",
                )
                next_page_button.click()
                time.sleep(2)
                next_page = 2
        except:
            pass
    inform = {}
    inform["name"] = restaurant_name
    inform["address"] = address_name
    inform["sort"] = sort
    inform["main_menu"] = ",".join(menu_list)
    inform["mean_price"] = mean_price
    inform["score"] = point
    inform["review_count"] = review_count
    inform["people_give_score"] = cnt
    inform["review_list"] = review_list

    return inform
