# __author__ = 'kevinz'
# import unittest
from .DbSetUp.database import engine
from datetime import datetime, timedelta, date
from dateutil.rrule import *
from dateutil.relativedelta import *
# from ddt import ddt, data
from itertools import cycle
from sqlalchemy.sql import text
import unittest
import holidays

import time
import random

"""
Data Generator
"""

# """
# [SQL for Org setUp]
# """
# legalEntity_prefix ="(ShortName,LongName,PayMasterLegalEntityId,XRefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,CountryCode,Address,Address2,GeoCityId,StateCode,PostalCode,County,LegalIdNumber,LegalIdNumberType,Active,EffectiveStart,EffectiveEnd,EIReferenceCode,IsAutoCreated,IsValidationRequired,PreferenceCodeId,IsNotDisbursePrintToBackOffice,CustomerImplementationStatusId,AddressCountryCode,TerritorialGeoStateId,PreferenceCodeExtended,CPPCalculationOptionForStatusIndianId,ApplyStatusIndianCalculation,PRProcessForEmploymentId,PRTaxElectionId)"
# #legalEntity_insurance ="(LegalEntityEmployeeInsuranceId,LegalEntityId,ReferenceCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,RateGroup,IsDefault,LegalEntityEmployeeInsurancePreferenceCodeId,PreferenceCodeExtended)"
# #legalEntity_insurance_rate_prefix="(LegalEntityEmployeeInsuranceRateId,LegalEntityEmployeeInsuranceId,Rate,EffectiveStart,EffectiveEnd,ClientId,LastModifiedUserId,LastModifiedTimestamp)"
# department_prefix="(ShortName,LongName,LabelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,XRefCode,LedgerCode)"
# job_prefix="(ShortName,LongName,LabelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,PunchPolicyId,XrefCode,JobRank,DFPayGradeId,JobQualifications,FLSAStatusId,EmployeeEEOId,JobClassificationId,LedgerCode,JobFamilyId,JobFunctionId,JobUDFString1,JobUDFString2,JobUDFString3,DFUnionId,IsUnionJob,EffectiveStart,EffectiveEnd,NOC)"
# deptjob_prefix="(DepartmentId,JobId,ClientId,LastModifiedUserId,LastModifiedTimestamp,CreationOrgUnitId,EffectiveStart,EffectiveEnd,ShortCode,LedgerCode,ClockTransferCode,IsNonService,DefaultHue,StandardCostRate,ShortName,LongName,PayClassId,PayTypeId,Officer,Executive,Status,EmploymentIndicatorId,FTE,PositionTermId,WeeklyHours,AverageDailyHours,SemiMonthlyTopHours,SemiMonthlyBottomHours,PayGroupId,IsWCBExempt,XRefCode,PPACAFullTime)"
# orgunit_prefix="(ShortName,LongName,OrgLevelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,IsStoreFlag,XRefCode,PhysicalLocation,LedgerCode,BusinessPhone,ContactName,ContactBusinessPhone,ContactCellPhone,Address,Address2,StateCode,PostalCode,CountryCode,OpeningDate,ClosingDate,ComparableOrgUnitId,ClockTransferCode,DepartmentId,ZoneId,OrgGroupId,StartDOW,GeoCityId,TimezoneId,County,IsAddressChanged,ComDataAccountId,IsOrgManaged,PsdCode,IsMobileOrg,DescriptiveLocation,Coordinates,LastModifiedCoordinateTime,TaxLocationAddressId)"
# orgunit_legalEntity_prefix="(OrgUnitId, LegalEntityId, LegalEntityWorkSiteStateId, EffectiveStart, EffectiveEnd, ClientId, LastModifiedUserId, LastModifiedTimestamp, PRBankAccountBranchAddressId, LegalEntityMasterBankAccountSettingId)"
# #orgunitParent_prefix="(OrgUnitId,ParentOrgUnitId,EffectiveStart,EffectiveEnd,ClientId,LastModifiedUserId,LastModifiedTimestamp,OrgUnitParentLeft,OrgUnitParentRight,ClosestPhysicalLocationOrgUnitId,ClosestAddressOrgUnitId,ClosestTaxationAddressOrgUnitId,ClosestTimeZoneOrgUnitId)"

# """
# [SQL for payRoll Setup Earning, Deduction, Tax]
# """
# appuser_prefix ="(UserId,LoginId,Password,Description,IsApproved,IsLockedOut,CreateTimestamp,LastLoginTimestamp,LastPasswordChangedTimestamp,LastLockoutTimestamp,FailedPasswordAttemptCount,FailedPasswordAttemptWindowStart,FailedPasswordAnswerAttemptCount,FailedPasswordAnswerAttemptWindowStart,ClientId,LastModifiedUserId,LastModifiedTimestamp,CultureID,CanSeeSelf,ResetOnNextLogin,ShowDisclaimer,UsesOrgSecurity,LogMode,EntityTypeId,IsDeleted,Display24HourTime,NumberDisplayCultureId,SecurityQuestionId1,SecurityQuestionId2,HashMethod,IsPinLockedOut,LastPinLockoutTimestamp,FailedPinAttemptCount,FailedPinAttemptWindowStart,IsBiometricLockedOut,LastBiometricLockoutTimestamp,FailedBiometricAttemptCount,FailedBiometricAttemptWindowStart,DefaultPasswordExpiryTimestamp,AnswersHashMethod,Answer1,Answer2,ShowEmailMissing,HasAcceptedPrivacyPolicy,HasAcceptedTermsOfUse,LegalAgreementsAcceptedTimestamp,LastSessionType)"
# employee_prefix ="(EmployeeId,ManagerId,LastName,FirstName,MiddleName,HomePhone,Address,Address2,City,StateCode,PostalCode,BirthDate,HireDate,TaxpayerId,EmergencyContact,EmergencyPhone,EmergencyCellPhone,AvatarUri,ClientId,LastModifiedUserId,LastModifiedTimestamp,XRefCode,Title,Suffix,Gender,BadgeNumber,RegisteredDisabled,BusinessPhone,CountryCode,StartDate,SocialSecurityNumber,EmergencyBusinessPhone,EmergencyContact2,EmergencyPhone2,EmergencyCellPhone2,EmergencyBusinessPhone2,EmergencyEmail,EmergencyEmail2,CommonName,CultureId,ClockSupervisor,EmergencyContactRelationshipTypeId,EmergencyContact2RelationshipTypeId,TaxExempt,SchoolYearId,ChecksumTimestamp,NewHireApproved,NewHireApprovedBy,NewHireApprovalDate,SeniorityDate,DisplayName,BioExempt,EmployeePin,ExportDate,CitizenshipTypeId,SSNExpiryDate,MaidenName,PreferredLastName,EligibleForRehire,TerminationDate,DateOfDeath,EstimatedReturnDate,RequiresExitInterview,ExitInterviewerEmployeeId,IsAboriginal,IsVisibleMinority,VeteranSeparationDate,PRPayrollTaxLocalJurisdictionId,LastPayrollNewHireExportDate,LastModifiedHRImportTimestamp,BioSensitivityLevelId,OriginalHireDate,COBRANotificationStatus,COBRANotificationSentDate,PhotoExempt,PPACAOverrideDate,SSNCountryCode)"
# personAddress_prefix ="(PersonId,CountryCode,Address1,Address2,Address3,City,StateCode,PostalCode,ContactInformationTypeId,EffectiveStart,EffectiveEnd,LastModifiedUserId,LastModifiedTimestamp,ClientId,County,LastModifiedHRImportTimestamp,IsPayrollMailing,Address4)"
# employeeEmploymentStatus_prefix ="(EmploymentStatusId,PayTypeId,PayClassId,EmployeeId,EffectiveStart,EffectiveEnd,Reason,ClientId,LastModifiedUserId,LastModifiedTimestamp,LastPayEditDate,PunchPolicyId,PayPolicyId,NormalWeeklyHours,AverageDailyHours,BaseRate,PayHolidayGroupId,CreatedUserId,CreatedTimestamp,PayGroupId,AlternateRate,VacationRate,AverageOvertimeRate,EmployeeGroupId,EntitlementPolicyId,ShiftRotationId,ShiftRotationDayOffset,ShiftRotationStartDate,BaseSalary,CreateShiftRotationShift,ChecksumTimestamp,TimeOffPolicyId,ShiftTradePolicyId,AttendancePolicyId,EmployeeSchedulePolicyId,EmployeeNumber,EmployeeOTGroupId,NormalSemiMonthlyHoursTop,NormalSemiMonthlyHoursBottom,PRPayrollPolicyId,LastModifiedHRImportTimestamp,JobStepPolicyId,BaseRateManuallySet,ScheduleChangePolicyId,AuthorizationPolicyId,DailyRate)"
# employeeWorkAssignment_prefix ="(EmployeeId,DeptJobId,OrgUnitId,IsPrimary,EffectiveStart,EffectiveEnd,Rate,Rank,FlatAmount,JobSetLevelId,EmploymentStatusReasonId,ClientId,LastModifiedUserId,LastModifiedTimestamp,ChecksumTimestamp,LastModifiedHRImportTimestamp,LegacyEmployeeJobId,LegacyEmployeeOrgUnitListId,LaborPercentage,FTE,PositionTermId,EmploymentIndicatorId,IsVirtual,PRWorkLocationOverrideId,IsStatutory,TipTypeGroupId,PRBankAccountBranchAddressId,IsPAPrimaryWorkSite,MultiJSalaryAllocationPercent,ParticipateInReciprocalTaxCalculation,BusinessTitle,LedgerCode)"

# optional paramters
# employeeDeduction_prefix ="(EmployeeDeductionId,EmployeeId,PRDeductionId,EffectiveStart,EffectiveEnd,ClientId,LastModifiedUserId,LastModifiedTimestamp,PRPayeeDeductionId,PREarnDeductScheduleId,PayeePayableTo,IsBlocked,ArrearMultipleLimitOption,OrgUnitId,DeptJobId)"
# employeeDeductionParam_prefix ="(EmployeeDeductionParamId,PRDeductionParamId,Value,ClientId,LastModifiedUserId,LastModifiedTimestamp,EmployeeDeductionId)"
# employeeEarning_prefix ="(EmployeeEarningId,EmployeeId,PREarningId,PRPayeeEarningId,LimitAmount,LimitPercent,EffectiveStart,EffectiveEnd,ClientId,LastModifiedUserId,LastModifiedTimestamp,PREarnDeductScheduleId,PayeePayableTo,IsBlocked,OrgUnitId,DeptJobId)"
# employeeEarmingParam_prefix ="(EmployeeEarningParamId,EmployeeEarningId,PREarningParamId,Value,ClientId,LastModifiedUserId,LastModifiedTimestamp)"

