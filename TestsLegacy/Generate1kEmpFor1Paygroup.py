#__author__ = 'kevinz'

# TFS732418
# Please update the python setup scripts with the following requirements:
#
# General Requirements:
#
# Ability to create any number of additional Dayforce Users (Employees with User Logins), linking each to a specified paygroup for a specified client instance
# - Each additional user should have "On-Demand Pay" enabled (EligibleForOnDemandPay in Employee table)
# - Each additional user should have an EmployeeEmploymentStatus based on the specified instance
# - Each additional user should have a primary EmployeeWorkAssignment based on the specified instance
#
# Specific Requirements:
#
# Initially, we want to create 100 additional Dayforce Users on the following client instance:
#   Site: int.dayforce.com/odp
#   Client Instance: intodp_700140 (cadmin/1)
#   DB Server: ncintdb01
#   Make all the users Salaried - auto-paid (so we don’t have to create quick entries). Salary = 100,000.
#   Each additional user should have a US Mobile phone number (PersonContact table)
#   Link to Paygroup: QA USA BW (paygroupId=9)
#   Sample of existing user:
#      select * from employee where employeeid=1015
#      select * from employeeemploymentstatus where employeeid=1015
#      select * from employeeworkassignment where employeeid=1015#

from Tests.DbSetUp.database import engine
    #as db
from datetime import datetime,timedelta,date
from dateutil.rrule import *
from dateutil.relativedelta import *
#from ddt import ddt, data
from itertools import cycle
import unittest
import holidays

import time
import random

#engine = db


"""
Data Generator
"""

"""
[SQL for Org setUp]
"""
legalEntity_prefix ="(ShortName,LongName,PayMasterLegalEntityId,XRefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,CountryCode,Address,Address2,GeoCityId,StateCode,PostalCode,County,LegalIdNumber,LegalIdNumberType,Active,EffectiveStart,EffectiveEnd,EIReferenceCode,IsAutoCreated,IsValidationRequired,PreferenceCodeId,IsNotDisbursePrintToBackOffice,CustomerImplementationStatusId,AddressCountryCode,TerritorialGeoStateId,PreferenceCodeExtended,CPPCalculationOptionForStatusIndianId,ApplyStatusIndianCalculation,PRProcessForEmploymentId,PRTaxElectionId)"
#legalEntity_insurance ="(LegalEntityEmployeeInsuranceId,LegalEntityId,ReferenceCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,RateGroup,IsDefault,LegalEntityEmployeeInsurancePreferenceCodeId,PreferenceCodeExtended)"
#legalEntity_insurance_rate_prefix="(LegalEntityEmployeeInsuranceRateId,LegalEntityEmployeeInsuranceId,Rate,EffectiveStart,EffectiveEnd,ClientId,LastModifiedUserId,LastModifiedTimestamp)"
department_prefix="(ShortName,LongName,LabelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,XRefCode,LedgerCode)"
job_prefix="(ShortName,LongName,LabelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,PunchPolicyId,XrefCode,JobRank,DFPayGradeId,JobQualifications,FLSAStatusId,EmployeeEEOId,JobClassificationId,LedgerCode,JobFamilyId,JobFunctionId,JobUDFString1,JobUDFString2,JobUDFString3,DFUnionId,IsUnionJob,EffectiveStart,EffectiveEnd,NOC)"
deptjob_prefix="(DepartmentId,JobId,ClientId,LastModifiedUserId,LastModifiedTimestamp,CreationOrgUnitId,EffectiveStart,EffectiveEnd,ShortCode,LedgerCode,ClockTransferCode,IsNonService,DefaultHue,StandardCostRate,ShortName,LongName,PayClassId,PayTypeId,Officer,Executive,Status,EmploymentIndicatorId,FTE,PositionTermId,WeeklyHours,AverageDailyHours,SemiMonthlyTopHours,SemiMonthlyBottomHours,PayGroupId,IsWCBExempt,XRefCode,PPACAFullTime)"
orgunit_prefix="(ShortName,LongName,OrgLevelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,IsStoreFlag,XRefCode,PhysicalLocation,LedgerCode,BusinessPhone,ContactName,ContactBusinessPhone,ContactCellPhone,Address,Address2,StateCode,PostalCode,CountryCode,OpeningDate,ClosingDate,ComparableOrgUnitId,ClockTransferCode,DepartmentId,ZoneId,OrgGroupId,StartDOW,GeoCityId,TimezoneId,County,IsAddressChanged,ComDataAccountId,IsOrgManaged,PsdCode,IsMobileOrg,DescriptiveLocation,Coordinates,LastModifiedCoordinateTime,TaxLocationAddressId)"
orgunit_legalEntity_prefix="(OrgUnitId, LegalEntityId, LegalEntityWorkSiteStateId, EffectiveStart, EffectiveEnd, ClientId, LastModifiedUserId, LastModifiedTimestamp, PRBankAccountBranchAddressId, LegalEntityMasterBankAccountSettingId)"
#orgunitParent_prefix="(OrgUnitId,ParentOrgUnitId,EffectiveStart,EffectiveEnd,ClientId,LastModifiedUserId,LastModifiedTimestamp,OrgUnitParentLeft,OrgUnitParentRight,ClosestPhysicalLocationOrgUnitId,ClosestAddressOrgUnitId,ClosestTaxationAddressOrgUnitId,ClosestTimeZoneOrgUnitId)"

