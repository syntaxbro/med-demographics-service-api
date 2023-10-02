Feature: Healthcare Worker Access
    Access by a healthcare worker

    Scenario: Healthcare worker using deprecated url
        Given I am a healthcare worker
        And I am using the deprecated url

        When I retrieve a patient

        Then I get a 404 HTTP response
    
    Scenario: Healthcare worker can retrieve patient
        Given I am a healthcare worker

        When I retrieve a patient

        Then I get a 200 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body contains the patient's NHS number
        And the response body is the correct shape

    Scenario: Attempt to retrieve a patient with missing authorization header
        Given I am a healthcare worker
        And I don't have an Authorization header

        When I retrieve a patient

        Then I get a 401 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body does not contain id
        And the response body is the Missing Authorization header response

    Scenario: Attempt to retrieve a patient with an empty authorization header
        Given I am a healthcare worker
        And I have an empty Authorization header

        When I retrieve a patient

        Then I get a 401 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body does not contain id
        And the response body is the Empty Authorization header response

    Scenario: Attempt to retrieve a patient with an invalid authorization header
        Given I am a healthcare worker
        And I have a header Authorization value of "Bearer abcdef123456789"

        When I retrieve a patient

        Then I get a 401 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body does not contain id
        And the response body is the Invalid Access Token response

    Scenario: Attempt to retrieve a patient without stating a role
        Given I am a healthcare worker
        And I don't have a NHSD-Session-URID header

        When I retrieve a patient

        Then I get a 400 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body does not contain id
        And the response body is the Missing URID header response

    Scenario: Attempt to retrieve a patient with an invalid role
        Given I am a healthcare worker
        And I have a header NHSD-Session-URID value of "invalid"

        When I retrieve a patient

        Then I get a 400 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body does not contain id
        And the response body is the Invalid URID header response

    Scenario: Attempt to retrieve a patient without Request ID header
        Given I am a healthcare worker
        And I have an empty X-Request-ID header

        When I retrieve a patient

        Then I get a 400 HTTP response
        And the response header does not contain X-Request-ID
        And the X-Correlation-ID response header matches the request
        And the response body does not contain id
        And the response body is the Empty X-Request ID response

    Scenario: Attempt to retrieve a patient with an invalid X-Request-ID
        Given I am a healthcare worker
        And I have a header X-Request-ID value of "1234"

        When I retrieve a patient

        Then I get a 400 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body does not contain id
        And the response body is the Invalid X-Request ID response

    Scenario: Attempt to retrieve a patient with a missing X-Request-ID
        Given I am a healthcare worker
        And I don't have a X-Request-ID header

        When I retrieve a patient

        Then I get a 412 HTTP response
        And the response header does not contain X-Request-ID
        And the X-Correlation-ID response header matches the request
        And the response body does not contain id
        And the response body is the Missing X-Request ID response

    Scenario: Healthcare worker can search for patient
        Given I am a healthcare worker
        And I have a patient's demographic details

        When I search for the patient's PDS record

        Then I get a 200 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body contains the expected values

    Scenario: Attempt to search for a patient with missing authorization header
        Given I am a healthcare worker
        And I have a patient's demographic details
        And I don't have an Authorization header

        When I search for the patient's PDS record

        Then I get a 401 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body is the Missing Authorization header response
        And the response body does not contain id

    Scenario: Attempt to search for a patient with an empty authorization header
        Given I am a healthcare worker
        And I have a patient's demographic details
        And I have an empty Authorization header

        When I search for the patient's PDS record

        Then I get a 401 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body does not contain id
        And the response body is the Empty Authorization header response

    Scenario: Attempt to search for a patient with an invalid authorization header
        Given I am a healthcare worker
        And I have a patient's demographic details
        And I have a header Authorization value of "Bearer abcdef123456789"

        When I search for the patient's PDS record

        Then I get a 401 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body does not contain id
        And the response body is the Invalid Access Token response

    Scenario: Attempt to search for a patient with an empty Request ID header
        Given I am a healthcare worker
        And I have a patient's demographic details
        And I have an empty X-Request-ID header

        When I search for the patient's PDS record

        Then I get a 400 HTTP response
        And the response header does not contain X-Request-ID
        And the X-Correlation-ID response header matches the request
        And the response body does not contain id
        And the response body is the Empty X-Request ID response

    Scenario: Attempt to search for a patient with an invalid X-Request-ID
        Given I am a healthcare worker
        And I have a patient's demographic details
        And I have a header X-Request-ID value of "1234"

        When I search for the patient's PDS record

        Then I get a 400 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body does not contain id
        And the response body is the Invalid X-Request ID response

    Scenario: Attempt to search for a patient with a missing X-Request-ID
        Given I am a healthcare worker
        And I have a patient's demographic details
        And I don't have a X-Request-ID header

        When I search for the patient's PDS record

        Then I get a 412 HTTP response
        And the response header does not contain X-Request-ID
        And the X-Correlation-ID response header matches the request
        And the response body does not contain id
        And the response body is the Missing X-Request ID response

    Scenario: Healthcare worker searches for sensitive patient
        Given I am a healthcare worker
        And I have a sensitive patient's demographic details

        When I search for the patient's PDS record

        Then I get a 200 HTTP response
        And the response body contains the expected values
        And the resposne body contains the sensitivity flag

    Scenario: Healthcare worker searches for patient without specifying gender
        Given I am a healthcare worker
        And I have a patient's demographic details without gender

        When I search for the patient's PDS record

        Then I get a 200 HTTP response
        And the response body contains the expected values

    Scenario: Healthcare worker searches for a patient with range for date of birth
        Given I am a healthcare worker
        And I have a patient's demographic details with a date of birth range

        When I search for the patient's PDS record

        Then I get a 200 HTTP response
        And the response body contains the expected values

    Scenario: Searching without gender can return mutliple results
        Given I am a healthcare worker
        And I enter a patient's vague demographic details

        When I search for the patient's PDS record

        Then I get a 200 HTTP response
        And the response body contains the expected values

    Scenario: Searching with fuzzy match
        Given I am a healthcare worker
        And I enter a patient's fuzzy demographic details

        When the query parameters contain _fuzzy-match as true
        And I search for the patient's PDS record

        Then I get a 200 HTTP response
        And the response body contains the expected values

    Scenario: Searching with unicode returns unicode record
        Given I am a healthcare worker
        And I enter a patient's unicode demographic details

        When I search for the patient's PDS record

        Then I get a 200 HTTP response
        And the response body contains the expected values

    Scenario: Searching with specified results limit can return error
        Given I am a healthcare worker
        And I enter a patient's vague demographic details

        When the query parameters contain _max-results as 1
        And I search for the patient's PDS record

        Then I get a 200 HTTP response
        And the response body is the Too Many Matches response

    Scenario: Update patient
        Given I am a healthcare worker
        And I have a patient's record to update
        And I wish to update the patient's gender

        When I update the patient's PDS record

        Then I get a 200 HTTP response
        And the response body contains the patient's new gender
        And the response body contains the record's new version number

    Scenario: Update patient using deprecated respond-async still returns 200
        Given I am a healthcare worker
        And I have a patient's record to update
        And I wish to update the patient's gender
        And I have a header Prefer value of "respond-async"

        When I update the patient's PDS record

        Then I get a 200 HTTP response
        And the response body contains the patient's new gender
        And the response body contains the record's new version number

    Scenario: Update patient with invalid wait header still updates
        Given I am a healthcare worker
        And I have a patient's record to update
        And I wish to update the patient's gender
        And I have a header X-Sync-Wait value of "invalid"

        When I update the patient's PDS record

        Then I get a 200 HTTP response
        And the response body contains the patient's new gender
        And the response body contains the record's new version number

    Scenario: Update patient with low wait header
        Given I am a healthcare worker
        And I have a patient's record to update
        And I wish to update the patient's gender
        And I have a header X-Sync-Wait value of "0.25"

        When I update the patient's PDS record

        Then I get a 503 HTTP response

    Scenario: Update patient with missing Authorization header
        Given I am a healthcare worker
        And I have a patient's record to update
        And I wish to update the patient's gender
        And I don't have a Authorization header

        When I update the patient's PDS record

        Then I get a 401 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body is the Missing Authorization header response

    Scenario: Update patient with an empty authorization header
        Given I am a healthcare worker
        And I have a patient's record to update
        And I wish to update the patient's gender
        And I have an empty Authorization header

        When I update the patient's PDS record

        Then I get a 401 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body is the Empty Authorization header response

    Scenario: Update patient with an invalid authorization header
        Given I am a healthcare worker
        And I have a patient's record to update
        And I wish to update the patient's gender
        And I have a header Authorization value of "Bearer abcdef123456789"

        When I update the patient's PDS record

        Then I get a 401 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body is the Invalid Access Token response

    Scenario: Update patient with an empty Request ID header
        Given I am a healthcare worker
        And I have a patient's record to update
        And I wish to update the patient's gender
        And I have an empty X-Request-ID header

        When I update the patient's PDS record

        Then I get a 400 HTTP response
        And the response header does not contain X-Request-ID
        And the X-Correlation-ID response header matches the request
        And the response body is the Empty X-Request ID response

    Scenario: Update patient with an invalid X-Request-ID
        Given I am a healthcare worker
        And I have a patient's record to update
        And I wish to update the patient's gender
        And I have a header X-Request-ID value of "1234"

        When I update the patient's PDS record

        Then I get a 400 HTTP response
        And the X-Request-ID response header matches the request
        And the X-Correlation-ID response header matches the request
        And the response body is the Invalid X-Request ID response

    Scenario: Update patient with a missing X-Request-ID
        Given I am a healthcare worker
        And I have a patient's record to update
        And I wish to update the patient's gender
        And I don't have a X-Request-ID header

        When I update the patient's PDS record

        Then I get a 412 HTTP response
        And the response header does not contain X-Request-ID
        And the X-Correlation-ID response header matches the request
        And the response body is the Missing X-Request ID response