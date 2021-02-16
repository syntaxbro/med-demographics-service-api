from .data.pds_scenarios import retrieve, search, update
from .utils import helpers
import json
from pytest_check import check


class TestUserRestrictedRetrievePatient:

    def test_retrieve_patient(self, headers_with_token):
        response = helpers.retrieve_patient(
            retrieve[0]["patient"],
            self.headers
        )
        helpers.check_retrieve_response_body(response, retrieve[0]["response"])
        helpers.check_response_status_code(response, 200)
        helpers.check_response_headers(response, self.headers)

    def test_retrieve_patient_with_missing_auth_header(self, headers):
        response = helpers.retrieve_patient(
            retrieve[1]["patient"],
            headers
        )
        helpers.check_retrieve_response_body(response, retrieve[1]["response"])
        helpers.check_response_status_code(response, 401)
        helpers.check_response_headers(response, headers)

    def test_retrieve_patient_with_blank_auth_header(self, headers):
        headers['authorization'] = ''
        response = helpers.retrieve_patient(
            retrieve[1]["patient"],
            headers
        )
        helpers.check_retrieve_response_body(
            response,
            retrieve[1]["response"]
        )
        helpers.check_response_status_code(response, 401)
        helpers.check_response_headers(response, headers)

    def test_retrieve_patient_with_invalid_auth_header(self, headers):
        headers['authorization'] = 'Bearer abcdef123456789'
        response = helpers.retrieve_patient(
            retrieve[2]["patient"],
            headers
        )
        helpers.check_retrieve_response_body(response, retrieve[2]["response"])
        helpers.check_response_status_code(response, 401)
        helpers.check_response_headers(response, headers)

    def test_retrieve_patient_with_missing_urid_header(self, headers_with_token):
        self.headers.pop("NHSD-Session-URID")
        response = helpers.retrieve_patient(
            retrieve[3]["patient"],
            self.headers
        )
        helpers.check_retrieve_response_body(response, retrieve[3]["response"])
        helpers.check_response_status_code(response, 400)
        helpers.check_response_headers(response, self.headers)

    def test_retrieve_patient_with_blank_x_request_header(self, headers_with_token):
        self.headers["X-Request-ID"] = ''
        response = helpers.retrieve_patient(
            retrieve[4]["patient"],
            self.headers
        )
        helpers.check_retrieve_response_body(response, retrieve[4]["response"])
        helpers.check_response_status_code(response, 400)
        self.headers.pop("X-Request-ID")
        helpers.check_response_headers(response, self.headers)

    def test_retrieve_patient_with_invalid_x_request_header(self, headers_with_token):
        self.headers["X-Request-ID"] = '1234'
        response = helpers.retrieve_patient(
            retrieve[5]["patient"],
            self.headers
        )
        helpers.check_retrieve_response_body(response, retrieve[5]["response"])
        helpers.check_response_status_code(response, 400)
        helpers.check_response_headers(response, self.headers)

    def test_retrieve_patient_with_missing_x_request_header(self, headers_with_token):
        self.headers.pop("X-Request-ID")
        response = helpers.retrieve_patient(
            retrieve[6]["patient"],
            self.headers
        )
        helpers.check_retrieve_response_body(response, retrieve[6]["response"])
        helpers.check_response_status_code(response, 412)
        helpers.check_response_headers(response, self.headers)


