import re
import sys
from datetime import datetime
from typing import Optional, List

from PyQt6 import QtGui
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QListWidgetItem

from clinic.controller import Controller
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.gui.create_note import Ui_create_note
from clinic.gui.create_patient import Ui_CreatePatient
from clinic.gui.edit_note import Ui_edit_note
from clinic.gui.edit_patient import Ui_EditPatient
from clinic.gui.login import Ui_Login
from clinic.gui.main_window import Ui_MainScreen
from clinic.gui.utils import count_digits, format_phone_number, format_date
from clinic.gui.warning import Ui_Warning
from clinic.note import Note
from clinic.patient import Patient

controller = Controller()
app = QApplication(sys.argv)


class LoginGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a central widget and set it for the main window
        self.main_window = None
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Set up the UI on the central widget
        self.ui = Ui_Login(self.central_widget)

        self.ui.pushButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.username_field.text()
        password = self.ui.password_field.text()
        try:
            # Try to log in using the provided credentials
            controller.login(username, password)
            self.switch_to_main_window()
        except InvalidLoginException:
            self.ui.login_message.setVisible(True)

    def switch_to_main_window(self):
        # Create the Main Window only after login succeeds
        self.main_window = MainGUI(self)
        self.main_window.setWindowTitle("Clinic - Manager")
        self.main_window.show()  # Show the main window
        self.hide()  # Hide the login window


class CreatePatientGUI(QMainWindow):
    def __init__(self, main_gui_window: 'MainGUI'):
        super().__init__()

        # Create a central widget and set it for the main window
        self.main_gui_window = main_gui_window
        self.main_window = None
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.resize(600, 700)

        # Set up the UI on the central widget
        self.ui = Ui_CreatePatient(self.central_widget)

        self.ui.phn_field.textChanged.connect(self.check_phn)
        self.ui.dob_field.textChanged.connect(self.check_dob)
        self.ui.phone_field.textChanged.connect(self.check_phone)
        self.ui.create_patient_btn.clicked.connect(self.create_patient)

        self.ui.create_patient_msg.setText("")

    def check_phn(self):
        phn = self.ui.phn_field.text().strip()

        try:
            phn = int(phn)
        except ValueError:
            self.ui.phn_field_message.setText("* phn must be numeric")
            self.ui.create_patient_msg.setText("fields with * require attention")
            return False

        if controller.search_patient(phn) is not None:
            self.ui.phn_field_message.setText("* phn must not already be in use")
            self.ui.create_patient_msg.setText("fields with * require attention")
            return False
        else:
            self.ui.phn_field_message.setText(" ")
            self.ui.create_patient_msg.setText("")
            return True

    def check_dob(self):
        dob = self.ui.dob_field.text()

        try:
            datetime.strptime(dob, "%Y-%m-%d")
            self.ui.dob_field_message.setText("")
            self.ui.create_patient_msg.setText("")
            return True
        except ValueError:
            self.ui.dob_field_message.setText("Invalid date format, use YYYY-MM-DD")
            self.ui.create_patient_msg.setText("fields with * require attention")
            return False

    def check_phone(self):
        phone = self.ui.phone_field.text()

        if count_digits(phone) != 10:
            self.ui.phone_field_msg.setText("* phone number must be 10 digits")
            self.ui.create_patient_msg.setText("fields with * require attention")
            return False
        else:
            self.ui.phone_field_msg.setText("")
            self.ui.create_patient_msg.setText("")
            return True

    def create_patient(self):
        phn = self.ui.phn_field.text().strip()
        name = self.ui.name_field.text().strip()
        dob = self.ui.dob_field.text().strip()
        email = self.ui.email_field.text().strip()
        phone = self.ui.phone_field.text().strip()
        address = self.ui.address_field.text().strip()

        if not (phn and name and dob and email and phone and address):
            self.ui.create_patient_msg.setText("Fields cannot be empty")
            return
        if not (self.check_phn() and self.check_dob() and self.check_phone()):
            return
        
        controller.create_patient(int(phn), name, dob, format_phone_number(phone), email, address)
        self.main_gui_window.handle_patient_search()
        self.close()


