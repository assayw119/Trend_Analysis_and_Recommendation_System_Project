import pandas as pd
import numpy as np
import os

# 클러스터 별로 사진 저장

dir = 'result2.csv'

train_data = pd.read_csv(dir)
train_data = pd.DataFrame(train_data)

groups = train_data.groupby('clust')
groups.size()

result = dict(list(groups))

#print(result[2].index)

for i in range(5):
    file_source = r'C:\Users\system888\Desktop\git\Trend_Analysis_and_Recommendation_System_Project\Inner_image_clustering\Inner_image'
    file_destination = r'C:\Users\system888\Desktop\git\Trend_Analysis_and_Recommendation_System_Project\Inner_image_clustering\cluster_image' +'\\'+ str(i)
    cls_index = list(result[i].index)
    cls2_index = []
    for j in range(len(cls_index)):
        cls2_index.append('#'+str(cls_index[j]).rjust(4,'0'))

    for g in cls2_index:
        os.replace(file_source +'\\'+ g, file_destination +'\\'+ g)