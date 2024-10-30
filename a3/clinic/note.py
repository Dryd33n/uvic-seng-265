import datetime


class Note:
    def __init__(self, code: int, text: str):
        self.code = code
        self.text = text
        self.timeStamp = datetime.datetime.now()

    def __eq__(self, other):
        return (self.code == other.code
                and self.text == other.text)

    def __repr__(self):
        return f"Note ({self.code}) from {self.timeStamp}: {self.text}"

    def update_note(self, msg: str):
        self.text = msg
