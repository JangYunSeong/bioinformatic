import pysam

def sum(array):
    count = 0
    for i in range(len(array)):
        count += int(array[i][1])
    return count
token = "1:N:0:CTTGTA"
samfile = pysam.AlignmentFile("/data3/projects/2022_KNU_EBV/aln/bwa/2022_CTCF-C_PE/CTCF-C-SNU719.bwa.sam", "rb")
fastq = open("/data3/projects/2022_KNU_EBV/aln/bwa/2021_SNU719/new/CTCF-ab_new.fastq", 'w')
for read in samfile.fetch():
    for i in read.tags:
        if i[0] == 'SA' and 'NC_007605' in i[1]:
            count = 0
            new = read.qname.split(':')
            newString = '@'
            for j in read.cigar:
                # print(j)
                if int(j[0]) == 0 or int(j[0]) == 4 or int(j[0]) == 5:
                    a= read.seq[count:(count + int(j[1]))]
                    b = "+\n" + read.qual[count:(count + int(j[1]))]
                    count += int(j[1])
                    for k in new:
                        newString += k + ':'
                    t = newString[:-1] + " " + token
                    # print(a)
                    # print(b)
                    if(a == ""):
                        pass
                    else:
                        result = t + '\n' + a + '\n' + b + '\n'
                        print(result)
                        # fastq.write(result)
                newString = '@'
            # print("total : "+read.seq)
            # print(sum(read.cigar))
            # print(read.cigar)
            # print(i)
            break
samfile.close()
fastq.close()