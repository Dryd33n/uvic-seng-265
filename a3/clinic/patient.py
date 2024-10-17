from clinic.patient_record import *

class Patient:
    def __init__(self,
                 phn: int,        # Patient Health Number
                 name: str,       # Patient Name
                 birthdate: str,  # Patient Birthdate
                 phone: str,      # Patient Phone Number
                 email: str,      # Patient Email
                 address: str):   # Patient Home Address
        self.phn = phn
        self.name = name
        self.birthdate = birthdate
        self.phone = phone
        self.email = email
        self.address = address
        self.record = PatientRecord()
