__author__ = 'Sulantha'
import sqlite3

class DBClient:
    def __init__(self, db = 'SQLDB/MCI_Conversion'):
        self.conn = sqlite3.connect(db, isolation_level=None)

    def executeAllRes(self, sql):
        res = self.conn.execute(sql)
        return res

    def executeNoResult(self, sql):
        self.conn.execute(sql)
