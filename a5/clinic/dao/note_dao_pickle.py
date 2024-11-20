import os
import pickle
from pathlib import Path
from typing import List

from clinic.dao.note_dao import NoteDAO
from clinic.note import Note


class NoteDAOPickle(NoteDAO):
    """
    This class handles the CRUD operations necessary for storing patient notes in binary files using
    the pickle library, this class should be instantiated once patient and each respective class is
    used to handle it's respective patient data file
    """

    def __init__(self, phn: int):
        """
        Initializes the Note Dao Pickly class with default values

        Class Attributes:
        - records_path: str:    Path to directory containing records
        - phn: str:             PHN of patient which instantiated this object
        - note_path: str:       Path to respective file containing note data

        :param phn: PHN of patient that instantiated this class
        """
        self.records_path = "clinic/records"
        self.phn = phn
        self.note_path = self.records_path + '/' + str(self.phn) + '.dat'
        self.init_note()

    def __repr__(self):
        """
        Returns a string representation of the object
        :return: string representation of the object
        """
        return f"Note Pickle Object for patient: {self.phn}"

    def create_note(self, text: str) -> None:
        """
        Creates a new note by getting all notes, appending new note and then writing updated
        list of notes

        :param text: message of note to be created
        """
        notes = self.list_notes()
        notes.insert(0, (Note(self.count_notes() + 1, text)))
        self.write_notes(notes)

    def retrieve_notes(self, search_string: str):
        """
        I chose not to implement this method to avoid repeating code since the same effect can
        be achieved by reusing code from the patient_record retrieve notes method by simply modifying
        the notes which are search through.

        :param search_string: text to be searched for in notes
        """
        pass  # METHOD NOT NEEDED FOR IMPLEMENTATION

    def update_note(self, key: int, text: str) -> None:
        """
        Updates a specific note by getting all notes then getting reference to specific note and then
        updating its message respectively.

        :param key:  code of note to be modified
        :param text: text to update not with
        """
        notes = self.list_notes()
        note = next((n for n in notes if n.code == key), None)

        note.text = text

        self.write_notes(notes)

    def delete_note(self, key: str) -> None:
        """
        Deletes a specific note by using list comprehension to remove note with matching key
        then writes the update list

        :param key: code of note to be deleted
        """
        notes = [n for n in self.list_notes() if n.code != key]
        self.write_notes(notes)

    def list_notes(self) -> List[Note]:
        """
        Returns a list of all the notes for the given patient

        :return: a list containing all notes of a patient
        """
        # If file is not empty
        if Path(self.note_path).stat().st_size > 0:
            # Open File
            with open(self.note_path, 'rb') as file:
                # Read contents using pickle
                return pickle.load(file)
        else:
            return []

    def search_note(self, key):
        """
        I chose not to implement this method to avoid repeating code since the same effect can
        be achieved by reusing code from the patient_record retrieve notes method by simply modifying
        the notes which are search through.

        :param key: key of note to search for
        """
        pass

    def write_notes(self, notes: List[Note]):
        """
        Writes a list of note to a patients respective pickle file

        :param notes: list of notes to be written
        """
        with open(self.note_path, 'wb') as file:
            pickle.dump(notes, file)

    def init_note(self):
        """
        Create note file if it has not already been created
        """
        files = os.listdir(self.records_path)
        filenames = [f.split('.')[0] for f in files]

        # If file does not exist yet
        if str(self.phn) not in filenames:
            # Create new file by opening file in write mode
            with open(self.note_path, 'wb') as file:
                pass

    def count_notes(self) -> int:
        """
        Returns the number of notes in the patients note file
        :return: number of notes in given patient note file
        """
        return len(self.list_notes())
