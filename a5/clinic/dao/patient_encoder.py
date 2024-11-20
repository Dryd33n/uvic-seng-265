import json
from json import JSONEncoder

from clinic.patient import Patient


class PatientEncoder(JSONEncoder):
    """
    Custom JSON encoder for Patient objects.

    Encodes Patient instances by converting them to a dictionary containing
    key attributes. Falls back to default JSON encoding for non-Patient objects.
    """

    def default(self, obj):
        """
        Converts a Patient object into a JSON-serializable dictionary.

        :param obj:   The object to encode.
        :return: Dictionary with Patient attributes if obj is a Patient. Otherwise, returns the default encoding.
        """
        if isinstance(obj, Patient):
            return {'__type__': "Patient",
                    'phn': obj.phn,
                    'name': obj.name,
                    'birthdate': obj.birthdate,
                    'phone': obj.phone,
                    'email': obj.email,
                    'address': obj.address}

        return super().default(obj)
