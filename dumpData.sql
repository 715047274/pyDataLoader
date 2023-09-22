SELECT * FROM LegalEntityMasterBankAccountSetting

--INSERT INTO LegalEntityMasterBankAccountSetting  VALUES(25,'CANLegalMasterBank20230912115537','long CANLegalMasterBank20230912115537','ref CANLegalMasterBank20230912115537','2021-01-01',NULL,1,NULL,NULL,10000,1001,CURRENT_TIMESTAMP,NULL)
INSERT INTO LegalEntityMasterBankAccountSetting
      (LegalEntityId, ShortName, LongName, XrefCode, EffectiveStart, EffectiveEnd, isDefault, FundingIdentifier,TaxServiceId,ServiceUserNumber,ClientId,LastModifiedUserId,LastModifiedTimestamp, IsFasterPayment)
 VALUES(25,'CANLegalMasterBank20230912115537','long CANLegalMasterBank20230912115537','ref CANLegalMasterBank20230912115537','2021-01-01',NULL,1,NULL,NULL,10000,1001,CURRENT_TIMESTAMP,NULL)



 -- INSERT INTO {tableName} {Expression} VALUES {Expression}
 /*
 const orgUnit = []
 -- todo:
 -- Create Table {
	testId: uniqueNumber,


 }



 const testData = {
	testName: 'testName',
	orgUnit:[
	  {siteOrg:{}, onSiteOrg:{}}
	],
	payGroup:[
	{paytype, payFeq, startDate,}
	],
	employee:[],

 }


 */
 Declare @right int
 exec CalibrateOrgLeftRight @OrgId=1113, @Left=1114, @NewRight=1;

 select * from OrgUnit





--setting up legal entity
SELECT geocityid as id FROM GeoCity WHERE ShortName ='Edmonton'
SELECT geocityid as id FROM GeoCity WHERE ShortName ='Edmonton'


INSERT INTO LegalEntity (ShortName,LongName,XRefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,CountryCode,Address,GeoCityId,StateCode,PostalCode,LegalIdNumber,LegalIdNumberType,Active,EffectiveStart,IsAutoCreated,IsValidationRequired,IsNotDisbursePrintToBackOffice,AddressCountryCode,ApplyStatusIndianCalculation) VALUES('CANLegal20230914161218', 'long CANLegal20230914161218', 'ref CANLegal20230914161218', 10000, 1001, CURRENT_TIMESTAMP, 'CAN', '1 Sir Winston Churchill Square', 33, 'AB', 'T5J 2R7','111111118', 1, 1, '2021-01-01', 0, 0, 0, 'CAN', 0)

INSERT INTO LegalEntityEmployeeInsurance (LegalEntityId,ReferenceCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,RateGroup,IsDefault,LegalEntityEmployeeInsurancePreferenceCodeId) VALUES('29','0001',10000,1001,CURRENT_TIMESTAMP,'0001',1,1)

INSERT INTO LegalEntityEmployeeInsuranceRate (LegalEntityEmployeeInsuranceId,Rate,EffectiveStart,ClientId,LastModifiedUserId,LastModifiedTimestamp)  VALUES (18,1.4,'2021-01-01',10000,1001,CURRENT_TIMESTAMP)

-- set up PRbanking
INSERT INTO PRBankAccount (ShortName,LongName,RoutingNumber,AccountNumber,CheckSigning,XRefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,UseForPrintingCheck,MICRIsBold) VALUES('CANPayrollBank20230914161218','long CANPayrollBank20230914161218',075900575,123456789,0,'ref CANPayrollBank20230914161218',10000,1001,CURRENT_TIMESTAMP,0,0)
INSERT INTO LegalEntityBankAccount (PRBankAccountTypeId,PRBankAccountId,ClientId,LastModifiedUserId,LastModifiedTimestamp,LegalEntityBankAccountDefId,CheckPrinting,CheckSigning,BankTransferDisbursementSourceId,CheckDisbursementSourceId,OverrideLegalEntityName,IsCTCRecipientIdRequired)  VALUES (1,17,10000,1001,CURRENT_TIMESTAMP,13,0,0,1,1,0,1)


INSERT INTO Department OUTPUT inserted.DepartmentId as id VALUES('CANDept20230914161218_1','long CANDept20230914161218_1',NULL,10000,1001,CURRENT_TIMESTAMP,'xref CANDept20230914161218_1',NULL)

-- OrgUnit

INSERT INTO OrgUnit (ShortName,LongName,OrgLevelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,IsStoreFlag,XRefCode,PhysicalLocation,IsOrgManaged,IsMobileOrg) VALUES('CANCorp20230914161218','long CANCorp20230914161218',0,10000,1001,CURRENT_TIMESTAMP,'n','ref CANCorp20230914161218',0,1,0)
INSERT INTO OrgUnitParent (OrgUnitId,ParentOrgUnitId,EffectiveStart,ClientId,LastModifiedUserId,LastModifiedTimestamp)  SELECT MAX(CTE1.OrgUnitId), MIN(CTE1.OrgUnitId),'2021-01-01',10000,1001,CURRENT_TIMESTAMP FROM OrgUnit CTE1 WHERE CTE1.orglevelid = 0



