# written by Taylor Paisie with Luke Jolly's help (he made me put this)
# running script:
# python randomSampling.py INPUT_FASTA OUTPUT_FASTA
# prompts user for number of randomly selected samples

import sys
import random
from Bio import SeqIO

# loading the fasta file and creating output fasta file
if len(sys.argv) < 3:
    print("ERROR: missing required arguments (input fasta, output fasta). RESISTANCE IS FUTILE.")
    sys.exit(1)

in_fasta = sys.argv[1]
random_fasta = sys.argv[2]

print("HOW MANY RANDOMLY SELECTED SAMPLES WOULD YOU LIKE HUMAN?")
num_samples = int(raw_input(">"))
print("I'm sorry, Dave. I'm afraid I can't do that. Just kidding.")

#rand_seqs = open(random_fasta, "w")

#making a list of sequences by id
#then randomly sampling from the records.id list
#the random sample is then put into a new fasta file

# Compile list of records to randomly chose from
all_records = {}
with open(in_fasta, "r") as f_in:
    for record in list(SeqIO.parse(f_in, "fasta")):
        # Name scheme broken out
        #month = record.id[0:2]
        #patient = record.id[2:5]
        #tissue_type = record.id[5]
        #mol_type = record.id[6]
        #seq_num = record.id[7:9]
        prefix = record.id[0:6]

        # If this if the first time we've encountered this prefix,
        # create a empty list
        if prefix not in all_records.keys():
            all_records[prefix] = []
        all_records[prefix].append(record)


# making a list of selected random records (samples)
random_records = []
for prefix, records in all_records.iteritems():
    if num_samples > len(records):
        print("WARN: only %i samples in group %s, selecting all." % (len(records), prefix))
        print("")
        random_records.extend(records)
    else:
        for i in range(1, num_samples + 1):
            x = random.randint(0, len(records) - 1)
            random_records.append(records[x])
            del(records[x])


# writing random_records to a fasta file
SeqIO.write(random_records, random_fasta, "fasta")