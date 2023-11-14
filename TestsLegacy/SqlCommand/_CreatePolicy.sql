CREATE PROCEDURE CreateLegalEntityWithCountryCode
    -- required paramters
	@testName NVARCHAR(100),
	@uuid NVARCHAR(100),
    @countryCode NVARCHAR(100),
   	@legalEntityId INT OUTPUT,
    @clientId INT = NULL,
    @cadminId INT = NULL
AS
BEGIN
	 -- If @clientId is not provided, use the default value of NULL
	IF @clientId IS NULL
		SET @clientId = 10000;
	-- If @cadminId is not provided, use the default value of NULL
	IF @cadminId IS NULL
		SET @cadminId = 1001;



END;




INSERT INTO TimeOffPolicy (ShortName,LongName,EnforceAllBlackoutDates,XRefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,AvailabilityEditingBlackoutWeeks,PreventRequestOnHolidays,AllDayOnly,EnforcePeriodWindow,SelectSchedule,IsElapsedTime,ShowElapsedTimeSelection,CalculateOnHolidays,AllowAdvancePay,PreventRequestOnTransmittedPeriods,PayAmountViewOnly,PreventRequestOnLockedPeriods,RestrictTotalWeeklyHoursToNormalWeeklyHours,PriorDaysToStartPayRecalc)
VALUES('CANTimeOffPolicy20231110131929','long CANTimeOffPolicy20231110131929',0,'ref CANTimeOffPolicy20231110131929',@clientId,@cadminId,CURRENT_TIMESTAMP,2,0,0,0,0,0,0,0,0,0,0,0,0,0)
INSERT INTO EmployeeSchedulePolicy VALUES('CANEmployeeSchedulePolicy20231110131929','long CANEmployeeSchedulePolicy20231110131929','2021-01-01',NULL, @clientId, @cadminId, CURRENT_TIMESTAMP, 'ref CANEmployeeSchedulePolicy20231110131929', NULL)
INSERT INTO EntitlementPolicy VALUES('CANEntitlementPolicy20231110131929','long CANEntitlementPolicy20231110131929','2021-01-01', NULL,@clientId,@cadminId,CURRENT_TIMESTAMP,'ref CANEntitlementPolicy20231110131929')

INSERT INTO PRPayrollPolicy (ShortName,LongName,StartDate,XrefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp) VALUES('CANPayrollPolicy20231110131929','long CANPayrollPolicy20231110131929','2021-01-01','ref CANPayrollPolicy20231110131929',@clientId,@cadminId,CURRENT_TIMESTAMP)
INSERT INTO PRPayrollPolicyRuleSet   VALUES(17,'CANPayrollPolicyRuleSet20231110131929','long CANPayrollPolicyRuleSet20231110131929', 1, @clientId, @cadminId, CURRENT_TIMESTAMP)
INSERT INTO PRPayrollPolicyRule   VALUES (24,'CANAutoPayRule','long CANAutoPayRule',198,1,1,@cadminId,CURRENT_TIMESTAMP,@clientId,'2021-01-01',NULL)
INSERT INTO PRPayrollPolicyElementValue   VALUES(100,NULL,1986,'4',@cadminId,CURRENT_TIMESTAMP,@clientId)
INSERT INTO PRPayrollPolicyRule   VALUES (24,'CANEarningRule','long CANEarningRule',178,2,1,@cadminId,CURRENT_TIMESTAMP,@clientId,'2021-01-01',NULL)
INSERT INTO PRPayrollPolicyRule   VALUES (24,'CANDeductionRule','long CANDeductionRule',179,3,1,@cadminId,CURRENT_TIMESTAMP,@clientId,'2021-01-01',NULL)
INSERT INTO PRPayrollPolicyRule   VALUES (24,'CANTaxRule','long CANTaxRule',180,4,1,@cadminId,CURRENT_TIMESTAMP,@clientId,'2021-01-01',NULL)
INSERT INTO PRPayrollPolicyRuleSet   VALUES(17,'CANPayrollPolicyRuleSet20231110131929','long CANPayrollPolicyRuleSet20231110131929', 1, @clientId, @cadminId, CURRENT_TIMESTAMP)
INSERT INTO PRPayrollPolicyRule   VALUES (25,'CANAutoPayRule','long CANAutoPayRule',198,1,1,@cadminId,CURRENT_TIMESTAMP,@clientId,'2021-01-01',NULL)
INSERT INTO PRPayrollPolicyElementValue   VALUES(104,NULL,1986,'4',@cadminId,CURRENT_TIMESTAMP,@clientId)
INSERT INTO PRPayrollPolicyRule   VALUES (25,'CANEarningRule','long CANEarningRule',178,2,1,@cadminId,CURRENT_TIMESTAMP,@clientId,'2021-01-01',NULL)
INSERT INTO PRPayrollPolicyRule   VALUES (25,'CANDeductionRule','long CANDeductionRule',179,3,1,@cadminId,CURRENT_TIMESTAMP,@clientId,'2021-01-01',NULL)
INSERT INTO PRPayrollPolicyRule   VALUES (25,'CANTaxRule','long CANTaxRule',180,4,1,@cadminId,CURRENT_TIMESTAMP,@clientId,'2021-01-01',NULL)

INSERT INTO PayGroupEarningRuleSet OUTPUT inserted.PayGroupEarningRuleSetId as id VALUES('CANPaygroupEarningRuleSet20231110131929','long CANPaygroupEarningRuleSet20231110131929',1,@clientId,@cadminId,CURRENT_TIMESTAMP,@payGroupId)
INSERT INTO PayGroupEarningRule OUTPUT inserted.PayGroupEarningRuleId as id VALUES(17,'CANPaygroupEarningRule20231110131929','long CANPaygroupEarningRule20231110131929',191,1,1,@cadminId,CURRENT_TIMESTAMP,@clientId,'2021-01-01',NULL,0)


