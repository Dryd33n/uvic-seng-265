from typing import List, Optional

from clinic.note import Note


class PatientRecord:
    """
    Represents a patient's record in the clinic.

    Class Attributes:
    - autoCounter: int      Auto-incrementing counter for note codes
    - records: List[Note]   List of notes in the patient
    """

    def __init__(self):
        """
        Initializes a new patient record with an empty list of notes and an auto-counter of 1.
        """
        self.autoCounter = 1
        self.records: List[Note] = []

    def __eq__(self, other) -> bool:
        """
        Compares two patient records for equality.
        :param other: the other patient record to compare to
        :return: true if the patient records have the same auto-counter and notes, false otherwise
        """
        return (self.autoCounter == other.autoCounter
                and self.records == other.records)

    def __repr__(self) -> str:
        """
        Returns a string representation of the patient record.
        :return: string representation of the patient record
        """
        return f"Patient Record with {len(self.records)} notes, auto-counter: {self.autoCounter}"

    def create_note(self, msg: str) -> Note:
        """
        Creates a new note with the given message and adds it to the patient record.
        :param msg: the message of the note
        :return: the new note
        """
        self.records.insert(0, (n := Note(self.autoCounter, msg)))
        self.autoCounter += 1
        return n

    def search_note(self, code: int) -> Optional[Note]:
        """
        Searches for a note with the given code in the patient record.
        :param code: the code of the note to search for
        :return: the note with the given code, or None if not found
        """
        note = next((n for n in self.records if n.code == code), None)

        return note

    def retrieve_notes(self, search: str) -> List[Note]:
        """
        Retrieves all notes that contain the given search string.
        :param search: the string to search for
        :return: sorted list of notes that contain the search string
        """
        return sorted([n for n in self.records if (search in n.text)], key=lambda n: n.code)

    def update_note(self, code: int, msg: str) -> bool:
        """
        Updates the note with the given code to have the new message.
        :param code: the code of the note to update
        :param msg: the new message for the note
        :return: true if the note was updated, false if the note was not found
        """
        note = self.search_note(code)

        if note:
            note.update_note(msg)
            return True
        else:
            return False

    def delete(self, code: int) -> bool:
        """
        Deletes the note with the given code.
        :param code: the code of the note to delete
        :return: true if the note was deleted, false if the note was not found
        """
        note = self.search_note(code)

        if note:
            self.records.remove(note)
            self.autoCounter -= 1
            return True
        else:
            return False

    def list_notes(self) -> List[Note]:
        """
        Lists all notes in the patient's record.
        :return: a list of all notes in the patient's record
        """
        return self.records


