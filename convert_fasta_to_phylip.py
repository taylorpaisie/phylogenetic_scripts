#!/bin/bash python

import sys, os
from Bio import SeqIO

handle = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')


SeqIO.convert(handle, "fasta", output, "phylip")