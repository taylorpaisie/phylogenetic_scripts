#!/bin/bash

import sys, os
from Bio import AlignIO, SeqIO, Nexus
from Bio import Alphabet

handle = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')

AlignIO.convert(handle, 'fasta', output, 'nexus', alphabet=Alphabet.generic_dna)
