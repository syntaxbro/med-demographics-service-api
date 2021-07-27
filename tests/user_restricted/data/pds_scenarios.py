retrieve = [
    {"scenario": "retrieve_patient", "patient": "5900038181", "response": {"address": [{"id": "9F4FF65D", "line": ["testing", "testing", "testing", "testing", "testing"], "period":{"start": "2021-01-22"}, "postalCode": "HL12 6HL", "use": "home"}], "birthDate": "2010-01-22", "extension": [{"extension": [{"url": "language", "valueCodeableConcept": {"coding": [{"code": "hy", "display": "Armenian", "system": "https://fhir.nhs.uk/R4/CodeSystem/UKCore-HumanLanguage", "version": "1.0.0"}]}}, {"url": "interpreterRequired", "valueBoolean": False}], "url": "https://fhir.nhs.uk/R4/StructureDefinition/Extension-UKCore-NHSCommunication"}], "gender": "female", "id": "5900038181", "identifier": [{"extension": [{"url": "https://fhir.nhs.uk/R4/StructureDefinition/Extension-UKCore-NHSNumberVerificationStatus", "valueCodeableConcept": {"coding": [{"code": "01", "display": "Number present and verified", "system": "https://fhir.nhs.uk/R4/CodeSystem/UKCore-NHSNumberVerificationStatus", "version": "1.0.0"}]}}], "system": "https://fhir.nhs.uk/Id/nhs-number", "value": "5900038181"}], "meta": {"security": [{"code": "U", "display": "unrestricted", "system": "https://www.hl7.org/fhir/valueset-security-labels.html"}], "versionId": "19"}, "name": [{"family": "Bogan", "given": ["Testing"], "id":"7EB47E61", "period":{"start": "2021-01-22"}, "prefix": ["Mr"], "suffix":["Bsc"], "use":"usual"}], "resourceType":"Patient"}},  # noqa: E231, E501
    {"scenario": "retrieve_auth_header_missing_or_blank", "patient": "5900038181", "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "forbidden", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "ACCESS_DENIED", "display": "Access Denied - Unauthorised"}]}, "diagnostics": "Invalid access token"}]}},  # noqa: E231, E501
    {"scenario": "retrieve_auth_header_invalid_token", "patient": "5900038181", "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "forbidden", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "ACCESS_DENIED", "display": "Access Denied - Unauthorised"}]}, "diagnostics": "Invalid Access Token"}]}},  # noqa: E231, E501
    {"scenario": "retrieve_urid_header_missing", "patient": "5900038181", "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "value", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "MISSING_VALUE", "display": "Required value is missing"}]}, "diagnostics": "Missing value in header 'NHSD-Session-URID'"}]}},  # noqa: E231, E501
    {"scenario": "retrieve_x_request_header_blank", "patient": "5900038181", "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "value", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "INVALID_VALUE", "display": "Provided value is invalid"}]}, "diagnostics": "Invalid value - '' in header 'X-Request-ID'"}]}},  # noqa: E231, E501
    {"scenario": "retrieve_x_request_header_invalid", "patient": "5900038181", "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "value", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "INVALID_VALUE", "display": "Provided value is invalid"}]}, "diagnostics": "Invalid value - '1234' in header 'X-Request-ID'"}]}},  # noqa: E231, E501
    {"scenario": "retrieve_x_request_header_missing", "patient": "5900038181", "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "structure", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "PRECONDITION_FAILED", "display": "Required condition was not fulfilled"}]}, "diagnostics": "Invalid request with error - X-Request-ID header must be supplied to access this resource"}]}},  # noqa: E231, E501
    {"scenario": "retrieve_related_person", "patient": "9450827834", "response": {'entry': [{'fullUrl': 'https://veit07.api.service.nhs.uk/personal-demographics/FHIR/R4/Patient/9450827834/RelatedPerson/268DB7E1', 'resource': {'active': True, 'address': [{'extension': [{'extension': [{'url': 'type', 'valueCoding': {'code': 'PAF', 'system': 'https://fhir.nhs.uk/R4/CodeSystem/UKCore-AddressKeyType'}}, {'url': 'value', 'valueString': '123'}], 'url': 'https://fhir.nhs.uk/R4/StructureDefinition/Extension-UKCore-AddressKey'}], 'line': ['1', 'x', 'l', 'leeds', 'y'], 'period': {'start': '2015-02-03'}, 'postalCode': 'LS1', 'use': 'home'}], 'extension': [{'url': 'https://fhir.nhs.uk/R4/StructureDefinition/Extension-UKCore-ContactRank', 'valuePositiveInt': 1}, {'extension': [{'url': 'PreferredContactMethod', 'valueCodeableConcept': {'coding': [{'code': '7', 'display': 'Sign Language', 'system': 'https://fhir.nhs.uk/R4/CodeSystem/UKCore-PreferredContactMethod'}]}}, {'url': 'PreferredContactTimes', 'valueString': '12'}, {'url': 'PreferredWrittenCommunicationFormat', 'valueCodeableConcept': {'coding': [{'code': '12', 'display': 'Braille', 'system': 'https://fhir.nhs.uk/R4/CodeSystem/UKCore-PreferredWrittenCommunicationFormat'}]}}], 'url': 'https://fhir.nhs.uk/R4/StructureDefinition/Extension-UKCore-ContactPreference'}, {'extension': [{'url': 'language', 'valueCodeableConcept': {'coding': [{'code': 'ak', 'display': 'Akan', 'system': 'https://fhir.nhs.uk/R4/CodeSystem/UKCore-HumanLanguage', 'version': '1.0.0'}]}}, {'url': 'interpreterRequired', 'valueBoolean': True}], 'url': 'https://fhir.nhs.uk/R4/StructureDefinition/Extension-UKCore-NHSCommunication'}], 'id': '268DB7E1', 'name': [{'family': 'a', 'given': ['b', 'c'], 'period': {'start': '2015-02-03'}, 'prefix': ['Dame'], 'suffix': ['d'], 'use': 'usual'}], 'patient': {'identifier': {'system': 'https://beta.api.digital.nhs.uk', 'value': '9452563966'}, 'reference': 'https://beta.api.digital.nhs.uk/Patient/9452563966', 'type': 'Patient'}, 'period': {'start': '2015-02-03'}, 'relationship': [{'coding': [{'code': 'BRO', 'display': 'brother', 'system': 'http://hl7.org/fhir/ValueSet/relatedperson-relationshiptype'}, {'code': 'Agent', 'display': 'Agent of patient', 'system': 'https://fhir.nhs.uk/R4/CodeSystem/UKCore-AdditionalRelatedPersonRole'}, {'code': 'N', 'display': 'Next-of-Kin', 'system': 'http://hl7.org/fhir/ValueSet/relatedperson-relationshiptype'}]}], 'resourceType': 'RelatedPerson'}}], 'resourceType': 'Bundle', 'total': 1, 'type': 'searchset'}},  # noqa: E231, E501
    {"scenario": "retrieve_urid_header_invalid", "patient": "5900038181", "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "value", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "INVALID_VALUE", "display": "Provided value is invalid"}]}, "diagnostics": "Invalid value - 'invalid' in header 'NHSD-Session-URID'. Refer to the guidance for this header in our API Specification https://digital.nhs.uk/developer/api-catalogue/personal-demographics-service-fhir"}]}}  # noqa: E231, E501
]

search = [
    {"scenario": "simple_search_happy_path", "query_params": {"family": "Mapping", "gender": "female", "birthdate": "eq2010-01-01"}, "response": {"entry": [{"fullUrl": "https://veit07.api.service.nhs.uk/personal-demographics/FHIR/R4/Patient/5900009068", "resource": {"address": [{"id": "A17EDBD4", "line": ["1", "westwood", "ecclechill", "bradfordian"], "period":{"start": "2020-02-24"}, "postalCode": "BD2 2LY", "use": "home"}], "birthDate": "2010-01-01", "deceasedDateTime": "2015-03-02T00:00:00+00:00", "extension": [{"extension": [{"url": "deathNotificationStatus", "valueCodeableConcept": {"coding": [{"code": "1", "display": "Informal - death notice received via an update from a local NHS Organisation such as GP or Trust", "system": "https://fhir.nhs.uk/R4/CodeSystem/UKCore-DeathNotificationStatus", "version": "1.0.0"}]}}, {"url": "systemEffectiveDate", "valueDateTime": "2020-02-27T16:14:58+00:00"}], "url": "https://fhir.nhs.uk/R4/StructureDefinition/Extension-UKCore-DeathNotificationStatus"}], "gender": "female", "generalPractitioner": [{"id": "1E2DE592", "identifier": {"period": {"start": "2020-02-28"}, "system": "https://fhir.nhs.uk/Id/ods-organization-code", "value": "B86055"}, "type": "Organization"}], "id": "5900009068", "identifier": [{"extension": [{"url": "https://fhir.nhs.uk/R4/StructureDefinition/Extension-UKCore-NHSNumberVerificationStatus", "valueCodeableConcept": {"coding": [{"code": "01", "display": "Number present and verified", "system": "https://fhir.nhs.uk/R4/CodeSystem/UKCore-NHSNumberVerificationStatus", "version": "1.0.0"}]}}], "system": "https://fhir.nhs.uk/Id/nhs-number", "value": "5900009068"}], "meta": {"security": [{"code": "U", "display": "unrestricted", "system": "https://www.hl7.org/fhir/valueset-security-labels.html"}], "versionId": "26"}, "multipleBirthInteger": 1, "name": [{"family": "Mapping", "given": ["Search", "Again"], "id":"8B5079EF", "period":{"start": "2020-03-05"}, "prefix": ["Dame"], "suffix":["MBA", "PHD"], "use":"usual"}], "resourceType":"Patient", "telecom":[{"id": "35CC8EA9", "period": {"start": "2020-02-24"}, "system": "phone", "use": "home", "value": "07900000000"}]}, "search": {"score": 1}}], "resourceType": "Bundle", "total": 1, "type": "searchset"}},  # noqa: E231, E501
    {"scenario": "simple_search_with_auth_header_missing_or_blank", "query_params": {"family": "Mapping", "gender": "female", "birthdate": "eq2010-01-01"}, "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "forbidden", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "ACCESS_DENIED", "display": "Access Denied - Unauthorised"}]}, "diagnostics": "Invalid access token"}]}},  # noqa: E231, E501
    {"scenario": "simple_search_with_auth_header_invalid_token", "query_params": {"family": "Mapping", "gender": "female", "birthdate": "eq2010-01-01"}, "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "forbidden", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "ACCESS_DENIED", "display": "Access Denied - Unauthorised"}]}, "diagnostics": "Invalid Access Token"}]}},  # noqa: E231, E501
    {"scenario": "simple_search_with_urid_header_missing", "query_params": {"family": "Mapping", "gender": "female", "birthdate": "eq2010-01-01"}, "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "value", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "MISSING_VALUE", "display": "Required value is missing"}]}, "diagnostics": "Missing value in header 'NHSD-Session-URID'"}]}},  # noqa: E231, E501
    {"scenario": "simple_search_with_x_request_header_blank", "query_params": {"family": "Mapping", "gender": "female", "birthdate": "eq2010-01-01"}, "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "value", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "INVALID_VALUE", "display": "Provided value is invalid"}]}, "diagnostics": "Invalid value - '' in header 'X-Request-ID'"}]}},  # noqa: E231, E501
    {"scenario": "simple_search_with_x_request_header_invalid", "query_params": {"family": "Mapping", "gender": "female", "birthdate": "eq2010-01-01"}, "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "value", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "INVALID_VALUE", "display": "Provided value is invalid"}]}, "diagnostics": "Invalid value - '1234' in header 'X-Request-ID'"}]}},  # noqa: E231, E501
    {"scenario": "simple_search_with_x_request_header_missing", "query_params": {"family": "Mapping", "gender": "female", "birthdate": "eq2010-01-01"}, "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "structure", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "PRECONDITION_FAILED", "display": "Required condition was not fulfilled"}]}, "diagnostics": "Invalid request with error - X-Request-ID header must be supplied to access this resource"}]}},  # noqa: E231, E501
    {"scenario": "simple_search_happy_path", "query_params": {"family": "Mapping", "birthdate": "eq2010-01-01"}, "response": {"entry": [{"fullUrl": "https://veit07.api.service.nhs.uk/personal-demographics/FHIR/R4/Patient/5900009068", "resource": {"address": [{"id": "A17EDBD4", "line": ["1", "westwood", "ecclechill", "bradfordian"], "period":{"start": "2020-02-24"}, "postalCode": "BD2 2LY", "use": "home"}], "birthDate": "2010-01-01", "deceasedDateTime": "2015-03-02T00:00:00+00:00", "extension": [{"extension": [{"url": "deathNotificationStatus", "valueCodeableConcept": {"coding": [{"code": "1", "display": "Informal - death notice received via an update from a local NHS Organisation such as GP or Trust", "system": "https://fhir.nhs.uk/R4/CodeSystem/UKCore-DeathNotificationStatus", "version": "1.0.0"}]}}, {"url": "systemEffectiveDate", "valueDateTime": "2020-02-27T16:14:58+00:00"}], "url": "https://fhir.nhs.uk/R4/StructureDefinition/Extension-UKCore-DeathNotificationStatus"}], "gender": "female", "generalPractitioner": [{"id": "1E2DE592", "identifier": {"period": {"start": "2020-02-28"}, "system": "https://fhir.nhs.uk/Id/ods-organization-code", "value": "B86055"}, "type": "Organization"}], "id": "5900009068", "identifier": [{"extension": [{"url": "https://fhir.nhs.uk/R4/StructureDefinition/Extension-UKCore-NHSNumberVerificationStatus", "valueCodeableConcept": {"coding": [{"code": "01", "display": "Number present and verified", "system": "https://fhir.nhs.uk/R4/CodeSystem/UKCore-NHSNumberVerificationStatus", "version": "1.0.0"}]}}], "system": "https://fhir.nhs.uk/Id/nhs-number", "value": "5900009068"}], "meta": {"security": [{"code": "U", "display": "unrestricted", "system": "https://www.hl7.org/fhir/valueset-security-labels.html"}], "versionId": "26"}, "multipleBirthInteger": 1, "name": [{"family": "Mapping", "given": ["Search", "Again"], "id":"8B5079EF", "period":{"start": "2020-03-05"}, "prefix": ["Dame"], "suffix":["MBA", "PHD"], "use":"usual"}], "resourceType":"Patient", "telecom":[{"id": "35CC8EA9", "period": {"start": "2020-02-24"}, "system": "phone", "use": "home", "value": "07900000000"}]}, "search": {"score": 1}}], "resourceType": "Bundle", "total": 1, "type": "searchset"}},  # noqa: E231, E501
    {"scenario": "simple_search_happy_path", "query_params": {"family": "Mapping", "birthdate": "le2010-01-02"}, "response": {"entry": [{"fullUrl": "https://veit07.api.service.nhs.uk/personal-demographics/FHIR/R4/Patient/5900009068", "resource": {"address": [{"id": "A17EDBD4", "line": ["1", "westwood", "ecclechill", "bradfordian"], "period":{"start": "2020-02-24"}, "postalCode": "BD2 2LY", "use": "home"}], "birthDate": "2010-01-01", "deceasedDateTime": "2015-03-02T00:00:00+00:00", "extension": [{"extension": [{"url": "deathNotificationStatus", "valueCodeableConcept": {"coding": [{"code": "1", "display": "Informal - death notice received via an update from a local NHS Organisation such as GP or Trust", "system": "https://fhir.nhs.uk/R4/CodeSystem/UKCore-DeathNotificationStatus", "version": "1.0.0"}]}}, {"url": "systemEffectiveDate", "valueDateTime": "2020-02-27T16:14:58+00:00"}], "url": "https://fhir.nhs.uk/R4/StructureDefinition/Extension-UKCore-DeathNotificationStatus"}], "gender": "female", "generalPractitioner": [{"id": "1E2DE592", "identifier": {"period": {"start": "2020-02-28"}, "system": "https://fhir.nhs.uk/Id/ods-organization-code", "value": "B86055"}, "type": "Organization"}], "id": "5900009068", "identifier": [{"extension": [{"url": "https://fhir.nhs.uk/R4/StructureDefinition/Extension-UKCore-NHSNumberVerificationStatus", "valueCodeableConcept": {"coding": [{"code": "01", "display": "Number present and verified", "system": "https://fhir.nhs.uk/R4/CodeSystem/UKCore-NHSNumberVerificationStatus", "version": "1.0.0"}]}}], "system": "https://fhir.nhs.uk/Id/nhs-number", "value": "5900009068"}], "meta": {"security": [{"code": "U", "display": "unrestricted", "system": "https://www.hl7.org/fhir/valueset-security-labels.html"}], "versionId": "26"}, "multipleBirthInteger": 1, "name": [{"family": "Mapping", "given": ["Search", "Again"], "id":"8B5079EF", "period":{"start": "2020-03-05"}, "prefix": ["Dame"], "suffix":["MBA", "PHD"], "use":"usual"}], "resourceType":"Patient", "telecom":[{"id": "35CC8EA9", "period": {"start": "2020-02-24"}, "system": "phone", "use": "home", "value": "07900000000"}]}, "search": {"score": 1}}], "resourceType": "Bundle", "total": 1, "type": "searchset"}},  # noqa: E231, E501
    {"scenario": "simple_search_patient_happy_path_sensitive", "query_params": {"family": "Middleton", "gender": "female", "birthdate": "eq2000-01-01"}, "response": {'entry': [{'fullUrl': 'https://veit07.api.service.nhs.uk/personal-demographics/FHIR/R4/Patient/5900018512', 'resource': {'birthDate': '2000-01-01', 'deceasedDateTime': '2009-05-01T00:00:00+00:00', 'gender': 'female', 'id': '5900018512', 'identifier': [{'extension': [{'url': 'https://fhir.nhs.uk/R4/StructureDefinition/Extension-UKCore-NHSNumberVerificationStatus', 'valueCodeableConcept': {'coding': [{'code': '01', 'display': 'Number present and verified', 'system': 'https://fhir.nhs.uk/R4/CodeSystem/UKCore-NHSNumberVerificationStatus', 'version': '1.0.0'}]}}], 'system': 'https://fhir.nhs.uk/Id/nhs-number', 'value': '5900018512'}], 'meta': {'security': [{'code': 'R', 'display': 'restricted', 'system': 'https://www.hl7.org/fhir/valueset-security-labels.html'}], 'versionId': '9'}, 'name': [{'family': 'Middleton', 'given': ['Cynthia', 'Cindy'], 'id':'7C3026E1', 'period':{'start': '2020-03-31'}, 'prefix': ['Baroness'], 'suffix':['Brnss'], 'use':'usual'}], 'resourceType':'Patient'}, 'search':{'score': 1}}], 'resourceType': 'Bundle', 'total': 1, 'type': 'searchset'}},  # noqa: E231, E501
    {"scenario": "simple_search_patient_sensitive_info_not_returned", "query_params": {"family": "Ukraine", "gender": "male", "birthdate": "eq2000-01-01"}, "response": {'entry': [{'fullUrl': 'https://veit07.api.service.nhs.uk/personal-demographics/FHIR/R4/Patient/5900013553', 'resource': {'birthDate': '2000-01-01', 'deceasedDateTime': '2020-01-01T00:00:00+00:00', 'gender': 'male', 'id': '5900013553', 'identifier': [{'extension': [{'url': 'https://fhir.nhs.uk/R4/StructureDefinition/Extension-UKCore-NHSNumberVerificationStatus', 'valueCodeableConcept': {'coding': [{'code': '01', 'display': 'Number present and verified', 'system': 'https://fhir.nhs.uk/R4/CodeSystem/UKCore-NHSNumberVerificationStatus', 'version': '1.0.0'}]}}], 'system': 'https://fhir.nhs.uk/Id/nhs-number', 'value': '5900013553'}], 'meta': {'security': [{'code': 'R', 'display': 'restricted', 'system': 'https://www.hl7.org/fhir/valueset-security-labels.html'}], 'versionId': '5'}, 'name': [{'family': 'Ukraine', 'given': ['John'], 'id': 'E504354F', 'period': {'start': '2020-03-31'}, 'prefix': ['Mr'], 'use': 'usual'}], 'resourceType': 'Patient'}, 'search': {'score': 1}}], 'resourceType': 'Bundle', 'total': 1, 'type': 'searchset'}},  # noqa: E231, E501
]

update = [
    {"scenario": "update_dob_happy_path", "patient": "9693632192", "patch": {"patches": [{"op": "replace", "path": "/birthDate", "value": "2001-01-01"}]}},  # noqa: E231, E501
    {"scenario": "update_with_auth_header_missing_or_blank", "patient": "9693632192", "patch": {"patches": [{"op": "replace", "path": "/birthDate", "value": "2001-01-01"}]}, "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "forbidden", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "ACCESS_DENIED", "display": "Access Denied - Unauthorised"}]}, "diagnostics": "Invalid access token"}]}},  # noqa: E231, E501
    {"scenario": "update_with_auth_header_invalid", "patient": "9693632192", "patch": {"patches": [{"op": "replace", "path": "/birthDate", "value": "2001-01-01"}]}, "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "forbidden", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "ACCESS_DENIED", "display": "Access Denied - Unauthorised"}]}, "diagnostics": "Invalid Access Token"}]}},  # noqa: E231, E501
    {"scenario": "update_with__urid_header_missing", "patient": "9693632192", "patch": {"patches": [{"op": "replace", "path": "/birthDate", "value": "2001-01-01"}]}, "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "value", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "MISSING_VALUE", "display": "Required value is missing"}]}, "diagnostics": "Missing value in header 'NHSD-Session-URID'"}]}},  # noqa: E231, E501
    {"scenario": "update_with_x_request_header_blank", "patient": "9693632192", "patch": {"patches": [{"op": "replace", "path": "/birthDate", "value": "2001-01-01"}]}, "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "value", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "INVALID_VALUE", "display": "Provided value is invalid"}]}, "diagnostics": "Invalid value - '' in header 'X-Request-ID'"}]}},  # noqa: E231, E501
    {"scenario": "update_with_x_request_header_invalid", "patient": "9693632192", "patch": {"patches": [{"op": "replace", "path": "/birthDate", "value": "2001-01-01"}]}, "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "value", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "INVALID_VALUE", "display": "Provided value is invalid"}]}, "diagnostics": "Invalid value - '1234' in header 'X-Request-ID'"}]}},  # noqa: E231, E501
    {"scenario": "update_with_x_request_header_missing", "patient": "9693632192", "patch": {"patches": [{"op": "replace", "path": "/birthDate", "value": "2001-01-01"}]}, "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "structure", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "PRECONDITION_FAILED", "display": "Required condition was not fulfilled"}]}, "diagnostics": "Invalid request with error - X-Request-ID header must be supplied to access this resource"}]}},  # noqa: E231, E501
    {"scenario": "update_with_low_x_sync_wait", "patient": "9693632192", "patch": {"patches": [{"op": "replace", "path": "/birthDate", "value": "2001-01-01"}]}, "response": {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "structure", "details": {"coding": [{"system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode", "version": "1", "code": "SERVICE_UNAVAILABLE", "display": "Service unavailable"}]}, "diagnostics": "The downstream domain processing has not completed within the configured timeout period. Retry your request after the time specified by the 'Retry-After' header, using the same 'X-Request-ID'"}]}},  # noqa: E231, E501
]
