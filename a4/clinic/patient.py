from typing import Optional

from clinic.dao.patient_dao import PatientDAO
from clinic.note import Note
from clinic.patient_record import *


class Patient:
    """
    Represents a patient in the clinic.

    Class Attributes:
    - phn: int          Patient Health Number
    - name: str         Patient Name
    - birthdate: str    Patient Birthdate
    - phone: str        Patient Phone Number
    - email: str        Patient Email
    - address: str      Patient Home Address
    """

    def __init__(self,
                 phn: int,        # Patient Health Number
                 name: str,       # Patient Name
                 birthdate: str,  # Patient Birthdate
                 phone: str,      # Patient Phone Number
                 email: str,      # Patient Email
                 address: str,    # Patient Home Address
                 autosave=False):
        """
        Initializes a new patient with the given information.
        :param phn:         Patient Health Number
        :param name:        Patient Name
        :param birthdate:   Patient Birthdate
        :param phone:       Patient Phone Number
        :param email:       Patient Email
        :param address:     Patient Home Address
        """
        self.phn = phn
        self.name = name
        self.birthdate = birthdate
        self.phone = phone
        self.email = email
        self.address = address
        self.record = PatientRecord(autosave=autosave, phn=phn)

    def __eq__(self, other):
        """
        Compares two patients for equality.
        :param other: other patient to compare to
        :return: true if the patients all attributes match,  false otherwise
        """
        return (self.phn == other.phn and
                self.name == other.name and
                self.birthdate == other.birthdate and
                self.phone == other.phone and
                self.email == other.email and
                self.address == other.address)

    def __repr__(self):
        """
        Returns a string representation of the patient.
        :return: string representation of the patient
        """
        return (f"Patient: {self.name}, {self.phn} D.O.B: {self.birthdate}, Phone: {self.phone}, Email: {self.email}, "
                f"Address: {self.address}")

    def update(self,
               phn: int,  # Patient Health Number
               name: str,  # Patient Name
               birthdate: str,  # Patient Birthdate
               phone: str,  # Patient Phone Number
               email: str,  # Patient Email
               address: str):  # Patient Home Address
        """
        Updates the patient's information.
        :param phn:         Patient Health Number
        :param name:        Patient Name
        :param birthdate:   Patient Birthdate
        :param phone:       Patient Phone Number
        :param email:       Patient Email
        :param address:     Patient Home Address
        :return:            None
        """
        self.phn = phn
        self.name = name
        self.birthdate = birthdate
        self.phone = phone
        self.email = email
        self.address = address

    def create_note(self, msg: str) -> Note:
        """
        Creates a new note on the patient's record.
        :param msg: the note message
        :return: the created note
        """
        return self.record.create_note(msg)

    def search_note(self, code: int) -> Note:
        """
        Searches for a note with the given code.
        :param code: the note code
        :return: the note that was found
        """
        return self.record.search_note(code)

    def retrieve_notes(self, search: str) -> List[Note]:
        """
        Retrieves all notes that contain the given search string.
        :param search: the search string
        :return: a list of notes that contain the search string
        """
        return self.record.retrieve_notes(search)

    def update_note(self, code: int, msg: str) -> bool:
        """
        Updates the note with the given code.
        :param code: the note code
        :param msg: the new note message
        :return: true if the note was updated, false otherwise
        """
        return self.record.update_note(code, msg)

    def delete_note(self, code: int) -> bool:
        """
        Deletes the note with the given code.
        :param code: the note code
        :return: true if the note was deleted, false otherwise
        """
        return self.record.delete(code)

    def list_notes(self) -> List[Note]:
        """
        Lists all notes in the patient's record.
        :return: a list of all notes in the patient's record
        """
        return self.record.list_notes()
