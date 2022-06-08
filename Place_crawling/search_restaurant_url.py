import requests
import pandas as pd
from fake_useragent import UserAgent


def restaurant(station, displayCount):

    dfs = []
    for page in range(1, 4):  # 1페이지부터 ~4(n) 페이지까지
        url = "https://map.naver.com/v5/api/search?caller=pcweb&query={}맛집&type=all&page={}&displayCount={}&isPlaceRecommendationReplace=true&lang=ko".format(
            station, page, displayCount
        )
        # headers = {"user-agent": UserAgent().chrome}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        try:
            datas_df = pd.DataFrame(response.json()["result"]["place"]["list"])
            datas_df = datas_df[["id"]]
            dfs.append(datas_df)
        except:
            continue
    result_df = pd.concat(dfs)
    result_df.reset_index(drop=True, inplace=True)

    ids = list(result_df["id"])

    id_ = []
    count = 0
    for i in ids:
        url = "https://m.place.naver.com/restaurant/{}/home".format(i)
        id_.append(url)
    return id_
    
