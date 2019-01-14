#first uploading the list of IDs using EPost
#can refer to the long list of IDs and download the associated data with EFetch
import sys, os
import urllib
import time
from Bio import SeqIO, Entrez
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature
from ftplib import FTP
from urllib.error import HTTPError


Entrez.api_key = "b8558abb22f17ea43a6fc07d48097c50a208"
print("NCBI needs your email.")
Entrez.email = input(str(">"))
print("Now the governement has your email address. Muahaha.")

id_list = open(sys.argv[1], 'r')

accessions = []
for line in id_list:
    line = line.strip()
    accessions.append(line)

fasta_output = open(sys.argv[2], "w")
for num in accessions:
    handle = Entrez.efetch(db="nuccore", id=num, rettype="fasta")
    fasta_seqs = SeqIO.parse(handle, "fasta")
    SeqIO.write(fasta_seqs, fasta_output, "fasta")
handle.close()
fasta_output.close()



#fasta file
