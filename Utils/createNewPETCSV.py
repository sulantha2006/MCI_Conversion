__author__ = 'Sulantha'
import csv

newPETCSV = 'CSVFiles/CSV_SUBJECT_PET_DATA.csv'
oldPETCSV = 'CSVFiles/ADNI_PET_META_LIST.csv'

fileContents = [['RID', 'PET_VISCODE', 'ADNI12', 'SCAN_DATE', 'SEQ_CODE', 'S_ID', 'I_ID', 'ADNI_PROC', 'ADNI_SUBJECT', 'ADNI_VISIT', 'ADNI_SEQ']]
ADNI_visitCode_Dict = {
    'ADNI1 Baseline': 'ad1_bl',
    'ADNI1/GO Month 6': 'adg_m6',
    'ADNI2 Year 1 Visit': 'ad2_m12',
    'ADNI2 Baseline-New Pt': 'ad2_bl',
    'ADNI1/GO Month 12': 'adg_m12',
    'ADNIGO Month 60': 'adg_m60',
    'ADNI1/GO Month 36': 'adg_m36',
    'ADNI1/GO Month 18': 'adg_m18',
    'ADNI2 Year 2 Visit': 'ad2_m24',
    'ADNI2 Initial Visit-Cont Pt': 'ad2_bl',
    'ADNI2 Initial Visit-New Pt': 'ad2_bl',
    'ADNI1/GO Month 24': 'adg_m24',
    'ADNI1/GO Month 48': 'adg_m48',
    'ADNI2 Year 3 Visit': 'ad2_m36',
    'ADNI2 Year 4 Visit}': 'ad2_m48',
    'ADNI1 Screening': 'ad1_sc',
    'ADNIGO Month 72': 'adg_m72',
    'Unscheduled': 'und',
    'No Visit Defined': 'und',
    'ADNI2 Year 4 Visit': 'ad2_m48',
    'ADNIGO Screening MRI': 'adg_sc',
    'ADNIGO Month 3 MRI': 'adg_m3',
    'ADNI2 Screening MRI-New Pt': 'ad2_sc',
    'ADNI2 Month 3 MRI-New Pt': 'ad2_m3',
    'ADNI2 Month 6-New Pt': 'ad2_m6',
    'ADNI2 No Visit Defined':'und'
}

def getVisCode(ADNI_VISIT):
    return ADNI_visitCode_Dict[ADNI_VISIT]

def getSEQ(ADNI_SEQ, ADNI_PROC):
    if 'Coreg, Avg, Std Img and Vox Siz, Uniform Resolution' in ADNI_SEQ:
        return 'TNL_PP'
    if ADNI_PROC == 'Original':
        return 'TNL_RW'
    return ''

def getADNI(ADNI_VISIT):
    if 'ADNI1' in ADNI_VISIT:
        return 'ADNI1'
    if 'ADNI2' in ADNI_VISIT:
        return 'ADNI2'

with open(oldPETCSV, 'rU') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            ADNI_PROC = row[0]
            ADNI_SUB = row[1]
            ADNI_VISIT = row[2]
            ADNI_SEQ = row[3]
            SCAN_DATE = row[4]
            S_ID = row[6]
            I_ID = row[7]
            ADNI12 = getADNI(ADNI_VISIT)

            RID = 'ADNI{0}'.format(ADNI_SUB.split('_')[-1])
            ADNI_VISCODE = getVisCode(ADNI_VISIT)
            SEQ_CODE = getSEQ(ADNI_SEQ, ADNI_PROC)

            fileContents.append([RID, ADNI_VISCODE, ADNI12, SCAN_DATE, SEQ_CODE, S_ID, I_ID, ADNI_PROC, ADNI_SUB, ADNI_VISIT, ADNI_SEQ])

with open(newPETCSV, 'wt') as outCSV:
        csv_writer = csv.writer(outCSV)
        csv_writer.writerows(fileContents)