SELECT * FROM LegalEntityMasterBankAccountSetting

SELECT * FROM LegalEntity




INSERT INTO OrgUnit (ShortName,LongName,OrgLevelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,IsStoreFlag,XRefCode,PhysicalLocation, Address,StateCode,PostalCode,CountryCode,GeoCityId,IsOrgManaged,IsMobileOrg)  VALUES('CANSite20230914161218_1324','long CANSite20230914161218_1324',999,10000,1001,CURRENT_TIMESTAMP,'n','ref CANSite20230914161218_1324',1,'1 Sir Winston Churchill Square','AB','T5J 2R7','CAN',33,1,0 )
INSERT INTO OrgUnitLegalEntity (OrgUnitId, LegalEntityId, EffectiveStart, ClientId, LastModifiedUserId, LastModifiedTimestamp)  VALUES(1324, 29, '2021-01-01', 10000, 1001, CURRENT_TIMESTAMP)
INSERT INTO OrgUnit (ShortName,LongName,OrgLevelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,IsStoreFlag,XRefCode,PhysicalLocation,DepartmentId,IsMobileOrg)  VALUES('CANOnsite20230914161218_1325','long CANOnsite20230914161218_1325',997,10000,1001,CURRENT_TIMESTAMP,'n','ref CANOnsite20230914161218_1325',0, 19, 0)

INSERT INTO OrgUnitParent (OrgUnitId,ParentOrgUnitId,EffectiveStart,ClientId,LastModifiedUserId,LastModifiedTimestamp)  SELECT MAX(child.OrgUnitId), MAX(parent.OrgUnitId),'2021-01-01',10000,1001,CURRENT_TIMESTAMP FROM OrgUnit child, OrgUnit parent  WHERE child.OrgLevelId=997 AND parent.OrgLevelId=999
INSERT INTO OrgUnitParent (OrgUnitId,ParentOrgUnitId,EffectiveStart,ClientId,LastModifiedUserId,LastModifiedTimestamp)  SELECT MAX(child.OrgUnitId), MAX(parent.OrgUnitId),'2021-01-01',10000,1001,CURRENT_TIMESTAMP FROM OrgUnit child, OrgUnit parent  WHERE child.OrgLevelId=999 AND parent.OrgLevelId=0


