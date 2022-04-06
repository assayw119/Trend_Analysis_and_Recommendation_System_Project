import certifi

# from models.information import Information
from pymongo import MongoClient
from config import MONGO_URL
from search_restaurant_url import restaurant  # 지역별 음식점의 링크 가져오기
from inform_restaurant import inform_restaurant  # 네이버 플레이스에서 음식점에 대한 정보 가져오기
from image_crawling import total_img_list_func  # 이미지 크롤링 후 리스트 가져오기
from reviews import total_reviews_list

if __name__ == "__main__":

    ca = certifi.where()
    client = MongoClient(MONGO_URL, tlsCAFile=ca)
    # client = MongoClient('localhost', 27017)

    db = client["test"]
    # print(db)
    urls = restaurant("충무로", 1)  # 3*n개의 url이 나옴
    # df = pd.DataFrame(columns=["이름", "분류", "분위기(테마키워드)", "주요 메뉴", "평균 가격", "평점", "리뷰 수"])
    for url in urls:
        review = {}
        review_list = total_reviews_list(url, 20)
        review["review_list"] = review_list
        result = inform_restaurant(url)
        total_img = total_img_list_func(url, 1)  # 각 url마다 몇 개의 이미지를 가져올것인가
        info = {
            "name": result["name"],
            "sort": result["sort"],
            "menu": result["main_menu"],
            "mean_price": result["mean_price"],
            "score": float(result["score"]),
            "people_give_score": result["people_give_score"],
            "review_count": int(result["review_count"]),
            "image": total_img[0],  # html 시험용으로 하나만
            "review_list": review["review_list"],
        }

        dpInsert = db.inform.insert_one(info)  # db에 정보 입력
        # df = pd.concat([df, pd.DataFrame(result)], ignore_index=False)
    print("finish!")
