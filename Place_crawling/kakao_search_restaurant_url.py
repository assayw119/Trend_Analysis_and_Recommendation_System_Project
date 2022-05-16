def kakao_restaurant(station, cnt):  # 15의 배수로 입력(15,30,....,150...)
    import requests

    app_key = "f58ecd8a6f3a91c7b483596610cb46f9"
    headers = {"Authorization": "KakaoAK {}".format(app_key)}
    # query = station + "맛집"
    query = station
    pages = range(cnt // 15)  # 1페이지당 15개의 음식점의 정보를 불러올 수 있다.
    url = (
        "https://dapi.kakao.com/v2/local/search/keyword.json?query={}&pages={}".format(
            query, pages
        )
    )
    urls = []
    for page in pages:
        response = requests.get(url, headers=headers)
        for dic in response.json()["documents"]:
            urls.append(dic["place_url"])
    return urls
