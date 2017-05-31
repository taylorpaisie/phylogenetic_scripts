# # python script by Taylor Paisie
# run as:
# python /Volumes/IT/PhylodynamicLab/Programs/scripts_python/extractHostAndIsolationSourceGBfile.py OUTPUTFILE

# import genbank file and parse command
import sys
from Bio import SeqIO

print("Enter Genbank file here.")
gb_file = raw_input(">")

# parse genbank file
save_host = open(sys.argv[1] + "_host.txt", "w")
for gb_record in SeqIO.parse(gb_file, "genbank") :
    # now do something with the record
        save_host.write(gb_record.name+"\t"),   # print genbank accession number with no new line
        for feat in gb_record.features:
                if feat.type == 'source':
                        source = gb_record.features[0]
                        for qualifiers in source.qualifiers:
                            if qualifiers == 'host':
                                host = source.qualifiers['host']
                                save_host.write(host[0]+"\n"),  #prints the host with no new line
save_host.close()


save_iso_source = open(sys.argv[1] + "_isolation_source.txt", "w")
for gb_record in SeqIO.parse(gb_file, "genbank") :
    # now do something with the record
        save_iso_source.write(gb_record.name+"\t"),   # print genbank accession number with no new line
        for feat in gb_record.features:
                if feat.type == 'source':
                        source = gb_record.features[0]
                        for qualifiers in source.qualifiers:
                            if qualifiers == 'isolation_source':
                                iso_source = source.qualifiers['isolation_source']
                                save_iso_source.write(iso_source[0]+"\n"),
                                #prints the isolation source with no new line
save_iso_source.close()


