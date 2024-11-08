from typing import List, Union, Optional, Dict
import hashlib
import os

from clinic.note import Note
from clinic.patient import Patient

from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException


def sha256_hash(input_string: str) -> str:
    # Convert the input string to bytes, then hash it
    sha256 = hashlib.sha256(input_string.encode())
    # Return the hexadecimal representation of the hash
    return sha256.hexdigest()


def load_users(path: str) -> Dict[str, str]:
    users = {}

    with open(path, 'r') as file:
        for line in file:
            user, password = line.strip().split(',')
            users[user] = password
        return users


class Controller:
    """
    Controller class for the clinic system.
    This class is responsible for managing the users, patients, and notes.

    Class Attributes:
    - isLogged: bool:            True if the user is logged in, False otherwise.
    - currentUser: str:          The username of the current user.
    - users: dict:               A dictionary of usernames and passwords.
    - patients: List[Patient]:   A list of patients.
    - currentPatient: Patient:   The current patient.
    """

    def __init__(self, autosave=False):
        """
        Initialize the controller with the default values.
        :param autosave: 
        """
        self.autosave = None
        self.isLogged = False
        self.currentUser = None
        self.users = load_users('../clinic/users.txt')
        self.patients: List[Patient] = []
        self.currentPatient: Patient = None

    def __repr__(self):
        """
        Returns a string representation of the controller.
        :return: string representation of the controller
        """
        rv = f"Controller with {len(self.patients)} patients\n"
        rv += (f"Currently Logged in as {self.currentUser}\n\n"
               if self.isLogged
               else "Not Logged in\n\n")
        rv += (f"Current Patient: {self.currentPatient.name}\n"
               if self.currentPatient
               else "No Current Patient \n")
        rv += "---------------------------------------------------------\n"
        for p in self.patients:
            rv += f"{p}\n"
        return rv

    def logout(self) -> bool:
        """
        Log out the current user if they are logged in.
        :return: bool: True if the user was logged out, False otherwise.
        """
        if self.isLogged:
            self.isLogged = False
            self.currentUser = None
            return True
        else:
            raise InvalidLogoutException

    def login(self, user: str, pwd_in: str) -> bool:
        """
        Log in the user if the username and password are correct.
        :param user:    The username to log in.
        :param pwd_in:  The password to log in.
        :return:        True if the user was logged in, False otherwise.
        """
        if self.isLogged:
            raise DuplicateLoginException

        # Assign password to variable and check if user exists
        if (password := self.users.get(user)) is None:
            raise InvalidLoginException
        elif password == sha256_hash(pwd_in):
            self.currentUser = user
            self.isLogged = True
            return True
        else:
            raise InvalidLoginException

    def is_logged(self) -> bool:
        """
        Check if the user is logged in.
        :return: true if the user is logged in, false otherwise.
        """
        return self.isLogged

    def create_patient(self, phn: int, name: str, dob: str, phone: str, email: str, addr: str) -> Optional[Patient]:
        """
        Create a new patient and add it to the list of patients.
        :param phn:     Patient Health Number
        :param name:    Patient Name
        :param dob:     Patient Birthdate
        :param phone:   Patient Phone Number
        :param email:   Patient Email
        :param addr:    Patient Home Address
        :return:        The created patient or None if the user is not logged in or the PHN is already in use.
        """
        # Not logged in guard case
        if not self.isLogged: raise IllegalAccessException
        # Phn already in use guard case
        if phn in [p.phn for p in self.patients]: raise IllegalOperationException

        patient_info = (phn, name, dob, phone, email, addr)  # pack patient info into tuple
        p = Patient(*patient_info)
        self.patients.append(p)
        return p

    def retrieve_patients(self, name_search: str) -> Optional[List[Patient]]:
        """
        Retrieve patients with the name search token in their name.
        :param name_search: The token to search for in the patient names.
        :return:            A list of patients with the name search token in their name or None if the user is not logged in.
        """
        # not logged in guard case
        if not self.isLogged: raise IllegalAccessException

        # return patients with name search token in their name if logged in
        return [p for p in self.patients if name_search in p.name]

    def search_patient(self, phn: int) -> Optional[Patient]:
        """
        Search for a patient with the given PHN.
        :param phn: The PHN to search for.
        :return:    The patient with the given PHN or None if the user is not logged in.
        """
        # not logged in guard case
        if not self.isLogged: raise IllegalAccessException

        # return patient with given phn if logged in
        return next((p for p in self.patients if p.phn == phn), None)

    def update_patient(self, phn: int,
                       new_phn: int,
                       new_name: str,
                       new_dob: str,
                       new_phone: str,
                       new_email: str,
                       new_addr: str) -> bool:
        """
        Update the patient with the given PHN.
        :param phn:         The PHN of the patient to update.
        :param new_phn:     The new PHN of the patient.
        :param new_name:    The new name of the patient.
        :param new_dob:     The new date of birth of the patient.
        :param new_phone:   The new phone number of the patient.
        :param new_email:   The new email of the patient.
        :param new_addr:    The new address of the patient.
        :return:            True if the patient was updated, False otherwise.
        """
        # not logged in guard case
        if not self.isLogged: raise IllegalAccessException
        # phn of patient to update is not found guard case
        if (phn not in [p.phn for p in self.patients]
                # new phn in use guard case
                or any(new_phn == p_.phn for p_ in self.patients if p_.phn != phn)
                # updating current patient guard case
                or (self.currentPatient is not None and phn == self.currentPatient.phn)
        ): raise IllegalOperationException

        new_info = (new_phn, new_name, new_dob, new_phone, new_email, new_addr)
        self.search_patient(phn).update(*new_info)
        return True

    def delete_patient(self, phn: int) -> Optional[bool]:
        """
        Delete the patient with the given PHN.
        :param phn: The PHN of the patient to delete.
        :return:    True if the patient was deleted, False otherwise.
        """
        # not logged in guard case
        if not self.isLogged: raise IllegalAccessException
        # phn not found guard case
        if (phn not in [p.phn for p in self.patients]
                # deleting current patient guard case
                or (self.currentPatient is not None and phn == self.currentPatient.phn)
        ): raise IllegalOperationException

        # search for patient with given phn set none if patient is current patient
        patient = (self.search_patient(phn)
                   if (self.currentPatient is None or phn != self.currentPatient.phn)
                   else None)

        # if patient is not current patient and is found remove patient from list
        if patient:
            self.patients.remove(patient)
            return True
        else:
            return None

    def list_patients(self) -> Optional[List[Patient]]:
        """
        List all patients.
        :return: A list of all patients or None if the user is not logged in.
        """
        # not logged in guard case
        if not self.isLogged: raise IllegalAccessException

        return self.patients

    def get_current_patient(self) -> Optional[Patient]:
        """
        Get the current patient.
        :return: The current patient or None if the user is not logged in.
        """
        # not logged in guard case
        if not self.isLogged: raise IllegalAccessException

        return self.currentPatient

    def set_current_patient(self, phn: int) -> bool:
        """
        Set the current patient.
        :param phn: The PHN of the patient to set as the current patient.
        :return:    True if the patient was set as the current patient, False otherwise.
        """
        # not logged in guard case
        if not self.isLogged: raise IllegalAccessException
        # phn not found guard case
        if phn not in [p.phn for p in self.patients]: raise IllegalOperationException

        patient = self.search_patient(phn)

        if patient:
            self.currentPatient = patient
        else:
            return False

    def unset_current_patient(self) -> None:
        """
        Unset the current patient if logged in.
        :return: None
        """
        # not logged in guard case
        if not self.isLogged: raise IllegalAccessException

        self.currentPatient = None

    def create_note(self, msg: str) -> Optional[Note]:
        """
        Create a note for the current patient.
        :param msg: The message to create the note with.
        :return:    The created note or None if the user is not logged in or the current patient is not set.
        """
        self.check_logged_in_and_patient_set()

        return self.currentPatient.create_note(msg)

    def search_note(self, code: int) -> Optional[Note]:
        """
        Search for a note with the given code.
        :param code: The code of the note to search for.
        :return:     The note with the given code or None if the user is not logged in or the current patient is not set
        """
        self.check_logged_in_and_patient_set()

        return self.currentPatient.search_note(code)

    def retrieve_notes(self, search: str) -> List[Note]:
        """
        Retrieve notes with the search token in the message. :param search: The token to search for in the notes.
        :return:       A list of notes with the search token in the message or None if the user is not logged in or
                       the current patient is not set.
        """
        self.check_logged_in_and_patient_set()

        return self.currentPatient.retrieve_notes(search)

    def update_note(self, code: int, msg: str) -> bool:
        """
        Update the note with the given code.
        :param code: The code of the note to update.
        :param msg:  The message to update the note with.
        :return:     True if the note was updated, False otherwise.
        """
        self.check_logged_in_and_patient_set()

        return self.currentPatient.update_note(code, msg)

    def delete_note(self, code: int) -> bool:
        """
        Delete the note with the given code.
        :param code: The code of the note to delete.
        :return:     True if the note was deleted, False otherwise.
        """
        self.check_logged_in_and_patient_set()

        return self.currentPatient.delete_note(code)

    def list_notes(self) -> Optional[List[Note]]:
        """
        List all notes for the current patient.
        :return: A list of all notes for the current patient or None if the
        user is not logged in or the current patient is not set.
        """
        self.check_logged_in_and_patient_set()

        return self.currentPatient.list_notes()

    def check_logged_in_and_patient_set(self) -> None:
        """
        Check if the user is logged in and the current patient is set.
        :return: True if the user is logged in and the current patient is set, False otherwise.
        """
        # not logged in guard case
        if not self.isLogged: raise IllegalAccessException
        # no current patient guard case
        if self.currentPatient is None: raise NoCurrentPatientException
