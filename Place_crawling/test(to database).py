import certifi
# from models.information import Information
from pymongo import MongoClient
from config import MONGO_URL
from search_restaurant_url import restaurant  # 지역별 음식점의 링크 가져오기
from inform_restaurant import inform_restaurant  # 네이버 플레이스에서 음식점에 대한 정보 가져오기
from image_crawling import total_img_list_func  # 이미지 크롤링 후 리스트 가져오기

if __name__ == "__main__":

    ca = certifi.where()
    # client = MongoClient(MONGO_URL, tlsCAFile=ca)
    client = MongoClient('localhost', 27017)

    db = client["test"]
    # print(db)
    urls = restaurant("충무로", 1)  # 3*n개의 url이 나옴
    # df = pd.DataFrame(columns=["이름", "분류", "분위기(테마키워드)", "주요 메뉴", "평균 가격", "평점", "리뷰 수"])
    for url in urls:

        result = inform_restaurant(url)
        total_img = total_img_list_func(url, 1)  # 각 url마다 몇 개의 이미지를 가져올것인가
        info = {
            "name": result["이름"],
            "sort": result["분류"],
            "mood": str(result["분위기(테마키워드)"]),
            "menu": result["주요 메뉴"],
            "mean_price": result["평균 가격"],
            "point": float(result["평점"]),
            "reviews": int(result["리뷰 수"]),
            "image": total_img[0],  # html 시험용으로 하나만
        }

        dpInsert = db.inform.insert_one(info)  # db에 정보 입력
        # df = pd.concat([df, pd.DataFrame(result)], ignore_index=False)
    print("finish!")
