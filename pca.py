import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv("C:\Bioinfo\Final.csv")
x = data.drop('Unnamed: 0',axis = 1).values
x = np.transpose(x)
pca = PCA(n_components = 3)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['component1', 'component2', 'component3'])
# print(pca.explained_variance_ratio_)
exon = ['DRR294987', 'DRR294994', 'DRR294988', 'DRR294989']
color = ['orange', 'red', 'green', 'cyan']
principalDf['exon'] = exon
df_pca = [0] * 4
for i in range(0,4):
    df_pca[i] = principalDf[principalDf['exon'] == exon[i]]
print(df_pca)
fig = plt.figure(figsize = (15,15))
ax = fig.add_subplot(111, projection = '3d')

ax.set_xlabel('component1', fontsize = 15)
ax.set_ylabel('component2', fontsize = 15)
ax.set_zlabel('component3', fontsize = 15)
ax.set_title('3 Component PCA', fontsize = 20)
for i in range(0,4):
    ax.scatter(df_pca[i]['component1'], df_pca[i]['component2'], df_pca[i]['component3'], color = color[i], alpha = 0.7, label = exon[i])
ax.legend()
ax.grid()