# python script by Taylor Paisie
#must have biopython install on computer

import sys, os, glob
from Bio import SeqIO, Entrez
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature
from Bio.SeqRecord import SeqRecord

# print("NCBI needs your email.")
# Entrez.email = input(">")
# print("Now the governement has your email address. Good luck hiding that internet history now.  Muahaha. ")


# goes through all the genbank files in the directory
# file_list = sorted(glob.glob("*.gb"))


# with open(sys.argv[2], 'w') as nfh:
#     for rec in SeqIO.parse(sys.argv[1], "genbank"):
#         if rec.features:
#             for feature in rec.features:
#                 if feature.type == "CDS":
#                 	for gene in feature.qualifiers:
#                 		if feature.qualifiers == ['gene'][0]:
#                     		nfh.write(">%s_%s\n" % (gene, rec.name, feature.location.extract(rec.seq)




# bash loop for script
# for i in {1..229}
# 	do
#		python /Users/taylorpaisie/Dropbox\ \(UFL\)/python_scripts/phylogenetic_scripts/extractCodingSeqs.py ORF${i} all_icp1.gb all_icp1_orf${i}
#	done



record = SeqIO.read(sys.argv[1], 'genbank')
output = open(sys.argv[2], 'w')

count = 0
for feature in record.features:
	if feature.type == 'CDS':
		count = count + 1
		feature_name = feature.qualifiers['gene'][0]
		feature_seq = feature.extract(record.seq)
		output.write(">" + feature_name + '\n' + str(feature_seq) + '\n')
output.close()
print(str(count) + " CDS Sequences extracted")