# written by Taylor Paisie
"""
Read sequences using Biopython, parse the name to get month and tissue information,
save sequences in dict with structure like seqs[month][tissue]=list of sequences,
and sample for per tissue per time point """




import random
from Bio import SeqIO

# loading the fasta file and creating output fasta file
in_fasta = "P01.fas"
random_fasta = "P01_random.fasta"

#rand_seqs = open(random_fasta, "w")

#making a list of sequences by id
#then randomly sampling from the records.id list
#the random sample is then put into a new fasta file

for i in range(1,19):
    with open(in_fasta, "r") as f_in:
        for record in SeqIO.parse(f_in, "fasta"):
            if record.id in record == "00P01Kr{0:02d}".format(i):
                subsamp = random.sample(1)
                rand_seqs = open(random_fasta, "w")
                SeqIO.write(subsamp, rand_seqs, "fasta")
            else:
                print("Yell at Brittany!  But not Taylor, Taylor is great.")





        #for samp in records.seq:
            #if records.id == "00P01Kr{0:02d}".format(i):
                #handle = random.sample(samp, 1)
                #rand_seq = SeqIO.write(ran_samp, random_fasta, "fasta")
            #else:
                #print("Yell at Brittany!  But not Taylor, Taylor is great.")









