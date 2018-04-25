# python script by Taylor Paisie
# run as:
# python /Volumes/IT/PhylodynamicLab/Programs/scripts_python/extractFromAccessionCountryDate.py INPUTFILE OUTPUTFILE


from ftplib import FTP
import sys, os
from Bio import SeqIO, Entrez

print("NCBI needs your email.")
Entrez.email = input(str(">"))
print("Now the governement has your email address. Muahaha.")


# this is your text file with the GB accession numbers
id_list = open(sys.argv[1])

accessions = []
for line in id_list:
    line = line.rstrip("\n")
    accessions.append(line)

gb_output = open(sys.argv[2] + ".xml", "w")
for gb_num in accessions:
    handle = Entrez.efetch(db="nucleotide", id=gb_num, rettype="xml", retmode="xml")
    gb_seqs = SeqIO.parse(handle, "seqxml")
    SeqIO.write(gb_seqs, gb_output, "seqxml")
handle.close()
gb_output.close()
#genbank file is now downloaded

#extract country and collection date from genbank file
gb_file = open(sys.argv[2] + ".xml", "r")
#extract country and collection date from genbank file
#take out accession numbers and country in a text file
save_country = open(sys.argv[2] + "_country.txt", "w")
for gb_record in SeqIO.parse(gb_file, "seqxml") :
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

gb_file = open(sys.argv[2] + ".xml", "r")
#take out accession numbers and collection date in a text file
# parse genbank file
save_date = open(sys.argv[2] + "_date.txt", "w")
for gb_record in SeqIO.parse(gb_file, "seqxml"):
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