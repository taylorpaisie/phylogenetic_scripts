# filtering by record name
# pulling out particular sequences from a large fasta (sequence) file
# cat FILENAME | curl -F 'gob=<-' gobin.io
# curl gobin.io/* > FILENAME
# perl -pi -e 's/\r/\n/g' to a text file saved in excel

import sys
from Bio import SeqIO

input_file = sys.argv[1]
id_file = sys.argv[2]
output_file = sys.argv[3]

wanted = list(line.rstrip("\n").split(None, 1)[0] for line in open(id_file))
print(wanted)
print("Found %i unique identifiers in %s" % (len(wanted), id_file))
records = (r for r in SeqIO.parse(input_file, "fasta") if r.id in wanted)
count = SeqIO.write(records, output_file, "fasta")
print("Saved %i records from %s to %s" % (count, input_file, output_file))
if count < len(wanted):
    print("Warning %i IDs not found in %s" % (len(wanted) - count, input_file))
