import time
import unittest

class TestObj:
    def __int__(self, testCaseName, **kwargs):
        #[clientId, cadminId, countryCode]
        self.testCaseName = "{0}{1}".format(testCaseName, time.strftime("%Y%m%d%H%M%S"))
        for key, value in ["clientId", "cadminId", "countryCode"]:
            self.key = kwargs[key]

class DayforceDataGenerator:
    def __int__(self, *args):
        self.testObj = TestObj(*args)

    def CreateLegalEntityBankAccount(self):
        print("Create LegalEntity")
        ## Create Legal Entity With Country Code
        legalentity_name = self.testObj.testCaseName
        legalentity_name_long =  self.testObj.testCaseName
        legalentity_name_xrefcode =  self.testObj.testCaseName
        legalentity_address = {}
        if ( self.testObj.countryCode == 'USA'):
            legalentity_address['Address'] = "1111 E. Main Street"
            legalentity_address['Province'] = "VA"
            legalentity_address['Postal Code'] = "23219"

        legalentity_legalidnum = "111111118"  # a 9-digit mod 10 number, Business Number must start with 1, 7 or 8
        legalentity_columns = "(ShortName,LongName,XRefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,CountryCode,Address,GeoCityId,StateCode,PostalCode," \
                              "LegalIdNumber,LegalIdNumberType,Active,EffectiveStart,IsAutoCreated," \
                              "IsValidationRequired,IsNotDisbursePrintToBackOffice,AddressCountryCode,ApplyStatusIndianCalculation)"
        values_str = "VALUES('{3}', '{4}', '{5}', {0}, {1}, {2}, '{6}', '{7}', {12}, '{8}', '{9}'," \
                     "'{10}', 1, 1, '{11}', 0, 0, 0, '{6}', 0)" \
            .format(_client_id, _last_mod_userId, _last_mod_timestamp, legalentity_name, legalentity_name_long,
                    legalentity_name_xrefcode, _country_code, legalentity_address['Address'],
                    legalentity_address['Province'], legalentity_address['Postal Code'],
                    legalentity_legalidnum, _start_date, legal_geocity_id)
        #### if Country Code USA
        #### if Country Code CAN


    def CreateDepartmentAndJob(self):
        print("Department and Job")

    def OrgSetup(self):
        print("Org Setup")
    def CreateGeneralConfiguration(self):
        print("Create General Configuration")

        # Stage1：
        # Create DepJob
        # Create EmployeeSchedulePolicy
        # Create PunchPolicy
        # Create PayHolidayGroup
        # Create Activity
        # Create TimeOffPolicy
        # Create PRPayrollPolicy

        #Stage2:
        # Create Payroll Policy Rule Set
        # Create Payroll AutoPay Rule
        # Create Payroll Earning Rule
        # Create Payroll Deduction Rule
        # Create Payroll Tax Rule
        # Create Payroll Wcb Rule

        #Stage3
        # -- Hourly(Non-Exempt) Hourly(Exempt) Salaried(Exempt) Salaried(Non-Exempt)
        # Set AutoPay policy (set Salary autopay flog true)

        #Stage4
        # Create Pay group
        # Map Pay Group to pay group earning rule set

        #Stage5
        # Calibrate Org Unit
        # Generate Calendar

    def CreateEmployee(self):
        print("Create Employee")

        # Generate Employee Number (get max value of the employee Id)
        # CreateEmployee with ( startDate, Name, CountryCode, StateCode, CityName, [OrgUnitId, DeptId, JobId, PayType, baseSalary, PayGroupId, Employee Status Parameters {pay policyId, timeoff policy, prpayoll policy, punch policy , }]


class DataLoaderTest(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

    def test_a_Init(self):
        print("test Init")

    def test_b_Orgunit(self):
        print("test OrgUnit")

    def test_c_Payroll(self):
        print("test Payroll")

    def test_e_Paygroup(self):
        print ("test paygroup")


    def test_f_Employee(self):
        print("test employee")