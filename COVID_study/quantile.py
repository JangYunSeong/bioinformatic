
import numpy as np
import pandas as pd

f = open("C:\Bioinfo\DRR294987.count", "rt")

array = {}
array2 = {}
while(True):
    a = f.readline()
    if(a==""):
        break
    name, num = a.split("\t")
    array[name] = int(num)
f.close()
f = open("C:\Bioinfo\DRR294994.count", "rt")
while(True):
    a = f.readline()
    if(a==""):
        break
    name, num = a.split("\t")
    array2[name] = int(num)
f.close()
df = pd.DataFrame({'DRR294987' : array, 'DRR294994' : array2})
df_sorted = pd.DataFrame(np.sort(df.values, axis = 0), index = df.index, columns=df.columns)
df_mean = df_sorted.mean(axis =1)
df_mean.index = np.arange(1,len(df_mean) + 1)
df_qn = df.rank(method ="min").stack().astype(int).map(df_mean).unstack()
print(df_qn)
df_qn.plot.density(linewidth=4)