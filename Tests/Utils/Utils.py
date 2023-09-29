class Utils:

    def __init__(self, engine):
        self.engine = engine

    def _getCurrentIdValue(self,tableName):
        sql = "SELECT IDENT_CURRENT('{0}') as id".format(tableName)
        id = int(self.engine.execute(sql).fetchone().id)
        return id

    def _getColumnValue(self, tableName, colName, whereclause):
        sql = "SELECT {0} as id FROM {1} WHERE {2}".format(colName, tableName, whereclause)
        id = self.engine.execute(sql).fetchone().id
        # print(id,flush=True)
        return id

    def _printSqlWithId(sql, id):
        print(sql + ": [id:" + str(id) + "]")

    def _execSql(self, sql, tableName, toprint=False):
        self.engine.execute(sql)
        if (toprint):
            id = self._getCurrentIdValue(tableName)
            self._printSqlWithId(sql, id)
            # print(sql + ": [id:" + str(id) + "]")

    def _execSqlWithResult(self, sql, tableName, toprint=False):
        self.engine.execute(sql)
        id = self._getCurrentIdValue(tableName)
        if (toprint):
            self._printSqlWithId(sql, id)
            # print(sql + ": [id:" + str(id) + "]")
        return id

    def _execSqlWithId(self, sql, toprint=False):
        id = self.engine.execute(sql).fetchone().id
        if (toprint):
            self._printSqlWithId(sql, id)
            # print(sql + ": [id:" + str(id) + "]")
        return id

    def _execInsertValuesOutputId(self, tableName, values):
        # sql = "INSERT INTO {0} Output inserted.{0}Id as id {1}".format(tableName, values)
        sql = "INSERT INTO {0} OUTPUT inserted.{0}Id as id VALUES({1})".format(tableName, values)
        id = self.engine.execute(sql).fetchone().id
        self._printSqlWithId(sql, id)
        return id

    def _execInsertOutputId(self, tableName, columns, values, toprint=False):
        sql = "INSERT INTO {0} {1} {2}".format(tableName, columns, values)
        self.engine.execute(sql)
        id = self._getCurrentIdValue(tableName)
        if (toprint):
            self._printSqlWithId(sql, id)
        return id

    def _execInsert(self, tableName, columns, values, toprint=False):
        sql = "INSERT INTO {0} {1} {2}".format(tableName, columns, values)
        self.engine.execute(sql)
        if (toprint):
            id = self._getCurrentIdValue(tableName)
            self._printSqlWithId(sql, id)