"""
[SQL for payRoll Setup Earning, Deduction, Tax]
"""
appuser_prefix ="(UserId,LoginId,Password,Description,IsApproved,IsLockedOut,CreateTimestamp,LastLoginTimestamp,LastPasswordChangedTimestamp,LastLockoutTimestamp,FailedPasswordAttemptCount,FailedPasswordAttemptWindowStart,FailedPasswordAnswerAttemptCount,FailedPasswordAnswerAttemptWindowStart,ClientId,LastModifiedUserId,LastModifiedTimestamp,CultureID,CanSeeSelf,ResetOnNextLogin,ShowDisclaimer,UsesOrgSecurity,LogMode,EntityTypeId,IsDeleted,Display24HourTime,NumberDisplayCultureId,SecurityQuestionId1,SecurityQuestionId2,HashMethod,IsPinLockedOut,LastPinLockoutTimestamp,FailedPinAttemptCount,FailedPinAttemptWindowStart,IsBiometricLockedOut,LastBiometricLockoutTimestamp,FailedBiometricAttemptCount,FailedBiometricAttemptWindowStart,DefaultPasswordExpiryTimestamp,AnswersHashMethod,Answer1,Answer2,ShowEmailMissing,HasAcceptedPrivacyPolicy,HasAcceptedTermsOfUse,LegalAgreementsAcceptedTimestamp,LastSessionType)"
employee_prefix ="(EmployeeId,ManagerId,LastName,FirstName,MiddleName,HomePhone,Address,Address2,City,StateCode,PostalCode,BirthDate,HireDate,TaxpayerId,EmergencyContact,EmergencyPhone,EmergencyCellPhone,AvatarUri,ClientId,LastModifiedUserId,LastModifiedTimestamp,XRefCode,Title,Suffix,Gender,BadgeNumber,RegisteredDisabled,BusinessPhone,CountryCode,StartDate,SocialSecurityNumber,EmergencyBusinessPhone,EmergencyContact2,EmergencyPhone2,EmergencyCellPhone2,EmergencyBusinessPhone2,EmergencyEmail,EmergencyEmail2,CommonName,CultureId,ClockSupervisor,EmergencyContactRelationshipTypeId,EmergencyContact2RelationshipTypeId,TaxExempt,SchoolYearId,ChecksumTimestamp,NewHireApproved,NewHireApprovedBy,NewHireApprovalDate,SeniorityDate,DisplayName,BioExempt,EmployeePin,ExportDate,CitizenshipTypeId,SSNExpiryDate,MaidenName,PreferredLastName,EligibleForRehire,TerminationDate,DateOfDeath,EstimatedReturnDate,RequiresExitInterview,ExitInterviewerEmployeeId,IsAboriginal,IsVisibleMinority,VeteranSeparationDate,PRPayrollTaxLocalJurisdictionId,LastPayrollNewHireExportDate,LastModifiedHRImportTimestamp,BioSensitivityLevelId,OriginalHireDate,COBRANotificationStatus,COBRANotificationSentDate,PhotoExempt,PPACAOverrideDate,SSNCountryCode)"
personAddress_prefix ="(PersonId,CountryCode,Address1,Address2,Address3,City,StateCode,PostalCode,ContactInformationTypeId,EffectiveStart,EffectiveEnd,LastModifiedUserId,LastModifiedTimestamp,ClientId,County,LastModifiedHRImportTimestamp,IsPayrollMailing,Address4)"
employeeEmploymentStatus_prefix ="(EmploymentStatusId,PayTypeId,PayClassId,EmployeeId,EffectiveStart,EffectiveEnd,Reason,ClientId,LastModifiedUserId,LastModifiedTimestamp,LastPayEditDate,PunchPolicyId,PayPolicyId,NormalWeeklyHours,AverageDailyHours,BaseRate,PayHolidayGroupId,CreatedUserId,CreatedTimestamp,PayGroupId,AlternateRate,VacationRate,AverageOvertimeRate,EmployeeGroupId,EntitlementPolicyId,ShiftRotationId,ShiftRotationDayOffset,ShiftRotationStartDate,BaseSalary,CreateShiftRotationShift,ChecksumTimestamp,TimeOffPolicyId,ShiftTradePolicyId,AttendancePolicyId,EmployeeSchedulePolicyId,EmployeeNumber,EmployeeOTGroupId,NormalSemiMonthlyHoursTop,NormalSemiMonthlyHoursBottom,PRPayrollPolicyId,LastModifiedHRImportTimestamp,JobStepPolicyId,BaseRateManuallySet,ScheduleChangePolicyId,AuthorizationPolicyId,DailyRate)"
employeeWorkAssignment_prefix ="(EmployeeId,DeptJobId,OrgUnitId,IsPrimary,EffectiveStart,EffectiveEnd,Rate,Rank,FlatAmount,JobSetLevelId,EmploymentStatusReasonId,ClientId,LastModifiedUserId,LastModifiedTimestamp,ChecksumTimestamp,LastModifiedHRImportTimestamp,LegacyEmployeeJobId,LegacyEmployeeOrgUnitListId,LaborPercentage,FTE,PositionTermId,EmploymentIndicatorId,IsVirtual,PRWorkLocationOverrideId,IsStatutory,TipTypeGroupId,PRBankAccountBranchAddressId,IsPAPrimaryWorkSite,MultiJSalaryAllocationPercent,ParticipateInReciprocalTaxCalculation,BusinessTitle,LedgerCode)"

_uniqueId = time.strftime("%Y%m%d%H%M%S")

#predefine address
_us_live_addresses = [
    {'Address':'241 C La Grande Prince','City':'Christiansted','County':None,'State':'VI','Zip Code':'00820'},
    {'Address':'442 Swaying  Willow Ave','City':'Fairhope','County':'Baldwin','State':'AL','Zip Code':'36532'},
    {'Address':'14899 Sterling Hwy','City':'Cooper Landing','County':'Kenai Peninsula','State':'AK','Zip Code':'99572'},
    {'Address':'15373 S Sierra Sands Ave','City':'Yuma','County':'Yuma','State':'AZ','Zip Code':'85365'},
    {'Address':'867 Highway 26 W','City':'Nashville','County':'Pike','State':'AR','Zip Code':'71852'},
    {'Address':'4732 Orange St','City':'Pico Rivera','County':'Los Angeles','State':'CA','Zip Code':'90660'},
    {'Address':'20727 Catclaw Ct','City':'Johnstown','County':'Weld','State':'CO','Zip Code':'80534'},
    {'Address':'385 South Rd','City':'New Hartford','County':'Litchfield','State':'CT','Zip Code':'06057'},
    {'Address':'14385 Megan Way','City':'Laurel','County':'Sussex','State':'DE','Zip Code':'19956'},
    {'Address':'3609 24th St NE','City':'Washington','County':'District Of Columbia','State':'DC','Zip Code':'20018'},
    {'Address':'30826 Nocatee Trl','City':'Sorrento','County':'Lake','State':'FL','Zip Code':'32776'},
    {'Address':'658 Hawkins Store Rd NE','City':'Kennesaw','County':'Cobb','State':'GA','Zip Code':'30144'},
    {'Address':'459 Opihikao Pl','City':'Honolulu','County':'Honolulu','State':'HI','Zip Code':'96825'},
    {'Address':'28 N Yellowstone Hwy','City':'Rigby','County':'Jefferson','State':'ID','Zip Code':'83442'},
    {'Address':'12109 187th St','City':'Mokena','County':'Will','State':'IL','Zip Code':'60448'},
    {'Address':'9919 Northwind Dr','City':'Indianapolis','County':'Marion','State':'IN','Zip Code':'46256'},
    {'Address':'851 High Ave','City':'Newton','County':'Jasper','State':'IA','Zip Code':'50208'},
    {'Address':'229 E Fpx Brier Rd','City':'Rose Hill','County':'Butler','State':'KS','Zip Code':'67133'},
    {'Address':'393 Summer Hill Dr','City':'Somerset','County':'Pulaski','State':'KY','Zip Code':'42503'},
    {'Address':'109 Jasmine Ct','City':'Belle Chasse','County':'Plaquemines','State':'LA','Zip Code':'70037'},
    {'Address':'114 Water St','City':'Eastport','County':'Washington','State':'ME','Zip Code':'04631'},
    {'Address':'15202 Poplar Hill Rd','City':'Accokeek','County':'Prince Georges','State':'MD','Zip Code':'20607'},
    {'Address':'28 Field Rd','City':'Medway','County':'Norfolk','State':'MA','Zip Code':'20607'},
    {'Address':'980 W Bemis Rd','City':'Saline','County':'Washtenaw','State':'MI','Zip Code':'48176'},
    {'Address':'6937 Newton Ave','City':'Richfield','County':'Hennepin','State':'MN','Zip Code':'55423'},
    {'Address':'120 Meadowview Rdg','City':'Brandon','County':'Rankin','State':'MS','Zip Code':'39047'},
    {'Address':'53 Dove Ct','City':'Farmington','County':'Saint Francois','State':'MO','Zip Code':'63640'},
    {'Address':'140 Wildhorse Trl','City':'Belgrade','County':'Gallatin','State':'MT','Zip Code':'59714'},
    {'Address':'6238 N 155th Ave','City':'Omaha','County':'Douglas','State':'NE','Zip Code':'68116'},
    {'Address':'3165 La Mesa Dr','City':'Henderson','County':'Clark','State':'NV','Zip Code':'89014'},
    {'Address':'984 Ocean Blvd','City':'Hampton','County':'Rockingham','State':'NH','Zip Code':'03842'},
    {'Address':'797 Muir Ter','City':'Scotch Plains','County':'Union','State':'NJ','Zip Code':'07076'},
    {'Address':'780 37th St','City':'Los Alamos','County':'Los Alamos','State':'NM','Zip Code':'87544'},
    {'Address':'22514 Murdock Ave','City':'Jamaica','County':'Queens','State':'NY','Zip Code':'11429'},
    {'Address':'363 21st Ave NW','City':'Hickory','County':'Catawba','State':'NC','Zip Code':'28601'},
    {'Address':'1015 45th Ave N','City':'Fargo','County':'Cass','State':'ND','Zip Code':'58102'},
    {'Address':'9900 Evan Miller Trl','City':'Olmsted Twp','County':'Cuyahoga','State':'OH','Zip Code':'44138'},
    {'Address':'300 E Glendale St','City':'Broken Arrow','County':'Tulsa','State':'OK','Zip Code':'74011'},
    {'Address':'3206 SW Cascade Ave','City':'Corvallis','County':'Benton','State':'OR','Zip Code':'97333'},
    {'Address':'6130 N 7th St','City':'Philadelphia','County':'Philadelphia','State':'PA','Zip Code':'19120'},
    {'Address':'35 Mia Ct','City':'Warwick','County':'Kent','State':'RI','Zip Code':'02886'},
    {'Address':'108 Riverhill Ct','City':'Cayce','County':'Lexington','State':'SC','Zip Code':'29033'},
    {'Address':'16714 Willow Wood Road','City':'Piedmont','County':'Meade','State':'SD','Zip Code':'57769'},
    {'Address':'8509 Barbee Ln','City':'Knoxville','County':'Knox','State':'TN','Zip Code':'37923'},
    {'Address':'1704 Zamora Dr #5','City':'Brownsville','County':'Cameron','State':'TX','Zip Code':'78526'},
    {'Address':'4367 W 5300 S','City':'Hooper','County':'Weber','State':'UT','Zip Code':'84315'},
    {'Address':'346 Broadlake Rd','City':'Colchester','County':'Chittenden','State':'VT','Zip Code':'05446'},
    {'Address':'2010 Russell Dr','City':'Rockingham','County':'Rockingham','State':'VA','Zip Code':'22801'},
    {'Address':'4341 157th Ave SE','City':'Bellevue','County':'King','State':'WA','Zip Code':'98006'},
    {'Address':'175 Cobun Valley Ln','City':'Morgantown','County':'Monongalia','State':'WV','Zip Code':'26508'},
    {'Address':'1150 240th Ave','City':'Luck','County':'Polk','State':'WI','Zip Code':'54853'},
    {'Address':'1119 Crescent Dr','City':'Cheyenne','County':'Laramie','State':'WY','Zip Code':'82007'},
    {'Address':'626 Pale San Vitores Road','City':'Tumon Guam','State':'GU','Zip Code':'96931'},
    {'Address':'11 Villas Del Mar','City':'Carolina','County':None,'State':'PR','Zip Code':'00979'}
]

