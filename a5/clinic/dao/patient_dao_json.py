from abc import ABC
from pathlib import Path
from typing import List

from clinic.dao.patient_decoder import PatientDecoder
from clinic.dao.patient_encoder import PatientEncoder
from clinic.dao.patient_dao import PatientDAO
import json
import os

from clinic.patient import Patient


class PatientDAOJSON(PatientDAO):
    """
    This class handles the CRUD operations necessary for storing patients in the json file, should
    only be one instance of this class handling all patient info
    """

    def __init__(self, auto_save=False):
        """
        Create a new patient dao json object.

        Class Attributes:
        - autosave: bool:   Whether the implementation is using persistence or not
        - json_path: str:   Path to the json file containing patients

        :param auto_save: whether the system is using persistence or not
        """
        self.auto_save = auto_save
        self.json_path = 'clinic/patients.json'
        self.init_file()

    def search_patient(self, key) -> None:
        """
        I chose not to implement this method to avoid repeating code since the
        same result is achieved by reusing the code in the patient class except
        modifying the patients that are searched through by using the list_patients()
        method.

        :param key: key of patient to be search
        """
        pass  # METHOD NOT NEEDED FOR IMPLEMENTATION

    def create_patient(self, patient: Patient) -> None:
        """
        creates a new patient by doing the following:
        Gets all the patients, appends a new patient and writes all patients to json

        :param patient: patient to add
        """
        patients = self.list_patients()
        patients.append(patient)
        self.write_patients(patients)

    def retrieve_patients(self, search_string: str) -> None:
        """
        I chose not to implement this method to avoid repeating code since the
        same result is achieved by reusing the code in the patient class except
        modifying the patients that are searched through by using the list_patients()
        method.

        :param search_string: search string to compare to names in list of patients
        :return: None
        """
        pass  # METHOD NOT NEEDED FOR IMPLEMENTATION

    def update_patient(self, key: int, patient: Patient) -> None:
        """
        Updates a given patient by doing the following:
        gets all patients, uses a list comprehension to replace patient with matching phn
        write the new list to the json file

        :param key:     phn of patient to update
        :param patient: patient containing new patient info
        """
        patients = self.list_patients()
        new_patients = [patient if key == p.phn else p for p in patients]
        self.write_patients(new_patients)

    def delete_patient(self, key: int) -> None:
        """
        Deletes a given patient by doing the following:
        get all patients, uses a generator to find specific patient to remove, remove patient from list
        write new patients to json file

        :param key: phn of patient to delete
        """
        patients = self.list_patients()
        patients.remove(next((p for p in patients if key == p.phn), None))
        self.write_patients(patients)

    def list_patients(self) -> List[Patient]:
        """
        Returns a list containing all patients in json file, reads and decodes json file

        :return: list of all patients
        """
        # If File is not empty
        if Path(self.json_path).stat().st_size > 0:
            # Open file
            with open(self.json_path, 'r') as file:
                # Read Json Data Using PatientDecoder
                patients = json.load(file, cls=PatientDecoder, autosave=self.auto_save)
                return patients
        else:
            return []

    def write_patients(self, patients: List[Patient]) -> None:
        """
        Write a list of patients to the json file

        :param patients: list of patients to be written
        """
        # Open File
        with open(self.json_path, 'w') as file:
            # Write Json Data Using PatientEncoder
            json.dump(patients, file, cls=PatientEncoder)

    def init_file(self) -> None:
        """
        creates the patient json file if it does not exist yet
        """
        # If File Doesn't Exist Yet
        if not os.path.exists(self.json_path):
            # Create the file
            with open(self.json_path, 'w') as file:
                pass