INSERT INTO PayHolidayGroup VALUES('CANPayHolidayGroup20231110131929','long CANPayHolidayGroup20231110131929',@clientId,@cadminId,CURRENT_TIMESTAMP,'ref CANPayHolidayGroup20231110131929',@orgUnitId,NULL)
INSERT INTO PunchPolicy (ShortName,LongName,GraceInEarly,MealGrace,BreakGrace,GraceAdjustInEarly,MealsEnabled,BreaksEnabled,MealsPaid,BreaksPaid,MainRoundNumerator,MainRoundDenominator,MealRoundNumerator,MealRoundDenominator,MealLengthRounding,BreakRoundNumerator,BreakRoundDenominator,BreakLengthRounding,ClientId,LastModifiedUserId,LastModifiedTimestamp,TimeBetweenMB,CreationOrgUnitId,XRefCode,ValidateMain,ExceptionInEarly,ValidateMeal,MealException,ValidateBreak,BreakException,RoundMain,RoundMeal,RoundBreak,GraceInLate,GraceOutEarly,GraceOutLate,ExceptionInLate,ExceptionOutEarly,ExceptionOutLate,AutoInjectBreaks,AutoInjectMeals,UseInAndOutAsMB,UseInAndOutAsMBThreshold,UseInAndOutAsMBType,PunchClock,TimesheetEntry,AutoPay,TimesheetEnterJob,TimesheetEnterProject,TimesheetEnterDocket,ValidateMealLength,ValidateBreakLength,AutoExtendBreaks,AutoExtendMeals,ExtendBreaksBySplit,ExtendMealsBySplit,GraceAdjustInLate,ValidateAgainstUnpostedSchedules,AutoInjectMBUsingSchedule,DisplayUnpostedSchedules,ValidateClockOrgUnit,GenerateEarlyLatePayCodes,ConsecutivePunchThreshold,MealPenaltyEnabled,MealPenalty1Minutes,MealPenalty1MinutesToWaive,MealPenalty1EmployeeWaivesByDefault,MealPenalty1SupervisorWaivesByDefault,MealPenalty2Minutes,MealPenalty2MinutesToWaive,MealPenalty2EmployeeWaivesByDefault,MealPenalty2SupervisorWaivesByDefault,ValidateClockDeviceGroup,ValidateEmployeePin,ValidateSupervisorPin,RoundSeconds,SupervisorInEarly,SupervisorInLate,AutoOutBySchedule,BusinessDayBySchedule,UnauthorizeOnEdit,GraceAdjustOutEarly,GraceAdjustOutLate,AutoInjectPunchesBySchedule,PeriodApproval,TimeClockLocationTransfer,TimeClockPositionTransfer,TimeClockProjectTransfer,TimeClockDocketTransfer,TimeClockDocketTransferWithQty,MainRoundNumeratorOut,MainRoundDenominatorOut,TimeClockSeparateDocketQty,GenerateDurationBasedPayCodes,TimeClockCombinedTransfer,MinimumUnscheduledShiftMealLength,MinimumUnscheduledShiftBreakLength,OutWithMealPrompt,OutWithBreakPrompt,EnterOrg,MealDurationRounding,NetworkLocationValidation,TipEntryPrompt,OutWithTipEntryPrompt,EmployeeTimesheetApprovalEdit,RelayControlScheduleValidationType,ProcessBiometricFailure,TransfersUsePriorRateIfJobRateUnset,ProcessPictureFailure,MealSubsidyPayAdjCodeId,MealSubsidyAmount,MealSubsidyMaxPerDay,MealSubsidyEnabled,AllowUnscheduledPunch,DurationTSUseStartEndTimes,AllowPunchingAtUnassignedLocations,MealPenaltyUseNetTime,MealPenaltyRequiredMinutes,MinimumScheduledShiftMealLength,MinimumScheduledShiftBreakLength,GenerateSeparateDurationBasedPayCodes,RecordPunchGeoLocation)
VALUES('CANPunchPolicy20231110131929','long CANPunchPolicy20231110131929',0,0,0,'n','n','n','n','n',0,0,0,0,'n',0,0,'n',@clientId,@cadminId,CURRENT_TIMESTAMP,0,@orgUnitId,'xref CANPunchPolicy20231110131929',1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,120,'m',1,0,0,0,0,0,0,0,0,0,0,0,'n',1,0,0,0,0,0,0,300,360,0,0,540,600,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,-1,0,1,0,0,0,0,30,0,0,0,0,0)
INSERT INTO PayPolicy VALUES(@orgUnitId,'CANPayPolicy20231110131929','long CANPayPolicy20231110131929','ref CANPayPolicy20231110131929',@clientId,@cadminId,CURRENT_TIMESTAMP,0,0,0,0,0,1,0,0,NULL,NULL,0)
INSERT INTO PunchPolicyAssignment SELECT MAX(newPunch.PunchPolicyId), MIN(ou.OrgUnitId),@clientId,@cadminId,CURRENT_TIMESTAMP FROM PunchPolicy newPunch, OrgUnit ou WHERE newPunch.ShortName like 'CAN%' and ou.OrgLevelId=0

INSERT INTO PayHolidayGroupAssignment SELECT MAX(newPunch.PayHolidayGroupId), MIN(ou.OrgUnitId),@clientId,@cadminId,CURRENT_TIMESTAMP FROM PayHolidayGroup newPunch, OrgUnit ou WHERE newPunch.ShortName like 'CAN%' and ou.OrgLevelId=0
