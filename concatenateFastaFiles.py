#!/usr/bin/env python
# python script by Taylor Paisie
# combines chr1 and chr2 into one sequences in the fasta file
# changes the name of the sequence to the name of the fasta file for combination of fasta files


import sys, glob, os
from Bio import SeqIO, Seq
from Bio.Alphabet import SingleLetterAlphabet

concat = Seq.Seq("", SingleLetterAlphabet())

# Loop through all sequences and concatenate into concat var
for fasta_file in glob.glob(os.path.join(sys.argv[1], "*.fasta")):
	concat = Seq.Seq("", SingleLetterAlphabet())
	for s in SeqIO.parse(fasta_file, "fasta"):
		concat += s
	print(fasta_file)


	concat.id = os.path.basename(fasta_file[:-13])
	concat.description = ""
	SeqIO.write(concat, fasta_file[:-13] + ".fasta", "fasta")

# to combine multiple fasta files:
# cat *.fa > all_seqs.fa