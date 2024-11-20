import datetime


class Note:
    """
    Represents a note in the patient record.

    Class Attributes:
    - code: int                       Note code
    - text: str                       Note text
    - timeStamp: datetime.datetime    Time stamp of the note
    """

    def __init__(self, code: int, text: str):
        """
        Initializes a new note with the given code and text.
        :param code: Code of the note
        :param text: Message of the note
        """
        self.code = code
        self.text = text
        self.timeStamp = datetime.datetime.now()

    def __eq__(self, other) -> bool:
        """
        Compares two notes for equality.
        :param other: the other note to compare to
        :return: true if the notes have the same code and text, false otherwise
        """
        return (self.code == other.code
                and self.text == other.text)

    def __repr__(self) -> str:
        """
        Returns a string representation of the note.
        :return: string representation of the note
        """
        return f"Note ({self.code}) from {self.timeStamp}: {self.text}"

    def update_note(self, msg: str) -> None:
        """
        Updates the note with the given message.
        :param msg: the new message
        :return: None
        """
        self.text = msg
