import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter
import cv2
import os
import glob

# 한식당의 rgb 평균 (kmeans)

def rgb_perc(k_cluster):
    #width = 300
   # palette = np.zeros((50, width, 3), np.uint8)

    n_pixels = len(k_cluster.labels_)
    counter = Counter(k_cluster.labels_)  # count how many pixels per cluster
    perc = {}
    for i in counter:
        perc[i] = np.round(counter[i] / n_pixels, 2)
    perc = np.array(list(perc.values()))

    # top5 color * perc = average RGB
    rgb_weight = k_cluster.cluster_centers_.T * perc
    rgb_avg = np.mean(rgb_weight, axis=1)

    # print('Percentage of color :', perc)
    # print('Each RGB :', k_cluster.cluster_centers_)
    # print('Avg_RGB :',rgb_avg)
    step = 0

    # for idx, centers in enumerate(k_cluster.cluster_centers_):
    #     palette[:, step:int(step + perc[idx]*width+1), :] = centers
    #     step += int(perc[idx]*width+1)

    return rgb_avg


dir = r"C:\Users\system888\Desktop\git\Trend_Analysis_and_Recommendation_System_Project\Inner_image_clustering"
folder = os.listdir(dir + '\Inner_image')
place_avg = np.array([[], []])
place_avg = np.empty((0, 3), float)
place_avg = place_avg.reshape(-1,3)
# item = 식당 번호
for item in folder:
    files = os.listdir(dir + '\Inner_image'+'\\'+str(item))
    place_rgb = np.array([[], []])
    place_rgb = np.empty((0, 3), float)
    place_rgb = place_rgb.reshape(-1, 3)

    for i in range(len(files)):
        print(i, end='')
        image = cv2.imread(dir+'\Inner_image'+'\\'+item+'\\'+files[i])
        clt = KMeans(n_clusters=5)
        clt = clt.fit(image.reshape(-1,3))
        place_rgb=np.append(place_rgb, [rgb_perc(clt)],axis=0)

    place_rgb = np.nan_to_num(place_rgb.mean(axis=0))
    print(place_rgb)
    # 한 식당 내부 이미지 30장의 rgb 평균
    print(item)
    place_avg = np.vstack([place_avg,place_rgb])

print(place_avg)


df_rgb = pd.DataFrame(place_avg)
df_rgb = df_rgb.rename(columns={0: 'R',1:'G',2:'B'})
df_rgb.to_csv('place_rgb_avg2.csv',index=False)



