import json
from typing import List

from clinic.patient import Patient


class PatientDecoder(json.JSONDecoder):
    """
    Custom JSON decoder for Patient objects.

    Decodes JSON objects into Patient instances if the object contains
    the '__type__' key set to 'Patient'. Uses an optional autosave feature
    for decoded Patient objects.
    """
    def __init__(self, autosave=False, *args, **kwargs):
        """
         Initializes the PatientDecoder.

         :param autosave: autosave If True, sets the autosave attribute for Patient instances created by this decoder.
         """
        self.autosave = autosave
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        """
        Converts a dictionary into a Patient object if it contains the
        appropriate '__type__' key.

        :param obj: The dictionary to decode.
        :return: Patient: A Patient instance if the dictionary represents a Patient
                 object, otherwise returns the original dictionary.
        """
        if '__type__' in obj and obj['__type__'] == 'Patient':
            # WHEN DECODER ENCOUNTERS PATIENT OBJECT
            return Patient(obj['phn'],
                           obj['name'],
                           obj['birthdate'],
                           obj['phone'],
                           obj['email'],
                           obj['address'],
                           autosave=self.autosave)

        return obj
