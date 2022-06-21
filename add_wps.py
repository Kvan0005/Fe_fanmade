import csv

# open the file in the write mode
with open('weapon_chart', 'a', encoding='UTF8') as f:
    # create the csv writer
    writer = csv.writer(f)
    thing = "SolKatti	Prf	1	14	12	95	25	30	–	2".split()
    # write a row to the csv file
    writer.writerow(thing)