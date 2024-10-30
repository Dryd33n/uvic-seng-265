from typing import List, Union, Optional

from clinic.patient import Patient


class Controller:

    def __init__(self):
        self.isLogged = False
        self.currentUser = None
        self.users = {"user": "clinic2024"}
        self.patients: List[Patient] = []
        self.currentPatient: Patient = None

    def logout(self):
        if self.isLogged:
            self.isLogged = False
            self.currentUser = None
            return True
        else:
            return False

    def login(self, user: str, pwd_in: str) -> bool:
        if self.isLogged:
            return False

        if (password := self.users.get(user)) is None:
            return False
        elif password == pwd_in:
            self.currentUser = user
            self.isLogged = True
            return True

    def is_logged(self):
        return self.isLogged

    def create_patient(self,
                       phn: int,
                       name: str,
                       dob: str,
                       phone: str,
                       email: str,
                       addr: str) -> Optional[Patient]:
        if (not self.isLogged or
                phn in [p.phn for p in self.patients]):
            return None

        patientInfo = (phn, name, dob, phone, email, addr)
        p = Patient(*patientInfo)
        self.patients.append(p)
        return p

    def retrieve_patients(self, name_search: str) -> Optional[List[Patient]]:
        if not self.isLogged:
            return None

        return [p for p in self.patients if name_search in p.name]

    def search_patient(self, phn: int) -> Optional[Patient]:
        if not self.isLogged:
            return None

        return next((p for p in self.patients if p.phn == phn), None)

    def update_patient(self,
                       phn: int,
                       new_phn: int,
                       new_name: str,
                       new_dob: str,
                       new_phone,
                       new_email,
                       new_addr):
        if not self.isLogged and self.patients is None:
            return False


                                            # ensure new phn is not already in use except by the updated patient
        patient = (self.search_patient(phn) if (not any(new_phn == p_.phn for p_ in self.patients if p_.phn != phn)
                                            # ensure iterated patient is not current patient
                                            and (self.currentPatient is None or phn != self.currentPatient.phn))
                                            else None)

        if patient:
            new_info = (new_phn, new_name, new_dob, new_phone, new_email, new_addr)
            patient.update(*new_info)
            return True
        else:
            return False

    def delete_patient(self, phn: int) -> Optional[bool]:
        if not self.isLogged:
            return False

        patient = self.search_patient(phn) if (self.currentPatient is None or phn != self.currentPatient.phn) else None

        if patient:
            self.patients.remove(patient)
            return True
        else:
            return None

    def list_patients(self):
        if self.isLogged:
            return self.patients

    def get_current_patient(self):
        if self.isLogged:
            return self.currentPatient

    def set_current_patient(self, phn: int):
        if not self.isLogged:
            return False

        patient = self.search_patient(phn)

        if patient:
            self.currentPatient = patient
        else:
            return False

    def unset_current_patient(self):
        if self.isLogged:
            self.currentPatient = None

    def create_note(self, param):
        pass

    def search_note(self, param):
        pass

    def retrieve_notes(self, param):
        pass

    def delete_note(self, param):
        pass

    def list_notes(self):
        pass

    def update_note(self, param, param1):
        pass