_us_work_addresses =[
    {'Address': '1654 Gadsden Hwy', 'City': 'Birmingham', 'State': 'AL', 'Zip Code': '35235'},
    {'Address': '150 W 100th Ave', 'City': 'Anchorage', 'State': 'AK', 'Zip Code': '99515'},
    {'Address': '3777 S Arizona Ave', 'City': 'Chandler', 'State': 'AZ', 'Zip Code': '85248'},
    {'Address': '420 S University Ave', 'City': 'Little Rock', 'State': 'AR', 'Zip Code': '72205'},
    {'Address': '29676 Rancho California Rd', 'City': 'Temecula', 'State': 'CA', 'Zip Code': '92591'},
    {'Address': '3810 Bloomington St', 'City': 'Colorado Springs', 'State': 'CO', 'Zip Code': '80922'},
    {'Address': '1075 Kennedy Rd', 'City': 'Windsor', 'State': 'CT', 'Zip Code': '06095'},
    {'Address': '148 John Hunn Brown Rd', 'City': 'Dover', 'State': 'DE', 'Zip Code': '19901'},
    {'Address': '3100 14th St NW', 'City': 'Washington', 'State': 'DC', 'Zip Code': '20010'},
    {'Address': '5601 NW 183rd St', 'City': 'Miami Gardens', 'State': 'FL', 'Zip Code': '33055'},
    {'Address': '1275 Caroline St NE', 'City': 'Atlanta', 'State': 'GA', 'Zip Code': '30307'},
    {'Address': '4450 Kapolei Pkwy Ste 100', 'City': 'Kapolei', 'State': 'HI', 'Zip Code': '96707'},
    {'Address': '633 N Milwaukee St', 'City': 'Boise', 'State': 'ID', 'Zip Code': '83704'},
    {'Address': '480 West Washington Street', 'City': 'East Peoria', 'State': 'IL', 'Zip Code': '61611'},
    {'Address': '8005 Calumet Ave', 'City': 'Munster', 'State': 'IN', 'Zip Code': '46321'},
    {'Address': '1441 Coral Ridge Ave', 'City': 'Coralville', 'State': 'IA', 'Zip Code': '52241'},
    {'Address': '10900 Stadium Dr', 'City': 'Kansas City', 'State': 'KS', 'Zip Code': '66111'},
    {'Address': '160 Pavilion Pkwy', 'City': 'Newport', 'State': 'KY', 'Zip Code': '41071'},
    {'Address': '3225 Louisiana Ave', 'City': 'Lafayette', 'State': 'LA', 'Zip Code': '70501'},
    {'Address': '200 Running Hill Rd', 'City': 'South Portland', 'State': 'ME', 'Zip Code': '04106'},
    {'Address': '5700 Bou Ave', 'City': 'Rockville', 'State': 'MD', 'Zip Code': '20852'},
    {'Address': '21 University Ave', 'City': 'Westwood', 'State': 'MA', 'Zip Code': '02090'},
    {'Address': '15901 Ford Rd', 'City': 'Dearborn', 'State': 'MI', 'Zip Code': '48126'},
    {'Address': '900 Nicollet Mall', 'City': 'Minneapolis', 'State': 'MN', 'Zip Code': '55403'},
    {'Address': '6365 I-55 N Jackson Ave', 'City': 'Jackson', 'State': 'MS', 'Zip Code': '39213'},
    {'Address': '3881 Mexico Rd', 'City': 'St Charles', 'State': 'MO', 'Zip Code': '63303'},
    {'Address': '2601 Central Ave', 'City': 'Billings', 'State': 'MT', 'Zip Code': '59102'},
    {'Address': '333 N 48th St', 'City': 'Lincoln', 'State': 'NE', 'Zip Code': '68504'},
    {'Address': '4001 S Maryland Pkwy', 'City': 'Las Vegas', 'State': 'NV', 'Zip Code': '89119'},
    {'Address': '310 Daniel Webster Hwy', 'City': 'Nashua', 'State': 'NH', 'Zip Code': '03060'},
    {'Address': '100 14th St', 'City': 'Jersey City', 'State': 'NJ', 'Zip Code': '07310'},
    {'Address': '2120 Louisiana Blvd NE', 'City': 'Albuquerque', 'State': 'NM', 'Zip Code': '87110'},
    {'Address': '555 8th Ave', 'City': 'New York', 'State': 'NY', 'Zip Code': '10018'},
    {'Address': '037 Durham-Chapel Hill Blvd', 'City': 'Durham', 'State': 'NC', 'Zip Code': '27707'},
    {'Address': '2400 10th St SW', 'City': 'Minot', 'State': 'ND', 'Zip Code': '58701'},
    {'Address': '1717 Olentangy River Rd', 'City': 'Columbus', 'State': 'OH', 'Zip Code': '43212'},
    {'Address': '800 SW 44th St', 'City': 'Oklahoma City', 'State': 'OK', 'Zip Code': '73109'},
    {'Address': '9800 SE Washington St', 'City': 'Portland', 'State': 'OR', 'Zip Code': '97216'},
    {'Address': '6231 Penn Ave', 'City': 'Pittsburgh', 'State': 'PA', 'Zip Code': '15206'},
    {'Address': '1245 Bald Hill Rd', 'City': 'Warwick', 'State': 'RI', 'Zip Code': '02886'},
    {'Address': '2070 Sam Rittenberg Blvd', 'City': 'Charleston', 'State': 'SC', 'Zip Code': '29407'},
    {'Address': '3600 S Louise Ave', 'City': 'Sioux Falls', 'State': 'SD', 'Zip Code': '57106'},
    {'Address': '5579 TN-153', 'City': 'Hixson', 'State': 'TN', 'Zip Code': '37343'},
    {'Address': '2100 Texas Ave S', 'City': 'College Station', 'State': 'TX', 'Zip Code': '77840'},
    {'Address': '1110 S 300 W', 'City': 'Salt Lake City', 'State': 'UT', 'Zip Code': '84101'},
    {'Address': '173 Pettingill Rd', 'City': 'Essex Junction', 'State': 'VT', 'Zip Code': '05452'},
    {'Address': '6600 Richmond Hwy', 'City': 'Alexandria', 'State': 'VA', 'Zip Code': '22306'},
    {'Address': '30 Bellis Fair Pkwy', 'City': 'Bellingham', 'State': 'WA', 'Zip Code': '98226'},
    {'Address': '30 RHL Blvd', 'City': 'South Charleston', 'State': 'WV', 'Zip Code': '25309'},
    {'Address': '4301 W Wisconsin Ave', 'City': 'Appleton', 'State': 'WI', 'Zip Code': '54913'},
    {'Address': '321 Yellowstone Ave', 'City': 'Cody', 'State': 'WY', 'Zip Code': '82414'},
    {'Address': '626 Pale San Vitores Road', 'City': 'Tumon Guam', 'State': 'GU', 'Zip Code': '96931'},
    {'Address': '11 Villas Del Mar', 'City': 'Carolina', 'County': '', 'State': 'PR', 'Zip Code': '00979'},
    {'Address': '123 Salomon Bay Rd', 'City': 'St John', 'State': 'VI', 'Zip Code': '00831'},
]

