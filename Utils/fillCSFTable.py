__author__ = 'Sulantha'
import csv
from SQLDB.DBClient import DBClient
DBClient = DBClient()
CSFFile = 'CSVFiles/CSV_SUBJECT_CSF_DATA.csv'

with open(CSFFile, 'rU') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for line in csv_reader:
        sql = "INSERT OR REPLACE INTO CSV_SUBJECT_CSF_DATA VALUES (NULL, '{0}', '{1}', '{2}', '{3}', '{4}')".format(line[0], line[1], line[2], line[3], line[4])
        DBClient.executeNoResult(sql)