class DataCommand:

    # PREarning table column
    PREarningColumn = "" \
                      "(ShortName,LongName,XrefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,SortOrder,IsInternal,IsGenerated,PREarningCodeId," \
                      "AllowPayee,PRPayRunDefId,IsHoursRateInPayEntryEnabled,IsPremium,IsPayDateEffective," \
                      "IsAutoCreated,IsValidationRequired,OutputZeroDollarEarning,IsGrossedUp,OverrideGrossedUpPercent," \
                      "PayoutBalanceInGrant,SuppressOnEarningStatement,IsHoursWorkedEnabled,IsOverTimeEarningsEnabled,IsOverTimeHoursEnabled," \
                      "PREarnDeductSourceTypeId,IsFLSAAdjustable,AllowMuliJSalaryAllocationSplit,GenerateOnlyOnCurrentPayGroup,PPACAHours," \
                      "IsEIRefund,PayoutToLastPeriodWithInsurableHours,PayOutBalanceOnTermination,IsAllowAutoPayReductionWithNoRate,DisplayOnCompensationStatement," \
                      "ExcludeScheduledAmountForLeapPeriod,AllowPieceQuantityWithoutPay,DisplayPieceQuantityInsteadOfHours,AdjustDocketRateDuringPayrollCalc,ProratePreTaxDed," \
                      "ExcludeFromDisposableNet,EnableProration,IsHoursRateInPayEntryErrorOverride,IsDecliningBalance,AllowArrears," \
                      "AllowPartial,ReclaimBalanceOnTermination,AllowPartialOnBalanceReclaim,DisplayBalanceOnEarningStatement,IsGenderPayGap)"

    OrgUnitColumn = " (ShortName,LongName,OrgLevelId,ClientId,LastModifiedUserId,LastModifiedTimestamp,IsStoreFlag,XRefCode,PhysicalLocation," \
                              " Address,StateCode,PostalCode,CountryCode,GeoCityId,IsOrgManaged,IsMobileOrg)"

    def __int__(self):
        self.dataId
