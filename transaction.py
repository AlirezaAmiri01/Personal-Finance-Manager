from datetime import date


class Transaction:
    def __init__(self, title, amount):
        self.id = None
        self.title = title
        self.amount = amount
        self.type = ""
        self.created_at = date.today()
