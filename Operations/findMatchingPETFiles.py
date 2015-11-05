import datetime
from SQLDB.DBClient import DBClient

dbc = DBClient()

getRescSQL = "SELECT * FROM CSV_RESULT_MCI_CONV_DATA"
allResults = dbc.executeAllRes(getRescSQL)
for rec in allResults:
    rec_id = rec[0]
    rid = rec[1]
    d1 = datetime.datetime.strptime(rec[7], '%Y-%m-%d')
    d2 = datetime.datetime.strptime(rec[8], '%Y-%m-%d')

    PETRecsSQL = "SELECT * FROM CSV_SUBJECT_PET_DATA WHERE RID = '{0}' AND SEQ_CODE = '{1}'".format(rid, 'TNL_PP')
    petData = dbc.executeAllRes(PETRecsSQL)
    allPETRECs = []
    for petRec in petData:
        allPETRECs.append([i for i in petRec])

    d1_match_list = []
    d2_match_list = []

    for petLine in allPETRECs:
        da = datetime.datetime.strptime(petLine[4], '%Y-%m-%d')
        if abs((da-d1).days) < 60:
            d1_match_list.append('{0}_{1}'.format(petLine[6], petLine[7]))
        if abs((da-d2).days) < 60:
            d2_match_list.append('{0}_{1}'.format(petLine[6], petLine[7]))

    sql = "INSERT INTO MCI_CONV_PET_MATCH VALUES (NULL, '{0}', '{1}', '{2}', '{3}', '{4}')".format(rid, rec[7], rec[8], ','.join(d1_match_list), ','.join(d2_match_list))
    dbc.executeNoResult(sql)