class EditPatientGUI(QMainWindow):
    def __init__(self, main_gui_window: 'MainGUI'):
        super().__init__()

        # Create a central widget and set it for the main window
        self.main_gui_window = main_gui_window
        self.main_window = None
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.resize(600, 700)

        # Set up the UI on the central widget
        self.ui = Ui_EditPatient(self.central_widget)

        self.ui.phn_field.textChanged.connect(self.check_phn)
        self.ui.dob_field.textChanged.connect(self.check_dob)
        self.ui.phone_field.textChanged.connect(self.check_phone)
        self.ui.edit_patient_button.clicked.connect(self.edit_patient)

        self.fill_old_details()

    def fill_old_details(self):
        patient = controller.get_current_patient()

        self.ui.old_phn_label.setText(str(patient.phn))
        self.ui.old_name_label.setText(patient.name)
        self.ui.old_dob_label.setText(patient.birthdate)
        self.ui.old_phone_label.setText(patient.phone)
        self.ui.old_email_label.setText(patient.email)
        self.ui.old_address_label.setText(patient.address)

    def check_phn(self):
        phn = self.ui.phn_field.text().strip()

        if not phn:
            self.ui.phn_field_message.setText("")
            self.ui.create_patient_msg.setText("")
            return True

        try:
            phn = int(phn)
        except ValueError:
            self.ui.phn_field_message.setText("* phn must be numeric")
            self.ui.create_patient_msg.setText("fields with * require attention")
            return False

        if not (controller.search_patient(phn) is None or phn == controller.get_current_patient().phn):
            self.ui.phn_field_message.setText("* phn must not already be in use")
            self.ui.create_patient_msg.setText("fields with * require attention")
            return False
        else:
            self.ui.phn_field_message.setText(" ")
            self.ui.create_patient_msg.setText("")
            return True

    def check_dob(self):
        dob = self.ui.dob_field.text()

        if not dob:
            self.ui.dob_field_message.setText("")
            self.ui.create_patient_msg.setText("")
            return True

        try:
            datetime.strptime(dob, "%Y-%m-%d")
            self.ui.dob_field_message.setText("")
            self.ui.create_patient_msg.setText("")
            return True
        except ValueError:
            self.ui.dob_field_message.setText("Invalid date format, use YYYY-MM-DD")
            self.ui.create_patient_msg.setText("fields with * require attention")
            return False

    def check_phone(self):
        phone = self.ui.phone_field.text()

        if not phone:
            self.ui.phone_field_msg.setText("")
            self.ui.create_patient_msg.setText("")
            return True

        if count_digits(phone) != 10:
            self.ui.phone_field_msg.setText("* phone number must be 10 digits")
            self.ui.create_patient_msg.setText("fields with * require attention")
            return False
        else:
            self.ui.phone_field_msg.setText("")
            self.ui.create_patient_msg.setText("")
            return True

    def edit_patient(self):
        phn = self.ui.phn_field.text().strip()
        name = self.ui.name_field.text().strip()
        dob = self.ui.dob_field.text().strip()
        email = self.ui.email_field.text().strip()
        phone = self.ui.phone_field.text().strip()
        address = self.ui.address_field.text().strip()

        if ((phn and not self.check_phn())
            or (dob and not self.check_dob())
            or (phone and not self.check_phone())):
            return

        if not phn:
            phn = controller.get_current_patient().phn
        if not name:
            name = controller.get_current_patient().name
        if not dob:
            dob = controller.get_current_patient().birthdate
        if not email:
            email = controller.get_current_patient().email
        if not phone:
            phone = controller.get_current_patient().phone
        if not address:
            address = controller.get_current_patient().address

        print(f"phn: {phn}, name: {name}, dob: {dob}, email: {email}, phone: {phone}, address: {address}")

        old_phn = controller.get_current_patient().phn
        controller.unset_current_patient()
        controller.update_patient(old_phn, int(phn), name, dob, format_phone_number(phone), email, address)
        controller.set_current_patient(int(phn))
        self.main_gui_window.fill_patient_details(controller.get_current_patient())
        self.main_gui_window.handle_patient_search()

        self.close()


