from Bio import SeqIO
import sys, glob

file_list = glob.glob(sys.argv[1])

with open(sys.argv[2], 'w') as w_file:
    for filen in file_list:
        with open(filen, 'rU') as o_file:
            seq_records = SeqIO.parse(o_file, 'fasta')
            SeqIO.write(seq_records, w_file, 'fasta')



#combines fasta files one by one

