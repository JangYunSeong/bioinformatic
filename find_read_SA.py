import pysam
import pandas as pd
def sum(read):
    result = 0
    for j in read.cigar:
        result += j[1]
    return result

url = ["2_CTCF.sa.bwa.sam", "CTCF-C-SNU719.sa.bwa.sam", "CTCF-ab_new.sa.bwa.sam", "/data3/projects/2022_KNU_EBV/aln/bwa/2021_SNU719/CTCF-ab_SA.bwa.sam"]
samfile = pysam.AlignmentFile("/data3/projects/2022_KNU_EBV/aln/bwa/2021_SNU719/combine/CTCF-C-SNU719.combine.sa.bwa.sam", "rb")
array = []
tmp = []
name = []
count = 0
for read in samfile.fetch():
    current = read.qname
    if read.pos == -1:
        pass
    else:
        a = read.pos
        if current in name:
            print("case1 " + current)
            count += 1
            if a in array[name.index(current)]:
                pass
            else:
                array[name.index(current)].append(a)
        else:
            print("case2 " + current)
            name.append(current)
            array.append([])
            array[name.index(current)].append(a)
newName = []
newArray = []
for i in range(0,len(name)):
    print(name[i] + " : " + str(array[i]))
    if len(array[i]) == 2:
        newName.append(name[i])
        newArray.append(array[i])
    # elif(len(array[i]) > 2):
    #     newName.append(name[i])
    #     newArray.append(array[i][0:2])
# print(count)
df = pd.DataFrame(newArray, index = newName)
print(df)
# df.to_csv('/data3/projects/2022_KNU_EBV/aln/bwa/2021_SNU719/new/CTCF-ab_SA.csv')
samfile.close()