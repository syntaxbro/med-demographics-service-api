error_responses = {
    "Missing Authorization header": {
        "resourceType": "OperationOutcome",
        "issue": [
            {
                "severity": "error",
                "code": "forbidden",
                "details": {
                    "coding": [
                        {
                            "system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode",
                            "version": "1",
                            "code": "ACCESS_DENIED",
                            "display": "Access Denied - Unauthorised"
                        }
                    ]
                },
                "diagnostics": "Missing Authorization header"
            }
        ]
    },
    "Empty Authorization header": {
        "resourceType": "OperationOutcome",
        "issue": [
            {
                "severity": "error",
                "code": "forbidden",
                "details": {
                    "coding": [
                        {
                            "system": "https://fhir.nhs.uk/R4/CodeSystem/Spine-ErrorOrWarningCode",
                            "version": "1",
                            "code": "ACCESS_DENIED",
                            "display": "Access Denied - Unauthorised"
                        }
                    ]
                },
                "diagnostics": "Empty Authorization header"
            }
        ]
    }
}