_list_dept_ids = list()
_list_deptjob_ids=list()
_list_paygroup_ids=list()
_list_paygroup_onsite_orgunit_ids=list()


def _getCurrentIdValue(tableName):
    sql ="SELECT IDENT_CURRENT('{0}') as id".format(tableName)
    id = int(engine.execute(sql).fetchone().id)
    return id

def _getColumnValue(tableName, colName, whereclause):
    sql = "SELECT {0} as id FROM {1} WHERE {2}".format(colName, tableName, whereclause)
    id = engine.execute(sql).fetchone().id
    #print(id,flush=True)
    return id

def _printSqlWithId(sql, id):
    print(sql + ": [id:" + str(id) + "]")

def _execSql(sql, tableName, toprint = False):
    engine.execute(sql)
    if( toprint ):
        id = _getCurrentIdValue(tableName)
        _printSqlWithId( sql, id )
        #print(sql + ": [id:" + str(id) + "]")

def _execSqlWithResult(sql, tableName, toprint = False):
    engine.execute(sql)
    id = _getCurrentIdValue(tableName)
    if (toprint):
        _printSqlWithId(sql, id)
        #print(sql + ": [id:" + str(id) + "]")
    return id

def _execSqlWithId(sql, toprint = False):
    id = engine.execute(sql).fetchone().id
    if( toprint ):
        _printSqlWithId( sql, id )
        #print(sql + ": [id:" + str(id) + "]")
    return id

def _execInsertValuesOutputId( tableName, values ):
    #sql = "INSERT INTO {0} Output inserted.{0}Id as id {1}".format(tableName, values)
    sql = "INSERT INTO {0} OUTPUT inserted.{0}Id as id VALUES({1})".format(tableName, values)
    id = engine.execute(sql).fetchone().id
    _printSqlWithId(sql, id)
    return id

def _execInsertOutputId( tableName, columns, values, toprint = False ):
    sql = "INSERT INTO {0} {1} {2}".format(tableName, columns, values)
    engine.execute(sql)
    id = _getCurrentIdValue(tableName)
    if (toprint):
        _printSqlWithId(sql, id)
    return id

def _execInsert( tableName, columns, values, toprint = False):
    sql = "INSERT INTO {0} {1} {2}".format( tableName, columns, values )
    engine.execute(sql)
    if( toprint ):
        id = _getCurrentIdValue(tableName)
        _printSqlWithId( sql, id )


_num_depts = 1
_num_paygroups = 1
_num_employees = 1000
_num_paygroup_sites = 1
_id_paygroup = "1K"
_test_id = "GridPerf"

_last_mod_userId = 1001
_last_mod_timestamp = "CURRENT_TIMESTAMP"
_culture_id = 1033

_site_level_id = 999
_onsite_level_id = 997
_corp_level_id = 0
_region_level_id = 1000
_country_code = "USA"

_current_year = datetime.now().year
_start_date = str(_current_year-1)+"-01-01"

_work_address_cycle = cycle(_us_work_addresses)
_live_address_cycle = cycle(_us_live_addresses)

_sample_user_id = 1002
_num_employees_to_create = 1000
_client_id = 10000