/*
C:\Dayforce\DataLoader\venv\Scripts\python.exe "C:/Program Files/JetBrains/PyCharm 2023.2/plugins/python/helpers/pycharm/_jb_pytest_runner.py" --target CANDataLoader.py::TestPerformance
Testing started at 3:48 PM ...
Launching pytest with arguments CANDataLoader.py::TestPerformance --no-header --no-summary -q in C:\Dayforce\DataLoader

============================= test session starts =============================
collecting ... collected 5 items

CANDataLoader.py::TestPerformance::test_a_Init
CANDataLoader.py::TestPerformance::test_b_Orgunit
CANDataLoader.py::TestPerformance::test_c_Payroll
CANDataLoader.py::TestPerformance::test_e_Paygroup
CANDataLoader.py::TestPerformance::test_f_Employee

======================== 5 passed, 1 warning in 4.02s =========================
PASSED                    [ 20%]test start
INSERT INTO GeoCity SELECT 'Edmonton', NULL, 60, 10000, 1001, CURRENT_TIMESTAMP FROM GeoState gs  WHERE NOT EXISTS (SELECT 1 FROM GeoCity WHERE shortname = 'Edmonton' and geostateid=60): [id:33]
INSERT INTO GeoCity SELECT 'Edmonton', NULL, 60, 10000, 1001, CURRENT_TIMESTAMP FROM GeoState gs  WHERE NOT EXISTS (SELECT 1 FROM GeoCity WHERE shortname = 'Edmonton' and geostateid=60): [id:33]

-----setting up legal entity
SELECT geocityid as id FROM GeoCity WHERE ShortName ='Edmonton': [id:33]
INSERT INTO LegalEntity (ShortName,LongName,XRefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,CountryCode,Address,GeoCityId,StateCode,PostalCode,LegalIdNumber,LegalIdNumberType,Active,EffectiveStart,IsAutoCreated,IsValidationRequired,IsNotDisbursePrintToBackOffice,AddressCountryCode,ApplyStatusIndianCalculation) VALUES('CANLegal20230918154811', 'long CANLegal20230918154811', 'ref CANLegal20230918154811', 10000, 1001, CURRENT_TIMESTAMP, 'CAN', '1 Sir Winston Churchill Square', 33, 'AB', 'T5J 2R7','111111118', 1, 1, '2021-01-01', 0, 0, 0, 'CAN', 0): [id:11]
INSERT INTO LegalEntityEmployeeInsurance (LegalEntityId,ReferenceCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,RateGroup,IsDefault,LegalEntityEmployeeInsurancePreferenceCodeId) VALUES('11','0001',10000,1001,CURRENT_TIMESTAMP,'0001',1,1): [id:6]
INSERT INTO LegalEntityEmployeeInsuranceRate (LegalEntityEmployeeInsuranceId,Rate,EffectiveStart,ClientId,LastModifiedUserId,LastModifiedTimestamp)  VALUES (6,1.4,'2021-01-01',10000,1001,CURRENT_TIMESTAMP): [id:5]

----set up PRbanking
INSERT INTO PRBankAccount (ShortName,LongName,RoutingNumber,AccountNumber,CheckSigning,XRefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,UseForPrintingCheck,MICRIsBold) VALUES('CANPayrollBank20230918154811','long CANPayrollBank20230918154811',075900575,123456789,0,'ref CANPayrollBank20230918154811',10000,1001,CURRENT_TIMESTAMP,0,0): [id:8]
INSERT INTO LegalEntityBankAccount (PRBankAccountTypeId,PRBankAccountId,ClientId,LastModifiedUserId,LastModifiedTimestamp,LegalEntityBankAccountDefId,CheckPrinting,CheckSigning,BankTransferDisbursementSourceId,CheckDisbursementSourceId,OverrideLegalEntityName,IsCTCRecipientIdRequired)  VALUES (1,8,10000,1001,CURRENT_TIMESTAMP,8,0,0,1,1,0,1): [id:8]
INSERT INTO Department OUTPUT inserted.DepartmentId as id VALUES('CANDept20230918154811_1','long CANDept20230918154811_1',NULL,10000,1001,CURRENT_TIMESTAMP,'xref CANDept20230918154811_1',NULL): [id:10]

----setup OrgUnit
INSERT INTO OrgUnit (ShortName,LongName,OrgLevelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,IsStoreFlag,XRefCode,PhysicalLocation,IsOrgManaged,IsMobileOrg) VALUES('CANCorp20230918154811','long CANCorp20230918154811',0,10000,1001,CURRENT_TIMESTAMP,'n','ref CANCorp20230918154811',0,1,0): [id:1277]
INSERT INTO OrgUnitParent (OrgUnitId,ParentOrgUnitId,EffectiveStart,ClientId,LastModifiedUserId,LastModifiedTimestamp)  SELECT MAX(CTE1.OrgUnitId), MIN(CTE1.OrgUnitId),'2021-01-01',10000,1001,CURRENT_TIMESTAMP FROM OrgUnit CTE1 WHERE CTE1.orglevelid = 0: [id:278]

SELECT geocityid as id FROM GeoCity WHERE ShortName ='Edmonton': [id:33]
INSERT INTO OrgUnit  (ShortName,LongName,OrgLevelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,IsStoreFlag,XRefCode,PhysicalLocation, Address,StateCode,PostalCode,CountryCode,GeoCityId,IsOrgManaged,IsMobileOrg)  VALUES('CANSite20230918154811_1278','long CANSite20230918154811_1278',999,10000,1001,CURRENT_TIMESTAMP,'n','ref CANSite20230918154811_1278',1,'1 Sir Winston Churchill Square','AB','T5J 2R7','CAN',33,1,0 ): [id:1278]
INSERT INTO OrgUnitLegalEntity (OrgUnitId, LegalEntityId, EffectiveStart, ClientId, LastModifiedUserId, LastModifiedTimestamp)  VALUES(1278, 11, '2021-01-01', 10000, 1001, CURRENT_TIMESTAMP): [id:134]
INSERT INTO OrgUnit (ShortName,LongName,OrgLevelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,IsStoreFlag,XRefCode,PhysicalLocation,DepartmentId,IsMobileOrg)  VALUES('CANOnsite20230918154811_1279','long CANOnsite20230918154811_1279',997,10000,1001,CURRENT_TIMESTAMP,'n','ref CANOnsite20230918154811_1279',0, 10, 0): [id:1279]
INSERT INTO OrgUnitParent (OrgUnitId,ParentOrgUnitId,EffectiveStart,ClientId,LastModifiedUserId,LastModifiedTimestamp)  SELECT MAX(child.OrgUnitId), MAX(parent.OrgUnitId),'2021-01-01',10000,1001,CURRENT_TIMESTAMP FROM OrgUnit child, OrgUnit parent  WHERE child.OrgLevelId=997 AND parent.OrgLevelId=999: [id:279]
INSERT INTO OrgUnitParent (OrgUnitId,ParentOrgUnitId,EffectiveStart,ClientId,LastModifiedUserId,LastModifiedTimestamp)  SELECT MAX(child.OrgUnitId), MAX(parent.OrgUnitId),'2021-01-01',10000,1001,CURRENT_TIMESTAMP FROM OrgUnit child, OrgUnit parent  WHERE child.OrgLevelId=999 AND parent.OrgLevelId=0: [id:280]


---- Setup Job And DepJob
INSERT INTO Job  (ShortName,LongName,ClientId,LastModifiedUserId,LastModifiedTimestamp,XrefCode,IsUnionJob,EffectiveStart)  VALUES( 'CANJob20230918154811','long CANJob20230918154811',10000,1001,CURRENT_TIMESTAMP,'ref CANJob20230918154811',0, '2021-01-01' ): [id:1009]
INSERT INTO DeptJob (DepartmentId, JobId, ClientId, LastModifiedUserId, LastModifiedTimestamp, CreationOrgUnitId, EffectiveStart, IsNonService, ShortName, LongName, Officer, Executive, Status, IsWCBExempt, XRefCode, PPACAFullTime) SELECT MAX(dept.DepartmentId), MAX(job.JobId),10000,1001,CURRENT_TIMESTAMP,1277,'2021-01-01',0,'CANDeptJob20230918154811','long CANDeptJob20230918154811',0,0,'OPEN',0,'ref CANDeptJob20230918154811',0 FROM Department dept, Job job WHERE dept.ShortName LIKE 'CAN%' and job.ShortName LIKE 'CAN%': [id:11]
INSERT INTO DeptJobAssignment (DeptJobId,OrgUnitId,ClientId,LastModifiedUserId,LastModifiedTimestamp,EffectiveStart) VALUES(11,1277,10000,1001,CURRENT_TIMESTAMP,2021-01-01): [id:11]

-- Setup TimeOffPolicy
INSERT INTO TimeOffPolicy (ShortName,LongName,EnforceAllBlackoutDates,XRefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,AvailabilityEditingBlackoutWeeks,PreventRequestOnHolidays,AllDayOnly,EnforcePeriodWindow,SelectSchedule,IsElapsedTime,ShowElapsedTimeSelection,CalculateOnHolidays,AllowAdvancePay,PreventRequestOnTransmittedPeriods,PayAmountViewOnly,PreventRequestOnLockedPeriods,RestrictTotalWeeklyHoursToNormalWeeklyHours,PriorDaysToStartPayRecalc)  VALUES('CANTimeOffPolicy20230918154811','long CANTimeOffPolicy20230918154811',0,'ref CANTimeOffPolicy20230918154811',10000,1001,CURRENT_TIMESTAMP,2,0,0,0,0,0,0,0,0,0,0,0,0,0): [id:11]

---payPolicy
----creating payrollPolicy

INSERT INTO PRPayrollPolicy (ShortName,LongName,StartDate,XrefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp) VALUES('CANPayrollPolicy20230918154811','long CANPayrollPolicy20230918154811','2021-01-01','ref CANPayrollPolicy20230918154811',10000,1001,CURRENT_TIMESTAMP): [id:11]
INSERT INTO PRPayrollPolicyRuleSet   VALUES(11,'CANPayrollPolicyRuleSet20230918154811','long CANPayrollPolicyRuleSet20230918154811', 1, 10000, 1001, CURRENT_TIMESTAMP): [id:11]
INSERT INTO PRPayrollPolicyRule   VALUES (11,'CANAutoPayRule','long CANAutoPayRule',198,1,1,1001,CURRENT_TIMESTAMP,10000,'2021-01-01',NULL): [id:47]
INSERT INTO PRPayrollPolicyElementValue   VALUES(47,NULL,1986,'4',1001,CURRENT_TIMESTAMP,10000): [id:34]
INSERT INTO PRPayrollPolicyRule   VALUES (11,'CANEarningRule','long CANEarningRule',178,2,1,1001,CURRENT_TIMESTAMP,10000,'2021-01-01',NULL): [id:48]
INSERT INTO PRPayrollPolicyRule   VALUES (11,'CANDeductionRule','long CANDeductionRule',179,3,1,1001,CURRENT_TIMESTAMP,10000,'2021-01-01',NULL): [id:49]
INSERT INTO PRPayrollPolicyRule   VALUES (11,'CANTaxRule','long CANTaxRule',180,4,1,1001,CURRENT_TIMESTAMP,10000,'2021-01-01',NULL): [id:50]
test end
PASSED                [ 80%]test start
INSERT INTO PayGroupEarningRuleSet OUTPUT inserted.PayGroupEarningRuleSetId as id VALUES('CANPaygroupEarningRuleSet20230918154811','long CANPaygroupEarningRuleSet20230918154811',1,10000,1001,CURRENT_TIMESTAMP,11): [id:9]
INSERT INTO PayGroupEarningRule OUTPUT inserted.PayGroupEarningRuleId as id VALUES(9,'CANPaygroupEarningRule20230918154811','long CANPaygroupEarningRule20230918154811',191,1,1,1001,CURRENT_TIMESTAMP,10000,'2021-01-01',NULL,0): [id:9]

---WE
pay dates:[datetime.datetime(2023, 2, 5, 0, 0), datetime.datetime(2023, 3, 5, 0, 0), datetime.datetime(2023, 4, 5, 0, 0), datetime.datetime(2023, 5, 5, 0, 0), datetime.datetime(2023, 6, 5, 0, 0), datetime.datetime(2023, 7, 5, 0, 0), datetime.datetime(2023, 8, 5, 0, 0), datetime.datetime(2023, 9, 5, 0, 0), datetime.datetime(2023, 10, 5, 0, 0), datetime.datetime(2023, 11, 5, 0, 0), datetime.datetime(2023, 12, 5, 0, 0), datetime.datetime(2024, 1, 5, 0, 0)]
calendar starts:[datetime.datetime(2023, 1, 1, 0, 0), datetime.datetime(2023, 2, 1, 0, 0), datetime.datetime(2023, 3, 1, 0, 0), datetime.datetime(2023, 4, 1, 0, 0), datetime.datetime(2023, 5, 1, 0, 0), datetime.datetime(2023, 6, 1, 0, 0), datetime.datetime(2023, 7, 1, 0, 0), datetime.datetime(2023, 8, 1, 0, 0), datetime.datetime(2023, 9, 1, 0, 0), datetime.datetime(2023, 10, 1, 0, 0), datetime.datetime(2023, 11, 1, 0, 0), datetime.datetime(2023, 12, 1, 0, 0)]
calendar ends:[datetime.datetime(2023, 2, 1, 0, 0), datetime.datetime(2023, 3, 1, 0, 0), datetime.datetime(2023, 4, 1, 0, 0), datetime.datetime(2023, 5, 1, 0, 0), datetime.datetime(2023, 6, 1, 0, 0), datetime.datetime(2023, 7, 1, 0, 0), datetime.datetime(2023, 8, 1, 0, 0), datetime.datetime(2023, 9, 1, 0, 0), datetime.datetime(2023, 10, 1, 0, 0), datetime.datetime(2023, 11, 1, 0, 0), datetime.datetime(2023, 12, 1, 0, 0), datetime.datetime(2024, 1, 1, 0, 0)]
effective starts:[datetime.datetime(2023, 1, 1, 8, 0), datetime.datetime(2023, 2, 1, 8, 0), datetime.datetime(2023, 3, 1, 8, 0), datetime.datetime(2023, 4, 1, 8, 0), datetime.datetime(2023, 5, 1, 8, 0), datetime.datetime(2023, 6, 1, 8, 0), datetime.datetime(2023, 7, 1, 8, 0), datetime.datetime(2023, 8, 1, 8, 0), datetime.datetime(2023, 9, 1, 8, 0), datetime.datetime(2023, 10, 1, 8, 0), datetime.datetime(2023, 11, 1, 8, 0), datetime.datetime(2023, 12, 1, 8, 0)]
effective ends:[datetime.datetime(2023, 2, 1, 8, 0), datetime.datetime(2023, 3, 1, 8, 0), datetime.datetime(2023, 4, 1, 8, 0), datetime.datetime(2023, 5, 1, 8, 0), datetime.datetime(2023, 6, 1, 8, 0), datetime.datetime(2023, 7, 1, 8, 0), datetime.datetime(2023, 8, 1, 8, 0), datetime.datetime(2023, 9, 1, 8, 0), datetime.datetime(2023, 10, 1, 8, 0), datetime.datetime(2023, 11, 1, 8, 0), datetime.datetime(2023, 12, 1, 8, 0), datetime.datetime(2024, 1, 1, 8, 0)]
transmitby dates:[datetime.datetime(2023, 1, 31, 0, 0), datetime.datetime(2023, 2, 28, 0, 0), datetime.datetime(2023, 3, 31, 0, 0), datetime.datetime(2023, 4, 30, 0, 0), datetime.datetime(2023, 5, 31, 0, 0), datetime.datetime(2023, 6, 30, 0, 0), datetime.datetime(2023, 7, 31, 0, 0), datetime.datetime(2023, 8, 31, 0, 0), datetime.datetime(2023, 9, 30, 0, 0), datetime.datetime(2023, 10, 31, 0, 0), datetime.datetime(2023, 11, 30, 0, 0), datetime.datetime(2023, 12, 31, 0, 0)]
payimpound dates:[datetime.datetime(2023, 2, 3, 0, 0), datetime.datetime(2023, 3, 3, 0, 0), datetime.datetime(2023, 4, 3, 0, 0), datetime.datetime(2023, 5, 3, 0, 0), datetime.datetime(2023, 6, 3, 0, 0), datetime.datetime(2023, 7, 3, 0, 0), datetime.datetime(2023, 8, 3, 0, 0), datetime.datetime(2023, 9, 3, 0, 0), datetime.datetime(2023, 10, 3, 0, 0), datetime.datetime(2023, 11, 3, 0, 0), datetime.datetime(2023, 12, 3, 0, 0), datetime.datetime(2024, 1, 3, 0, 0)]
payrun dates:[datetime.datetime(2023, 2, 3, 0, 0), datetime.datetime(2023, 3, 3, 0, 0), datetime.datetime(2023, 4, 3, 0, 0), datetime.datetime(2023, 5, 3, 0, 0), datetime.datetime(2023, 6, 3, 0, 0), datetime.datetime(2023, 7, 3, 0, 0), datetime.datetime(2023, 8, 3, 0, 0), datetime.datetime(2023, 9, 3, 0, 0), datetime.datetime(2023, 10, 3, 0, 0), datetime.datetime(2023, 11, 3, 0, 0), datetime.datetime(2023, 12, 3, 0, 0), datetime.datetime(2024, 1, 3, 0, 0)]
shifted pay dates:[1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
shifted payrun dates:[0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0]
shifted payimpound dates:[0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0]
INSERT INTO PayGroupCalendar(PayGroupId,EffectiveStart,EffectiveEnd,Locked,TransmitByDate,Transmitted,ClientId,LastModifiedUserId,LastModifiedTimestamp,ApproveByDate,PayPeriod,PayPeriodSuffix,CalendarStart,CalendarEnd,ExportSequence,PayImpoundDate,PayRunDate,PayDate,IsPayDateAutoshifted,IsPayRunDateAutoshifted,IsPayImpoundDateAutoshifted,CommitByTimeOfDay,FuturePunchesEnabled,Closed) VALUES (11,'2023-01-01 08:00:00','2023-02-01 08:00:00',0,'2023-01-31 00:00:00',0,10000,1001,CURRENT_TIMESTAMP,'2023-01-31 00:00:00','01','00','2023-01-01 00:00:00','2023-02-01 00:00:00',-1,'2023-02-03 00:00:00','2023-02-03 00:00:00','2023-02-03 00:00:00',1,0,0,'2023-02-03 00:00:00',0,0) : [paygroupcalendar:702][paygroup:11]
INSERT INTO PayGroupCalendar(PayGroupId,EffectiveStart,EffectiveEnd,Locked,TransmitByDate,Transmitted,ClientId,LastModifiedUserId,LastModifiedTimestamp,ApproveByDate,PayPeriod,PayPeriodSuffix,CalendarStart,CalendarEnd,ExportSequence,PayImpoundDate,PayRunDate,PayDate,IsPayDateAutoshifted,IsPayRunDateAutoshifted,IsPayImpoundDateAutoshifted,CommitByTimeOfDay,FuturePunchesEnabled,Closed) VALUES (11,'2023-02-01 08:00:00','2023-03-01 08:00:00',0,'2023-02-28 00:00:00',0,10000,1001,CURRENT_TIMESTAMP,'2023-02-28 00:00:00','02','00','2023-02-01 00:00:00','2023-03-01 00:00:00',-1,'2023-03-03 00:00:00','2023-03-03 00:00:00','2023-03-03 00:00:00',1,0,0,'2023-03-03 00:00:00',0,0) : [paygroupcalendar:703][paygroup:11]
INSERT INTO PayGroupCalendar(PayGroupId,EffectiveStart,EffectiveEnd,Locked,TransmitByDate,Transmitted,ClientId,LastModifiedUserId,LastModifiedTimestamp,ApproveByDate,PayPeriod,PayPeriodSuffix,CalendarStart,CalendarEnd,ExportSequence,PayImpoundDate,PayRunDate,PayDate,IsPayDateAutoshifted,IsPayRunDateAutoshifted,IsPayImpoundDateAutoshifted,CommitByTimeOfDay,FuturePunchesEnabled,Closed) VALUES (11,'2023-03-01 08:00:00','2023-04-01 08:00:00',0,'2023-03-31 00:00:00',0,10000,1001,CURRENT_TIMESTAMP,'2023-03-31 00:00:00','03','00','2023-03-01 00:00:00','2023-04-01 00:00:00',-1,'2023-04-03 00:00:00','2023-04-03 00:00:00','2023-04-05 00:00:00',0,0,0,'2023-04-03 00:00:00',0,0) : [paygroupcalendar:704][paygroup:11]
INSERT INTO PayGroupCalendar(PayGroupId,EffectiveStart,EffectiveEnd,Locked,TransmitByDate,Transmitted,ClientId,LastModifiedUserId,LastModifiedTimestamp,ApproveByDate,PayPeriod,PayPeriodSuffix,CalendarStart,CalendarEnd,ExportSequence,PayImpoundDate,PayRunDate,PayDate,IsPayDateAutoshifted,IsPayRunDateAutoshifted,IsPayImpoundDateAutoshifted,CommitByTimeOfDay,FuturePunchesEnabled,Closed) VALUES (11,'2023-04-01 08:00:00','2023-05-01 08:00:00',0,'2023-04-30 00:00:00',0,10000,1001,CURRENT_TIMESTAMP,'2023-04-30 00:00:00','04','00','2023-04-01 00:00:00','2023-05-01 00:00:00',-1,'2023-05-03 00:00:00','2023-05-03 00:00:00','2023-05-05 00:00:00',0,0,0,'2023-05-03 00:00:00',0,0) : [paygroupcalendar:705][paygroup:11]
INSERT INTO PayGroupCalendar(PayGroupId,EffectiveStart,EffectiveEnd,Locked,TransmitByDate,Transmitted,ClientId,LastModifiedUserId,LastModifiedTimestamp,ApproveByDate,PayPeriod,PayPeriodSuffix,CalendarStart,CalendarEnd,ExportSequence,PayImpoundDate,PayRunDate,PayDate,IsPayDateAutoshifted,IsPayRunDateAutoshifted,IsPayImpoundDateAutoshifted,CommitByTimeOfDay,FuturePunchesEnabled,Closed) VALUES (11,'2023-05-01 08:00:00','2023-06-01 08:00:00',0,'2023-05-31 00:00:00',0,10000,1001,CURRENT_TIMESTAMP,'2023-05-31 00:00:00','05','00','2023-05-01 00:00:00','2023-06-01 00:00:00',-1,'2023-06-02 00:00:00','2023-06-02 00:00:00','2023-06-05 00:00:00',0,1,1,'2023-06-02 00:00:00',0,0) : [paygroupcalendar:706][paygroup:11]
INSERT INTO PayGroupCalendar(PayGroupId,EffectiveStart,EffectiveEnd,Locked,TransmitByDate,Transmitted,ClientId,LastModifiedUserId,LastModifiedTimestamp,ApproveByDate,PayPeriod,PayPeriodSuffix,CalendarStart,CalendarEnd,ExportSequence,PayImpoundDate,PayRunDate,PayDate,IsPayDateAutoshifted,IsPayRunDateAutoshifted,IsPayImpoundDateAutoshifted,CommitByTimeOfDay,FuturePunchesEnabled,Closed) VALUES (11,'2023-06-01 08:00:00','2023-07-01 08:00:00',0,'2023-06-30 00:00:00',0,10000,1001,CURRENT_TIMESTAMP,'2023-06-30 00:00:00','06','00','2023-06-01 00:00:00','2023-07-01 00:00:00',-1,'2023-06-30 00:00:00','2023-06-30 00:00:00','2023-07-05 00:00:00',0,1,1,'2023-06-30 00:00:00',0,0) : [paygroupcalendar:707][paygroup:11]
INSERT INTO PayGroupCalendar(PayGroupId,EffectiveStart,EffectiveEnd,Locked,TransmitByDate,Transmitted,ClientId,LastModifiedUserId,LastModifiedTimestamp,ApproveByDate,PayPeriod,PayPeriodSuffix,CalendarStart,CalendarEnd,ExportSequence,PayImpoundDate,PayRunDate,PayDate,IsPayDateAutoshifted,IsPayRunDateAutoshifted,IsPayImpoundDateAutoshifted,CommitByTimeOfDay,FuturePunchesEnabled,Closed) VALUES (11,'2023-07-01 08:00:00','2023-08-01 08:00:00',0,'2023-07-31 00:00:00',0,10000,1001,CURRENT_TIMESTAMP,'2023-07-31 00:00:00','07','00','2023-07-01 00:00:00','2023-08-01 00:00:00',-1,'2023-08-03 00:00:00','2023-08-03 00:00:00','2023-08-04 00:00:00',1,0,0,'2023-08-03 00:00:00',0,0) : [paygroupcalendar:708][paygroup:11]
INSERT INTO PayGroupCalendar(PayGroupId,EffectiveStart,EffectiveEnd,Locked,TransmitByDate,Transmitted,ClientId,LastModifiedUserId,LastModifiedTimestamp,ApproveByDate,PayPeriod,PayPeriodSuffix,CalendarStart,CalendarEnd,ExportSequence,PayImpoundDate,PayRunDate,PayDate,IsPayDateAutoshifted,IsPayRunDateAutoshifted,IsPayImpoundDateAutoshifted,CommitByTimeOfDay,FuturePunchesEnabled,Closed) VALUES (11,'2023-08-01 08:00:00','2023-09-01 08:00:00',0,'2023-08-31 00:00:00',0,10000,1001,CURRENT_TIMESTAMP,'2023-08-31 00:00:00','08','00','2023-08-01 00:00:00','2023-09-01 00:00:00',-1,'2023-09-01 00:00:00','2023-09-01 00:00:00','2023-09-05 00:00:00',0,1,1,'2023-09-01 00:00:00',0,0) : [paygroupcalendar:709][paygroup:11]
INSERT INTO PayGroupCalendar(PayGroupId,EffectiveStart,EffectiveEnd,Locked,TransmitByDate,Transmitted,ClientId,LastModifiedUserId,LastModifiedTimestamp,ApproveByDate,PayPeriod,PayPeriodSuffix,CalendarStart,CalendarEnd,ExportSequence,PayImpoundDate,PayRunDate,PayDate,IsPayDateAutoshifted,IsPayRunDateAutoshifted,IsPayImpoundDateAutoshifted,CommitByTimeOfDay,FuturePunchesEnabled,Closed) VALUES (11,'2023-09-01 08:00:00','2023-10-01 08:00:00',0,'2023-09-30 00:00:00',0,10000,1001,CURRENT_TIMESTAMP,'2023-09-30 00:00:00','09','00','2023-09-01 00:00:00','2023-10-01 00:00:00',-1,'2023-10-03 00:00:00','2023-10-03 00:00:00','2023-10-05 00:00:00',0,0,0,'2023-10-03 00:00:00',0,0) : [paygroupcalendar:710][paygroup:11]
INSERT INTO PayGroupCalendar(PayGroupId,EffectiveStart,EffectiveEnd,Locked,TransmitByDate,Transmitted,ClientId,LastModifiedUserId,LastModifiedTimestamp,ApproveByDate,PayPeriod,PayPeriodSuffix,CalendarStart,CalendarEnd,ExportSequence,PayImpoundDate,PayRunDate,PayDate,IsPayDateAutoshifted,IsPayRunDateAutoshifted,IsPayImpoundDateAutoshifted,CommitByTimeOfDay,FuturePunchesEnabled,Closed) VALUES (11,'2023-10-01 08:00:00','2023-11-01 08:00:00',0,'2023-10-31 00:00:00',0,10000,1001,CURRENT_TIMESTAMP,'2023-10-31 00:00:00','10','00','2023-10-01 00:00:00','2023-11-01 00:00:00',-1,'2023-11-03 00:00:00','2023-11-03 00:00:00','2023-11-03 00:00:00',1,0,0,'2023-11-03 00:00:00',0,0) : [paygroupcalendar:711][paygroup:11]
INSERT INTO PayGroupCalendar(PayGroupId,EffectiveStart,EffectiveEnd,Locked,TransmitByDate,Transmitted,ClientId,LastModifiedUserId,LastModifiedTimestamp,ApproveByDate,PayPeriod,PayPeriodSuffix,CalendarStart,CalendarEnd,ExportSequence,PayImpoundDate,PayRunDate,PayDate,IsPayDateAutoshifted,IsPayRunDateAutoshifted,IsPayImpoundDateAutoshifted,CommitByTimeOfDay,FuturePunchesEnabled,Closed) VALUES (11,'2023-11-01 08:00:00','2023-12-01 08:00:00',0,'2023-11-30 00:00:00',0,10000,1001,CURRENT_TIMESTAMP,'2023-11-30 00:00:00','11','00','2023-11-01 00:00:00','2023-12-01 00:00:00',-1,'2023-12-01 00:00:00','2023-12-01 00:00:00','2023-12-05 00:00:00',0,1,1,'2023-12-01 00:00:00',0,0) : [paygroupcalendar:712][paygroup:11]
INSERT INTO PayGroupCalendar(PayGroupId,EffectiveStart,EffectiveEnd,Locked,TransmitByDate,Transmitted,ClientId,LastModifiedUserId,LastModifiedTimestamp,ApproveByDate,PayPeriod,PayPeriodSuffix,CalendarStart,CalendarEnd,ExportSequence,PayImpoundDate,PayRunDate,PayDate,IsPayDateAutoshifted,IsPayRunDateAutoshifted,IsPayImpoundDateAutoshifted,CommitByTimeOfDay,FuturePunchesEnabled,Closed) VALUES (11,'2023-12-01 08:00:00','2024-01-01 08:00:00',0,'2023-12-31 00:00:00',0,10000,1001,CURRENT_TIMESTAMP,'2023-12-31 00:00:00','12','00','2023-12-01 00:00:00','2024-01-01 00:00:00',-1,'2024-01-03 00:00:00','2024-01-03 00:00:00','2024-01-05 00:00:00',0,0,0,'2024-01-03 00:00:00',0,0) : [paygroupcalendar:713][paygroup:11]
INSERT INTO PayGroupCalendarOrg (PayGroupCalendarId,OrgUnitId,Approved,ApprovedUserId,ApprovedDate,PayApproved,PayApprovedUserId,PayApprovedDate,Locked,LastModifiedUserId,LastModifiedTimestamp,ClientId) SELECT g.PayGroupCalendarId, a.ChildOrgUnitId as OrgUnitId, 1,1001,CURRENT_TIMESTAMP,1,1001,CURRENT_TIMESTAMP,0,1001,CURRENT_TIMESTAMP,10000 from PayGroupCalendar g, (SELECT DISTINCT ChildOrgUnitId from [dbo].[HierarchyOrgView] WHERE ParentOrgUnitId = 1277 and ChildOrgLevelId = 999) a WHERE g.PaygroupId=11: [paygroupcalendarorg:4109][paygroup:11]
INSERT INTO PayGroupCalculationCalendar SELECT p.PayGroupCalendarId, p.EffectiveStart, p.EffectiveEnd, 10000,1001,CURRENT_TIMESTAMP,p.CalendarStart,p.CalendarEnd FROM PayGroupCalendar p WHERE p.PayGroupId=11: [paygroupcalculationcalendar:1478][paygroup:11]




test end
PASSED                [100%]test start
Employee id starts at [1039] and ends at [1039]
the employee will insert into the orgunitid:[1279, 1281, 1283, 1285, 1287, 1289, 1291, 1293, 1295, 1297, 1299, 1301, 1303, 1305, 1307, 1309, 1311, 1313, 1315, 1317, 1319, 1321, 1323, 1325, 1327, 1329, 1331, 1333, 1335, 1337, 1339, 1341, 1343, 1345, 1347, 1349, 1351, 1353, 1355, 1357, 1359, 1361, 1363, 1365, 1367, 1369, 1371, 1373, 1375, 1377, 1379, 1381, 1383, 1385, 1387, 1389, 1391, 1393, 1395, 1397, 1399, 1401, 1403, 1405, 1407, 1409, 1411, 1413, 1415, 1417, 1419, 1421, 1423, 1425, 1427, 1429, 1431, 1433, 1435, 1437, 1439, 1441, 1443, 1445, 1447, 1449, 1451, 1453, 1455, 1457, 1459, 1461, 1463, 1465, 1467, 1469, 1471, 1473, 1475, 1477], paygroupid:11
Total elapsed time [0.927239179611206] to generate 1 employees
test end

Process finished with exit code 0



*/




/*
--- Create LegalEntity In Country
	* Create prBankAccount ---> USA: if(isCustomerBank) CreateDefaultCustomerBankAccount ; else CreateDefaulBankAccount --> LegalEntityMasterBankSetting
	                       ---> CAN: CreateDefaultLegalEntityCAN --> CreateDefaultEIRateGroupForLegalEntity
											|---> Address: 4110 Yonge Street, M2P 2B7, ON, 111111118,Toronto ,
	* Create LegalEntity

*/

select * from LegalEntityMasterBankAccountSetting


SELECT * FROM PREarning