import json
from typing import List

from clinic.patient import Patient


def object_hook(obj):

    if '__type__' in obj and obj['__type__'] == 'Patient':
    # WHEN DECODER ENCOUNTERS PATIENT OBJECT
        return Patient(obj['phn'],
                       obj['name'],
                       obj['birthdate'],
                       obj['phone'],
                       obj['email'],
                       obj['address'],)

    return obj


class PatientDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=object_hook, *args, **kwargs)

