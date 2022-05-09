import numpy as np
import pandas as pd
from PIL import Image
import urllib.request
import os
import glob

# 총 데이터에서 사진 없는 식당 제외
input_dir = "merge_data.csv"
train_data = pd.read_csv(input_dir)
train_data = pd.DataFrame(train_data)
train_data = train_data.dropna(subset=['img_inner'])
image_data = train_data.img_inner.str.split(',')
image_mat = np.array(image_data)
print(len(image_mat[0]))
print(train_data.info())
train_data.to_csv(input_dir, index=False, encoding='utf-8-sig')

def downImage(dir, img_url, img_name):
    urllib.request.urlretrieve(img_url, dir + '\#' +str(img_name).rjust(2,'0')+'.jpg')

img_dir = "Inner_image"
for i in range(len(image_mat)):
    os.mkdir(img_dir + '\#' + str(i).rjust(4, '0'))
    restaur_folder = img_dir + "\#" + str(i).rjust(4, '0')
    for j in range(len(image_mat[i])):
        downImage(restaur_folder, image_mat[i][j],str(i).rjust(4,'0')+'-'+str(j).rjust(2,'0'))