_uniqueId = time.strftime("%Y%m%d%H%M%S")

# predefine address
_cdn_live_addresses = [
    {'Address': '1 Sir Winston Churchill Square', 'City': 'Edmonton', 'Province': 'AB', 'Postal Code': 'T5J 2R7'},
    # {'Address': '210 North Bay Road', 'City': 'Vancouver', 'Province': 'BC', 'Postal Code': 'V2S 1J0'},
    # {'Address': '1170 Summerville Ave', 'City': 'Winnipeg', 'Province': 'MB', 'Postal Code': 'R3T 1J3'},
    # {'Address': '125 Smith Street', 'City': 'Moncton', 'Province': 'NB', 'Postal Code': 'E1A 1J0'},
    # {'Address': '1960 Topsail Rd', 'City': 'Paradise', 'Province': 'NL', 'Postal Code': 'A1L 3W2'},
    # {'Address': '125 2nd Street', 'City': 'Yellowknife', 'Province': 'NT', 'Postal Code': 'X1A 1B0'},
    # {'Address': '125 Amherst Ave', 'City': 'Halifax', 'Province': 'NS', 'Postal Code': 'B4B 1H0'},
    # {'Address': '126 South Street', 'City': 'Iqaluit', 'Province': 'NU', 'Postal Code': 'X0A 1H9'},
    # {'Address': '4113 Hope Street', 'City': 'Barrie', 'Province': 'ON', 'Postal Code': 'M2P 2B7'},
    # {'Address': '23 Green Gable Row', 'City': 'Charlottetown', 'Province': 'PE', 'Postal Code': 'C1A 3P2'},
    # {'Address': '125 Main Street', 'City': 'Moose Jaw', 'Province': 'SK', 'Postal Code': 'S4L 3P2'},
    # {'Address': '12 Gold Rush Way', 'City': 'Whitehorse', 'Province': 'YT', 'Postal Code': 'Y1A 1A0'},
    # {'Address': '4683 Avenue Westmount', 'City': 'Westmount', 'Province': 'QC', 'Postal Code': 'H3Y 1W7'}
]

_cdn_work_addresses = [
    {'Address': '1 Sir Winston Churchill Square', 'City': 'Edmonton', 'Province': 'AB', 'Postal Code': 'T5J 2R7'},
    # {'Address': '125 Center Street', 'City': 'Vancouver', 'Province': 'BC', 'Postal Code': 'V1M 3P2'},
    # {'Address': '125 Main Street', 'City': 'Winnipeg', 'Province': 'MB', 'Postal Code': 'R3C 3P2'},
    # {'Address': '125 Edmonton Ave', 'City': 'Moncton', 'Province': 'NB', 'Postal Code': 'E1B 3P2'},
    # {'Address': '125 Main Street', 'City': 'St John', 'Province': 'NL', 'Postal Code': 'A1A 3P2'},
    # {'Address': '125 Main Street', 'City': 'Yellowknife', 'Province': 'NT', 'Postal Code': 'X1A 1A0'},
    # {'Address': '125 Main Street', 'City': 'Halifax', 'Province': 'NS', 'Postal Code': 'B2V 3P2'},
    # {'Address': '125 Main Street', 'City': 'Iqaluit', 'Province': 'NU', 'Postal Code': 'X0A 1H9'},
    # {'Address': '4110 Yonge Street', 'City': 'Toronto', 'Province': 'ON', 'Postal Code': 'M2P 2B7'},
    # {'Address': '125 Main Street', 'City': 'Charlottetown', 'Province': 'PE', 'Postal Code': 'C1A 3P2'},
    # {'Address': '125 Main Street', 'City': 'Regina', 'Province': 'SK', 'Postal Code': 'S4L 3P2'},
    # {'Address': '125 Main Street', 'City': 'Whitehorse', 'Province': 'YT', 'Postal Code': 'Y1A 1A0'},
    # {'Address': '845 Sherbrooke St. W', 'City': 'Montreal', 'Province': 'QC', 'Postal Code': 'H3A 2T5'}
]

_list_dept_ids = list()
_list_deptjob_ids = list()
_list_paygroup_ids = list()
_list_paygroup_onsite_orgunit_ids = list()


def _getCurrentIdValue(tableName):
    sql = "SELECT IDENT_CURRENT('{0}') as id".format(tableName)
    id = int(engine.execute(sql).fetchone().id)
    return id


def _getColumnValue(tableName, colName, whereclause):
    sql = "SELECT {0} as id FROM {1} WHERE {2}".format(colName, tableName, whereclause)
    id = engine.execute(sql).fetchone().id
    # print(id,flush=True)
    return id


def _printSqlWithId(sql, id):
    print(sql + ": [id:" + str(id) + "]")


def _execSql(sql, tableName, toprint=False):
    engine.execute(sql)
    if (toprint):
        id = _getCurrentIdValue(tableName)
        _printSqlWithId(sql, id)
        # print(sql + ": [id:" + str(id) + "]")


def _execSqlWithResult(sql, tableName, toprint=False):
    engine.execute(sql)
    id = _getCurrentIdValue(tableName)
    if (toprint):
        _printSqlWithId(sql, id)
        # print(sql + ": [id:" + str(id) + "]")
    return id


def _execSqlWithId(sql, toprint=False):
    id = engine.execute(sql).fetchone().id
    if (toprint):
        _printSqlWithId(sql, id)
        # print(sql + ": [id:" + str(id) + "]")
    return id


def _execInsertValuesOutputId(tableName, values):
    # sql = "INSERT INTO {0} Output inserted.{0}Id as id {1}".format(tableName, values)
    sql = "INSERT INTO {0} OUTPUT inserted.{0}Id as id VALUES({1})".format(tableName, values)
    id = engine.execute(sql).fetchone().id
    _printSqlWithId(sql, id)
    return id


def _execInsertOutputId(tableName, columns, values, toprint=False):
    sql = "INSERT INTO {0} {1} {2}".format(tableName, columns, values)
    engine.execute(sql)
    id = _getCurrentIdValue(tableName)
    if (toprint):
        _printSqlWithId(sql, id)
    return id


def _execInsert( tableName, columns, values, toprint=False):
    sql = "INSERT INTO {0} {1} {2}".format(tableName, columns, values)
    engine.execute(sql)
    if (toprint):
        id = _getCurrentIdValue(tableName)
        _printSqlWithId(sql, id)


# legalEntity= 26
# _num_sites = 1
_num_employees_list = [1] #25000, 50000, 75000, ]
_id_paygroup_list = ['150K'] #25K, '50K', '', '']
_num_depts = 1
_num_paygroups = len(_num_employees_list)
_num_paygroup_sites = 100

_client_id = 10000

_last_mod_userId = 1001
_last_mod_timestamp = "CURRENT_TIMESTAMP"
_culture_id = 1033

_site_level_id = 999
_onsite_level_id = 997
_corp_level_id = 0
_region_level_id = 1000
_country_code = "CAN"
_start_date = "2021-01-01"

_work_address_cycle = cycle(_cdn_work_addresses)
_live_address_cycle = cycle(_cdn_live_addresses)


