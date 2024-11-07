import unittest
from unittest import TestCase
from clinic.patient import Patient


class PatientTest(TestCase):

    def test_patient_update(self):
        expected_patient_0 = Patient(0, "-1", "-1", "-1", "-1",
                                     "-1")
        expected_patient_1 = Patient(1, "Patient 1", "DOB 1", "Phone 1", "Email 1",
                                     "Address 1")
        expected_patient_2 = Patient(2, "Patient 2", "DOB 2", "Phone 2", "Email 2",
                                     "Address 2")
        expected_patient_3 = Patient(3, "Patient 3", "DOB 3", "Phone 3", "Email 3",
                                     "Address 3")

        expected_patient_0.update(1, "Patient 1", "DOB 1", "Phone 1", "Email 1",
                                     "Address 1")
        self.assertEqual(expected_patient_0, expected_patient_1)
        expected_patient_0.update(2, "Patient 2", "DOB 2", "Phone 2", "Email 2",
                                  "Address 2")
        self.assertEqual(expected_patient_0, expected_patient_2)
        expected_patient_0.update(3, "Patient 3", "DOB 3", "Phone 3", "Email 3",
                                  "Address 3")
        self.assertEqual(expected_patient_0, expected_patient_3)


if __name__ == '__main__':
    unittest.main()
