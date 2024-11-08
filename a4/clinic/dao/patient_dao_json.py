from abc import ABC
from pathlib import Path
from typing import List

from clinic.dao.patient_decoder import PatientDecoder
from clinic.dao.patient_encoder import PatientEncoder
from clinic.dao.patient_dao import PatientDAO
import json
import os


class PatientDAOJSON(PatientDAO):

    def __init__(self, auto_save=False):
        self.auto_save = auto_save
        self.json_path = '../clinic/patients.json'

    def search_patient(self, key):
        if self.auto_save:
            pass

    def create_patient(self, patient):
        patients = self.list_patients()
        patients.append(patient)
        self.write_patients(patients)

    def retrieve_patients(self, search_string):
        pass

    def update_patient(self, key, patient):
        pass

    def delete_patient(self, key):
        patients = self.list_patients()
        patients.remove(next((p for p in patients if key == p.phn), None))
        self.write_patients(patients)

    def list_patients(self):
        if Path(self.json_path).stat().st_size > 0:
            with open(self.json_path, 'r') as file:
                print("READING")
                patients = json.load(file, cls=PatientDecoder)
                return patients
        else:
            return []

    def write_patients(self, patients: List['Patient']):
        try:
            with open(self.json_path, 'w') as file:
                json.dump(patients, file, indent=4, cls=PatientEncoder)
                file.flush()  # Ensure data is written to disk
                os.fsync(file.fileno())  # Ensure data is written to disk
        except Exception as e:
            print(f"Error writing to file: {e}")
