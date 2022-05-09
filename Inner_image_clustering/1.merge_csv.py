import numpy as np
import pandas as pd
# import urllib.request
import os
import glob


# 동별 csv 병합
def merge_csv(input_dir,output_dir):
  allFile_list = glob.glob(os.path.join(input_dir, '*.csv'))
  allData = []
  for file in allFile_list:
    df = pd.read_csv(file)
    allData.append(df)
  merge_data = pd.concat(allData, axis=0, ignore_index=True)
  merge_data.to_csv(output_dir, index=False, encoding='utf-8-sig')


dir = r'C:\Users\system888\Desktop\git\Trend_Analysis_and_Recommendation_System_Project'
input_dir = dir + '\Region'
output_dir = dir + '\Inner_image_clustering\merge_data.csv'
merge_csv(input_dir, output_dir)

