__author__ = 'Sulantha'
from SQLDB.DBClient import DBClient
import csv

newPETCSV = 'CSVFiles/CSV_RESULT_MCI_CONV_DATA.csv'
DBC = DBClient()

getAllMCIAtanyPointRIDs = "SELECT DISTINCT RID FROM CSV_SUBJECT_DX_DATA WHERE DX_Current_Code_TNL = 'MCI'"
allRIDs = DBC.executeAllRes(getAllMCIAtanyPointRIDs)
finalList = [['RID', 'DX_BL', 'REC_ID_1', 'REC_ID_2', 'VISCODE_1', 'VISCODE_2', 'EXAM_DATE_1', 'EXAM_DATE_2', 'DX_1', 'DX_2', 'CONV']]

for rid in allRIDs:
    allSubjectINFOSQL = "SELECT * FROM CSV_SUBJECT_DX_DATA WHERE RID = '{0}' ORDER BY VISCODE ASC".format(rid[0])
    allSubjectINFO = DBC.executeAllRes(allSubjectINFOSQL)
    subRecs = []
    for subRec in allSubjectINFO:
        subRecs.append(subRec)

    if len(subRecs) == 1:
        print("Only one rec found. Skipping. - {0}".format(subRecs[0]))

    for rec in subRecs:
        vis = 0 if rec[2] == 'bl' else int(rec[2][1:])
        vis24_str = 'm{0}'.format(vis+24)
        visit24_rec = None
        for newRec in subRecs:
            if newRec[2] == vis24_str:
                visit24_rec = newRec
                break
        if visit24_rec:
            if rec[21] == 'MCI':
                conv = 1 if newRec[21] == 'AD' else 0
                finalList.append([rec[1], rec[4], rec[0], newRec[0], rec[2], newRec[2], rec[3], newRec[3], rec[21], newRec[21], conv])

with open(newPETCSV, 'wt') as outCSV:
        csv_writer = csv.writer(outCSV)
        csv_writer.writerows(finalList)

