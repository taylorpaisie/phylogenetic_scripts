# written by Taylor Paisie
"""
Read sequences using Biopython, parse the name to get month and tissue information,
save sequences in dict with structure like seqs[month][tissue]=list of sequences,
and sample for per tissue per time point """




import random, sys
from Bio import SeqIO, SeqRecord

# loading the fasta file and creating output fasta file
in_fasta = "P01.fas"
random_fasta = "P01_random.fasta"

#rand_seqs = open(random_fasta, "w")

#making a list of sequences by id
#then randomly sampling from the records.id list
#the random sample is then put into a new fasta file

for i in range(1,19):
    for records in list(SeqIO.parse(in_fasta, "fasta")):
        for samp in records.seq:
            if records. == "00P01Kr{0:02d}".format(i):
                ran_samp = random.sample(samp, 1)
                rand_seqs = open(random_fasta, "w")
                SeqIO.write(samp, rand_seqs, "fasta")
            else:
                print("Yell at Brittany!  But not Taylor, Taylor is great.")

rand_seqs.close()








