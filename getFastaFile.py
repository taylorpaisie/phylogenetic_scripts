#first uploading the list of IDs using EPost
#can refer to the long list of IDs and download the associated data with EFetch
from Bio import Entrez, SeqIO
import sys


Entrez.email = "tpaisie@ufl.edu"

id_list = open(sys.argv[1])

accessions = []
for line in id_list:
    line = line.strip()
    accessions.append(line)

fasta_output = open(sys.argv[2], "w")
for num in accessions:
    handle = Entrez.efetch(db="nucleotide", id=num, rettype="fasta")
    fasta_seqs = SeqIO.parse(handle, "fasta")
    SeqIO.write(fasta_seqs, fasta_output, "fasta")
handle.close()
fasta_output.close()



#fasta file



