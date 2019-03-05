import  csv


def import_sample_data():
    with open('./sample_data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for element in readCSV:
            print('date %s' % element)


import_sample_data()