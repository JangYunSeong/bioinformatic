# search index which is bigger than 0 in bed
# search terms about reference.fasta file and append these
# make new fasta file
from Bio import SeqIO
# seq = SeqIO.read("/data3/PUBLIC_DATA/ref_genomes/homo_sapiens/hg38_fasta/hg38.1.fa", 'fasta')
# print(seq[10073142:10073192])
# print(seq.description)
import pandas as pd
total = []
count = 1
# index = ["4940-4984", "9889-9941", "10279-10315"]
index = ["10279-10315","4940-4984", "9889-9941"]
for i in range(1,23):
    total.append(str(i))
total.append("X")
total.append("Y")
array = []
name_array = []
# for i in index:
#     fasta = open("/data3/projects/2022_KNU_EBV/trimmed/2021_SNU719/yj/humanannot/hg38.sa.pos" + str(index.index(i) + 3) + ".fasta", "w")
#     for k in total[:-2]:
#         csv_test = pd.read_csv("/data3/projects/2022_KNU_EBV/trimmed/2021_SNU719/yj/chr_bed/chr" + k +".csv", index_col = 0)
#         seq = SeqIO.read("/data3/PUBLIC_DATA/ref_genomes/homo_sapiens/hg38_fasta/hg38."+ k +".fa", 'fasta')
#         tmp = csv_test.loc[i]
#         for k in range(0,len(tmp.values)):
#             if tmp.values[k] > 0:
#                 pos = tmp.index[k].split('-')
#                 for t in range(0,tmp.values[k]):
#                     header = "hg38.sa." + i + "." + str(count)
#                     count += 1
#                     lines = ">" + header + '\n' + str(seq.seq[int(pos[0]):int(pos[1])])+'\n'
#                     fasta.write(lines)
#     fasta.close()
fasta = open("/data3/projects/2022_KNU_EBV/trimmed/2021_SNU719/yj/motif/hg38.sa.other.fasta", "w")
for k in total[:-2]:
    csv_test = pd.read_csv("/data3/projects/2022_KNU_EBV/trimmed/2021_SNU719/yj/chr_bed/chr" + k +".csv", index_col = 0)
    seq = SeqIO.read("/data3/PUBLIC_DATA/ref_genomes/homo_sapiens/hg38_fasta/hg38."+ k +".fa", 'fasta')
    for i in csv_test.index:
        tmp = csv_test.loc[i]
        if i in index:
            pass
        else:
            for k in range(0,len(tmp.values)):
                if tmp.values[k] > 0:
                    pos = tmp.index[k].split('-')
                    for t in range(0,tmp.values[k]):
                        header = "hg38.sa." + i + "." + str(count)
                        count += 1
                        lines = ">" + header + '\n' + str(seq.seq[int(pos[0]):int(pos[1])])+'\n'
                        fasta.write(lines)
fasta.close()