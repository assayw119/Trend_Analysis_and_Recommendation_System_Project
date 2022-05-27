import numpy as np
import pandas as pd
import os
import glob


def processing(df1, df2):
    df1.columns = [
        "name",
        "address",
        "sort",
        "menu",
        "mean_price",
        "kakao_score",
        "kakao_people_give_score",
        "kakao_review_count",
        "kakao_review_list",
    ]

    df2.columns = [
        "name",
        "dong",
        "sort",
        "menu",
        "mean_price",
        "naver_score",
        "naver_people_give_score",
        "naver_review_count",
        "naver_review_list",
        "img_food",
        "img_inner",
    ]

    df2["dong"] = naver.split("/")[-1].split(".")[0]

    df_merge = pd.merge(df2, df1, on="name").drop(
        ["mean_price_x", "menu_y", "mean_price_y"], axis=1
    )

    df_merge = df_merge.astype({"kakao_score": "float32"})
    df_merge = df_merge.astype({"kakao_people_give_score": "int32"})
    df_merge = df_merge.astype({"naver_score": "float32"})

    df_merge.loc[
        df_merge["naver_people_give_score"] == "표기 안함", "naver_people_give_score"
    ] = 0
    df_merge = df_merge.astype({"naver_people_give_score": "int32"})

    df_merge["total_score"] = (
        df_merge["naver_score"] * df_merge["naver_people_give_score"]
        + df_merge["kakao_score"] * df_merge["kakao_people_give_score"]
    )

    df_merge["total_score"] = df_merge["total_score"] / (
        df_merge["naver_people_give_score"] + df_merge["kakao_people_give_score"]
    )
    df_merge["total_score"] = df_merge["total_score"].round(2)

    df_merge["total_review_count"] = (
        df_merge["naver_review_count"] + df_merge["kakao_review_count"]
    )

    return df_merge


df = pd.DataFrame(
    columns=[
        "name",
        "dong",
        "sort_x",
        "menu_x",
        "naver_score",
        "naver_people_give_score",
        "naver_review_count",
        "naver_review_list",
        "img_food",
        "img_inner",
        "address",
        "sort_y",
        "kakao_score",
        "kakao_people_give_score",
        "kakao_review_count",
        "kakao_review_list",
        "total_score",
    ]
)

road1 = "/Users/seop/Documents/GitHub/Trend_Analysis_and_Recommendation_System_Project/Region/naver"
road2 = "/Users/seop/Documents/GitHub/Trend_Analysis_and_Recommendation_System_Project/Region/kakao"

allFile_list = glob.glob(os.path.join(road1, "*.csv"))
allFile_list2 = glob.glob(os.path.join(road2, "*.csv"))

for naver, kakao in zip(allFile_list, allFile_list2):
    df_naver = pd.read_csv(naver)
    df_kakao = pd.read_csv(kakao)

    try:
        df_naver.drop(["Unnamed: 0"], axis=1, inplace=True)
        df_kakao.drop(["Unnamed: 0"], axis=1, inplace=True)
        df_merge = processing(df_kakao, df_naver)

        df = pd.concat([df, df_merge], ignore_index=False)
    except:
        pass

df = df.drop(
    [
        "naver_score",
        "kakao_score",
        "naver_people_give_score",
        "kakao_people_give_score",
        "kakao_review_count",
        "naver_review_count",
    ],
    axis=1,
)
df = df.reset_index(drop=True).reset_index().rename(columns={"index": "id"})


df.to_csv("naver_kakao_matzip.csv", encoding="utf-8-sig")
