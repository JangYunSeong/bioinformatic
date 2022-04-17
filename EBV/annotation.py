import HTSeq
import pandas as pd
name = []
pos = []
ebv = "/data3/PUBLIC_DATA/ref_genomes/Human_gammaherpesvirus_4_EBV/NC_007605.1.gtf"
human = "/data3/PUBLIC_DATA/ref_genomes/homo_sapiens/hg38/hg38.gtf"
def gtf_count():
    gtf_file = HTSeq.GFF_Reader(human)
    print(gtf_file)
    exons = HTSeq.GenomicArrayOfSets("auto", stranded=True)
    for feature in gtf_file:
        exons[feature.iv] += feature.attr["transcript_id"]
        # print(feature.attr["transcript_id"])
        array = feature.get_gff_line().split('\t')
        if "gene_name" in feature.attr:
            name.append(feature.attr["gene_name"])
        else:
            name.append(feature.attr["transcript_id"])
        pos.append([int(array[3]),int(array[4])])
    df = pd.DataFrame(pos, index = name, columns=["start","end"])
    print(df)
    df.to_csv("/data3/projects/2022_KNU_EBV/trimmed/2021_SNU719/yj/SNU719_count/ebvPos.csv")
gtf_count()