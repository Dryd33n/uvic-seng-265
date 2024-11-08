import unittest
from unittest import TestCase
from clinic.note import Note


class NoteTest(TestCase):
    def test_update_note(self):
        note_1 = Note(1, "TEST NOTE 1")
        rnote_1 = Note(1, "TEST NOTE 1 UPDATED")
        note_2 = Note(2, "TEST NOTE 2")
        rnote_2 = Note(2, "TEST NOTE 2 UPDATED")

        note_1.update_note("TEST NOTE 1 UPDATED")
        self.assertEqual(note_1, rnote_1, "Note Successfully updated")
        note_2.update_note("TEST NOTE 2 UPDATED")
        self.assertEqual(note_2, rnote_2, "Note Successfully updated")


if __name__ == '__main__':
    unittest.main()
