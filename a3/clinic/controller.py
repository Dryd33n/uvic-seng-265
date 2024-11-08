from typing import List, Union, Optional

from clinic.note import Note
from clinic.patient import Patient


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

    def __init__(self):
        """
        Initialize the controller with the default values.
        """
        self.isLogged = False
        self.currentUser = None
        self.users = {"user": "clinic2024"}
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
            return False

    def login(self, user: str, pwd_in: str) -> bool:
        """
        Log in the user if the username and password are correct.
        :param user:    The username to log in.
        :param pwd_in:  The password to log in.
        :return:        True if the user was logged in, False otherwise.
        """
        if self.isLogged:
            return False

        # Assign password to variable and check if user exists
        if (password := self.users.get(user)) is None:
            return False
        elif password == pwd_in:
            self.currentUser = user
            self.isLogged = True
            return True

    def is_logged(self) -> bool:
        """
        Check if the user is logged in.
        :return: true if the user is logged in, false otherwise.
        """
        return self.isLogged

    def create_patient(self, phn: int, name: str, dob: str, phone: str,  email: str, addr: str) -> Optional[Patient]:
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
        if (not self.isLogged                           # is not logged in
            or phn in [p.phn for p in self.patients]):  # or phn is already in use
            return None

        patientInfo = (phn, name, dob, phone, email, addr)  # pack patient info into tuple
        p = Patient(*patientInfo)
        self.patients.append(p)
        return p

    def retrieve_patients(self, name_search: str) -> Optional[List[Patient]]:
        """
        Retrieve patients with the name search token in their name.
        :param name_search: The token to search for in the patient names.
        :return:            A list of patients with the name search token in their name or None if the user is not logged in.
        """
        # return patients with name search token in their name if logged in
        return ([p for p in self.patients if name_search in p.name]
                if self.isLogged
                else None)

    def search_patient(self, phn: int) -> Optional[Patient]:
        """
        Search for a patient with the given PHN.
        :param phn: The PHN to search for.
        :return:    The patient with the given PHN or None if the user is not logged in.
        """
        # return patient with given phn if logged in
        return (next((p for p in self.patients if p.phn == phn), None)
                if self.isLogged
                else None)

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
        # guard clause to ensure user is logged in there are patients
        if not self.isLogged and self.patients is None:
            return False

        patient = (self.search_patient(phn)
                       # ensure new phn is not already in use except by the updated patient
                   if (not any(new_phn == p_.phn for p_ in self.patients if p_.phn != phn)
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
        """
        Delete the patient with the given PHN.
        :param phn: The PHN of the patient to delete.
        :return:    True if the patient was deleted, False otherwise.
        """
        if not self.isLogged:
            return False

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
        return (self.patients
                if self.isLogged
                else None)

    def get_current_patient(self) -> Optional[Patient]:
        """
        Get the current patient.
        :return: The current patient or None if the user is not logged in.
        """
        return (self.currentPatient
                if self.isLogged
                else None)

    def set_current_patient(self, phn: int) -> bool:
        """
        Set the current patient.
        :param phn: The PHN of the patient to set as the current patient.
        :return:    True if the patient was set as the current patient, False otherwise.
        """
        if not self.isLogged:
            return False

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
        if self.isLogged:
            self.currentPatient = None

    def create_note(self, msg: str) -> Optional[Note]:
        """
        Create a note for the current patient.
        :param msg: The message to create the note with.
        :return:    The created note or None if the user is not logged in or the current patient is not set.
        """
        return (self.currentPatient.create_note(msg)
                if self.logged_and_patient_set()
                else None)

    def search_note(self, code: int) -> Optional[Note]:
        """
        Search for a note with the given code.
        :param code: The code of the note to search for.
        :return:     The note with the given code or None if the user is not logged in or the current patient is not set
        """
        return (self.currentPatient.search_note(code)
                if self.logged_and_patient_set()
                else None)

    def retrieve_notes(self, search: str) -> Optional[List[Note]]:
        """
        Retrieve notes with the search token in the message. :param search: The token to search for in the notes.
        :return:       A list of notes with the search token in the message or None if the user is not logged in or
                       the current patient is not set.
        """
        return (self.currentPatient.retrieve_notes(search)
                if self.logged_and_patient_set()
                else None)

    def update_note(self, code: int, msg: str) -> bool:
        """
        Update the note with the given code.
        :param code: The code of the note to update.
        :param msg:  The message to update the note with.
        :return:     True if the note was updated, False otherwise.
        """
        return (self.currentPatient.update_note(code, msg)
                if self.logged_and_patient_set()
                else False)

    def delete_note(self, code: int) -> bool:
        """
        Delete the note with the given code.
        :param code: The code of the note to delete.
        :return:     True if the note was deleted, False otherwise.
        """
        return (self.currentPatient.delete_note(code)
                if self.logged_and_patient_set()
                else False)

    def list_notes(self) -> Optional[List[Note]]:
        """
        List all notes for the current patient.
        :return: A list of all notes for the current patient or None if the
        user is not logged in or the current patient is not set.
        """
        return (self.currentPatient.list_notes()
                if self.logged_and_patient_set()
                else None)

    def logged_and_patient_set(self) -> bool:
        """
        Check if the user is logged in and the current patient is set.
        :return: True if the user is logged in and the current patient is set, False otherwise.
        """
        return self.isLogged and (self.currentPatient is not None)
