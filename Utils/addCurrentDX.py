__author__ = 'Sulantha'
from SQLDB.DBClient import DBClient
DBClient = DBClient()
getAllRecsSQL = "SELECT RID FROM CSV_SUBJECT_DX_DATA"

dxCodeDict = {"NL":1, "Dementia":3,"MCI":2}
dxSTRDict = {1:'CN', 3:'AD', 2:'MCI'}


allRes = DBClient.executeAllRes(getAllRecsSQL)
for rec in allRes:
    subRID = rec[0]
    allRecsForSub = "SELECT * FROM CSV_SUBJECT_DX_DATA WHERE RID = '{0}' ORDER BY VISCODE ASC".format(subRID)
    subResults = DBClient.executeAllRes(allRecsForSub)

    subDXList = []

    for subRec in subResults:
        dx = subRec[19]
        if dx == '':
            subDXList.append(0)
            continue
        if 'to' in dx:
            dx = dx.split('to')[1].strip()
        dxCode = dxCodeDict[dx]
        subDXList.append(dxCode)

    allRecsForSub = "SELECT * FROM CSV_SUBJECT_DX_DATA WHERE RID = '{0}' ORDER BY VISCODE ASC".format(subRID)
    subResults = DBClient.executeAllRes(allRecsForSub)
    idx = 0

    for newsubRec in subResults:
        oldDX = subDXList[idx]
        if oldDX is 0 and idx is 0 and len(subDXList) > 1:
            try:
                newDX = next(filter(lambda x: x!=0, subDXList))
            except StopIteration:
                newDX = 0
            subDXList[0] = newDX
        if oldDX is 0 and idx is 0 and len(subDXList) == 1:
            newDX = 0

        if oldDX is 0 and idx > 0:
            newDX = subDXList[idx-1]
            subDXList[idx] = newDX
        if oldDX is not 0:
            newDX = oldDX
        record_id = newsubRec[0]

        if newDX is 0:
            sql = "UPDATE CSV_SUBJECT_DX_DATA SET DX_Current_TNL = '{0}', DX_Current_Code_TNL = '{1}' WHERE RECORD_ID = '{2}'".format('','',record_id)
        else:
            sql = "UPDATE CSV_SUBJECT_DX_DATA SET DX_Current_TNL = '{0}', DX_Current_Code_TNL = '{1}' WHERE RECORD_ID = '{2}'".format(newDX, dxSTRDict[newDX], record_id)
        print(sql)
        idx += 1
        DBClient.executeNoResult(sql)




