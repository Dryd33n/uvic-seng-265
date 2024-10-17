import datetime


class Note:
    def __init__(self, code: int, text: str):
        self.code = code
        self.text = text
        self.timeStamp = datetime.datetime.now()

