import csv

def add_wps():
    # open the file in the write mode
    with open('weapon_chart.csv', 'a', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)
        thing = "SolKatti	Prf	1	14	12	95	25	30	–	2".split()
        # write a row to the csv file
        writer.writerow(thing)

def add_player(msg):
    with open('unit_chart.csv', 'a', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)
        thing = msg.split(sep="	", maxsplit=13)
        # write a row to the csv file
        writer.writerow(thing)


if __name__ == '__main__':
    msg = "Wallace	Knight	12	30	13	7	5	10	15	2	13	4	Thunder	Lance A"
    add_player(msg)