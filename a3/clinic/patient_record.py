from typing import List

from clinic.note import Note


class PatientRecord:
    def __init__(self):
        self.autoCounter = 1
        self.records: List[Note] = []

    def __eq__(self, other):
        return (self.autoCounter == other.autoCounter
                and self.records == other.records)

    def __repr__(self):
        return f"Patient Record with {len(self.records)} notes, auto-counter: {self.autoCounter}"

    def create_note(self, msg: str) -> Note:
        self.records.insert(0, (n := Note(self.autoCounter, msg)))
        self.autoCounter += 1
        return n

    def search_note(self, code: int) -> Note:
        note = next((n for n in self.records if n.code == code), None)

        return note

    def retrieve_notes(self, search: str) -> List[Note]:
        return sorted([n for n in self.records if (search in n.text)], key=lambda n: n.code)

    def update_note(self, code: int, msg: str) -> bool:
        note = self.search_note(code)

        if note:
            note.update_note(msg)
            return True
        else:
            return False

    def delete(self, code: int) -> bool:
        note = self.search_note(code)

        if note:
            self.records.remove(note)
            self.autoCounter -= 1
            return True
        else:
            return False

    def list_notes(self) -> List[Note]:
        return self.records