class CreateNoteGUI(QMainWindow):
    def __init__(self, main_gui_window: 'MainGUI'):
        super().__init__()

        # Create a central widget and set it for the main window
        self.main_gui_window = main_gui_window
        self.main_window = None
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Set up the UI on the central widget
        self.ui = Ui_create_note(self.central_widget)

        self.ui.create_note_btn.clicked.connect(self.create_note)

    def create_note(self):
        note = self.ui.note_content_field.toPlainText().strip()

        if not note:
            self.ui.create_note_msg.setText("Note cannot be empty")
            return

        controller.create_note(note)
        self.main_gui_window.handle_record_search()
        self.close()


class EditNoteGUI(QMainWindow):
    def __init__(self, main_gui_window: 'MainGUI'):
        super().__init__()

        # Create a central widget and set it for the main window
        self.main_gui_window = main_gui_window
        self.main_window = None
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Set up the UI on the central widget
        self.ui = Ui_edit_note(self.central_widget)

        self.ui.create_note_btn.clicked.connect(self.edit_note)

    def edit_note(self):
        note = self.ui.note_content_field.toPlainText().strip()

        if not note:
            self.ui.edit_note_msg.setText("Note cannot be empty")
            return

        controller.update_note(self.main_gui_window.current_note.code, note)
        self.main_gui_window.handle_record_search()
        self.main_gui_window.fill_record_details(controller.search_note(self.main_gui_window.current_note.code))
        self.close()


class WarningGUI(QMainWindow):
    def __init__(self, message: str):
        super().__init__()

        # Create a central widget and set it for the main window
        self.main_window = None
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Set up the UI on the central widget
        self.ui = Ui_Warning(self.central_widget)

        self.ui.button.clicked.connect(self.close_window)

    def close_window(self):
        self.hide()


