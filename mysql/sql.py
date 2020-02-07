import pymysql as mysql

class Sql:
    def __init__(self,localhost,username,password,dbname):
        self.db = mysql(localhost,username,password,dbname)
        self.cursor = self.db.cursor()

    def _execute(self,sql):
        return self.cursor.execute(sql)

    def get_data_one(self,sql):
        self._execute(sql)
        return self.cursor.fetchone()

    def get_data_all(self,sql):
        self._execute(sql)
        return self.cursor.fetchall()

    def get_data_count(self,tablename):
        sql = "select count(*) from {}".format(tablename)
        return self._execute(sql)