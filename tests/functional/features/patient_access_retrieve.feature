Feature: Patient Access (Retrieve)
	Retrieve a PDS record as a patient

	Scenario: Patient can retrieve self
		Given I am a P9 user
		And Scope added to product
		
		When I retrieve my details

		Then I get a 200 HTTP response code

	Scenario: Patient cannot retrieve another patient
		Given I am a P9 user
		And Scope added to product
		
		When I retrieve a patient

		Then I get a 403 HTTP response code
		And ACCESS_DENIED is at issue[0].details.coding[0].code in the response body
		And Patient cannot perform this action is at issue[0].details.coding[0].display in the response body

	Scenario: Patient retrieve uses incorrect path
		Given I am a P9 user
		And Scope added to product
		
		When I retrieve my details using an incorrect path

		Then I get a 403 HTTP response code
		And ACCESS_DENIED is at issue[0].details.coding[0].code in the response body
		And Patient cannot perform this action is at issue[0].details.coding[0].display in the response body