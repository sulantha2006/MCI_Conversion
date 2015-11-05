__author__ = 'Sulantha'

import csv

def getNewRID(subID, prefix):
    if prefix in subID:
        return subID
    if len(subID) == 1:
        subID = '000{0}'.format(subID)
    elif len(subID) == 2:
        subID = '00{0}'.format(subID)
    elif len(subID) == 3:
        subID = '0{0}'.format(subID)
    elif len(subID) == 4:
        subID = subID
    return '{0}{1}'.format(prefix, subID)

def fixRID(csvFile, header):
    fileContents = list(csv.reader(open(csvFile)))
    idx = 0

    with open(csvFile, 'rU') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if header:
                idx += 1
                header = False
                continue
            ident = row[0]
            newRID = getNewRID(ident, 'ADNI')
            fileContents[idx] = row[1:]
            fileContents[idx].insert(0, newRID)
            idx += 1

    with open(csvFile, 'wt') as outCSV:
        csv_writer = csv.writer(outCSV)
        csv_writer.writerows(fileContents)

fixRID('/Users/Sulantha/PycharmProjects/MCI_Conversion/CSVFiles/CSV_SUBJECT_CSF_DATA.csv', True)