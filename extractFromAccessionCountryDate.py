# python script by Taylor Paisie
# run as:
# python /Volumes/IT/PhylodynamicLab/Programs/scripts_python/extractFromAccessionCountryDate.py INPUTFILE OUTPUTFILE

import sys, os
import urllib
import time
from Bio import SeqIO, Entrez
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature
from ftplib import FTP
from urllib.error import HTTPError

# print("Your NCBI API key")
Entrez.api_key = "b8558abb22f17ea43a6fc07d48097c50a208"
print("NCBI needs your email.")
Entrez.email = input(str(">"))
print("Now the governement has your email address. Muahaha.")


# this is your text file with the GB accession numbers
id_list = open(sys.argv[1], 'r')

accessions = []
for line in id_list:
    line = line.rstrip("\n")
    accessions.append(line)


gb_output = open(sys.argv[2] + ".txt", "w")

for gb_num in accessions:
    handle = Entrez.efetch(db="nuccore", id=gb_num, rettype="gb", retmode="text")
    gb_seqs = SeqIO.parse(handle, "gb")
    SeqIO.write(gb_seqs, gb_output, "gb")
handle.close()
gb_output.close()
# genbank file is now downloaded

# extract country and collection date from genbank file
gb_file = open(sys.argv[2] + ".txt", "r")
#extract country and collection date from genbank file
#take out accession numbers and country in a text file
save_country = open(sys.argv[2] + "_country.txt", "w")
for gb_record in SeqIO.parse(gb_file, "gb") :
    # now do something with the record
        save_country.write(gb_record.name+"\t"),   # print genbank accession number with no new line
        for feat in gb_record.features:
                if feat.type == 'source':
                        source = gb_record.features[0]
                        for qualifiers in source.qualifiers:
                            if qualifiers == 'country':
                                country = source.qualifiers['country']
                                save_country.write(country[0]+"\n"),  #prints the country with no new line
save_country.close()
gb_file.close()

gb_file = open(sys.argv[2] + ".txt", "r")
#take out accession numbers and collection date in a text file
# parse genbank file
save_date = open(sys.argv[2] + "_date.txt", "w")
for gb_record in SeqIO.parse(gb_file, "gb"):
    # now do something with the record
        save_date.write(gb_record.name+"\t"),   # print genbank accession number with no new line
        for feat in gb_record.features:
                if feat.type == 'source':
                        source = gb_record.features[0]
                        for qualifiers in source.qualifiers:
                                if qualifiers == 'collection_date':
                                        date = source.qualifiers['collection_date']
                                        save_date.write(date[0] + "\n"),  # prints the country with no new line
save_date.close()
gb_file.close()


