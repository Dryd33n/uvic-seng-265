from abc import ABC, abstractmethod
from typing import List



class PatientDAO(ABC):

    @abstractmethod
    def create_patient(self, patient):
        pass

    @abstractmethod
    def retrieve_patients(self, search_string):
        pass

    @abstractmethod
    def update_patient(self, key, patient):
        pass

    @abstractmethod
    def delete_patient(self, key):
        pass

    @abstractmethod
    def list_patients(self) -> List['Patient']:
        pass

    @abstractmethod
    def search_patient(self, key):
        pass