class TestPerformance(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

    def test_a_Init(self):

        def setClientInfo():
            client_address = next(_work_address_cycle)
            clientaddress_name = "{0}ClientAddress".format(_country_code)
            clientaddress_clientaddresstype = "Primary"

            clientcontact_firstname = "{0}ContactFirst".format(_country_code)
            clientcontact_lastname = "{0}ContactLast".format(_country_code)
            clientcontact_phonenum = "2894524587"
            deliverypkg_name = "{0} Delivery Package".format(_country_code)
            clientaddresstype_id = _getColumnValue("ClientAddresstype", "ClientAddresstypeId",
                                                   "CodeName ='{0}'".format(clientaddress_clientaddresstype))

            clientaddress_sql = "INSERT INTO ClientAddress SELECT '{4}','{4}','{5}',NULL,NULL,'{6}','{7}','{3}','{8}',{0},{1},{2},NULL,1,{9}" \
                                " WHERE NOT EXISTS (SELECT 1 FROM ClientAddress WHERE CountryCode = '{3}' and ClientId={0})" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, _country_code, clientaddress_name,
                        client_address['Address'], client_address['City'], client_address['Province'],
                        client_address['Postal Code'],
                        clientaddresstype_id)
            _execSql(clientaddress_sql, "ClientAddress")
            clientaddress_id = _getColumnValue("ClientAddress", "ClientAddressId",
                                               "CountryCode = '{0}' and ClientId={1}".format(_country_code, _client_id))
            _printSqlWithId(clientaddress_sql, clientaddress_id)

            clientcontact_type_id = _getColumnValue("ClientContactType", "ClientContactTypeId",
                                                    "CodeName = 'PayrollDelivery'")

            clientcontact_sql = "INSERT INTO ClientContact SELECT {4},'{6}',NULL,'{7}',NULL,NULL,{0},{1},{2},'{3}','{5}',NULL,{8},1" \
                                " WHERE NOT EXISTS (SELECT 1 FROM ClientContact WHERE CountryCode = '{3}' and ClientId={0})" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, _country_code, clientcontact_type_id,
                        clientcontact_firstname, clientcontact_lastname, clientcontact_phonenum, _culture_id)
            _execSql(clientcontact_sql, "ClientContact")
            clientcontact_id = _getColumnValue("ClientContact", "ClientContactId",
                                               "CountryCode = '{0}' and ClientId={1}"
                                               .format(_country_code, _client_id))
            _printSqlWithId(clientcontact_sql, clientcontact_id)

            # look for courier in the current countrycode
            fedex_courier_id = _getColumnValue("Courier", "CourierId", "CodeName ='Fedex'")

            geocountry_id = _getColumnValue("GeoCountry", "GeoCountryId", "CountryCode = '{0}'".format(_country_code))
            sql = "SELECT MAX(CountrySortOrder) as num FROM CourierCountry WHERE GeoCountryId='{0}'".format(
                geocountry_id)
            next_sort_order = engine.execute(sql).fetchone().num + 1

            couriercountry_sql = "INSERT INTO CourierCountry SELECT {0},{1},{2},0,0,CURRENT_TIMESTAMP" \
                                 " WHERE NOT EXISTS (SELECT 1 FROM CourierCountry WHERE CourierId = {0} and GeoCountryId={1})" \
                .format(fedex_courier_id, geocountry_id, next_sort_order)
            _execSql(couriercountry_sql, "CourierCountry")
            couriercountry_id = _getColumnValue("CourierCountry", "CourierCountryId",
                                                "CourierId = '{0}' and GeoCountryId={1}"
                                                .format(fedex_courier_id, geocountry_id))
            _printSqlWithId(couriercountry_sql, couriercountry_id)

            deliverypackage_sql = "INSERT INTO DeliveryPackage SELECT 1,'{4}',NULL,{0},{1},{2},1,1,'{3}',1,0,1,1,NULL,NULL" \
                                  " WHERE NOT EXISTS (SELECT 1 FROM DeliveryPackage WHERE CountryCode = '{3}' and ClientId={0})" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, _country_code, deliverypkg_name)
            _execSql(deliverypackage_sql, "DeliveryPackage")
            deliverypackage_id = _getColumnValue("DeliveryPackage", "DeliveryPackageId",
                                                 "CountryCode = '{0}' and ClientId={1}".format(_country_code,
                                                                                               _client_id))
            _printSqlWithId(deliverypackage_sql, deliverypackage_id)

            deliverypackageinstruction_sql = "INSERT INTO DeliveryPackageInstruction SELECT {3},{4},{5},NULL,{6},123,NULL,{0},{1},{2},1,1,NULL,NULL,NULL,NULL" \
                                             " WHERE NOT EXISTS " \
                                             "(SELECT 1 FROM DeliveryPackageInstruction WHERE DeliveryPackageId = '{3}' and ClientId={0})" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, deliverypackage_id, clientaddress_id,
                        clientcontact_id, fedex_courier_id)
            _execSql(deliverypackageinstruction_sql, "DeliveryPackageInstruction")
            deliverypackageinstruction_id = _getColumnValue("DeliveryPackageInstruction",
                                                            "DeliveryPackageInstructionId",
                                                            "DeliveryPackageId = '{0}' and ClientId={1}".format(
                                                                deliverypackage_id, _client_id))
            _printSqlWithId(deliverypackageinstruction_sql, deliverypackageinstruction_id)

        # in case we need to add geocity code to the DB
        def initGeoCity():
            address_list = [_cdn_live_addresses, _cdn_work_addresses]
            for y in range(len(address_list)):
                for x in range(len(address_list[y])):
                    geostate_id = _getColumnValue("GeoState", "GeoStateId",
                                                  "StateCode = '{0}'".format(address_list[y][x]['Province']))
                    geocity_sql = "INSERT INTO GeoCity SELECT '{3}', NULL, {4}, {0}, {1}, {2} FROM GeoState gs " \
                                  " WHERE NOT EXISTS (SELECT 1 FROM GeoCity WHERE shortname = '{3}' and geostateid={4})" \
                        .format(_client_id, _last_mod_userId, _last_mod_timestamp, address_list[y][x]['City'],
                                geostate_id)
                    _execSql(geocity_sql, "GeoCity")
                    geocity_id = _getColumnValue("GeoCity", "GeoCityId",
                                                 "ShortName = '{0}' and GeoStateId = {1} and ClientId={2}"
                                                 .format(address_list[y][x]['City'], geostate_id, _client_id))
                    _printSqlWithId(geocity_sql, geocity_id)

        def createEarning(name, xrefcode, codename):
            # do not create if the earning code already exists
            sql = "SELECT COUNT(*) as num FROM PREarning (NOLOCK) WHERE ShortName='{0}' AND XrefCode='{1}'".format(name,
                                                                                                                   xrefcode)
            count = engine.execute(sql).fetchone().num
            if count == 0:
                prearningcode_id = _getColumnValue("PREarningCode", "PREarningCodeId",
                                                   "CodeName = '{0}'".format(codename))
                payrundef_id = _getColumnValue("PRPayRunDef", "PRPayRunDefId", "XrefCode = 'NORMAL'")
                sourcetype_id = _getColumnValue("PREarnDeductSourceType", "PREarnDeductSourceTypeId",
                                                "XrefCode = 'PAYROLL'")
                sql = "INSERT INTO PREarning " \
                      "(ShortName,LongName,XrefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,SortOrder,IsInternal,IsGenerated,PREarningCodeId," \
                      "AllowPayee,PRPayRunDefId,IsHoursRateInPayEntryEnabled,IsPremium,IsPayDateEffective," \
                      "IsAutoCreated,IsValidationRequired,OutputZeroDollarEarning,IsGrossedUp,OverrideGrossedUpPercent," \
                      "PayoutBalanceInGrant,SuppressOnEarningStatement,IsHoursWorkedEnabled,IsOverTimeEarningsEnabled,IsOverTimeHoursEnabled," \
                      "PREarnDeductSourceTypeId,IsFLSAAdjustable,AllowMuliJSalaryAllocationSplit,GenerateOnlyOnCurrentPayGroup,PPACAHours," \
                      "IsEIRefund,PayoutToLastPeriodWithInsurableHours,PayOutBalanceOnTermination,IsAllowAutoPayReductionWithNoRate,DisplayOnCompensationStatement," \
                      "ExcludeScheduledAmountForLeapPeriod,AllowPieceQuantityWithoutPay,DisplayPieceQuantityInsteadOfHours,AdjustDocketRateDuringPayrollCalc,ProratePreTaxDed," \
                      "ExcludeFromDisposableNet,EnableProration,IsHoursRateInPayEntryErrorOverride,IsDecliningBalance,AllowArrears," \
                      "AllowPartial,ReclaimBalanceOnTermination,AllowPartialOnBalanceReclaim,DisplayBalanceOnEarningStatement,IsGenderPayGap)" \
                      " SELECT " \
                      "'{4}', '{4}', '{5}', {0}, {1}, {2}, MAX(a.SortOrder)+1, 0, 0, {3}, " \
                      " 0, {6}, 0, 0, 0, 0, 0, 0, 0, 0," \
                      " 0, 0, 1, 0, 0, {7}, 0, 0, 0, 0," \
                      " 0, 0, 0, 0, 1, 0, 0, 0, 0, 1," \
                      " 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 " \
                      " FROM PREarning a WHERE a.SortOrder < 999" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, prearningcode_id,
                            name, xrefcode, payrundef_id, sourcetype_id)
                _execSql(sql, "PREarning", True)
                # prearning_id = _getColumnValue("PREarning", "PREarningId", "XrefCode ='REGEARN1'")
                # _printSqlWithId(sql, prearning_id)
            else:
                prearning_id = _getColumnValue("PREarning", "PREarningId", "XrefCode ='{0}'".format(xrefcode))
                print("Earning {1}:{0} has already been created".format(prearning_id, name))

        def createEarnings():

            # todo: create (if not exists) RegularEarning
            earnings = [
                {'Name': "RegularEarning", 'XrefCode': "REGEARN1", 'CodeName': "REG"}
            ]

            for i in earnings:
                createEarning(i['Name'], i['XrefCode'], i['CodeName'])

        # createRegEarning()
        # createEarnings()
        # setClientInfo()
        initGeoCity()

    def test_b_Orgunit(self):

        orgunit_corpname = "{1}Corp{0}".format(_uniqueId, _country_code)
        orgunit_corpname_long = "long " + orgunit_corpname
        orgunit_corpname_xrefcode = "ref " + orgunit_corpname
        orgunit_physicallocn = "1"
        orgunit_nonphysicallocn = "0"
        orgunit_isstoreflag = "n"

        def createSiteOrgUnit(legalentity_id):
            orgunit_id = _getCurrentIdValue('OrgUnit') + 1
            site_address = next(_work_address_cycle)
            site_name = "{2}Site{0}_{1}".format(_uniqueId, orgunit_id, _country_code)
            site_name_long = "long " + site_name
            site_name_xrefcode = "ref " + site_name

            city_sql = "SELECT geocityid as id FROM GeoCity WHERE ShortName ='{0}'".format(site_address['City'])
            site_geocity_id = _execSqlWithId(city_sql, True)

            orgunit_columns = " (ShortName,LongName,OrgLevelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,IsStoreFlag,XRefCode,PhysicalLocation," \
                              " Address,StateCode,PostalCode,CountryCode,GeoCityId,IsOrgManaged,IsMobileOrg)"
            values_str = " VALUES('{3}','{4}',{6},{0},{1},{2},'{7}','{5}',{8},'{10}','{11}','{12}','{9}',{13},1,0 )" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, site_name, site_name_long,
                        site_name_xrefcode, _site_level_id, orgunit_isstoreflag, orgunit_physicallocn, _country_code,
                        site_address['Address'], site_address['Province'], site_address['Postal Code'], site_geocity_id)
            _execInsert("OrgUnit", orgunit_columns, values_str, True)

            createOrgUnitLegalEntity(orgunit_id, legalentity_id)
            onsite_org_unit = createOnsiteOrgUnit(orgunit_id)
            createOrgUnitParent(_corp_level_id, _site_level_id)
            return onsite_org_unit

        def createOnsiteOrgUnit(site_orgunit_id):
            #            deptid_list = ",".join(str(x) for x in _list_dept_ids)
            #            print("list of dept ids: " + deptid_list)

            # for idx in _list_dept_ids:
            orgunit_id = site_orgunit_id + 1

            onsite_name = "{2}Onsite{0}_{1}".format(_uniqueId, orgunit_id, _country_code)
            onsite_name_long = "long " + onsite_name
            onsite_name_xrefcode = "ref " + onsite_name

            orgunit_columns = "(ShortName,LongName,OrgLevelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,IsStoreFlag,XRefCode,PhysicalLocation,DepartmentId,IsMobileOrg)"
            values_str = " VALUES('{3}','{4}',{6},{0},{1},{2},'{7}','{5}',{8}, {9}, 0)" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, onsite_name, onsite_name_long,
                        onsite_name_xrefcode, _onsite_level_id, orgunit_isstoreflag, orgunit_nonphysicallocn,
                        _list_dept_ids[0])
            _execInsert("OrgUnit", orgunit_columns, values_str, True)

            createOrgUnitParent(_site_level_id, _onsite_level_id)
            # print("created department id: {0}".format(dept_id))
            return orgunit_id

        def createLegalEntity():
            print("setting up legal entity")

            legalentity_name = "{1}Legal{0}".format(_uniqueId, _country_code)
            legalentity_name_long = "long " + legalentity_name
            legalentity_name_xrefcode = "ref " + legalentity_name
            legalentity_legalidnum = "111111118" # a 9-digit mod 10 number, Business Number must start with 1, 7 or 8
            legalentity_address = next(_work_address_cycle)
            city_sql = "SELECT geocityid as id FROM GeoCity WHERE ShortName ='{0}'".format(legalentity_address['City'])
            legal_geocity_id = _execSqlWithId(city_sql, True)

            legalentity_columns = "(ShortName,LongName,XRefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,CountryCode,Address,GeoCityId,StateCode,PostalCode," \
                                  "LegalIdNumber,LegalIdNumberType,Active,EffectiveStart,IsAutoCreated," \
                                  "IsValidationRequired,IsNotDisbursePrintToBackOffice,AddressCountryCode,ApplyStatusIndianCalculation)"
            values_str = "VALUES('{3}', '{4}', '{5}', {0}, {1}, {2}, '{6}', '{7}', {12}, '{8}', '{9}'," \
                         "'{10}', 1, 1, '{11}', 0, 0, 0, '{6}', 0)" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, legalentity_name, legalentity_name_long,
                        legalentity_name_xrefcode, _country_code, legalentity_address['Address'],
                        legalentity_address['Province'], legalentity_address['Postal Code'],
                        legalentity_legalidnum, _start_date, legal_geocity_id)
            legalentity_id = _execInsertOutputId("LegalEntity", legalentity_columns, values_str, True)
            return legalentity_id

        def createCorpOrgUnit():
            orgunit_columns = "(ShortName,LongName,OrgLevelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,IsStoreFlag,XRefCode,PhysicalLocation,IsOrgManaged,IsMobileOrg)"
            values_str = "VALUES('{3}','{4}',{6},{0},{1},{2},'{7}','{5}',{8},1,0)" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, orgunit_corpname, orgunit_corpname_long,
                        orgunit_corpname_xrefcode, _corp_level_id, orgunit_isstoreflag, orgunit_nonphysicallocn)
            _corp_orgunit_id = _execInsertOutputId("OrgUnit", orgunit_columns, values_str, True)
            createOrgUnitParentCorpParent()

        def createOrgUnitLegalEntity(site_orgunit_id, legalentity_id):
            orgunitlegalentity_columns = "(OrgUnitId, LegalEntityId, EffectiveStart, ClientId, LastModifiedUserId, LastModifiedTimestamp)"
            values_str = " VALUES({4}, {5}, '{3}', {0}, {1}, {2})" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, _start_date, site_orgunit_id, legalentity_id)
            _execInsert("OrgUnitLegalEntity", orgunitlegalentity_columns, values_str, True)

        def createOrgUnitParent(parentlevelid, childlevelid):
            orgunitparent_columns = "(OrgUnitId,ParentOrgUnitId,EffectiveStart,ClientId,LastModifiedUserId,LastModifiedTimestamp)"
            values_str = " SELECT MAX(child.OrgUnitId), MAX(parent.OrgUnitId),'{3}',{0},{1},{2} FROM OrgUnit child, OrgUnit parent " \
                         " WHERE child.OrgLevelId={4} AND parent.OrgLevelId={5}" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, _start_date, childlevelid, parentlevelid)
            _execInsert("OrgUnitParent", orgunitparent_columns, values_str, True)

        def createOrgUnitParentCorpParent():
            orgunitparent_columns = "(OrgUnitId,ParentOrgUnitId,EffectiveStart,ClientId,LastModifiedUserId,LastModifiedTimestamp)"
            values_str = " SELECT MAX(CTE1.OrgUnitId), MIN(CTE1.OrgUnitId),'{3}',{0},{1},{2} FROM OrgUnit CTE1" \
                         " WHERE CTE1.orglevelid = {4}" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, _start_date, _corp_level_id)
            _execInsert("OrgUnitParent", orgunitparent_columns, values_str, True)

        def calibrateOrgLeftRight():
            engine.execute(text("{call CalibrateOrgLeftRight(1000,1,1)};"))
            engine.execute(text("{call PopulateOrgHierarchyTable(1,1)};"))

        def createLegalEntityEmploymentInsurance(legalentity_id):

            # if the Country Code is Canada Setup the Employee Insurance rate
            # todo: set up LegalEntityEmployeeInsurance + LegalEntityEmployeeInsuranceRate
            legalentityemploymentinsurance_columns = "(LegalEntityId,ReferenceCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,RateGroup,IsDefault,LegalEntityEmployeeInsurancePreferenceCodeId)"
            values_str = "VALUES('{3}','0001',{0},{1},{2},'0001',1,1)" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, legalentity_id)
            legalentityemploymentinsurance_id = _execInsertOutputId("LegalEntityEmployeeInsurance", legalentityemploymentinsurance_columns, values_str, True)

            legalentityemploymentinsurancerate_columns = "(LegalEntityEmployeeInsuranceId,Rate,EffectiveStart,ClientId,LastModifiedUserId,LastModifiedTimestamp)"
            values_str = " VALUES ({3},1.4,'{4}',{0},{1},{2})" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, legalentityemploymentinsurance_id, _start_date)
            _execInsert("LegalEntityEmployeeInsuranceRate", legalentityemploymentinsurancerate_columns, values_str, True)

            sql = "UPDATE LegalEntity SET EIReferenceCode={0} WHERE LegalEntityId={1}".format(legalentityemploymentinsurance_id, legalentity_id)
            _execSql(sql, "LegalEntity")

        def createBankAccounts(legalentity_id):
            # todo: 1.set up prbankacount 2.create master bankAccount Setting,3.setup bankaccount def, 4. set up bankacount
            prbankacct_name = "{1}PayrollBank{0}".format(_uniqueId, _country_code)
            prbankacct_name_long = "long " + prbankacct_name
            prbankacct_name_xrefcode = "ref " + prbankacct_name
            prbankacct_routingnum = "075900575"
            prbankacct_acctnum = "123456789"

            legalentity_masterbankacct_name = "{1}LegalMasterBank{0}".format(_uniqueId, _country_code)
            legalentity_masterbankacct_name_long = "long " + legalentity_masterbankacct_name
            legalentity_masterbankacct_name_xrefcode = "ref " + legalentity_masterbankacct_name

            legalentity_bankacctdefname = "{1}LegalBankAccountDef{0}".format(_uniqueId, _country_code)
            legalentity_bankacctdefname_long = "long " + legalentity_bankacctdefname

            legalentity_bankacct_type = 1

            print("set up PRbanking")
            # todo: OUTPUT inserted.xxx only works when inserting values for the entire table; i.e. OUTPUT inserted.xxx follows by VALUES()"

            prbankaccount_columns = "(ShortName,LongName,RoutingNumber,AccountNumber,CheckSigning,XRefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp," \
                                    "UseForPrintingCheck,MICRIsBold)"
            values_str = "VALUES('{3}','{4}',{6},{7},0,'{5}',{0},{1},{2},0,0)" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, prbankacct_name, prbankacct_name_long,
                        prbankacct_name_xrefcode, prbankacct_routingnum, prbankacct_acctnum)
            prbankacct_id = _execInsertOutputId("PRBankAccount", prbankaccount_columns, values_str, True)

            values_str = "VALUES({3},'{4}','{5}','{6}','{7}',NULL,1,NULL,{3},NULL,{0},{1},{2},NULL)" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, legalentity_id,
                        legalentity_masterbankacct_name, legalentity_masterbankacct_name_long,
                        legalentity_masterbankacct_name_xrefcode, _start_date)
            legalentity_masterBankAcctCoulmns = "(LegalEntityId, ShortName, LongName, XrefCode, EffectiveStart, EffectiveEnd, isDefault, FundingIdentifier,TaxServiceId,ServiceUserNumber,ClientId,LastModifiedUserId,LastModifiedTimestamp, IsFasterPayment)"
            legalentity_masterbankacct_id = _execInsertOutputId("LegalEntityMasterBankAccountSetting", legalentity_masterBankAcctCoulmns, values_str, True)


            legalentity_bankAcctColumns = "(ShortName, LongName, IsApproved, EffectiveStart, EffectiveEnd, ApprovedOn, ClientId, LastModifiedUserId, LastModifiedTimeStamp, CVDApproved, CVDApprovedOn, FOSApprovalState, FOSApprovalFileSentOn, FOSApprovedOn, NumberOfFOSCVDTransmitTries, LegalEntityMasterBankAccountSettingId)"
            values_str = "VALUES('{3}','{4}',1,'{5}',NULL,NULL,{0},{1},{2},0,NULL,NULL,NULL,NULL,NULL,{6})" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, legalentity_bankacctdefname,
                        legalentity_bankacctdefname_long, _start_date, legalentity_masterbankacct_id)
            legalentity_bankacctdef_id = _execInsertOutputId("LegalEntityBankAccountDef", legalentity_bankAcctColumns, values_str, True)

            legalentitybankaccount_columns = "(PRBankAccountTypeId,PRBankAccountId,ClientId,LastModifiedUserId,LastModifiedTimestamp,LegalEntityBankAccountDefId," \
                                             "CheckPrinting,CheckSigning,BankTransferDisbursementSourceId,CheckDisbursementSourceId," \
                                             "OverrideLegalEntityName,IsCTCRecipientIdRequired)"
            values_str = " VALUES ({3},{4},{0},{1},{2},{5},0,0,1,1,0,1)" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, legalentity_bankacct_type, prbankacct_id,
                        legalentity_bankacctdef_id)
            _execInsert("LegalEntityBankAccount", legalentitybankaccount_columns, values_str, True)

        def createDepartment():

            for idx in range(_num_depts):
                dept_name = "{2}Dept{0}_{1}".format(_uniqueId, idx + 1, _country_code)
                dept_name_long = "long " + dept_name
                dept_name_xrefcode = "xref " + dept_name

                values_str = "'{3}','{4}',NULL,{0},{1},{2},'{5}',NULL" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, dept_name, dept_name_long,
                            dept_name_xrefcode)
                dept_id = _execInsertValuesOutputId("Department", values_str)
                _list_dept_ids.append(dept_id)

        legalentity_id = createLegalEntity()
        createLegalEntityEmploymentInsurance(legalentity_id)
        createBankAccounts(legalentity_id)
        createDepartment()
        createCorpOrgUnit()

        for x in range(_num_paygroup_sites):
            orgunit_id = createSiteOrgUnit(legalentity_id)
            _list_paygroup_onsite_orgunit_ids.append(orgunit_id)

        calibrateOrgLeftRight()

    def test_c_Payroll(self):

        sql_str = "SELECT MAX(OrgUnitId) as id FROM OrgUnit WHERE ShortName LIKE '{0}%' and OrgLevelId=0".format(
            _country_code)
        creation_orgunit_id = engine.execute(sql_str).fetchone().id

        def getAllPREarningTypes():
            sql = "SELECT PREarningTypeId as id FROM PREarningType"
            rows = engine.execute(sql).fetchall()
            # values = ','.join(rows)
            values = [str(x.id) for x in rows]
            return ','.join(values)

        def generateJob():
            # todo 2. create job
            job_name = "{1}Job{0}".format(_uniqueId, _country_code)
            job_name_long = "long " + job_name
            job_name_xrefcode = "ref " + job_name

            job_columns = " (ShortName,LongName,ClientId,LastModifiedUserId,LastModifiedTimestamp,XrefCode,IsUnionJob,EffectiveStart)"
            values_str = " VALUES( '{3}','{4}',{0},{1},{2},'{5}',0, '{6}' )" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, job_name, job_name_long, job_name_xrefcode,
                        _start_date)
            _execInsert("Job", job_columns, values_str, True)

        def generateDeptJob():
            # todo: 3. generate depjobid
            deptjob_name = "{1}DeptJob{0}".format(_uniqueId, _country_code)
            deptjob_name_long = "long " + deptjob_name
            deptjob_name_xrefcode = "ref " + deptjob_name
            deptjob_status = "OPEN"

            deptjob_columns = "(DepartmentId, JobId, ClientId, LastModifiedUserId, LastModifiedTimestamp, CreationOrgUnitId, EffectiveStart, IsNonService," \
                              " ShortName, LongName, Officer, Executive, Status, IsWCBExempt, XRefCode, PPACAFullTime)"
            values_str = "SELECT MAX(dept.DepartmentId), MAX(job.JobId),{0},{1},{2},{3},'{4}',0,'{5}','{6}',0,0,'{8}',0,'{7}',0" \
                         " FROM Department dept, Job job WHERE dept.ShortName LIKE '{9}%' and job.ShortName LIKE '{9}%'" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, creation_orgunit_id, _start_date,
                        deptjob_name, deptjob_name_long, deptjob_name_xrefcode, deptjob_status, _country_code)
            deptjob_id = _execInsertOutputId("DeptJob", deptjob_columns, values_str, True)

            deptjobassignment_columns = "(DeptJobId,OrgUnitId,ClientId,LastModifiedUserId,LastModifiedTimestamp,EffectiveStart)"
            values_str = "VALUES({3},{4},{0},{1},{2},{5})" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, deptjob_id, creation_orgunit_id,
                        _start_date)
            _execInsert("DeptJobAssignment", deptjobassignment_columns, values_str, True)

        def createPRPayrollPolicy():
            # Todo: 1. create prpayrollpolicy ;2. map prpayrollpolicy to org 3.map PrPayRollRuleSet link to PrpayrollPolicy

            print("creating payrollPolicy")

            prpayrollpolicy_name = "{0}PayrollPolicy{1}".format(_country_code, _uniqueId)
            prpayrollpolicy_name_long = "long " + prpayrollpolicy_name
            prpayrollpolicy_name_xrefcode = "ref " + prpayrollpolicy_name

            prpayrollpolicy_columns = "(ShortName,LongName,StartDate,XrefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp)"
            values_str = "VALUES('{3}','{4}','{6}','{5}',{0},{1},{2})" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, prpayrollpolicy_name,
                        prpayrollpolicy_name_long, prpayrollpolicy_name_xrefcode, _start_date)
            prpayrollpolicy_id = _execInsertOutputId("PRPayrollPolicy", prpayrollpolicy_columns, values_str, True)

            createPRPayrollPolicyRuleSet(prpayrollpolicy_id)
            # map_prPayrollpolicyRuleset()
            generatePRPayrollRules()

            return prpayrollpolicy_id

        def createPRPayrollPolicyRuleSet(payrollpolicy_id):
            prpayrollpolicy_ruleset_name = "{1}PayrollPolicyRuleSet{0}".format(_uniqueId, _country_code)
            prpayrollpolicy_ruleset_name_long = "long " + prpayrollpolicy_ruleset_name

            values_str = " VALUES({3},'{4}','{5}', 1, {0}, {1}, {2})" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, payrollpolicy_id,
                        prpayrollpolicy_ruleset_name, prpayrollpolicy_ruleset_name_long)
            _execInsert("PRPayrollPolicyRuleSet", "", values_str, True)

        def generatePRPayrollRules():
            # Todo: 1.autopayRule, 2. earningRule, 3. dedcutionRule, 4. taxRule, 5.wcbRule

            regearn_id = _getColumnValue("PREarning", "PREarningId", "XrefCode = 'REGEARN1'")
            dfelement_autopay_rule = _getColumnValue("DFElement", "DFElementId", "CodeName='AutoPayRule'")
            autopayrule_id = generatePRPayrollPolicyRule('AutoPayRule', dfelement_autopay_rule, 1)
            generatePRPayrollPolicyElem(autopayrule_id, dfelement_autopay_rule, "AUTO_PAY_EARNING", regearn_id)

            dfelement_applyearning_rule = _getColumnValue("DFElement", "DFElementId", "CodeName='ApplyEarningsRule'")
            generatePRPayrollPolicyRule('EarningRule', dfelement_applyearning_rule, 2)

            dfelement_applydeduction_rule = _getColumnValue("DFElement", "DFElementId",
                                                            "CodeName='ApplyDeductionsRule'")
            generatePRPayrollPolicyRule('DeductionRule', dfelement_applydeduction_rule, 3)

            dfelement_applytax_rule = _getColumnValue("DFElement", "DFElementId", "CodeName='ApplyTaxesRule'")
            generatePRPayrollPolicyRule('TaxRule', dfelement_applytax_rule, 4)

        def generatePRPayrollPolicyElem(rule_id, dfelement_id, dfelementparam_codename, value):
            dfelementparam_id = _getColumnValue("DFElementParam", "DFElementParamId",
                                                "DFElementId={0} and CodeName ='{1}'"
                                                .format(dfelement_id, dfelementparam_codename))
            values_str = " VALUES({3},NULL,{4},'{5}',{1},{2},{0})" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, rule_id, dfelementparam_id, value)
            _execInsert("PRPayrollPolicyElementValue", "", values_str, True)

        def generatePRPayrollPolicyRule(name, dfelement_id, sequence):
            ruleset_id = _getCurrentIdValue('PRPayrollPolicyRuleSet')
            prpayrollpolicyrule_name = _country_code + name
            prpayrollpolicyrule_name_long = "long " + prpayrollpolicyrule_name

            values_str = " VALUES ({3},'{4}','{5}',{6},{7},1,{1},{2},{0},'{8}',NULL)" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, ruleset_id, prpayrollpolicyrule_name,
                        prpayrollpolicyrule_name_long, dfelement_id, sequence, _start_date)
            prpayrollpolicyrule_id = _execInsertOutputId("PRPayrollPolicyRule", "", values_str, True)
            return prpayrollpolicyrule_id

        def policyAssignment(policyName):
            '''
            MAX orgUnit will be latest create OrgUnit Corp
            MIN orgUnit will be the Corp
            :param policyName:
            :return:
            '''
            policyassignment_sql = "INSERT INTO {3}Assignment" \
                                   " SELECT MAX(newPunch.{3}Id), MIN(ou.OrgUnitId),{0},{1},{2}" \
                                   " FROM {3} newPunch, OrgUnit ou WHERE newPunch.ShortName like '{4}%' and ou.OrgLevelId=0" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, policyName, _country_code)
            print(policyassignment_sql)
            '''
                Error to display the recent inserted PunchPolicyAssignment
            '''
            _execSql(policyassignment_sql, "{0}Assignment".format(policyName), False)

        def generatePunchPolicy():
            punchpolicy_name = "{1}PunchPolicy{0}".format(_uniqueId, _country_code)
            punchpolicy_name_long = "long " + punchpolicy_name
            punchpolicy_name_xrefcode = "xref " + punchpolicy_name

            punchpolicy_sql = "INSERT INTO PunchPolicy" \
                              " (ShortName,LongName,GraceInEarly,MealGrace,BreakGrace,GraceAdjustInEarly,MealsEnabled,BreaksEnabled,MealsPaid,BreaksPaid," \
                              "MainRoundNumerator,MainRoundDenominator,MealRoundNumerator,MealRoundDenominator,MealLengthRounding," \
                              "BreakRoundNumerator,BreakRoundDenominator,BreakLengthRounding,ClientId,LastModifiedUserId," \
                              "LastModifiedTimestamp,TimeBetweenMB,CreationOrgUnitId,XRefCode,ValidateMain," \
                              "ExceptionInEarly,ValidateMeal,MealException,ValidateBreak,BreakException," \
                              "RoundMain,RoundMeal,RoundBreak,GraceInLate,GraceOutEarly," \
                              "GraceOutLate,ExceptionInLate,ExceptionOutEarly,ExceptionOutLate,AutoInjectBreaks," \
                              "AutoInjectMeals,UseInAndOutAsMB,UseInAndOutAsMBThreshold,UseInAndOutAsMBType,PunchClock," \
                              "TimesheetEntry,AutoPay,TimesheetEnterJob,TimesheetEnterProject,TimesheetEnterDocket," \
                              "ValidateMealLength,ValidateBreakLength,AutoExtendBreaks,AutoExtendMeals,ExtendBreaksBySplit," \
                              "ExtendMealsBySplit,GraceAdjustInLate,ValidateAgainstUnpostedSchedules,AutoInjectMBUsingSchedule,DisplayUnpostedSchedules," \
                              "ValidateClockOrgUnit,GenerateEarlyLatePayCodes,ConsecutivePunchThreshold,MealPenaltyEnabled,MealPenalty1Minutes," \
                              "MealPenalty1MinutesToWaive,MealPenalty1EmployeeWaivesByDefault,MealPenalty1SupervisorWaivesByDefault,MealPenalty2Minutes,MealPenalty2MinutesToWaive," \
                              "MealPenalty2EmployeeWaivesByDefault,MealPenalty2SupervisorWaivesByDefault,ValidateClockDeviceGroup,ValidateEmployeePin,ValidateSupervisorPin," \
                              "RoundSeconds,SupervisorInEarly,SupervisorInLate,AutoOutBySchedule,BusinessDayBySchedule," \
                              "UnauthorizeOnEdit,GraceAdjustOutEarly,GraceAdjustOutLate,AutoInjectPunchesBySchedule,PeriodApproval," \
                              "TimeClockLocationTransfer,TimeClockPositionTransfer,TimeClockProjectTransfer,TimeClockDocketTransfer," \
                              "TimeClockDocketTransferWithQty,MainRoundNumeratorOut,MainRoundDenominatorOut,TimeClockSeparateDocketQty,GenerateDurationBasedPayCodes," \
                              "TimeClockCombinedTransfer,MinimumUnscheduledShiftMealLength,MinimumUnscheduledShiftBreakLength,OutWithMealPrompt,OutWithBreakPrompt," \
                              "EnterOrg,MealDurationRounding,NetworkLocationValidation,TipEntryPrompt,OutWithTipEntryPrompt," \
                              "EmployeeTimesheetApprovalEdit,RelayControlScheduleValidationType,ProcessBiometricFailure,TransfersUsePriorRateIfJobRateUnset,ProcessPictureFailure," \
                              "MealSubsidyPayAdjCodeId,MealSubsidyAmount,MealSubsidyMaxPerDay,MealSubsidyEnabled,AllowUnscheduledPunch," \
                              "DurationTSUseStartEndTimes,AllowPunchingAtUnassignedLocations,MealPenaltyUseNetTime,MealPenaltyRequiredMinutes,MinimumScheduledShiftMealLength," \
                              "MinimumScheduledShiftBreakLength,GenerateSeparateDurationBasedPayCodes,RecordPunchGeoLocation)" \
                              " VALUES('{3}','{4}',0,0,0,'n','n','n','n','n',0,0,0,0,'n',0,0,'n',{0},{1}," \
                              "{2},0,{6},'{5}',1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0," \
                              "0,1,120,'m',1,0,0,0,0,0,0,0,0,0,0,0,'n',1,0,0," \
                              "0,0,0,0,300,360,0,0,540,600,0,0,0,0,0,1,0,0,0,0," \
                              "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0," \
                              "0,0,0,0,0,0,1,0,0,0,-1,0,1,0,0,0,0,30,0," \
                              "0,0,0,0)" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, punchpolicy_name, punchpolicy_name_long,
                        punchpolicy_name_xrefcode, creation_orgunit_id)

            _execSql(punchpolicy_sql, "PunchPolicy", True)

            policyAssignment("PunchPolicy")

        def generatePayHolidayGroup():
            payholidaygroup_name = "{1}PayHolidayGroup{0}".format(_uniqueId, _country_code)
            payholidaygroup_name_long = "long " + payholidaygroup_name
            payholidaygroup_name_xrefcode = "ref " + payholidaygroup_name

            payholidaygroup_sql = "INSERT INTO PayHolidayGroup " \
                                  "VALUES('{3}','{4}',{0},{1},{2},'{5}',{6},NULL)" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, payholidaygroup_name,
                        payholidaygroup_name_long, payholidaygroup_name_xrefcode, creation_orgunit_id)

            _execSql(payholidaygroup_sql, "PayHolidayGroup", True)

            policyAssignment("PayHolidayGroup")

        def generateTimeOffPolicy():
            print("TimeOffPolicy")
            timeoffpolicy_name = "{1}TimeOffPolicy{0}".format(_uniqueId, _country_code)
            timeoffpolicy_name_long = "long " + timeoffpolicy_name
            timeoffpolicy_name_xrefcode = "ref " + timeoffpolicy_name

            timeoffpolicy_columns = "(ShortName,LongName,EnforceAllBlackoutDates,XRefCode,ClientId,LastModifiedUserId," \
                                    "LastModifiedTimestamp,AvailabilityEditingBlackoutWeeks,PreventRequestOnHolidays,AllDayOnly,EnforcePeriodWindow," \
                                    "SelectSchedule,IsElapsedTime,ShowElapsedTimeSelection,CalculateOnHolidays,AllowAdvancePay," \
                                    "PreventRequestOnTransmittedPeriods,PayAmountViewOnly,PreventRequestOnLockedPeriods,RestrictTotalWeeklyHoursToNormalWeeklyHours,PriorDaysToStartPayRecalc)"
            values_str = " VALUES('{3}','{4}',0,'{5}',{0},{1},{2},2,0,0,0,0,0,0,0,0,0,0,0,0,0)" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, timeoffpolicy_name, timeoffpolicy_name_long,
                        timeoffpolicy_name_xrefcode)
            _execInsert("TimeOffPolicy", timeoffpolicy_columns, values_str, True)

        def generateEmployeeSchedulePolicy():
            print("employeeSchedulePolicy")
            employeeschedulepolicy_name = "{1}EmployeeSchedulePolicy{0}".format(_uniqueId, _country_code)
            employeeschedulepolicy_name_long = "long " + employeeschedulepolicy_name
            employeeschedulepolicy_name_xrefcode = "ref " + employeeschedulepolicy_name

            employeeschedulepolicy_sql = "INSERT INTO EmployeeSchedulePolicy" \
                                         " VALUES('{4}','{5}','{3}',NULL, {0}, {1}, {2}, '{6}', NULL)" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, _start_date,
                        employeeschedulepolicy_name, employeeschedulepolicy_name_long,
                        employeeschedulepolicy_name_xrefcode)
            _execSql(employeeschedulepolicy_sql, "EmployeeSchedulePolicy", True)

        def generatePayPolicy():
            print("payPolicy")
            paypolicy_name = "{1}PayPolicy{0}".format(_uniqueId, _country_code)
            paypolicy_name_long = "long " + paypolicy_name
            paypolicy_name_xrefcode = "ref " + paypolicy_name

            paypolicy_sql = "INSERT INTO PayPolicy" \
                            " VALUES({6},'{3}','{4}','{5}',{0},{1},{2},0,0,0,0,0,1,0,0,NULL,NULL,0)" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, paypolicy_name, paypolicy_name_long,
                        paypolicy_name_xrefcode, creation_orgunit_id)
            _execSql(paypolicy_sql, "PayPolicy", True)

        def generateEntitlementPolicy():
            # print("entitleMentPolicy")
            entitlementpolicy_name = "{1}EntitlementPolicy{0}".format(_uniqueId, _country_code)
            entitlementpolicy_name_long = "long " + entitlementpolicy_name
            entitlementpolicy_name_xrefcode = "ref " + entitlementpolicy_name

            # sql="insert into EntitlementPolicy values ('{0}','{0}','{1}',null,{2},{3},{4},'TestFga')" \
            #    "".format(entitlementpolicy_name,datetime.now().year,clientId,lastModifiedUserId,lastModifiedTimeStamp)
            # engine.execute(sql)
            entitlementpolicy_sql = "INSERT INTO EntitlementPolicy" \
                                    " VALUES('{4}','{5}','{3}', NULL,{0},{1},{2},'{6}')" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, _start_date,
                        entitlementpolicy_name, entitlementpolicy_name_long, entitlementpolicy_name_xrefcode)
            _execSql(entitlementpolicy_sql, "EntitlementPolicy",True)

        def enableAutoPay():
            hourly_nonexempt_paytype_id = getPayTypeId('Hourly(Non-Exempt)')
            hourly_exempt_paytype_id = getPayTypeId('Hourly(Exempt)')
            salaried_exempt_paytype_id = getPayTypeId('Salaried(Exempt)')
            salaried_nonexempt_paytype_id = getPayTypeId('Salaried(Non-Exempt)')
            updatePayTypeTable(0, hourly_nonexempt_paytype_id)
            updatePayTypeTable(0, hourly_exempt_paytype_id)
            updatePayTypeTable(1, salaried_exempt_paytype_id)
            updatePayTypeTable(1, salaried_nonexempt_paytype_id)

        def getPayTypeId(xrefcode):
            sql = "SELECT PayTypeId as id FROM PayType where XRefCode='{0}' and Clientid={1}" \
                .format(xrefcode, _client_id)
            return engine.execute(sql).fetchone().id

        def updatePayTypeTable(is_payroll_autopay, paytype_id):
            sql = "UPDATE PayType SET IsPayrollAutoPay={0} where PayTypeId={1}".format(is_payroll_autopay, paytype_id)
            engine.execute(sql)

        # generate_department()
        generateJob()
        generateDeptJob()
        # map_deptjob()
        generatePunchPolicy()
        generateTimeOffPolicy()
        generateEmployeeSchedulePolicy()
        generatePayHolidayGroup()
        generateEntitlementPolicy()
        generatePayPolicy()

        policy_id = createPRPayrollPolicy()
        createPRPayrollPolicyRuleSet(policy_id)
        generatePRPayrollRules()

        enableAutoPay()

    # def test_d_PayrollPolicy(self):

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
            current_year = datetime.now().year
            payholidaygroup_id = _getColumnValue("PayHolidayGroup", "MAX(PayHolidayGroupId)",
                                                 "ShortName like '{0}%'".format(_country_code))
            startdayofweek_id = 1  # 1 = Monday, ..., 7 = Sunday
            paydayofweek_id = 5
            businessday_starttime = "08:00:00"
            paydate_adjusttype_id = 1  # 1 = date before, 2 = date after, 3 = no offset
            paydate_offset = 2
            taxyear_startmonth = 4 if _country_code == 'GBR' else 'NULL'
            taxyear_startday = 6 if _country_code == 'GBR' else 'NULL'
            maxdetailrecords_timedata = 1000

            paygroup_identifier = "'E{0}'".format(random.randrange(1000, 9999)) if _country_code == 'CAN' else 'NULL'

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
                           "GrossDecrementEarningType,DefaultBusinessDateValue,PayGroupIdentifier)" \
                           " VALUES('{3}','{4}',{6},'{7}','{5}',{0},{1},{2},{13},0," \
                           "'{7}','{7}',0,0,{11},{6},0,0,'{12}',0," \
                           "0,1,4,0,{14},{18},{15},{15},'{7}',{8}," \
                           "0,1,0,1,{10},0,0,0,{15},0," \
                           "{6},1,0,0,2,0,0,0,0,0," \
                           "0,0,0,0,{19},0,0,1,0,{16}," \
                           "{17},0,0,0,0,0,0,0,0,''," \
                           "'',0,{9})" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, paygroup_name, paygroup_name_long,
                        paygroup_name_xrefcode, pay_freq, current_year, geo_country_id, paygroup_identifier,
                        payholidaygroup_id, startdayofweek_id, businessday_starttime, num_future_periods,
                        paydate_adjusttype_id,
                        paydate_offset, taxyear_startmonth, taxyear_startday, paydayofweek_id,
                        maxdetailrecords_timedata)

            paygroup_id = _execSqlWithResult(paygroup_sql, 'Paygroup')
            return paygroup_id

        def paygroupAssignment(paygroup_id, orgunitId):
            paygroup_assignment_sql = "INSERT INTO PaygroupAssignment" \
                                      " VALUES({3},{4},{0},{1},{2})" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, paygroup_id, orgunitId)
            _execSql(paygroup_assignment_sql, "PaygroupAssignment")

        def createPaygroupMapping(paygroup_id):
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

            paygroupearningruleset_id = createPaygroupEarningRuleSet(paygroup_id)
            paygrouprule_id = createPaygroupEarningRule(paygroupearningruleset_id, dfelem_paygroupearningmapping_id)
            mapPaygroupEarningElementValue(paygrouprule_id, dfelemparam_paycategories_id, reg_paycategory_id)
            mapPaygroupEarningElementValue(paygrouprule_id, dfelemparam_payadjcodes_id, work_payadjcode_id)
            mapPaygroupEarningElementValue(paygrouprule_id, dfelemparam_earningcode_id, reg_earning_id)

        def createPaygroupEarningRuleSet(payGroupId):
            paygroupearningruleset_name = "{1}PaygroupEarningRuleSet{0}".format(_uniqueId, _country_code)
            paygroupearningruleset_name_long = "long " + paygroupearningruleset_name

            value_str = "'{3}','{4}',1,{0},{1},{2},{5}" \
                .format(_client_id, _last_mod_userId, _last_mod_timestamp, paygroupearningruleset_name,
                        paygroupearningruleset_name_long, payGroupId)
            paygroupearningruleset_id = _execInsertValuesOutputId("PayGroupEarningRuleSet", value_str)

            return paygroupearningruleset_id

        def createPaygroupEarningRule(paygroupearningruleset_id, dfelement_id):
            paygroupearningrule_name = "{1}PaygroupEarningRule{0}".format(_uniqueId, _country_code)
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
            orgunit_id = engine.execute("SELECT MAX(OrgUnitId) as id FROM OrgUnit WHERE OrgLevelId=0").fetchone().id
            paygroupAssignment(paygroup_id, orgunit_id)

        def generatePaygroupCalendar(paygroup_id, payfreq_id):

            current_year = datetime.now().year

            if _country_code == 'USA':
                list_holidays = holidays.UnitedStates(years=current_year)
            elif _country_code == 'CAN':
                list_holidays = holidays.Canada(years=current_year)
            elif _country_code == 'GBR':
                list_holidays = holidays.UnitedKingdom(years=current_year)

            start_date = date(current_year, 1, 1)
            pay_type = {1: relativedelta(weeks=+1),
                        2: relativedelta(weeks=+2),
                        3: relativedelta(days=+14),
                        4: relativedelta(months=+1)}

            first_paydate_current_year = start_date + pay_type[payfreq_id]

            startdayofweek = _getColumnValue("Paygroup", "StartofWeek", "PaygroupId = {0}".format(paygroup_id))
            paydayofweek = _getColumnValue("Paygroup", "PayDateDayOfWeekId", "PaygroupId = {0}".format(paygroup_id))

            byweekday_code = ['', MO, TU, WE, TH, FR, SA, SU]
            print(byweekday_code[3])

            if payfreq_id == 1:  # weekly
                # list_pay_dates = list(rrule(DAILY, byweekday=byweekday_code[paydayofweek], interval=1, count=52,
                #                            dtstart=first_paydate_current_year))
                list_calendar_start = list(rrule(DAILY, byweekday=byweekday_code[startdayofweek], interval=1, count=52,
                                                 dtstart=start_date))
                list_calendar_end = [x + pay_type[payfreq_id] for x in list_calendar_start]
            elif payfreq_id == 2:  # bi-weekly
                # list_pay_dates = list(rrule(DAILY, byweekday=byweekday_code[paydayofweek], interval=2, count=26,
                #                            dtstart=first_paydate_current_year))
                list_calendar_start = list(rrule(DAILY, byweekday=byweekday_code[startdayofweek], interval=2, count=26,
                                                 dtstart=start_date))
                list_calendar_end = [x + pay_type[payfreq_id] for x in list_calendar_start]
            elif payfreq_id == 3:  # semi-monthly
                list_calendar_start = list(rrule(MONTHLY, bymonthday=(1, 15), interval=1, count=24,
                                                 dtstart=start_date))
                list_calendar_end = list(rrule(MONTHLY, bymonthday=(1, 15), interval=1, count=24,
                                               dtstart=first_paydate_current_year))
                # list_pay_dates = [x + relativedelta(days=+5) for x in list_calendar_start]
            elif payfreq_id == 4:  # monthly
                list_calendar_start = list(rrule(MONTHLY, bymonthday=1, interval=1, count=12,
                                                 dtstart=start_date))
                list_calendar_end = [x + pay_type[payfreq_id] for x in list_calendar_start]

            list_effective_start = [x + timedelta(hours=8) for x in list_calendar_start]
            list_effective_end = [x + timedelta(hours=8) for x in list_calendar_end]
            list_transmitby_dates = [x - timedelta(1) for x in list_calendar_end]
            list_payimpound_dates = [x + timedelta(2) for x in list_calendar_end]
            list_payrun_dates = [x + timedelta(2) for x in list_calendar_end]
            list_pay_dates = [x + timedelta(4) for x in list_calendar_end]

            print("pay dates:{0}".format(list_pay_dates))
            # print("start dates:{0}".format(list_start_dates))
            print("calendar starts:{0}".format(list_calendar_start))
            print("calendar ends:{0}".format(list_calendar_end))
            print("effective starts:{0}".format(list_effective_start))
            print("effective ends:{0}".format(list_effective_end))
            print("transmitby dates:{0}".format(list_transmitby_dates))
            print("payimpound dates:{0}".format(list_payimpound_dates))
            print("payrun dates:{0}".format(list_payrun_dates))

            def auto_shift(day):
                while (day in list_holidays) or (day.isoweekday() > 5):
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
                        .format(_client_id, _last_mod_userId, _last_mod_timestamp, paygroup_id, list_effective_start[x],
                                list_effective_end[x], list_transmitby_dates[x], str(x + 1).zfill(2),
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
        # payfreq_id = _getColumnValue('PayFrequency', 'PayFrequencyId', "ShortName='Weekly'")
        for x in range(_num_paygroups):
            name = "{1}{2}Paygroup{0}".format(_uniqueId, _country_code, _id_paygroup_list[x])
            paygroup_freq = "Monthly"  # Weekly, Bi-Weekly, Semi-Monthly, Monthly
            payfreq_id = _getColumnValue("PayFrequency", "PayFrequencyId", "ShortName='{0}'".format(paygroup_freq))
            paygroup_id = generatePaygroup(name, payfreq_id)
            mapLatestPayGroupOrgunit(paygroup_id)
            createPaygroupMapping(paygroup_id)
            generatePaygroupCalendar(paygroup_id, payfreq_id)

            _list_paygroup_ids.append(int(paygroup_id))

    def test_f_Employee(self):

        sql1 = "SET IDENTITY_INSERT Appuser ON"
        engine.execute(sql1)

        # appuser
        password = "$2a$04$y9FvNfU.2Pr9p.j.6DUz0eBek5AAXfSYnYJ4z41ck1pQQISYJ9ecq"

        # employee
        birth_date = "1990-07-12"
        gender = "M"
        #registeredDisabled = "false"

        employee_SSN = "864865241"

        normal_weekly_hour = 40
        normal_semimonthly_hour = 88  # needed for monthly paygroups autopays
        base_salary = 52000
        base_rate = base_salary / (52 * normal_weekly_hour)
        #average_daily_hour = 8
        is_virtual = 0

        employmentstatus_id = _getColumnValue('EmploymentStatus', 'EmploymentStatusId',
                                              "ShortName='Active' and ClientId={0}".format(_client_id))
        paytype_id = _getColumnValue('PayType', 'PayTypeId',
                                     "ShortName='Salaried(Non-Exempt)' and ClientId={0}".format(_client_id))
        payclass_id = _getColumnValue('PayClass', 'PayClassId', "ShortName='FT' and ClientId={0}".format(_client_id))
        employee_entitytype_id = _getColumnValue('EntityType', 'EntityTypeId', "ShortName='Employee'")
        employmentstatusreason_id = _getColumnValue('EmploymentStatusReason', 'EmploymentStatusReasonId',
                                                    "ShortName='New Hire'")
        contactinfotype_id = _getColumnValue('ContactInformationType', 'ContactInformationTypeId',
                                             "ShortName='Primary Residence'")

        punch_policy_id = _getCurrentIdValue(
            'PunchPolicy')  # str(engine.execute("select IDENT_CURRENT ('punchPolicy') as id").fetchone().id)
        pay_policy_id = _getCurrentIdValue(
            'PayPolicy')  # str(engine.execute("select IDENT_CURRENT ('payPolicy') as id").fetchone().id)
        pay_holiday_group_id = _getCurrentIdValue(
            'PayHolidayGroup')  # str(engine.execute("select IDENT_CURRENT ('payHolidayGroup') as id").fetchone().id)
        entitlement_policy_id = _getCurrentIdValue(
            'EntitlementPolicy')  # str(engine.execute("select IDENT_CURRENT ('entitlementPolicy') as id").fetchone().id)
        time_off_policy_id = _getCurrentIdValue(
            'TimeOffPolicy')  # str(engine.execute("select IDENT_CURRENT ('timeOffPolicy') as id").fetchone().id)
        employee_schedule_policy_id = _getCurrentIdValue(
            'EmployeeSchedulePolicy')  # str(engine.execute("select IDENT_CURRENT ('employeeSchedulePolicy') as id").fetchone().id)
        pr_payroll_policy_id = _getCurrentIdValue(
            'PRPayrollPolicy')  # str(engine.execute("select IDENT_CURRENT ('prPayrollPolicy') as id").fetchone().id)
        dept_job_id = _getCurrentIdValue(
            'DeptJob')  # str(engine.execute("select IDENT_CURRENT ('deptjob') as id").fetchone().id)

        def createEmployees(id, num, list_onsite_orgunit_ids, paygroup_id):

            start_number = id
            end_number = start_number + num
            print("Employee id starts at [" + str(start_number) + "] and ends at [" + str(end_number - 1) + "]")

            onsite_orgunit_id_cycle = cycle(
                list_onsite_orgunit_ids)  # if len(_list_small_paygroup_onsite_orgunit_ids) > 0 else 0
            # paygroup_id_cycle = cycle(list_paygroup_ids)  # if len(_list_small_paygroup_ids) > 0 else 0

            print("the employee will insert into the orgunitid:{0}, paygroupid:{1}"
                  .format(list_onsite_orgunit_ids, paygroup_id))

            t0 = time.time()
            for employee_id in range(start_number, end_number):
                onsite_orgunit_id = next(onsite_orgunit_id_cycle) if str(onsite_orgunit_id_cycle) != '0' else 0
                # paygroup_id = next(paygroup_id_cycle) if str(paygroup_id_cycle) != '0' else _getCurrentIdValue('PayGroup')  # engine.execute("select IDENT_CURRENT ('payGroup') as id").fetchone().id
                live_address = next(_live_address_cycle)

                employee_xrefcode = "{1}_{2} XrefCode{0}".format(employee_id, _country_code, live_address['Province'])
                # display_name = "{2}_{1} Emp_{0}".format(employee_id, live_address['Province'],_country_code)
                last_name = "Last{0}".format(employee_id)
                first_name = "First{0}".format(employee_id)
                display_name = first_name + " " + last_name
                login_id = "Login{0}".format(employee_id)

                appuser_sql = "INSERT INTO AppUser" \
                              " (UserId,LoginId,Password,IsApproved,IsLockedOut,CreateTimestamp,ClientId,LastModifiedUserId,LastModifiedTimestamp,CultureID," \
                              "CanSeeSelf,ResetOnNextLogin,ShowDisclaimer,UsesOrgSecurity,EntityTypeId,IsDeleted,Display24HourTime,HashMethod,IsPinLockedOut,IsBiometricLockedOut," \
                              "ShowEmailMissing,HasAcceptedPrivacyPolicy,HasAcceptedTermsOfUse,AllowNativeAuthentication)" \
                              " VALUES({3},'{4}','{5}',1,0,{2},{0},{1},{2},{6}," \
                              "0,0,0,1,{7},0,0,'BCrypt4',0,0," \
                              "1,0,0,0)" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, employee_id, login_id, password,
                            _culture_id, employee_entitytype_id)

                _execSql(appuser_sql, "AppUser")

                employee_sql = "INSERT INTO Employee" \
                               " (EmployeeId,LastName,FirstName,BirthDate,HireDate,ClientId,LastModifiedUserId,LastModifiedTimestamp," \
                               "XRefCode,Gender,StartDate,SocialSecurityNumber,DisplayName," \
                               "BioExempt,RequiresExitInterview,PhotoExempt,SendFirstTimeAccessEmail,FirstTimeAccessVerificationAttempts,FirstTimeAccessEmailSentCount)" \
                               " VALUES('{3}','{4}','{5}','{6}','{7}',{0},{1},{2}," \
                               "'{8}','{9}','{7}','{10}','{11}'," \
                               "0,0,0,0,0,0)" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, employee_id, last_name, first_name,
                            birth_date, _start_date, employee_xrefcode, gender, employee_SSN, display_name)
                _execSql(employee_sql, "Employee")

                employeeemploymentstatus_sql = "INSERT INTO EmployeeEmploymentStatus" \
                                               " (EmploymentStatusId,PayTypeId,PayClassId,EmployeeId,EffectiveStart,Reason,ClientId,LastModifiedUserId," \
                                               "LastModifiedTimestamp,PunchPolicyId,PayPolicyId,NormalWeeklyHours,BaseRate,CreatedUserId,CreatedTimestamp,PayGroupId," \
                                               "BaseSalary,CreateShiftRotationShift,ChecksumTimestamp,EmployeeNumber,PRPayrollPolicyId," \
                                               "PayHolidayGroupId,EntitlementPolicyId,TimeOffPolicyId,EmployeeSchedulePolicyId,NormalSemiMonthlyHoursTop,NormalSemiMonthlyHoursBottom)" \
                                               " VALUES({3},{4},{5},{6},'{7}',{8},{0},{1}," \
                                               "{2},{9},{10},{11},{12},0,'{7}',{13}," \
                                               "{14},0,NULL,'{15}',{16}," \
                                               "'{17}',{18},'{19}',{20},{21},{21})" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, employmentstatus_id, paytype_id,
                            payclass_id, employee_id, _start_date, employmentstatusreason_id, punch_policy_id,
                            pay_policy_id, normal_weekly_hour, base_rate, paygroup_id, base_salary,
                            employee_xrefcode, pr_payroll_policy_id, pay_holiday_group_id, entitlement_policy_id, time_off_policy_id,
                            employee_schedule_policy_id, normal_semimonthly_hour)
                _execSql(employeeemploymentstatus_sql, "EmployeeEmploymentStatus", True)

                employeeworkassignment_sql = "INSERT INTO EmployeeWorkAssignment" \
                                             " (EmployeeId,DeptJobId,OrgUnitId,IsPrimary,EffectiveStart,ClientId,LastModifiedUserId,LastModifiedTimestamp," \
                                             "IsVirtual,IsStatutory,IsPAPrimaryWorkSite,LedgerCode,RecordSource,IsExclusiveLoan,IsDefaultLoanPosition)" \
                                             " VALUES({3},{4},{5},1,'{6}',{0},{1},{2}," \
                                             "{7},0,0,'',1,0,0)" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, employee_id, dept_job_id,
                            onsite_orgunit_id, _start_date, is_virtual)
                _execSql(employeeworkassignment_sql, "EmployeeWorkAssignment", True)

                personaddress_sql = "INSERT INTO PersonAddress" \
                                    "(PersonId,CountryCode,Address1,City,StateCode,PostalCode,ContactInformationTypeId,EffectiveStart," \
                                    "LastModifiedUserId,LastModifiedTimestamp,ClientId,IsPayrollMailing)" \
                                    " VALUES({3},'{4}','{5}','{6}','{7}','{8}',{10},'{9}',{1},{2},{0},1)" \
                    .format(_client_id, _last_mod_userId, _last_mod_timestamp, employee_id, _country_code,
                            live_address['Address'], live_address['City'],
                            live_address['Province'], live_address['Postal Code'], _start_date, contactinfotype_id)
                _execSql(personaddress_sql, "PersonAddress", True)


            print("Total elapsed time [{0}] to generate {1} employees".format(str(time.time() - t0), num))

        engine.execute("SET IDENTITY_INSERT Appuser ON")

        # print("the employee will insert into the orgunitid :{0}, paygrouplist :{1}".format(
        #    _list_small_paygroup_onsite_orgunit_ids, _list_small_paygroup_ids))
        # onsite_orgunit_id_cycle = cycle(_list_small_paygroup_onsite_orgunit_ids) if len(
        #    _list_small_paygroup_onsite_orgunit_ids) > 0 else 0
        # paygroup_id_cycle = cycle(_list_small_paygroup_ids) if len(_list_small_paygroup_ids) > 0 else 0
        for y in range(len(_num_employees_list)):
            employee_id_to_start = _getCurrentIdValue(
                'AppUser') + 1  # int(engine.execute("select IDENT_CURRENT ('appuser') as id ").fetchone().id)+1

            # print("Appuser id starts at [" + str(start_number) + "] and ends at [" + str(end_number - 1) + "]")
            createEmployees(employee_id_to_start, _num_employees_list[y], _list_paygroup_onsite_orgunit_ids,
                            _list_paygroup_ids[y])

        engine.execute("SET IDENTITY_INSERT AppUser OFF")

    # def test_f_update_PRPayrollTax(self):
    #    sql ="INSERT INTO PRPayrollTax (PRTaxAuthorityInstanceId, ShortName, LongName, ClientId, LastModifiedTimestamp, LastModifiedUserId)" \
    #         "Select DISTINCT a.PRTaxAuthorityInstanceId, a.DisplayName, a.ShortName, {0}, CURRENT_TIMESTAMP, 0" \
    #         "From PRTaxAuthorityInstance a Where a.PRTaxAuthorityInstanceId LIKE '%USA%' AND " \
    #         "PRTaxAuthorityInstanceId NOT IN (Select PrTaxAuthorityInstanceId From PRPayrollTax)".format(_client_id)
    #    engine.execute(sql)
    #    print("PRPayrollTax USA updated")
    # def _g_assign_features(self):
    #    sql="""insert into FeatureRoleList (FeatureId,RoleId,EffectiveStart,ClientId,LastModifiedUserId,LastModifiedTimestamp,DelayedLoad,ViewType,AdminOnly)
    #            values (1550,1005,CURRENT_TIMESTAMP,{0},0,CURRENT_TIMESTAMP,0,3,0),(1551,1005,CURRENT_TIMESTAMP,{0},0,CURRENT_TIMESTAMP,0,3,0),(1558,1005,CURRENT_TIMESTAMP,{0},0,CURRENT_TIMESTAMP,0,3,0)
    #            ,(1588,1005,CURRENT_TIMESTAMP,{0},0,CURRENT_TIMESTAMP,0,3,0),(1589,1005,CURRENT_TIMESTAMP,{0},0,CURRENT_TIMESTAMP,0,3,0),(1590,1005,CURRENT_TIMESTAMP,{0},0,CURRENT_TIMESTAMP,0,3,0)
    #            ,(1706,1005,CURRENT_TIMESTAMP,{0},0,CURRENT_TIMESTAMP,0,3,0),(1707,1005,CURRENT_TIMESTAMP,{0},0,CURRENT_TIMESTAMP,0,3,0)""".format(_client_id)

    def execute(self):
        unittest.main()


if __name__ == '__main__':
    testPerformance = TestPerformance()
    testPerformance.execute()
