import sys, os
import urllib
import time
from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SearchIO, Entrez
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature
from ftplib import FTP
from urllib.error import HTTPError

#first uploading the list of IDs using EPost
#can refer to the long list of IDs and download the associated data with EFetch
Entrez.api_key = "b8558abb22f17ea43a6fc07d48097c50a208"
print("NCBI needs your email.")
Entrez.email = input(str(">"))
print("Now the governement has your email address. Muahaha.")

id_list = open(sys.argv[1], 'r')

accessions = []
for line in id_list:
    line = line.strip()
    accessions.append(line)

gb_output = open(sys.argv[2], "w")
for gb_num in accessions:
    gb_handle = Entrez.efetch(db="nucleotide", id=gb_num, rettype="gb", retmode="text")
    gb_seqs = SeqIO.parse(gb_handle, "gb")
    SeqIO.write(gb_seqs, gb_output, "gb")
gb_handle.close()
gb_output.close()



