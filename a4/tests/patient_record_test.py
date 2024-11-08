import unittest
from unittest import TestCase

from clinic.note import Note
from clinic.patient_record import PatientRecord


# noinspection DuplicatedCode
class PatientRecordTest(TestCase):

    def setUp(self) -> None:
        self.patient_record = PatientRecord()

    def test_create_note(self):
        expected_note_1 = Note(1, "Note 1")
        expected_note_2 = Note(2, "Note 2")
        expected_note_3 = Note(3, "Note 3")

        self.assertEqual(expected_note_1, self.patient_record.create_note("Note 1"))
        self.assertEqual(expected_note_2, self.patient_record.create_note("Note 2"))
        self.assertEqual(expected_note_3, self.patient_record.create_note("Note 3"))

    def test_search_note(self):
        expected_note_1 = Note(1, "Note 1")
        expected_note_2 = Note(2, "Note 2")
        expected_note_3 = Note(3, "Note 3")

        self.assertIsNone(self.patient_record.search_note(1))

        self.assertEqual(expected_note_1, self.patient_record.create_note("Note 1"))
        self.assertEqual(expected_note_2, self.patient_record.create_note("Note 2"))
        self.assertEqual(expected_note_3, self.patient_record.create_note("Note 3"))

        self.assertEqual(expected_note_1, self.patient_record.search_note(1))
        self.assertEqual(expected_note_2, self.patient_record.search_note(2))
        self.assertEqual(expected_note_3, self.patient_record.search_note(3))

        self.assertIsNone(self.patient_record.search_note(0))

    def test_retrieve_notes(self):
        expected_note_1 = Note(1, "Note 1")
        expected_note_2 = Note(2, "Note 2")
        expected_note_3 = Note(3, "Note 3")
        expected_note_4 = Note(4, "Note 4")
        expected_note_5 = Note(5, "Note 5")

        self.assertTrue(len(self.patient_record.retrieve_notes("Note")) == 0)

        self.assertEqual(expected_note_1, self.patient_record.create_note("Note 1"))
        self.assertTrue(len(self.patient_record.retrieve_notes("Note")) == 1)
        self.assertEqual(expected_note_2, self.patient_record.create_note("Note 2"))
        self.assertTrue(len(self.patient_record.retrieve_notes("Note")) == 2)
        self.assertEqual(expected_note_3, self.patient_record.create_note("Note 3"))
        self.assertTrue(len(self.patient_record.retrieve_notes("Note")) == 3)
        self.assertEqual(expected_note_4, self.patient_record.create_note("Note 4"))
        self.assertTrue(len(self.patient_record.retrieve_notes("Note")) == 4)
        self.assertEqual(expected_note_5, self.patient_record.create_note("Note 5"))
        self.assertTrue(len(self.patient_record.retrieve_notes("Note")) == 5)

        self.assertTrue(len(self.patient_record.retrieve_notes("False")) == 0)

        self.assertTrue(len(self.patient_record.retrieve_notes("1")) == 1)
        self.assertTrue(len(self.patient_record.retrieve_notes("2")) == 1)
        self.assertTrue(len(self.patient_record.retrieve_notes("3")) == 1)
        self.assertTrue(len(self.patient_record.retrieve_notes("4")) == 1)
        self.assertTrue(len(self.patient_record.retrieve_notes("5")) == 1)

        retrieved_notes = self.patient_record.retrieve_notes("Note")
        self.assertEqual(expected_note_1, retrieved_notes[0])
        self.assertEqual(expected_note_2, retrieved_notes[1])
        self.assertEqual(expected_note_3, retrieved_notes[2])
        self.assertEqual(expected_note_4, retrieved_notes[3])
        self.assertEqual(expected_note_5, retrieved_notes[4])

    def test_update_note(self):
        expected_note_1 = Note(1, "Note 1")
        expected_note_2 = Note(2, "Note 2")
        expected_note_3 = Note(3, "Note 3")
        expected_note_4 = Note(4, "Note 4")
        expected_note_5 = Note(5, "Note 5")

        self.assertFalse(self.patient_record.update_note(1, "NO NOTES ADDED"))

        self.assertEqual(expected_note_1, self.patient_record.create_note("Note 1"))
        self.assertEqual(expected_note_2, self.patient_record.create_note("Note 2"))
        self.assertEqual(expected_note_3, self.patient_record.create_note("Note 3"))
        self.assertEqual(expected_note_4, self.patient_record.create_note("Note 4"))
        self.assertEqual(expected_note_5, self.patient_record.create_note("Note 5"))

        expected_note_1 = Note(1, "Note 1 Updated")
        expected_note_2 = Note(2, "Note 2 Updated")
        expected_note_3 = Note(3, "Note 3 Updated")
        expected_note_4 = Note(4, "Note 4 Updated")
        expected_note_5 = Note(5, "Note 5 Updated")

        self.assertTrue(self.patient_record.update_note(1, "Note 1 Updated"))
        self.assertEqual(expected_note_1, self.patient_record.search_note(1))
        self.assertTrue(self.patient_record.update_note(2, "Note 2 Updated"))
        self.assertEqual(expected_note_2, self.patient_record.search_note(2))
        self.assertTrue(self.patient_record.update_note(3, "Note 3 Updated"))
        self.assertEqual(expected_note_3, self.patient_record.search_note(3))
        self.assertTrue(self.patient_record.update_note(4, "Note 4 Updated"))
        self.assertEqual(expected_note_4, self.patient_record.search_note(4))
        self.assertTrue(self.patient_record.update_note(5, "Note 5 Updated"))
        self.assertEqual(expected_note_5, self.patient_record.search_note(5))

        self.assertFalse(self.patient_record.update_note(-1, "NOTE DOESN'T EXIST"))

    def test_delete_note(self):
        expected_note_1 = Note(1, "Note 1")
        expected_note_2 = Note(2, "Note 2")
        expected_note_3 = Note(3, "Note 3")
        expected_note_4 = Note(4, "Note 4")
        expected_note_5 = Note(5, "Note 5")

        self.assertFalse(self.patient_record.delete(1))

        self.assertEqual(expected_note_1, self.patient_record.create_note("Note 1"))
        self.assertEqual(expected_note_2, self.patient_record.create_note("Note 2"))
        self.assertEqual(expected_note_3, self.patient_record.create_note("Note 3"))
        self.assertEqual(expected_note_4, self.patient_record.create_note("Note 4"))
        self.assertEqual(expected_note_5, self.patient_record.create_note("Note 5"))

        self.assertFalse(self.patient_record.delete(-1))

        self.assertTrue(self.patient_record.delete(1))
        self.assertIsNone(self.patient_record.search_note(1))
        self.assertTrue(len(self.patient_record.list_notes()) == 4)
        self.assertTrue(self.patient_record.delete(2))
        self.assertIsNone(self.patient_record.search_note(2))
        self.assertTrue(len(self.patient_record.list_notes()) == 3)
        self.assertTrue(self.patient_record.delete(3))
        self.assertIsNone(self.patient_record.search_note(3))
        self.assertTrue(len(self.patient_record.list_notes()) == 2)
        self.assertTrue(self.patient_record.delete(4))
        self.assertIsNone(self.patient_record.search_note(4))
        self.assertTrue(len(self.patient_record.list_notes()) == 1)
        self.assertTrue(self.patient_record.delete(5))
        self.assertIsNone(self.patient_record.search_note(5))
        self.assertTrue(len(self.patient_record.list_notes()) == 0)

        self.assertFalse(self.patient_record.delete(1))
        self.assertFalse(self.patient_record.delete(2))
        self.assertFalse(self.patient_record.delete(3))
        self.assertFalse(self.patient_record.delete(4))
        self.assertFalse(self.patient_record.delete(5))

    def tests_list_notes(self):
        expected_note_1 = Note(1, "Note 1")
        expected_note_2 = Note(2, "Note 2")
        expected_note_3 = Note(3, "Note 3")
        expected_note_4 = Note(4, "Note 4")
        expected_note_5 = Note(5, "Note 5")

        self.assertTrue(len(self.patient_record.list_notes()) == 0)

        self.assertEqual(expected_note_1, self.patient_record.create_note("Note 1"))
        self.assertEqual(expected_note_2, self.patient_record.create_note("Note 2"))
        self.assertEqual(expected_note_3, self.patient_record.create_note("Note 3"))
        self.assertEqual(expected_note_4, self.patient_record.create_note("Note 4"))
        self.assertEqual(expected_note_5, self.patient_record.create_note("Note 5"))

        retrieved_notes = self.patient_record.list_notes()
        self.assertTrue(len(self.patient_record.list_notes()) == 5)
        self.assertEqual(expected_note_1, retrieved_notes[4])
        self.assertEqual(expected_note_2, retrieved_notes[3])
        self.assertEqual(expected_note_3, retrieved_notes[2])
        self.assertEqual(expected_note_4, retrieved_notes[1])
        self.assertEqual(expected_note_5, retrieved_notes[0])




if __name__ == '__main__':
    unittest.main()
