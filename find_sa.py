import pysam
samfile = pysam.AlignmentFile("/data3/projects/2022_KNU_EBV/aln/bwa/2021_SNU719/Input.bwa.bam", "rb")
strings = ["Input.bwa.sam","CTCF-ab.bwa.sam", "Ig-G.bwa.sam"]
saString = ["Input_SA.bwa.sam","CTCF-ab_SA.bwa.sam", "Ig-G_SA.bwa.sam"]
for i in range(0,3):
    url = "/data3/projects/2022_KNU_EBV/aln/bwa/2021_SNU719/" + strings[i]
    url_sa = "/data3/projects/2022_KNU_EBV/aln/bwa/2021_SNU719/" + saString[i]
    samfile = pysam.AlignmentFile(url,"rb")
    safile = pysam.AlignmentFile(url_sa, "wb", template =samfile)
    for read in samfile.fetch():
        if read.is_paired:
            for k in read.tags:
                if "SA" in k:
                    safile.write(read)
                    break
    samfile.close()