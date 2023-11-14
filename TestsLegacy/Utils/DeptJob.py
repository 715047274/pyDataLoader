class DeptJob:

    def __init__(self,uniqueId, jobName, depName, client_id = 10000 ):
        self.jobName = jobName
        self.depName = depName
        self.uniqueId = uniqueId
        dept_name = "{0}Dept{1}".format(depName, uniqueId)
        dept_name_long = "long " + depName
        dept_name_xrefcode = "xref " + depName

        # values_str = "'{3}','{4}',NULL,{0},{1},{2},'{5}',NULL" \
        #     .format(client_id, _last_mod_userId, _last_mod_timestamp, dept_name, dept_name_long,
        #             dept_name_xrefcode)
