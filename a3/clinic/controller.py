from typing import List, Union, Optional

from clinic.patient import Patient

class Controller:

    def __init__(self):
        self.isLogged = False
        self.currentUser = None
        self.users = {"user": "clinic2024"}
        self.patients: List[Patient] = []

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

        retrieved_list: List[Patient] = []

        for pat in self.patients:
            if name_search in pat.name:
                retrieved_list.append(pat)

        return retrieved_list

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

        if ((p := self.search_patient(phn)) is not None and
            new_phn not in [pat.phn for pat in self.patients if pat.phn != phn]):

            new_info = (new_phn, new_name, new_dob, new_phone, new_email, new_addr)
            p.update(*new_info)
            return True

        return False



    def get_current_patient(self):
        pass

    def list_patients(self):
        pass

    def delete_patient(self, param):
        pass

    def search_patient(self, phn: int) -> Optional[Patient]:
        for p in self.patients:
            if p.phn == phn:
                return p

        return None



    def set_current_patient(self, param):
        pass

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
