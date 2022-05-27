import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
import seaborn as sns
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d


dir = 'place_rgb_avg.csv'


train_data = pd.read_csv(dir)
train_data = pd.DataFrame(train_data)

train_data

df_f = train_data.copy()

ks = range(1,10)
inertias = []
for k in ks:
  model = KMeans(n_clusters=k)
  model.fit(df_f)
  inertias.append(model.inertia_)
  # Plot ks vs inertias
plt.figure(figsize=(4, 4))
plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()


clust_model = KMeans(n_clusters = 5 # 클러스터 갯수
                     # , n_init=10 # initial centroid를 몇번 샘플링한건지, 데이터가 많으면 많이 돌릴수록안정화된 결과가 나옴
                     # , max_iter=500 # KMeans를 몇번 반복 수행할건지, K가 큰 경우 1000정도로 높여준다
                     # , random_state = 42 # , algorithm='auto'
                     )

# 생성한 모델로 데이터를 학습시킴
clust_model.fit(df_f) # unsupervised learning

# 결과 값을 변수에 저장
centers = clust_model.cluster_centers_ # 각 군집의 중심점
pred = clust_model.predict(df_f) # 각 예측군집
print(pd.DataFrame(centers))
print(pred[:10])

clust_df2 = df_f.copy()
clust_df2['clust'] = pred
clust_df2.to_csv('\Inner_image_clustering\\result.csv',index= False)


fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
X = clust_df2
# 데이터 scatterplot
ax.scatter( X.iloc[:,0]
           , X.iloc[:,1]
           , X.iloc[:,2]
           , c = X.clust
           , s = 10
           , cmap = "rainbow"
            , alpha = 1
           )

# centroid scatterplot
ax.scatter(centers[:,0],centers[:,1],centers[:,2] ,c='black', s=200, marker='.')
plt.show()

print(clust_df2)