# python script by Taylor Paisie
#must have biopython install on computer

import sys, os
from Bio import SeqIO, Entrez
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature

Entrez.api_key = "b8558abb22f17ea43a6fc07d48097c50a208"
print("NCBI needs your email.")
Entrez.email = input(str(">"))
print("Now the governement has your email address. Good luck hiding that internet history now.  Muahaha. ")


# this is your text file with the GB accession numbers
#print("Input your text file with the GB accession numbers")
id_list = open(sys.argv[1], 'r') 

accessions = []
for line in id_list:
    line = line.rstrip("\n")
    accessions.append(line)

gb_output = open(sys.argv[2] + ".txt", "w")
for gb_num in accessions:
    handle = Entrez.efetch(db="nucleotide", id=gb_num, rettype="gb", retmode="text")
    gb_seqs = SeqIO.parse(handle, "gb")
    SeqIO.write(gb_seqs, gb_output, "gb")
handle.close()
gb_output.close()
#genbank file is now downloaded


#parses through genbank file and will put product with those labels in a fasta file
gb_file = open(sys.argv[2] + ".txt", "r")
#take out accession numbers and collection date in a text file
# parse genbank file
save_subtype = open(sys.argv[2] + "_subtype.txt", "w")
for gb_record in SeqIO.parse(gb_file, "gb"):
    # now do something with the record
        save_subtype.write(gb_record.name+"\t"),   # print genbank accession number with no new line
        for feat in gb_record.features:
                if feat.type == 'source':
                        source = gb_record.features[0]
                        for qualifiers in source.qualifiers:
                                if qualifiers == 'note':
                                        subtype = source.qualifiers['note']
                                        save_subtype.write(subtype[0] + "\n"),  # prints the country with no new line
save_subtype.close()
gb_file.close()



# run as:
# python extractGeneFromAccessionList.py LISTOFGBACCESSIONS.txt PREFIXFORGBANDFASTAFILE SEARCHTERM