class MainGUI(QMainWindow):
    def __init__(self, login_window: 'LoginGUI'):
        super().__init__()
        # Create a central widget and set it for the main window
        self.edit_note_window = None
        self.edit_patient_window = None
        self.create_note_window = None
        self.current_note = None
        self.warning_window = None
        self.create_patient_window = None
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Set up the UI on the central widget
        self.ui = Ui_MainScreen(self.central_widget)
        self.setMinimumSize(800, 600)

        self.ui.main_create_patient_btn.clicked.connect(self.open_create_patient_gui)
        self.ui.edit_patient_btn.clicked.connect(self.open_edit_patient_gui)
        self.ui.logout_btn.clicked.connect(self.logout)
        self.ui.patient_search_field.textChanged.connect(self.handle_patient_search)
        self.ui.patient_list.itemClicked.connect(self.switch_current_patient)
        self.ui.delete_patient_btn.clicked.connect(self.delete_patient)
        self.ui.delete_patient_btn_2.clicked.connect(self.delete_patient)
        self.ui.record_search_field.textChanged.connect(self.handle_record_search)
        self.ui.create_patient_record_note_btn.clicked.connect(self.open_create_note)
        self.ui.edit_note_btn.clicked.connect(self.open_edit_note)
        self.ui.record_list.itemClicked.connect(self.switch_current_note)
        self.ui.delete_note_btn.clicked.connect(self.delete_note)

        self.login_window = login_window

        self.init_ui_components()

    def init_ui_components(self):
        self.handle_patient_search()
        self.fill_patient_details(None)
        self.fill_records([])
        self.fill_record_details(None)
        self.ui.record_search_message.setText("select patient first")

    def open_create_patient_gui(self):
        self.create_patient_window = CreatePatientGUI(self)
        self.create_patient_window.setWindowTitle("Clinic - Create Patient")
        self.create_patient_window.show()

    def open_edit_patient_gui(self):
        if controller.get_current_patient() is None:
            self.warning_window = WarningGUI("Cannot edit patient without selecting patient first, please select "
                                             "patient from search panel.")
            self.warning_window.setWindowTitle("Clinic - Warning")
            self.warning_window.show()
            return

        self.edit_patient_window = EditPatientGUI(self)
        self.edit_patient_window.setWindowTitle("Clinic - Edit Patient")
        self.edit_patient_window.show()

    def handle_patient_search(self):
        search_term = self.ui.patient_search_field.text()
        search_term.strip()

        # SEARCH TERM EMPTY - SHOW ALL PATIENTS
        if len(search_term) == 0:
            self.fill_patient_list(controller.list_patients())
            self.ui.patient_search_message.setText("showing all patients")
        # SEARCH TERM CONTAINS DIGIT - SEARCH BY PHN
        elif re.search(r'\d', search_term):
            patient = controller.search_patient(int(search_term))

            if patient:
                self.ui.patient_search_message.setText("patient with matching PHN found")
                self.fill_patient_list([patient])
            else:
                self.ui.patient_search_message.setText("no patient with mentioned PHN")
                self.fill_patient_list([])
        # SEARCH TERM CONTAINS STRING - SEARCH BY NAME
        else:
            patients = controller.retrieve_patients(search_term)
            self.ui.patient_search_message.setText(f"{len(patients)} matching patients found")
            self.fill_patient_list(patients)

    def fill_patient_list(self, patients: List[Patient]):
        # STYLING OPTIONS
        font = QFont()
        font.setFamilies([u"Montserrat"])
        icon = QIcon(QIcon.fromTheme(u"address-book-new"))

        self.ui.patient_list.clear()

        for patient in patients:
            item = QListWidgetItem(self.ui.patient_list)
            item.setFont(font)
            item.setIcon(icon)

            item.setText(patient.name)
            item.setData(32, patient)

    def fill_patient_details(self, patient: Optional[Patient]):
        if patient:
            # Parse the date
            date_obj = datetime.strptime(patient.birthdate, "%Y-%m-%d")
            dob = date_obj.strftime("%b %d, %Y").upper()
            dob = dob.replace(" 0", " ")

            self.ui.patient_details_title.setText(f"CURRENT PATIENT: {patient.name.upper()}")
            self.ui.patient_first_name.setText(patient.name)
            self.ui.patient_phn.setText(str(patient.phn))
            self.ui.patient_dob.setText(dob)
            self.ui.patient_phone_number.setText(patient.phone)
            self.ui.patient_email_address.setText(patient.email)
            self.ui.patient_home_address.setText(patient.address)
        else:
            self.ui.patient_details_title.setText(f"CURRENT PATIENT: NONE")
            self.ui.patient_first_name.setText(" ")
            self.ui.patient_phn.setText(" ")
            self.ui.patient_dob.setText(" ")
            self.ui.patient_phone_number.setText(" ")
            self.ui.patient_email_address.setText(" ")
            self.ui.patient_home_address.setText(" ")

    def switch_current_patient(self, item):
        patient = item.data(32)

        controller.unset_current_patient()
        controller.set_current_patient(patient.phn)
        self.fill_patient_details(patient)
        self.current_note = None
        self.ui.record_search_field.clear()
        self.handle_record_search()

    def delete_patient(self):
        if controller.get_current_patient() is None:
            self.warning_window = WarningGUI("Cannot delete patient without selecting patient first, please select "
                                             "patient from search panel.")
            self.warning_window.setWindowTitle("Clinic - Warning")
            self.warning_window.show()
            return

        patient = controller.get_current_patient()
        controller.unset_current_patient()
        self.fill_patient_details(None)
        controller.delete_patient(patient.phn)
        self.handle_patient_search()
        self.handle_record_search()
        self.fill_record_details(None)

    def handle_record_search(self):
        search_term = self.ui.record_search_field.text().strip()

        if controller.get_current_patient() is None:
            self.fill_records([])
            self.ui.record_search_message.setText("select patient first")
            return

        if len(search_term) == 0:
            self.fill_records(controller.list_notes())
            self.ui.record_search_message.setText("showing all records")
        else:
            try:
                code = int(search_term)
                note = controller.search_note(code)
                if note:
                    self.fill_records([note])
                    self.ui.record_search_message.setText("note found with matching code")
                else:
                    self.fill_records([])
                    self.ui.record_search_message.setText("no note with mentioned code")
            except ValueError:
                notes = controller.retrieve_notes(search_term)
                self.fill_records(notes)
                self.ui.record_search_message.setText(f"{len(notes)} matching notes found")

    def fill_records(self, records: List[Note]):
        font = QFont()
        font.setFamilies([u"Montserrat"])
        icon = QIcon(QIcon.fromTheme(u"format-justify-left"))

        self.ui.record_list.clear()

        for record in records:
            item = QListWidgetItem(self.ui.record_list)
            item.setFont(font)
            item.setIcon(icon)

            record_text = record.text
            if len(record_text) > 35:
                record_text = record_text[:32] + "..."

            item.setText(f"{record.code}: {record_text}")

            item.setData(32, record)

    def fill_record_details(self, record: Optional[Note]):
        if record:
            self.ui.note_content.setText(record.text)
            self.ui.note_number.setText(f"Note Number {record.code}")
            self.ui.note_date.setText(format_date(record.timeStamp))
        else:
            self.ui.note_number.setText(" ")
            self.ui.note_content.setText(" ")
            self.ui.note_date.setText(" ")

    def open_create_note(self):
        if controller.get_current_patient() is None:
            self.warning_window = WarningGUI("Cannot create note without selecting patient first, please select "
                                             "patient from search panel.")
            self.warning_window.setWindowTitle("Clinic - Warning")
            self.warning_window.show()
            return

        self.create_note_window = CreateNoteGUI(self)
        self.create_note_window.setWindowTitle("Clinic - Create Note")
        self.create_note_window.show()

    def open_edit_note(self):
        if self.current_note is None:
            self.warning_window = WarningGUI("Cannot edit note without selecting note first, please select "
                                             "note from search panel.")
            self.warning_window.setWindowTitle("Clinic - Warning")
            self.warning_window.show()
            return

        self.edit_note_window = EditNoteGUI(self)
        self.edit_note_window.setWindowTitle("Clinic - Edit Note")
        self.edit_note_window.ui.note_content_field.setPlainText(self.current_note.text)
        self.edit_note_window.show()

    def delete_note(self):
        if self.current_note is None:
            self.warning_window = WarningGUI("Cannot delete note without selecting note first, please select "
                                             "note from search panel.")
            self.warning_window.setWindowTitle("Clinic - Warning")
            self.warning_window.show()
            return

        controller.delete_note(self.current_note.code)
        self.handle_record_search()
        self.fill_record_details(None)


    def logout(self):
        # When logging out, destroy the main window and return to the login window
        controller.isLogged = False
        self.login_window.ui.username_field.clear()
        self.login_window.ui.password_field.clear()
        self.close()  # Close the MainGUI
        self.login_window.show()  # Show the LoginGUI again

    def switch_current_note(self, item):
        note = item.data(32)
        self.current_note = note
        self.fill_record_details(note)





def main():
    font = QFont("Montserrat", 10)
    app.setFont(font)

    QtGui.QFontDatabase.addApplicationFont("./clinic/gui/content/fonts/Montserrat-VariableFont_wght.ttf")
    QtGui.QFontDatabase.addApplicationFont("./clinic/gui/content/fonts/Montserrat-Italic-VariableFont_wght.ttf")

    login_window = LoginGUI()
    login_window.setWindowTitle("Clinic - Login")
    login_window.show()

    sys.exit(app.exec())
