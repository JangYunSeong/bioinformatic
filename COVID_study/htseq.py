import collections
import json

import HTSeq
    
gtf_file = HTSeq.GFF_Reader("/data-Raid10/PUBLIC_DATA/ref_genomes/homo_sapiens/hg38.gtf")
features = HTSeq.GenomicArrayOfSets("auto", stranded=True)

for feature in gtf_file:
    if feature.type == "exon":
        features[feature.iv] += feature.attr["gene_id"]

almnt_file = HTSeq.SAM_Reader("/data-Raid10/projects/2022_COVID19_study/ys/DRR294987/DRR294987_analysisAligned.out.sam")
counts = collections.Counter()
for bundle in HTSeq.pair_SAM_alignments(almnt_file, bundle=True):
    if len(bundle) != 1:
        continue  # Skip multiple alignments
    first_almnt, second_almnt = bundle[0]  # extract pair
    print("bundle[0] : ", bundle[0])
    if not first_almnt is None and second_almnt is None:
        counts["_unmapped"] += 1
        continue
    gene_ids = set()
    if first_almnt is not None:
        for iv, val in features[first_almnt.iv].steps():
            gene_ids |= val
    if second_almnt is not None:
        for iv, val in features[second_almnt.iv].steps():
            gene_ids |= val
    if len(gene_ids) == 1:
        gene_id = list(gene_ids)[0]
        counts[gene_id] += 1
    elif len(gene_ids) == 0:
        counts["_no_feature"] += 1
    else:
        counts["_ambiguous"] += 1
file_data = collections.OrderedDict()
for gene_id in counts:
    file_data[gene_id] = counts[gene_id].get_text()
    print(gene_id, counts[gene_id])
GENOME_FILE_PATH = "/data-Raid10/projects/2022_COVID19_study/ys/DRR294987/DRR294987.count"
with open(GENOME_FILE_PATH, 'w') as DRR294987_genome_outfile:  # regions
    json.dump(file_data, DRR294987_genome_outfile, ensure_ascii=False, indent='\t')
