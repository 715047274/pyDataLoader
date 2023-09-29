IF NOT EXISTS (SELECT * FROM sys.objects WHERE name = 'GetCityAndStateIds' AND type = 'P')
BEGIN
    EXEC('
    CREATE PROCEDURE GetCityAndStateIds
        @countryCode NVARCHAR(100),
        @cityName NVARCHAR(100),
        @stateCode NVARCHAR(100),
        @clientId INT = NULL,
        @cadminId INT = NULL,
        @cityId INT OUTPUT,
        @stateId INT OUTPUT
    AS
    BEGIN
        BEGIN TRY
            -- Check if the Country Code exists
            IF NOT EXISTS (SELECT 1 FROM GeoCountry WHERE CountryCode = @countryCode)
            BEGIN
                -- Country Code does not exist, throw an exception
                THROW 51000, ''Country Code does not exist'', 1;
            END;

            -- Check if the State Code exists
            IF NOT EXISTS (SELECT 1 FROM GeoState WHERE StateCode = @stateCode)
            BEGIN
                -- State Code does not exist, throw an exception
                THROW 51001, ''State Code does not exist'', 1;
            END;

            -- Attempt to retrieve the CityId and StateId
            SELECT @cityId = city.GeoCityId, @stateId = state.GeoStateId
            FROM GeoCity city
            JOIN GeoState state ON city.GeoStateId = state.GeoStateId
            JOIN GeoCountry country ON state.GeoCountryId = country.GeoCountryId
            WHERE country.CountryCode = @countryCode
                AND state.StateCode = @stateCode
                AND city.ShortName = @cityName;

            -- Check if the city was found
            IF @cityId IS NULL
            BEGIN
                -- If @clientId is not provided, use the default value of NULL
                IF @clientId IS NULL
                    SET @clientId = 10000;

                -- If @cadminId is not provided, use the default value of NULL
                IF @cadminId IS NULL
                    SET @cadminId = 1001;

                SELECT @stateId = GeoStateId FROM GeoState WHERE StateCode = @stateCode;

                -- City not found, so insert it into GeoCity
                INSERT INTO GeoCity (ShortName, GeoStateId, LastModifiedTimestamp, ClientId, LastModifiedUserId)
                VALUES (@cityName, @stateId, CURRENT_TIMESTAMP, @clientId, @cadminId);

                -- Retrieve the newly inserted CityId
                SELECT @cityId = SCOPE_IDENTITY();
            END;
        END TRY
        BEGIN CATCH
            -- Handle exceptions
            THROW;
        END CATCH;
    END;
    ');
END;