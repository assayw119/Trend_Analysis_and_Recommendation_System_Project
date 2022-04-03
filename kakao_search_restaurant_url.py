import requests

app_key = "f58ecd8a6f3a91c7b483596610cb46f9"
headers = {"Authorization": "KakaoAK {}".format(app_key)}
query = "충무로 맛집"
pages = range(1)  # 1페이지당 15개의 음식점의 정보를 불러올 수 있다.
url = "https://dapi.kakao.com/v2/local/search/keyword.json?query={}&pages={}".format(
    query, pages
)
urls = []
for page in pages:
    response = requests.get(url, headers=headers)
    urls.append(response.json()["documents"][place_url])
