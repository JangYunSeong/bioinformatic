import pandas as pd
total = []
for i in range(1,23):
    total.append(str(i))
total.append("X")
total.append("Y")
array = []
name_array = []
for k in total:

    csv_test = pd.read_csv("/data3/projects/2022_KNU_EBV/trimmed/2021_SNU719/yj/chr_bed/chr" + k +".csv", index_col = 0)
    for i in range(0,len(csv_test.index)):
        tmp = csv_test.iloc[i].sum()
        name = csv_test.iloc[i].name
        if tmp==0:
            pass
        else:
            if name not in name_array:
                name_array.append(name)
                array.append(tmp)
            else:
                array[name_array.index(name)] += tmp
    df = pd.DataFrame(array, columns=['count'], index=name_array)
    df_sorted = df.sort_values(by=df.columns[0], ascending=False)
    print(df_sorted)
    df_sorted.to_csv("/data3/projects/2022_KNU_EBV/trimmed/2021_SNU719/yj/SNU719_count/chr" + k + "_count.csv")
    array = []
    name_array = []