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

    def get_phn(self) -> int:
        return self.phn