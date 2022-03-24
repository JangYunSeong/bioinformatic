import numpy as np
import pandas as pd

bed = open("/data3/projects/2022_KNU_EBV/trimmed/2021_SNU719/yj/CTCF-C-SNU719.bed")
url = "/data3/projects/2022_KNU_EBV/trimmed/2021_SNU719/yj/SNU719_chr/"
chromosome = ['chr1']
prev = "chr1"
temparray = ""
array = ""
while True:
    line = bed.readline().split()
    if not line:
        urls = url + prev + ".bed"
        urlTemp = open(urls, "w")
        urlTemp.write(str(temparray))
        urlTemp.close()
        break
    newtmp = ""
    chrtmp = line[0].split(',')[0]
    starttmp = line[1].split(',')[0]
    endtmp = line[2].split(',')[0]
    qnametmp = line[3].split(',')
    for i in range(0,len(qnametmp)):
        newtmp += qnametmp[i]
        newtmp += ','
    array = chrtmp + '\t' +starttmp +'\t' + endtmp + '\t' + newtmp[0:-1]
    if chrtmp not in chromosome:
        chromosome.append(chrtmp)
        urls = url + prev+ ".bed"
        urlTemp = open(urls ,"w")
        urlTemp.write(str(temparray))
        urlTemp.close()
        temparray = ""
        temparray+=array + '\n'
        prev = chrtmp
    else:
        temparray+=array + '\n'
bed.close()