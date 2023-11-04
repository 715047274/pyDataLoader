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
    	DECLARE
		  @address NVARCHAR(255) = null ,
		  @postCode NVARCHAR(255) = null ,
		  @legalNumber NVARCHAR(255) = null ,
		  @startDate NVARCHAR(255) = null;

		DECLARE
		  @cityName NVARCHAR(100) = null,
		  @stateCode NVARCHAR(100)= null ,
		  @legalEntityName NVARCHAR(255)= null,
		  @cId INT,
	      @sId INT;
	  DECLARE
	      @client INT = @clientId,
		  @cadmin INT = @cadminId
    IF @countryCode = 'USA'
		BEGIN

          SET @legalEntityName = @testName + ' LegalEntity ' + @uuid;
		  SET @cityName = 'Richmond'
		  SET @stateCode = 'VA'
		  SET @address = '1111 E. Main Street'
		  SET @postCode = '23219'
		  SET @startDate = '2021-01-01'
		  SET @legalNumber = '201512140'

		   -- Execute logic for USA
		  EXEC GetCityAndStateIds
			    @countryCode = @countryCode,
				@cityName = @cityName,
				@stateCode = @stateCode,
		        @clientId = @client,
		        @cadminId = @cadmin,
				@cityId = @cId OUTPUT,
				@stateId = @sId OUTPUT;

		   -- Insert data into the LegalEntity table
            INSERT INTO LegalEntity (
                ShortName,
                LongName,
                XRefCode,
                ClientId,
                LastModifiedUserId,
                LastModifiedTimestamp,
                CountryCode,
                Address,
                GeoCityId,
                StateCode,
                PostalCode,
				County,
                LegalIdNumber,
                LegalIdNumberType,
                Active,
                EffectiveStart,
                IsAutoCreated,
                IsValidationRequired,
                IsNotDisbursePrintToBackOffice,
                AddressCountryCode,
                ApplyStatusIndianCalculation,
				PRCompanyId
            )
            VALUES (
                @legalEntityName,
                @legalEntityName,
                @legalEntityName,
                @clientId,
                @cadminId,
                CURRENT_TIMESTAMP,
                @countryCode,
                @address,
                @cId,
                @stateCode,
                @postCode,
				'Richmond City',
                @legalNumber,
                1,
                1,
                @startDate,
                0,
                0,
                1,
                @countryCode,
                0,
				2
            );

	SET @legalEntityId = SCOPE_IDENTITY()
	-- todo bank account setup
	DECLARE @bankId INT,
			@masterLegalEntityId INT,
			@bankAccountId INT

	INSERT INTO PRBankAccount (ShortName,LongName,RoutingNumber,AccountNumber,CheckSigning,XRefCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,UseForPrintingCheck,MICRIsBold)
	VALUES('AssociatedBank', null ,075900575,123456789,0, null ,@clientId,@cadminId,CURRENT_TIMESTAMP,0,1)

	SET @bankId = SCOPE_IDENTITY()

	DECLARE @masterLegalName NVARCHAR(100) = @legalEntityName+'_Master'

	INSERT INTO LegalEntityMasterBankAccountSetting (LegalEntityId, ShortName, LongName, XrefCode, EffectiveStart, EffectiveEnd, isDefault, FundingIdentifier,TaxServiceId,ServiceUserNumber,ClientId,LastModifiedUserId,LastModifiedTimestamp, IsFasterPayment)
	VALUES(@legalEntityId,@masterLegalName,null,null,'2011-01-01',NULL,1,NULL,@legalEntityId,NULL,@clientId,@cadminId,CURRENT_TIMESTAMP,NULL)

	SET @masterLegalEntityId = SCOPE_IDENTITY()

	DECLARE @bankAccountName NVARCHAR(100) = @legalEntityName+'_BankDef'

	INSERT INTO LegalEntityBankAccountDef
	(ShortName, LongName, IsApproved, EffectiveStart, EffectiveEnd, ApprovedOn, ClientId, LastModifiedUserId, LastModifiedTimeStamp, CVDApproved, CVDApprovedOn, FOSApprovalState, FOSApprovalFileSentOn, FOSApprovedOn, NumberOfFOSCVDTransmitTries, LegalEntityMasterBankAccountSettingId)
	VALUES(@bankAccountName,null,1,'2011-01-01',NULL,'2011-01-01',@clientId,@cadminId,CURRENT_TIMESTAMP,0,NULL,NULL,NULL,NULL,NULL,@masterLegalEntityId)

	SET @bankAccountId = SCOPE_IDENTITY()

	INSERT INTO LegalEntityBankAccount (PRBankAccountTypeId,PRBankAccountId,ClientId,LastModifiedUserId,LastModifiedTimestamp,LegalEntityBankAccountDefId,CheckPrinting,CheckSigning,BankTransferDisbursementSourceId,CheckDisbursementSourceId,OverrideLegalEntityName,IsCTCRecipientIdRequired,
	CheckCompanyName, CheckAddressLine1, CheckCity,CheckStateCode, CheckCountryCode, CheckPhoneNumber, CheckPostalCode,DirectDepositPRBankAccountId, PROCCPartnerBankId)
	VALUES (1,@bankId,@clientId,@cadminId,CURRENT_TIMESTAMP,@bankAccountId,1,1,1,1,0,1, 'checkCompany', '123 address', 'Bloomington', 'MN', 'USA', '5553332222', '55416',@bankAccountId, 5)

		END;

    ELSE IF @countryCode = 'CAN'
		BEGIN

		   SET @cityName = 'Toronto'
		   SET @stateCode = 'ON'
		   SET @address = '4110 Yonge Street'
		   SET @postCode = 'M2P 2B7'
		   SET @startDate = '2021-01-01'
		   SET @legalNumber = '111111118'
           SET @legalEntityName = @testName + ' LegalEntity ' + @uuid;

           -- Execute logic for CAN
		   EXEC GetCityAndStateIds
			    @countryCode = @countryCode,
				@cityName = @cityName,
				@stateCode = @stateCode,
		        @clientId = @client,
		        @cadminId = @cadmin,
				@cityId = @cId OUTPUT,
				@stateId = @sId OUTPUT;


		  -- Insert data into the LegalEntity table
            INSERT INTO LegalEntity (
                ShortName,
                LongName,
                XRefCode,
                ClientId,
                LastModifiedUserId,
                LastModifiedTimestamp,
                CountryCode,
                Address,
                GeoCityId,
                StateCode,
                PostalCode,
                LegalIdNumber,
                LegalIdNumberType,
                Active,
                EffectiveStart,
                IsAutoCreated,
                IsValidationRequired,
                IsNotDisbursePrintToBackOffice,
                AddressCountryCode,
                ApplyStatusIndianCalculation,
				PRCompanyId
            )
            VALUES (
                @legalEntityName,
                @legalEntityName,
                @legalEntityName,
                @clientId,
                @cadminId,
                CURRENT_TIMESTAMP,
                @countryCode,
                @address,
                @cId,
                @stateCode,
                @postCode,
                @legalNumber,
                1,
                1,
                @startDate,
                0,
                0,
                1,
                @countryCode,
                0,
				1
            );

	SET @legalEntityId = SCOPE_IDENTITY()
	--SELECT * FROM LegalEntity where LegalEntityId = @legalEntityId
	-- Insert Legal Entity Insurance
	DECLARE @legalEntityInsuranceId INT

	INSERT INTO LegalEntityEmployeeInsurance (LegalEntityId,ReferenceCode,ClientId,LastModifiedUserId,LastModifiedTimestamp,RateGroup,IsDefault,LegalEntityEmployeeInsurancePreferenceCodeId)
	VALUES(@legalEntityId,'0001',@clientId,@cadminId,CURRENT_TIMESTAMP,'0001',1,1)

	SET @legalEntityInsuranceId = SCOPE_IDENTITY()

	INSERT INTO LegalEntityEmployeeInsuranceRate (LegalEntityEmployeeInsuranceId,Rate,EffectiveStart,ClientId,LastModifiedUserId,LastModifiedTimestamp)
	VALUES (@legalEntityInsuranceId,1.4,@startDate,@clientId,@cadminId,CURRENT_TIMESTAMP)
	-- update Legal Entity Table
	UPDATE LegalEntity SET EIReferenceCode = @legalEntityInsuranceId WHERE LegalEntityId = @legalEntityId

		END;
    ELSE
    BEGIN
        -- Country code is neither 'USA' nor 'CAN', throw an exception
        THROW 51003, 'Country Code is not USA or CAN', 1;
    END;
END;


DROP PROCEDURE CreateLegalEntityWithCountryCode