from datetime import date


class Transaction:
    def __init__(self, title, amount):
        self.id = None
        self.title = title
        self.amount = amount
        self.type = ""
        self.created_at = date.today()

    def __str__(self):
        created = self.created_at.strftime("%Y/%m/%m/%d")
        return (
            f"\nid          : {self.id}\n"
            f"\ntitle       : {self.title}\n"
            f"\namount      : {self.amount}\n"
            f"\ntype        : {self.type}\n"
            f"\ncreated_at  : {created}\n"

        )
