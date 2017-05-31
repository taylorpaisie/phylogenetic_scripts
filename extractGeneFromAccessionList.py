# python script by Taylor Paisie
#must have biopython install on computer

import sys, os
from Bio import SeqIO, Entrez
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature
from urllib2 import HTTPError

print("NCBI needs your email.")
Entrez.email = raw_input(">")
print("Now the governement has your email address. Good luck hiding that internet history now.  Muahaha. ")


# this is your text file with the GB accession numbers
#print("Input your text file with the GB accession numbers")
id_list = open(sys.argv[1], 'r') 

accessions = []
for line in id_list:
    line = line.rstrip("\n")
    accessions.append(line)

gb_output = open(sys.argv[2] + ".gb", "w")
for gb_num in accessions:
    handle = Entrez.efetch(db="nucleotide", id=gb_num, rettype="gb", retmode="text")
    gb_seqs = SeqIO.parse(handle, "gb")
    SeqIO.write(gb_seqs, gb_output, "gb")
handle.close()
gb_output.close()
#genbank file is now downloaded


#parses through genbank file and will put product with those labels in a fasta file
product = sys.argv[3]


with open(sys.argv[2] + ".fasta", 'w') as nfh:
    for rec in SeqIO.parse(sys.argv[2] + ".gb", "genbank"):
        if rec.features:
            for feature in rec.features:
                if feature.type == "CDS" and product in feature.qualifiers['product'][0] :
                    nfh.write(">%s from %s\n%s\n" % (feature.qualifiers['product'][0],
                                                     rec.name, feature.location.extract(rec).seq))



# run as:
# python extractGeneFromAccessionList.py LISTOFGBACCESSIONS.txt PREFIXFORGBANDFASTAFILE SEARCHTERM