from abc import ABC, abstractmethod


class NoteDAO(ABC):

    @abstractmethod
    def create_note(self, text) -> None:
        pass

    @abstractmethod
    def retrieve_notes(self, search_string) -> None:
        pass

    @abstractmethod
    def update_note(self, key, text):
        pass

    @abstractmethod
    def delete_note(self, key):
        pass

    @abstractmethod
    def list_notes(self):
        pass

    @abstractmethod
    def search_note(self, key):
        pass
