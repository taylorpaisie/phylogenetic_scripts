import sys
from Bio import SeqIO

#change the fasta file sequence names to a text file list of new ids
#grabbing the file and the names


fasta_file = open(sys.argv[1]+".fa", "r")

new_fasta = open(sys.argv[1]+"_new.fa", "w")

new_ids = open(sys.argv[2], "r")

for f in fasta_file.readlines():
    if f.__contains__(">"):
        new_fasta.write(">" + new_ids.readline() + "\n")
    else:
        new_fasta.write(f)

new_fasta.close()
fasta_file.close()
new_ids.close()