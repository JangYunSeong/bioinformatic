import pandas as pd
total = []
for i in range(1,23):
    total.append(str(i))
total.append("X")
total.append("Y")
ebvannot = pd.read_csv('/data3/projects/2022_KNU_EBV/trimmed/2021_SNU719/yj/SNU719_count/ebvPos.csv',index_col=0)
array = [[] * 18 for _ in range(18)]
other = 'LMP-2B'
for i in range(1,len(ebvannot.index)):
    # print(ebvannot.index[i],ebvannot['start'][i],ebvannot['end'][i])
    tmp = [int(ebvannot['start'][i]),int(ebvannot['end'][i]), ebvannot.index[i]]
    index = int(ebvannot['start'][i]) // 10000
    array[index].append(tmp)
for m in total:
    annotarray = []
    url = "/data3/projects/2022_KNU_EBV/trimmed/2021_SNU719/yj/SNU719_count/chr" + m + "_count.csv"
    chrcount = pd.read_csv(url, index_col = 0)
    print('chr' + m)
    for k in chrcount.index:
        flag = 0
        temp = list(map(int,k.split('-')))
        pos = temp[0] // 10000
        for i in array[pos]:
            if(i[0] <= temp[0] and temp[1] <= i[1]):
                # print("yes : " + i[2])
                annotarray.append(i[2])
                flag = 1
                break
        if flag == 0:
            # print("no : " + other)
            annotarray.append(other)
        # print(temp)
    df = pd.DataFrame(annotarray, index = chrcount.index, columns=['gene_name'])
    new_df =pd.concat([chrcount,df], axis=1)
    print(new_df)
    new_df.to_csv("/data3/projects/2022_KNU_EBV/trimmed/2021_SNU719/yj/SNU719_count/chr" + m +"_count.csv")