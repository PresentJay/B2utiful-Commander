class fhir:
    def __str__(self):
        return self

    def __init__(self):
        self.resource = resource()


class resource(fhir):
    def __str__(self):
        return self

    def __init__(self, *args, **kwar1gs):
        # Individuals
        self.Patient = "Patient"
        self.Practitioner = "Practitioner"
        self.PractitionerRole = "PractitionerRole"
        self.Person = "Person"
        self.RelatedPerson = "RelatedPerson"

        # Entitles
        self.Organization = "Organization"
        self.Location = "Location"

        # Terminology
        self.CodeSystem = "CodeSystem"
        self.ValueSet = "ValueSet"

        # Conformance
        self.SearchParameter = "SearchParameter"

        # Summary
        self.Procedure = "Procedure"
        self.Condition = "Condition"

        # Diagnostics
        self.Observation = "Observation"

        # Management
        self.Encounter = "Encounter"

        # Medication
        self.Medication = "Medication"

        # Security
        self.Consent = "Consent"


class http(fhir):
    def __init__(self):
        # [FHIR HTTP]
        self.Search = "Search"
        self.Read = "Read"
        self.History = "History"
        self.Create = "Create"
        self.Delete = "Delete"
        self.Update = "Update"

    def __str__(self):
        return self