class TestPerformance(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

    def test_a_Init(self):

        def initGeoCity():
            address_list =[_us_live_addresses,_us_work_addresses]
            for y in range(len(address_list)):
                for x in range(len(address_list[y])):
                    sql ="insert into geocity select '{0}',NULL,gs.GeoStateId, {2},1001, CURRENT_TIMESTAMP " \
                         "from GeoState gs where gs.StateCode='{1}' and NOT EXISTS (SELECT a.shortname FROM GeoCity a" \
                         " WHERE a.shortname = '{0}' and gs.StateCode='{1}')".format(address_list[y][x]['City'],address_list[y][x]['State'],_client_id)
                    # list_address.append(get_latest_table('geocity'))
                    print(_us_live_addresses[x]['City'],_us_live_addresses[x]['State'])
                    print(sql)
                    engine.execute(sql)

        #initGeoCity()

    def test_e_Paygroup(self):
        # Todo: 1. create paygroup 2. map Paygroup mapping wiht earning

        def generatePaygroup(paygroup_name, pay_freq):

                if _country_code == 'USA':
                    geo_country_id = 1
                elif _country_code == 'CAN':
                    geo_country_id = 2
                elif _country_code == 'GBR':
                    geo_country_id = 3
                else:
                    geo_country_id = 0

                if pay_freq == 1:  # weekly
                    num_future_periods = 52
                elif pay_freq == 2:  # bi-weekly
                    num_future_periods = 26
                elif pay_freq == 3:  # semi-monthly
                    num_future_periods = 24
                elif pay_freq == 4:  # monthly
                    num_future_periods = 12

                paygroup_name_long = "long " + paygroup_name
                paygroup_name_xrefcode = "ref " + paygroup_name

                # CountryCode = 3 #2 if geoCountryCode=='CAN' else 1
                payholidaygroup_id = _getColumnValue("PayHolidayGroup", "MAX(PayHolidayGroupId)", "GeoCountryId={0}".format(geo_country_id))
                startdayofweek_id = 1  # 1 = Monday, ..., 7 = Sunday
                paydayofweek_id = 5
                businessday_starttime = "00:00:00"
                paydate_adjusttype_id = 1  # 1 = date before, 2 = date after, 3 = no offset
                paydate_offset = 2
                taxyear_startmonth = 4 if _country_code == 'GBR' else 'NULL'
                taxyear_startday = 6 if _country_code == 'GBR' else 'NULL'
                maxdetailrecords_timedata = 1000
                defaultlookback_value = 0

                paygroup_identifier = "'E{0}'".format(
                    random.randrange(1000, 9999)) if _country_code == 'CAN' else 'NULL'

                # col: 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3
                # value: 10, 10, 10, 10, 10, 10, 10, 3

                paygroup_sql = "INSERT INTO Paygroup" \
                               " (ShortName,LongName,PayFrequencyId,PayStartRef,XRefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,FuturePeriods,PayArrears," \
                               "ApproveByTimeOfDay,TransmitByTimeOfDay,TransmitWithIssues,TransmitWithUnauthorizedRecords,StartofWeek," \
                               "CalculationFrequencyId,SyncExportXML,ExcludeFromPayroll,BusinessDayStart,SendTestFilesToPayroll," \
                               "SequenceVersion,NextSequence,MaxNumAccounts,AllowDistributeByPct,PRPayDateAdjustTypeId," \
                               "PayDateDayOfWeekId,PayRunDateOffset,PayImpoundDaysOffest,CommitByTimeOfDay,GeoCountryId," \
                               "PrintedAdvices,IgnorePastIssues,SendAllExportDefinitions,IsPayrollCommit,PayHolidayGroupId," \
                               "IsGLAccrual,DisableMultiJTaxn,IsNotDisbursePrintToBackOffice,PayrollDepositOffset,ParticipateInBPS," \
                               "PayrollFrequencyId,PRPrintLocalizationPolicyId,IsPayrollByPrimaryLegalEntity,IsLargePayGroup,HoursDisplayPrecisionInStatements," \
                               "IsProcessPayrollEntitlement,EarningStatementDetailLevel,IsPayrollAdjustWFMHours,IsWFMCommitOnPayrollLock,IsAutoUpdateImportedPayEntryEarningRateAmount," \
                               "ForceMyPayEarningReplace,IPSEnabled,AllowFutureDatedImport,SupressTrivialTaxLocationMessages,MaximumDetailRecordsInTimeData," \
                               "RespectEmployeeLevelMultiJ,EnableStatementEmailNotification,SendEmailToVerifiedAddressOnly,DefaultAlternateFundingForOffCycle,TaxYearStartMonth," \
                               "TaxYearStartDay,PayRunApprovalAlertEnabled,ExportCertifiedPayrollToD2X,EnableTaxFormEmailNotification,DisplayDocketInfoOnEarningStatement," \
                               "ApproveOnThreshold,DisplayTimeCollectionEarningStatement,ForceDataEntryReplace,EnableGrossDataOnESHeader,GrossIncrementEarningType," \
                               "GrossDecrementEarningType,DefaultBusinessDateValue,PayGroupIdentifier,TrailingTaxationDefaultLookback)" \
                               " VALUES('{3}','{4}',{6},'{7}','{5}',{0},{1},{2},{13},0," \
                               "'{7}','{7}',0,0,{11},{6},0,0,'{12}',0," \
                               "0,1,4,0,{14},{18},{15},{15},'{7}',{8}," \
                               "0,1,0,1,{10},0,0,0,{15},0," \
                               "{6},1,0,0,2,0,0,0,0,0," \
                               "0,0,0,0,{19},0,0,1,0,{16}," \
                               "{17},0,0,0,0,0,0,0,0,''," \
                               "'',0,{9},{20})" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, paygroup_name, paygroup_name_long,
                            paygroup_name_xrefcode, pay_freq, _current_year, geo_country_id, paygroup_identifier,
                            payholidaygroup_id, startdayofweek_id, businessday_starttime, num_future_periods,
                            paydate_adjusttype_id,
                            paydate_offset, taxyear_startmonth, taxyear_startday, paydayofweek_id,
                            maxdetailrecords_timedata,
                            defaultlookback_value)

                paygroup_id = _execSqlWithResult(paygroup_sql, 'Paygroup')
                return paygroup_id

        def paygroupAssignment(paygroup_id, orgunitId):
                paygroup_assignment_sql = "INSERT INTO PaygroupAssignment" \
                                          " VALUES({3},{4},{0},{1},{2})" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, paygroup_id, orgunitId)
                _execSql(paygroup_assignment_sql, "PaygroupAssignment")

        def createPaygroupMapping(paygroup_id, sub_id):
                dfelem_paygroupearningmapping_id = _getColumnValue("DFElement", "DFElementId",
                                                                   "CodeName='PayGroupEarningMapping'")
                dfelemparam_paycategories_id = _getColumnValue("DFElementParam", "DFElementParamId",
                                                               "CodeName='PAYCATGORIES_CONTRIBUTING_TO_MAPPING'")
                dfelemparam_payadjcodes_id = _getColumnValue('DFElementParam', 'DFElementParamId',
                                                             "CodeName='PAYADJCODES_CONTRIBUTING_TO_MAPPING'")
                dfelemparam_earningcode_id = _getColumnValue('DFElementParam', 'DFElementParamId',
                                                             "CodeName='EARNING_CODE'")

                reg_paycategory_id = _getColumnValue("PayCategory", "PayCategoryId",
                                                     "Shortname = 'Reg' and ClientId={0}".format(_client_id))
                work_payadjcode_id = _getColumnValue('PayAdjCode', 'PayAdjCodeId',
                                                     "Shortname ='WRK' and Clientid={0}".format(_client_id))
                reg_earning_id = _getColumnValue('PREarning', 'PREarningId',
                                                 "Shortname ='Regular Earning' and Clientid={0}".format(_client_id))

                paygroupearningruleset_id = createPaygroupEarningRuleSet(paygroup_id, sub_id)
                paygrouprule_id = createPaygroupEarningRule(paygroupearningruleset_id, sub_id,
                                                            dfelem_paygroupearningmapping_id)

                mapPaygroupEarningElementValue(paygrouprule_id, dfelemparam_paycategories_id, reg_paycategory_id)
                mapPaygroupEarningElementValue(paygrouprule_id, dfelemparam_payadjcodes_id, work_payadjcode_id)
                mapPaygroupEarningElementValue(paygrouprule_id, dfelemparam_earningcode_id, reg_earning_id)

        def createPaygroupEarningRuleSet(payGroupId, id):
                paygroupearningruleset_name = "{2}PaygroupEarningRuleSet{1}_{0}".format(_uniqueId, id, _test_id)
                paygroupearningruleset_name_long = "long " + paygroupearningruleset_name

                value_str = "'{3}','{4}',1,{0},{1},{2},{5}" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, paygroupearningruleset_name,
                            paygroupearningruleset_name_long, payGroupId)
                paygroupearningruleset_id = _execInsertValuesOutputId("PayGroupEarningRuleSet", value_str)

                return paygroupearningruleset_id

        def createPaygroupEarningRule(paygroupearningruleset_id, id, dfelement_id):
                paygroupearningrule_name = "{2}PaygroupEarningRule{1}_{0}".format(_uniqueId, id, _test_id)
                paygroupearningrule_name_long = "long " + paygroupearningrule_name

                value_str = "{3},'{4}','{5}',{6},1,1,{1},{2},{0},'{7}',NULL,0" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, paygroupearningruleset_id,
                            paygroupearningrule_name, paygroupearningrule_name_long, dfelement_id, _start_date)
                paygroupearningrule_id = _execInsertValuesOutputId("PayGroupEarningRule", value_str)

                return paygroupearningrule_id

        def mapPaygroupEarningElementValue(paygroupearningrule_id, dfelementparam_id, value):
                paygroupearningelementvalue_sql = "INSERT INTO PayGroupEarningElementValue" \
                                                  " VALUES ({3},NULL,{4},{5},{1},{2},{0})" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp,
                            paygroupearningrule_id, dfelementparam_id, value)
                _execSql(paygroupearningelementvalue_sql, "PayGroupEarningElementValue")

        def mapLatestPayGroupOrgunit(paygroup_id):
                orgunit_id = engine.execute("SELECT MIN(OrgUnitId) as id FROM OrgUnit WHERE OrgLevelId=0").fetchone().id
                paygroupAssignment(paygroup_id, orgunit_id)

        def generatePaygroupCalendar(paygroup_id, payfreq_id):

                us_holiday = holidays.UnitedStates()
                current_year = datetime.now().year
                start_date = date(current_year - 1, 1, 1)
                end_date = date(current_year, 12, 31)
                pay_type = {1: relativedelta(weeks=+1),
                            2: relativedelta(weeks=+2),
                            3: relativedelta(days=+15),
                            4: relativedelta(months=+1)}

                first_paydate_current_year = start_date + pay_type[payfreq_id]

                startdayofweek = _getColumnValue("Paygroup", "StartofWeek", "PaygroupId = {0}".format(paygroup_id))
                paydayofweek = _getColumnValue("Paygroup", "PayDateDayOfWeekId", "PaygroupId = {0}".format(paygroup_id))

                byweekday_code = ['', MO, TU, WE, TH, FR, SA, SU]
                # print(byweekday_code[3])

                if payfreq_id == 1:  # weekly
                    # list_pay_dates = list(rrule(DAILY, byweekday=byweekday_code[paydayofweek], interval=1, count=52,
                    #                            dtstart=first_paydate_current_year))
                    list_calendar_start = list(rrule(DAILY, byweekday=byweekday_code[startdayofweek], interval=1,
                                                     dtstart=start_date, until=end_date))
                    list_calendar_end = [x + pay_type[payfreq_id] for x in list_calendar_start]
                elif payfreq_id == 2:  # bi-weekly
                    # list_pay_dates = list(rrule(DAILY, byweekday=byweekday_code[paydayofweek], interval=2, count=26,
                    #                            dtstart=first_paydate_current_year))
                    list_calendar_start = list(rrule(DAILY, byweekday=byweekday_code[startdayofweek], interval=2,
                                                     dtstart=start_date, until=end_date))
                    list_calendar_end = [x + pay_type[payfreq_id] for x in list_calendar_start]
                elif payfreq_id == 3:  # semi-monthly
                    list_calendar_start = list(rrule(MONTHLY, bymonthday=(1, 16), interval=1,
                                                     dtstart=start_date, until=end_date))
                    list_calendar_end = list(rrule(MONTHLY, bymonthday=(1, 16), interval=1,
                                                   dtstart=first_paydate_current_year,
                                                   until=end_date + relativedelta(days=+1)))

                #                list_calendar_start = list(rrule(MONTHLY, bymonthday=(1,16), interval=1, count=24,
                #                                            dtstart=start_date))
                #                list_calendar_end = list(rrule(MONTHLY, bymonthday=(1,16), interval=1, count=24,
                #                                            dtstart=first_paydate_current_year))
                # list_pay_dates = [x + relativedelta(days=+5) for x in list_calendar_start]
                elif payfreq_id == 4:  # monthly
                    list_calendar_start = list(rrule(MONTHLY, bymonthday=1, interval=1,
                                                     dtstart=start_date, until=end_date))
                    #                list_calendar_start = list(rrule(MONTHLY, bymonthday=1, interval=1, count=12,
                    #                                            dtstart=start_date))
                    list_calendar_end = [x + pay_type[payfreq_id] for x in list_calendar_start]

                # list_effective_start = [x for x in list_calendar_start]
                # list_effective_end = [x for x in list_calendar_end]
                list_transmitby_dates = [x - timedelta(1) for x in list_calendar_end]
                list_payimpound_dates = [x + timedelta(2) for x in list_calendar_end]
                list_payrun_dates = [x + timedelta(2) for x in list_calendar_end]
                list_pay_dates = [x + timedelta(4) for x in list_calendar_end]

                print("pay dates:{0}".format(list_pay_dates))
                # print("start dates:{0}".format(list_start_dates))
                print("calendar starts:{0}".format(list_calendar_start))
                print("calendar ends:{0}".format(list_calendar_end))
                print("effective starts:{0}".format(list_calendar_start))
                print("effective ends:{0}".format(list_calendar_end))
                print("transmitby dates:{0}".format(list_transmitby_dates))
                print("payimpound dates:{0}".format(list_payimpound_dates))
                print("payrun dates:{0}".format(list_payrun_dates))

                def auto_shift(day):
                    while (day in us_holiday) or (day.isoweekday() > 5):
                        day = day + timedelta(-1)
                    # print(day)
                    return day

                def is_auto_shifted(list1, list2):
                    return list(map(lambda x: 0 if x[0] == x[1] else 1, zip(list1, list2)))

                business_pay_dates = list(map(auto_shift, list_pay_dates))
                business_payrun_dates = list(map(auto_shift, list_payrun_dates))
                business_payimpound_dates = list(map(auto_shift, list_payimpound_dates))
                is_payrun_date_auto_shifted = is_auto_shifted(business_payrun_dates, list_payrun_dates)
                is_pay_date_auto_shifted = is_auto_shifted(business_pay_dates, list_pay_dates)
                is_payimpound_date_auto_shifted = is_auto_shifted(business_payimpound_dates, list_payimpound_dates)

                print("shifted pay dates:{0}".format(is_pay_date_auto_shifted))
                print("shifted payrun dates:{0}".format(is_payrun_date_auto_shifted))
                print("shifted payimpound dates:{0}".format(is_payimpound_date_auto_shifted))

                def createPayGroupCalendar(paygroup_id):
                    for x in range(len(business_pay_dates)):

                        sql = "INSERT INTO PayGroupCalendar" \
                              "(PayGroupId,EffectiveStart,EffectiveEnd,Locked,TransmitByDate," \
                              "Transmitted,ClientId,LastModifiedUserId,LastModifiedTimestamp,ApproveByDate," \
                              "PayPeriod,PayPeriodSuffix,CalendarStart,CalendarEnd,ExportSequence," \
                              "PayImpoundDate,PayRunDate,PayDate,IsPayDateAutoshifted,IsPayRunDateAutoshifted," \
                              "IsPayImpoundDateAutoshifted,CommitByTimeOfDay,FuturePunchesEnabled,Closed)" \
                              " VALUES ({3},'{4}','{5}',0,'{6}',0,{0},{1},{2},'{6}'," \
                              "'{7}','00','{8}','{9}',-1,'{10}','{11}','{12}',{13},{14}," \
                              "{15},'{11}',0,0) " \
                            .format(_client_id, _last_mod_userId, _last_mod_timestamp, paygroup_id,
                                    list_calendar_start[x],
                                    list_calendar_end[x], list_transmitby_dates[x], str((x % 24) + 1).zfill(2),
                                    list_calendar_start[x], list_calendar_end[x],
                                    business_payimpound_dates[x], business_payrun_dates[x], business_pay_dates[x],
                                    is_pay_date_auto_shifted[x], is_payrun_date_auto_shifted[x],
                                    is_payimpound_date_auto_shifted[x])
                        engine.execute(sql)
                        # print( "PayGroupCalendar sql: " + sql + "[paygroup:" + str(paygroup_id) + "]")
                        paygroupcalendar_id = _getCurrentIdValue("PayGroupCalendar")
                        print(sql + ": [paygroupcalendar:" + str(paygroupcalendar_id) + "][paygroup:" + str(
                            paygroup_id) + "]")

                def createPayGroupCalendarOrg(paygroup_id):

                    parent_orgunit_id = engine.execute(
                        "SELECT MAX(OrgUnitId) as id FROM OrgUnit WHERE OrgLevelId=0").fetchone().id

                    paygroupcalendarorg_sql = "INSERT INTO PayGroupCalendarOrg" \
                                              " (PayGroupCalendarId,OrgUnitId,Approved,ApprovedUserId,ApprovedDate," \
                                              "PayApproved,PayApprovedUserId,PayApprovedDate,Locked,LastModifiedUserId," \
                                              "LastModifiedTimestamp,ClientId)" \
                                              " SELECT g.PayGroupCalendarId, a.ChildOrgUnitId as OrgUnitId, 1,{1},{2},1,{1},{2},0,{1},{2},{0} from PayGroupCalendar g," \
                                              " (SELECT DISTINCT ChildOrgUnitId from [dbo].[HierarchyOrgView] WHERE ParentOrgUnitId = {4} and ChildOrgLevelId = 999) a" \
                                              " WHERE g.PaygroupId={3}" \
                        .format(_client_id, _last_mod_userId, _last_mod_timestamp, paygroup_id, parent_orgunit_id)
                    engine.execute(paygroupcalendarorg_sql)
                    paygroupcalendarorg_id = _getCurrentIdValue("PayGroupCalendarOrg")
                    print(paygroupcalendarorg_sql + ": [paygroupcalendarorg:" + str(
                        paygroupcalendarorg_id) + "][paygroup:" + str(paygroup_id) + "]")

                def createPayGroupCalculationCalendar(paygroup_id):

                    paygroupcalcuationcalendar_sql = "INSERT INTO PayGroupCalculationCalendar" \
                                                     " SELECT p.PayGroupCalendarId, p.EffectiveStart, p.EffectiveEnd, {0},{1},{2},p.CalendarStart,p.CalendarEnd FROM PayGroupCalendar p" \
                                                     " WHERE p.PayGroupId={3}" \
                                                     "".format(_client_id, _last_mod_userId, _last_mod_timestamp,
                                                               paygroup_id)
                    engine.execute(paygroupcalcuationcalendar_sql)
                    paygroupcalculationcalendar_id = _getCurrentIdValue("PayGroupCalculationCalendar")
                    print(paygroupcalcuationcalendar_sql + ": [paygroupcalculationcalendar:" + str(
                        paygroupcalculationcalendar_id) + "][paygroup:" + str(paygroup_id) + "]")

                createPayGroupCalendar(paygroup_id)
                createPayGroupCalendarOrg(paygroup_id)
                createPayGroupCalculationCalendar(paygroup_id)

        """
            main method
        """
        for x in range(_num_paygroups):
                name = "{3}{2}Test{0} ({1})".format(_uniqueId, x + 1, _id_paygroup, _test_id)
                paygroup_freq = "Monthly"  # Weekly, Bi-Weekly, Semi-Monthly, Monthly
                payfreq_id = _getColumnValue("PayFrequency", "PayFrequencyId", "ShortName='{0}'".format(paygroup_freq))
                paygroup_id = generatePaygroup(name, payfreq_id)
                mapLatestPayGroupOrgunit(paygroup_id)
                createPaygroupMapping(paygroup_id, x + 1)
                generatePaygroupCalendar(paygroup_id, payfreq_id)
                _list_paygroup_ids.append(int(paygroup_id))

    def test_e_employee(self):

        #paygroup_id = _getColumnValue('EmployeeEmploymentStatus', 'PayGroupId',
        # "EmployeeId={1} and ClientId={0}".format(_client_id, _sample_user_id))
        paygroup_id = _getColumnValue("Paygroup", "MAX(PayGroupId)", "ShortName LIKE '%{0}%'".format(_test_id))

        #get_orgunitid_sql = "SELECT DISTINCT orgunitid FROM EmployeeWorkAssignment a JOIN employeeemploymentstatus b ON a.employeeid=b.employeeid WHERE b.paygroupid={0}".format(paygroup_id)
        get_orgunitid_sql = "SELECT MIN(orgunitid) as orgunitid FROM OrgUnit WHERE OrgLevelId=997"
        list_orgunit_ids = engine.execute(get_orgunitid_sql).fetchall()
        list_onSite_orgunitId = [x.orgunitid for x in list_orgunit_ids]

        print("the employee will insert into the orgunitid :{0}".format(list_onSite_orgunitId))
        print("the employee will insert into the paygrouplist :{0}".format(paygroup_id))
        depart_orgunitId = cycle(list_onSite_orgunitId) if len(list_onSite_orgunitId)>0 else 0
        #cycle_payGroupId =cycle(list_payGroupId) if len(list_payGroupId) >0 else 0
        current_live_address =cycle(_us_live_addresses)

        #appuser_password = "$2a$04$y9FvNfU.2Pr9p.j.6DUz0eBek5AAXfSYnYJ4z41ck1pQQISYJ9ecq"
        appuser_password = _getColumnValue('AppUser', 'Password', "UserId={1} and ClientId={0}".format(_client_id, 1001))

        appuser_entitytype_id = _getColumnValue('AppUser', 'EntityTypeId',
                                                "UserId={1} and ClientId={0}".format(_client_id, 1001))
        appuser_culture_id = _getColumnValue('AppUser', 'CultureID',
                                             "UserId={1} and ClientId={0}".format(_client_id, 1001))
        appuser_hashmethod_id = _getColumnValue('AppUser', 'HashMethod',
                                                "UserId={1} and ClientId={0}".format(_client_id, 1001))
        userrole_roleid = _getColumnValue('UserRoleList', 'RoleId',
                                          "UserId={1} and ClientId={0} and IsDefault=1".format(_client_id, 1001))
        employmentstatus_id = _getColumnValue('EmployeeEmploymentStatus', 'EmploymentStatusId',
                                              "EmployeeId={1} and ClientId={0} and EffectiveEnd is NULL".format(_client_id, _sample_user_id))
        paytype_id = _getColumnValue('EmployeeEmploymentStatus', 'PayTypeId',
                                     "EmployeeId={1} and ClientId={0} and EffectiveEnd is NULL".format(_client_id, _sample_user_id))
        payclass_id = _getColumnValue('EmployeeEmploymentStatus', 'PayClassId',
                                      "EmployeeId={1} and ClientId={0} and EffectiveEnd is NULL".format(_client_id, _sample_user_id))
        # employmentstatusreason_id = _getColumnValue('EmploymentStatusReason', 'EmploymentStatusReasonId', "EmployeeId={1} and ClientId={0}".format(_client_id, _sample_user_id))
        punch_policy_id = _getColumnValue('EmployeeEmploymentStatus', 'PunchPolicyId',
                                          "EmployeeId={1} and ClientId={0} and EffectiveEnd is NULL".format(_client_id, _sample_user_id))
        pay_policy_id = _getColumnValue('EmployeeEmploymentStatus', 'PayPolicyId',
                                        "EmployeeId={1} and ClientId={0} and EffectiveEnd is NULL".format(_client_id, _sample_user_id))
        pay_holiday_group_id = _getColumnValue('EmployeeEmploymentStatus', 'PayHolidayGroupId',
                                               "EmployeeId={1} and ClientId={0} and EffectiveEnd is NULL".format(_client_id, _sample_user_id))
        #paygroup_id = _getColumnValue('EmployeeEmploymentStatus', 'PayGroupId',
         #                             "EmployeeId={1} and ClientId={0}".format(_client_id, _sample_user_id))
        time_off_policy_id = _getColumnValue('EmployeeEmploymentStatus', 'TimeOffPolicyId',
                                             "EmployeeId={1} and ClientId={0} and EffectiveEnd is NULL".format(_client_id, _sample_user_id))
        pr_payroll_policy_id = _getColumnValue('EmployeeEmploymentStatus', 'PRPayrollPolicyId',
                                               "EmployeeId={1} and ClientId={0} and EffectiveEnd is NULL".format(_client_id, _sample_user_id))
        entitle_policy_id = _getColumnValue('EmployeeEmploymentStatus', 'EntitlementPolicyId',
                                               "EmployeeId={1} and ClientId={0} and EffectiveEnd is NULL".format(_client_id, _sample_user_id))
        #emp_sched_policy_id = _getColumnValue('EmployeeEmploymentStatus', 'EmployeeSchedulePolicyId',
        #                                    "EmployeeId={1} and ClientId={0} and EffectiveEnd is NULL".format(_client_id, _sample_user_id))
        reason_id = _getColumnValue('EmployeeEmploymentStatus', 'Reason',
                                          "EmployeeId={1} and ClientId={0} and EffectiveEnd is NULL".format(_client_id, _sample_user_id))
        created_timestamp = _last_mod_timestamp
            #_getColumnValue('EmployeeEmploymentStatus', 'CreatedTimestamp',
             #                             "EmployeeId={1} and ClientId={0} and EffectiveEnd is NULL".format(_client_id, _sample_user_id))
        dept_job_id = _getColumnValue('EmployeeWorkAssignment', 'DeptJobId',
                                      "EmployeeId={1} and ClientId={0} and EffectiveEnd is NULL".format(_client_id, _sample_user_id))
        personaddr_countrycode = _country_code

        # employee
        birth_date = "1970-07-12"
        hire_date = "1999-01-01"
        start_date = "2014-07-21"
        soc_sec_num = "864865241"
        normal_weekly_hour = 40
        normal_semimonthly_hour = 100
        base_rate = 25
        base_salary = base_rate * 52 * normal_weekly_hour
        avg_daily_hour = 8

        t0 = time.time()

        def createEmployees(startNumber, num):

            sql1 = "SET IDENTITY_INSERT Appuser "
            engine.execute(sql1 + "ON")

            print(startNumber)
            endNumber = startNumber + num

            for employee_id in range(startNumber,endNumber):
                orgunit_departMentId = next(depart_orgunitId) if str(depart_orgunitId) != '0' else 0
                live_address=next(current_live_address)

                #appuser
                login_id = "Test{0}".format(employee_id)
                employee_xrefcode = "test{0}".format(employee_id)
                last_name = "LastName{0}".format(employee_id)
                first_name = "FirstName{0}".format(employee_id)
                display_name = "{2}{1} Emp{0}".format(employee_id,live_address['State'],_test_id)

                org_unit_id =str(orgunit_departMentId) if str(orgunit_departMentId)!= '0' else str(engine.execute("select max(OrgUnitId) as id from OrgUnit where OrgLevelId='997'").fetchone().id)

                # PersonAddress
                personaddr_addr1 = live_address['Address']
                personaddr_city = live_address['City']
                personaddr_state_code = live_address['State']
                personaddr_postal_code = live_address['Zip Code']
                #personaddr_county = 'NULL' if live_address['County'] is None else "'"+live_address['County']+"'"


                #personaddr_county = live_address['County']
                primres_contactinfotype_id = _getColumnValue('ContactInformationType', 'ContactInformationTypeId', "XrefCode='PrimaryResidence'")

                appuser_sql = "INSERT INTO AppUser" \
                              " (UserId,LoginId,Password,IsApproved,IsLockedOut," \
                              "CreateTimestamp,ClientId,LastModifiedUserId,LastModifiedTimestamp,CultureID," \
                              "CanSeeSelf,ResetOnNextLogin,ShowDisclaimer,UsesOrgSecurity,EntityTypeId," \
                              "IsDeleted,Display24HourTime,HashMethod,IsPinLockedOut,IsBiometricLockedOut," \
                              "ShowEmailMissing,HasAcceptedPrivacyPolicy,HasAcceptedTermsOfUse,AllowNativeAuthentication)" \
                              " VALUES({3},'{4}','{5}',1,0," \
                              "{2},{0},{1},{2},{6}," \
                              "0,0,0,1,{7}," \
                              "0,0,'{8}',0,0," \
                              "1,0,0,0)" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, employee_id, login_id, appuser_password,
                            appuser_culture_id, appuser_entitytype_id, appuser_hashmethod_id)
                _execSql(appuser_sql, "AppUser")

                userrolelist_sql = "INSERT INTO UserRoleList" \
                                   " (UserId, RoleId, IsDefault, EffectiveStart, Clientid, LastModifiedUserId, LastModifiedTimestamp)" \
                                   " VALUES({3},{4}, 1, '{5}', {0}, {1}, {2})" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, employee_id, userrole_roleid, start_date)
                _execSql(userrolelist_sql, "UserRoleList")

                employee_sql = "INSERT INTO Employee" \
                               " (EmployeeId,LastName,FirstName,BirthDate," \
                               "HireDate,ClientId,LastModifiedUserId,LastModifiedTimestamp,XRefCode," \
                               "Gender,StartDate,SocialSecurityNumber,DisplayName,BioExempt," \
                               "RequiresExitInterview,PhotoExempt,SendFirstTimeAccessEmail,FirstTimeAccessVerificationAttempts,FirstTimeAccessEmailSentCount," \
                               "PredictiveOptIn,CultureId,TaxExempt,NewHireApproved,NewHireApprovalDate,SeniorityDate)" \
                               " VALUES('{3}','{4}','{5}','{6}'," \
                               "'{12}',{0},{1},{2},'{8}'," \
                               "'M','{7}','{9}','{10}',0," \
                               "0,0,0,0,0," \
                               "1,{11},0,1,'{7}','{7}')" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, employee_id, last_name, first_name,
                            birth_date, start_date, employee_xrefcode, soc_sec_num, display_name,
                            appuser_culture_id,hire_date)
                _execSql(employee_sql, "Employee")

                employeeemploymentstatus_sql = "INSERT INTO EmployeeEmploymentStatus" \
                                               " (EmploymentStatusId,PayTypeId,PayClassId,EmployeeId,EffectiveStart," \
                                               "ClientId, LastModifiedUserId, LastModifiedTimestamp, PunchPolicyId, PayPolicyId," \
                                               "NormalWeeklyHours, AverageDailyHours, BaseRate, CreatedUserId, CreatedTimestamp," \
                                               "PayGroupId, BaseSalary, CreateShiftRotationShift, ChecksumTimestamp, EmployeeNumber," \
                                               "PRPayrollPolicyId, PayHolidayGroupId, TimeOffPolicyId, NormalSemiMonthlyHoursBottom, NormalSemiMonthlyHoursTop," \
                                               "Reason, EntitlementPolicyId)" \
                                               " VALUES({3},{4},{5},{6},'{7}'," \
                                               "{0},{1},{2},{8},{9}," \
                                               "{10},{11},{12},0,{21}," \
                                               "{13}, {14},0,NULL,'{15}'," \
                                               "{16},{17},{18},{19},{19}," \
                                               "{20},{22})" \
                                        .format(_client_id, _last_mod_userId, _last_mod_timestamp, employmentstatus_id, paytype_id, payclass_id,
                            employee_id, start_date, punch_policy_id, pay_policy_id, normal_weekly_hour,
                            avg_daily_hour, base_rate, paygroup_id, base_salary, employee_xrefcode,
                            pr_payroll_policy_id, pay_holiday_group_id, time_off_policy_id, normal_semimonthly_hour, reason_id,
                            created_timestamp,entitle_policy_id)
                #"Reason, EntitlementPolicyId, EmployeeSchedulePolicyId)" \
                    # "{20},{22},{23})" \
                #,emp_sched_policy_id)
                _execSql(employeeemploymentstatus_sql, "EmployeeEmploymentStatus")

                employeeworkassignment_sql = "INSERT INTO EmployeeWorkAssignment" \
                                             " (EmployeeId,DeptJobId,OrgUnitId,IsPrimary,EffectiveStart," \
                                             "ClientId,LastModifiedUserId,LastModifiedTimestamp,IsVirtual,IsStatutory," \
                                             "IsPAPrimaryWorkSite,LedgerCode,RecordSource,IsExclusiveLoan,IsDefaultLoanPosition)" \
                                             " VALUES({3},{4},{5},1,'{6}'," \
                                             "{0},{1},{2},0,0," \
                                             "0,'',1,0,0)" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, employee_id, dept_job_id, org_unit_id,
                            start_date)
                _execSql(employeeworkassignment_sql, "EmployeeWorkAssignment")

                personaddress_sql = "INSERT INTO PersonAddress" \
                                    "(PersonId,CountryCode,Address1,City,StateCode," \
                                    "PostalCode,ContactInformationTypeId,EffectiveStart,LastModifiedUserId,LastModifiedTimestamp," \
                                    "ClientId,IsPayrollMailing,County,DisplayOnTaxForm,DisplayOnEarningStatement,ReGeoCode)" \
                                    " VALUES({3},'{4}','{5}','{6}','{7}'," \
                                    "'{8}',{10},'{9}',{1},{2}," \
                                    "{0},0,null,0,0,0)" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, employee_id, personaddr_countrycode, personaddr_addr1,
                            personaddr_city, personaddr_state_code, personaddr_postal_code, start_date, primres_contactinfotype_id)
                            #personaddr_county)
                _execSql(personaddress_sql, "PersonAddress")

            engine.execute(sql1 + "OFF")
            print("Total elapsed time [{0}] to generate {1} employees".format(str(time.time() - t0), num))

        employee_id_to_start = _getCurrentIdValue('AppUser') + 1
        createEmployees(employee_id_to_start, _num_employees_to_create)

    #def test_z(self):
        ## get_paygroup_sql = "SELECT paygroupid FROM paygroup WHERE shortname like '%performanceTest30k%'"
        #paygroup_id = _getColumnValue('Paygroup', 'PayGroupId', "ShortName LIKE '%performanceTest30k%'")
        #get_orgunitid_sql = "SELECT DISTINCT orgunitid FROM EmployeeWorkAssignment a JOIN employeeemploymentstatus b ON a.employeeid=b.employeeid WHERE b.paygroupid={0}".format(paygroup_id)
        #list_orgunit_is = engine.execute(get_orgunitid_sql).fetchall()
        #list_paygroup = [x.orgunitid for x in list_orgunit_is]
        #print(list_paygroup)

    def execute(self):
        unittest.main()

if __name__ == '__main__':
    testPerformance = TestPerformance()
    testPerformance.execute()
