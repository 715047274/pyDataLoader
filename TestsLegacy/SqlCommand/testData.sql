
DECLARE @name NVARCHAR(100) = 'test',
		@country NVARCHAR(100) = 'USA',
		@lId INT,
		@id NVARCHAR(100) = format(getdate(),'yyyyMMddHHmmss'),
		@client INT = 0,
		@admin INT = 0;

Exec CreateLegalEntityWithCountryCode
		@testName = @name,
		@uuid = @id,
		@countryCode = @country,
		@legalEntityId = @lId,
		@clientId = @client,
        @cadminId = @admin
		