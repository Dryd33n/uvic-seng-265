from typing import Optional

from clinic.note import Note
from clinic.patient_record import *


class Patient:
    def __init__(self,
                 phn: int,  # Patient Health Number
                 name: str,  # Patient Name
                 birthdate: str,  # Patient Birthdate
                 phone: str,  # Patient Phone Number
                 email: str,  # Patient Email
                 address: str):  # Patient Home Address
        self.phn = phn
        self.name = name
        self.birthdate = birthdate
        self.phone = phone
        self.email = email
        self.address = address
        self.record = PatientRecord()

    def __eq__(self, other):
        return (self.phn == other.phn and
                self.name == other.name and
                self.birthdate == other.birthdate and
                self.phone == other.phone and
                self.email == other.email and
                self.address == other.address)

    def __repr__(self):
        return (f"Patient: {self.name} #{self.phn} D.O.B: {self.birthdate}, Phone: {self.phone}, Email: {self.email}, "
                f"Address: {self.address}")

    def update(self,
               phn: int,  # Patient Health Number
               name: str,  # Patient Name
               birthdate: str,  # Patient Birthdate
               phone: str,  # Patient Phone Number
               email: str,  # Patient Email
               address: str):  # Patient Home Address
        self.phn = phn
        self.name = name
        self.birthdate = birthdate
        self.phone = phone
        self.email = email
        self.address = address

    def create_note(self, msg: str) -> Note:
        return self.record.create_note(msg)

    def search_note(self, code: int) -> Note:
        return self.record.search_note(code)

    def retrieve_notes(self, search: str) -> List[Note]:
        return self.record.retrieve_notes(search)

    def update_note(self, code: int, msg: str) -> bool:
        return self.record.update_note(code, msg)

    def delete_note(self, code: int) -> bool:
        return self.record.delete(code)

    def list_notes(self) -> List[Note]:
        return self.record.list_notes()