class TestUserRestrictedSearchPatient:

    def test_search_patient_happy_path(self, headers_with_token):
        response = helpers.search_patient(
            search[0]["query_params"],
            self.headers
        )
        helpers.check_search_response_body(response, search[0]["response"])
        helpers.check_response_status_code(response, 200)
        helpers.check_response_headers(response, self.headers)

    def test_search_patient_with_missing_auth_header(self, headers):
        response = helpers.search_patient(
            search[1]["query_params"],
            headers
        )
        helpers.check_search_response_body(response, search[1]["response"])
        helpers.check_response_status_code(response, 401)
        helpers.check_response_headers(response, headers)

    def test_search_patient_with_blank_auth_header(self, headers):
        headers['authorization'] = ''
        response = helpers.search_patient(
            search[1]["query_params"],
            headers
        )
        helpers.check_search_response_body(response, search[1]["response"])
        helpers.check_response_status_code(response, 401)
        helpers.check_response_headers(response, headers)

    def test_search_patient_with_invalid_auth_header(self, headers):
        headers['authorization'] = 'Bearer abcdef123456789'
        response = helpers.search_patient(
            search[2]["query_params"],
            headers
        )
        helpers.check_search_response_body(response, search[2]["response"])
        helpers.check_response_status_code(response, 401)
        helpers.check_response_headers(response, headers)

    def test_search_patient_with_missing_urid_header(self, headers_with_token):
        self.headers.pop("NHSD-Session-URID")
        response = helpers.search_patient(
            search[3]["query_params"],
            self.headers
        )
        helpers.check_search_response_body(response, search[3]["response"])
        helpers.check_response_status_code(response, 400)
        helpers.check_response_headers(response, self.headers)

    def test_search_patient_with_blank_x_request_header(self, headers_with_token):
        self.headers["X-Request-ID"] = ''
        response = helpers.search_patient(
            search[4]["query_params"],
            self.headers
        )
        helpers.check_search_response_body(response, search[4]["response"])
        helpers.check_response_status_code(response, 400)
        self.headers.pop("X-Request-ID")
        helpers.check_response_headers(response, self.headers)

    def test_search_patient_with_invalid_x_request_header(self, headers_with_token):
        self.headers["X-Request-ID"] = '1234'
        response = helpers.search_patient(
            search[5]["query_params"],
            self.headers
        )
        helpers.check_search_response_body(response, search[5]["response"])
        helpers.check_response_status_code(response, 400)
        helpers.check_response_headers(response, self.headers)

    def test_search_patient_with_missing_x_request_header(self, headers_with_token):
        self.headers.pop("X-Request-ID")
        response = helpers.search_patient(
            search[6]["query_params"],
            self.headers
        )
        helpers.check_search_response_body(response, search[6]["response"])
        helpers.check_response_status_code(response, 412)
        helpers.check_response_headers(response, self.headers)

    def test_search_patient_happy_path_genderfree(self, headers_with_token):
        response = helpers.search_patient(
            search[7]["query_params"],
            self.headers
        )
        helpers.check_search_response_body(response, search[0]["response"])
        helpers.check_response_status_code(response, 200)
        helpers.check_response_headers(response, self.headers)

    def test_search_advanced_alphanumeric_genderfree(self, headers_with_token):
        response = helpers.search_patient(
            search[8]["query_params"],
            self.headers
        )
        helpers.check_search_response_body(response, search[0]["response"])
        helpers.check_response_status_code(response, 200)
        helpers.check_response_headers(response, self.headers)

    def test_simple_trace_no_gender(self, headers_with_token):
        """See TestBase37101 Chain 7001"""
        print(self.headers)
        response = helpers.search_patient(
            {"family": "JAMESONGLE", "birthdate": "1982-03-14"},
            self.headers
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["resourceType"] == "Bundle"
        assert response_body["type"] == "searchset"
        assert response_body["total"] == 1
        assert response_body["entry"][0]["resource"]["id"] == "9912003071"

    def test_simple_trace_no_gender_no_result(self, headers_with_token):
        """See TestBase37101 Chain 7002"""
        print(self.headers)
        response = helpers.search_patient(
            {"family": "Clarke", "birthdate": "1975-01-01"},
            self.headers
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["resourceType"] == "Bundle"
        assert response_body["type"] == "searchset"
        assert response_body["total"] == 0

    def test_no_gender_postcode_format_doesnt_affect_score(self, headers_with_token):
        """See TestBase37101 Chain 7003"""
        response_1 = helpers.search_patient(
            {"family": "JAMESONGLE", "birthdate": "1982-03-14", "address-postcode": "LS27 8RR"},
            self.headers
        )
        response_1_body = response_1.json()

        response_2 = helpers.search_patient(
            {"family": "JAMESONGLE", "birthdate": "1982-03-14", "address-postcode": "ls278rr"},
            self.headers
        )
        response_2_body = response_2.json()

        assert response_1.status_code == 200
        assert response_2.status_code == response_1.status_code
        assert response_1_body["entry"][0]["resource"]["id"] == "9912003071"
        assert response_1_body["entry"][0]["resource"]["id"] == response_2_body["entry"][0]["resource"]["id"]
        assert response_1_body["entry"][0]["search"]["score"] == 1
        assert response_1_body["entry"][0]["search"]["score"] == response_2_body["entry"][0]["search"]["score"]

    def test_algorithmic_search_without_gender(self, headers_with_token):
        """See TestBase37102 Chain 7001"""
        response = helpers.search_patient(
            {"family": "STSimilar01", "birthdate": "1975-01-01"},
            self.headers
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["type"] == "searchset"
        assert response_body["resourceType"] == "Bundle"
        assert response_body["total"] == 3
        assert response_body["entry"][0]["search"]["score"] == 1
        assert response_body["entry"][0]["resource"]["id"] == "9990000050"
        assert response_body["entry"][0]["resource"]["gender"] == "male"
        assert response_body["entry"][0]["resource"]["birthDate"] == "1975-01-01"
        assert response_body["entry"][1]["search"]["score"] == 1
        assert response_body["entry"][1]["resource"]["id"] == "9990000069"
        assert response_body["entry"][1]["resource"]["gender"] == "male"
        assert response_body["entry"][1]["resource"]["birthDate"] == "1975-01-01"
        assert response_body["entry"][2]["search"]["score"] == 1
        assert response_body["entry"][2]["resource"]["id"] == "9990000077"
        assert response_body["entry"][2]["resource"]["gender"] == "male"
        assert response_body["entry"][2]["resource"]["birthDate"] == "1975-01-01"

    def test_algorithmic_fuzzy_match_unknown_gender(self, headers_with_token):
        """See TestBase37104 Chain 0001"""
        response = helpers.search_patient(
            {"family": "ATUnknow", "given": "Nisha", "birthdate": "1980-09-19", "_fuzzy-match": "true"},
            self.headers
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["type"] == "searchset"
        assert response_body["resourceType"] == "Bundle"
        assert response_body["entry"][0]["search"]["score"] == 0.9896
        assert response_body["entry"][0]["resource"]["id"] == "9990001502"

    def test_algorithmic_fuzzy_match_unicode(self, headers_with_token):
        """See TestBase37104 Chain 0007"""
        response = helpers.search_patient(
            {"family": "PÀTSÖN", "given": "PÀULINÉ", "birthdate": "1979-07-27", "_fuzzy-match": "true"},
            self.headers
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["type"] == "searchset"
        assert response_body["resourceType"] == "Bundle"
        assert response_body["entry"][0]["search"]["score"] == 0.9806
        assert response_body["entry"][0]["resource"]["id"] == "9930000011"
        assert response_body["entry"][0]["resource"]["gender"] == "female"
        assert response_body["entry"][0]["resource"]["birthDate"] == "1979-07-27"
        assert response_body["entry"][0]["resource"]["name"][0]["family"] == "PÀTTISÖN"
        assert response_body["entry"][0]["resource"]["name"][0]["given"][0] == "PÀULINÉ"
        assert response_body["entry"][1]["search"]["score"] == 0.8595
        assert response_body["entry"][1]["resource"]["id"] == "9930000054"
        assert response_body["entry"][1]["resource"]["gender"] == "female"
        assert response_body["entry"][1]["resource"]["birthDate"] == "1979-07-27"

    def test_algorithmic_fuzzy_match_regular_returns_unicode(self, headers_with_token):
        """See TestBase37104 Chain 0008"""
        response = helpers.search_patient(
            {"family": "PATSON", "given": "PAULINE", "birthdate": "1979-07-27", "_fuzzy-match": "true"},
            self.headers
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["type"] == "searchset"
        assert response_body["resourceType"] == "Bundle"
        assert response_body["entry"][0]["search"]["score"] == 0.9806
        assert response_body["entry"][0]["resource"]["id"] == "9930000054"
        assert response_body["entry"][0]["resource"]["gender"] == "female"
        assert response_body["entry"][0]["resource"]["birthDate"] == "1979-07-27"
        assert response_body["entry"][0]["resource"]["name"][0]["family"] == "PATTISON"
        assert response_body["entry"][0]["resource"]["name"][0]["given"][0] == "PAULINE"
        assert response_body["entry"][1]["search"]["score"] == 0.8595
        assert response_body["entry"][1]["resource"]["id"] == "9930000011"
        assert response_body["entry"][1]["resource"]["gender"] == "female"
        assert response_body["entry"][1]["resource"]["birthDate"] == "1979-07-27"

    def test_algorithmic_fuzzy_match_for_birthdate_range(self, headers_with_token):
        """See TestBase37104 Chain 0009"""
        response = helpers.search_patient(
            {
                "family": "ATUnknow", "given": "Nisha", "birthdate": "le1990-09-19",
                "birthdate": "ge1970-09-19", "_fuzzy-match": "true"
            },
            self.headers
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["type"] == "searchset"
        assert response_body["resourceType"] == "Bundle"
        assert response_body["entry"][0]["search"]["score"] == 0.9896
        assert response_body["entry"][0]["resource"]["id"] == "9990001502"

    def test_algorithmic_exact_match_requested_but_not_found(self, headers_with_token):
        """See TestBase37105 Chain 0003"""
        response = helpers.search_patient(
            {
                "family": "PÀTSÖN", "given": "PÀULINÉ", "birthdate": "1979-07-27",
                "_fuzzy-match": "true", "_exact-match": "true"
            },
            self.headers
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["type"] == "searchset"
        assert response_body["resourceType"] == "Bundle"
        assert response_body["total"] == 0

    def test_algorithmic_requesting_50_results(self, headers_with_token):
        """See TestBase37107 Chain 0004"""
        response = helpers.search_patient(
            {
                "family": "PATSON", "given": "PAULINE", "birthdate": "1979-07-27",
                "_fuzzy-match": "true", "_max-results": "50"
            },
            self.headers
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["type"] == "searchset"
        assert response_body["resourceType"] == "Bundle"
        assert response_body["entry"][0]["search"]["score"] == 0.9806
        assert response_body["entry"][0]["resource"]["id"] == "9930000054"
        assert response_body["entry"][1]["search"]["score"] == 0.8595

    def test_algorithmic_requesting_1_result_too_many_matches(self, headers_with_token):
        """See TestBase37107 Chain 0008"""
        response = helpers.search_patient(
            {
                "family": "PATSON", "given": "PAULINE", "birthdate": "1979-07-27",
                "_fuzzy-match": "true", "_max-results": "1"
            },
            self.headers
        )
        response_body = response.json()

        assert response_body["resourceType"] == "OperationOutcome"
        assert response_body["issue"][0]["details"]["coding"][0]["code"] == "TOO_MANY_MATCHES"
        assert response_body["issue"][0]["details"]["coding"][0]["display"] == "Too Many Matches"


class TestUserRestrictedPatientUpdate:

    def test_update_patient_dob(self, headers_with_token, create_random_date):

        #  send retrieve patient request to retrieve the patient record (Etag Header) & versionId
        response = helpers.retrieve_patient(
            update[0]["patient"],
            self.headers
        )
        patient_record = response.headers["Etag"]
        versionId = (json.loads(response.text))["meta"]["versionId"]

        # add the new dob to the patch, send the update and check the response
        update[0]["patch"]["patches"][0]["value"] = self.new_date
        update_response = helpers.update_patient(
            update[0]["patient"],
            patient_record,
            update[0]["patch"],
            self.headers
        )
        with check:
            assert update_response.text == ""
        helpers.check_response_status_code(update_response, 202)
        helpers.check_response_headers(update_response, self.headers)

        # send message poll request and check the response contains the updated attributes
        poll_message_response = helpers.poll_message(
            update_response.headers["content-location"],
            self.headers
        )

        with check:
            assert (json.loads(poll_message_response.text))["birthDate"] == self.new_date
        with check:
            assert int((json.loads(poll_message_response.text))["meta"]["versionId"]) == int(versionId) + 1
        helpers.check_response_status_code(poll_message_response, 200)

    def test_update_patient_with_missing_auth_header(self, headers):
        update_response = helpers.update_patient(
            update[1]["patient"],
            'W/"14"',
            update[1]["patch"],
            headers
        )
        helpers.check_retrieve_response_body(update_response, update[1]["response"])
        helpers.check_response_status_code(update_response, 401)
        helpers.check_response_headers(update_response, headers)

    def test_update_patient_with_blank_auth_header(self, headers):
        headers['authorization'] = ''
        update_response = helpers.update_patient(
            update[1]["patient"],
            'W/"14"',
            update[1]["patch"],
            headers
        )
        helpers.check_retrieve_response_body(update_response, update[1]["response"])
        helpers.check_response_status_code(update_response, 401)
        helpers.check_response_headers(update_response, headers)

    def test_update_patient_with_invalid_auth_header(self, headers):
        headers['authorization'] = 'Bearer abcdef123456789'
        update_response = helpers.update_patient(
            update[2]["patient"],
            'W/"14"',
            update[2]["patch"],
            headers
        )
        helpers.check_retrieve_response_body(update_response, update[2]["response"])
        helpers.check_response_status_code(update_response, 401)
        helpers.check_response_headers(update_response, headers)

    def test_update_patient_with_missing_urid_header(self, headers_with_token):
        self.headers.pop("NHSD-Session-URID")
        update_response = helpers.update_patient(
            update[3]["patient"],
            'W/"14"',
            update[3]["patch"],
            self.headers
        )
        helpers.check_retrieve_response_body(update_response, update[3]["response"])
        helpers.check_response_status_code(update_response, 400)
        helpers.check_response_headers(update_response, self.headers)

    def test_update_patient_with_blank_x_request_header(self, headers_with_token):
        self.headers["X-Request-ID"] = ''
        update_response = helpers.update_patient(
            update[4]["patient"],
            'W/"14"',
            update[4]["patch"],
            self.headers
        )
        helpers.check_retrieve_response_body(update_response, update[4]["response"])
        helpers.check_response_status_code(update_response, 400)
        self.headers.pop("X-Request-ID")
        helpers.check_response_headers(update_response, self.headers)

    def test_update_patient_with_invalid_x_request_header(self, headers_with_token):
        self.headers["X-Request-ID"] = '1234'
        update_response = helpers.update_patient(
            update[5]["patient"],
            'W/"14"',
            update[5]["patch"],
            self.headers
        )
        helpers.check_retrieve_response_body(update_response, update[5]["response"])
        helpers.check_response_status_code(update_response, 400)
        helpers.check_response_headers(update_response, self.headers)

    def test_update_patient_with_missing_x_request_header(self, headers_with_token):
        self.headers.pop("X-Request-ID")
        update_response = helpers.update_patient(
            update[6]["patient"],
            'W/"14"',
            update[6]["patch"],
            self.headers
        )
        helpers.check_retrieve_response_body(update_response, update[6]["response"])
        helpers.check_response_status_code(update_response, 412)
        helpers.check_response_headers(update_response, self.headers)
