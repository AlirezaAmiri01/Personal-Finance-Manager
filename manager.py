
from storage import save_transaction, load_transaction


class Manager:

    def __init__(self):
        self.transactions = load_transaction()
        if self.transactions:
            self.next_id = max(
                transaction.id for transaction in self.transactions)+1

        else:
            self.next_id = 1

        self.balance = 0
        for transaction in self.transactions:
            if transaction.type == "Income":
                self.balance += transaction.amount
            else:
                self.balance -= transaction.amount

    def add_income(self, transaction):
        if transaction.amount > 0:
            transaction.id = self.next_id
            self.next_id += 1

            self.transactions.append(transaction)
            self.balance += transaction.amount
            transaction.type = "Income"
            self.save()
            print("save")
            return True

        return False

    def add_expense(self, transaction):
        if transaction.amount > 0 and transaction.amount <= self.balance:

            transaction.id = self.next_id
            self.next_id += 1

            self.transactions.append(transaction)
            self.balance -= transaction.amount
            transaction.type = "Expense"
            self.save()
            return True

        return False

    def show_incomes(self):
        incomes_list = []
        for transaction in self.transactions:
            if transaction.type == "Income":
                incomes_list.append(transaction)
        return incomes_list

    def show_expenses(self):
        expenses_list = []
        for transaction in self.transactions:
            if transaction.type == "Expense":
                expenses_list.append(transaction)
        return expenses_list

    def show_balance(self):
        return self.balance

    def show_all(self):
        return self.transactions

    def search_transaction(self, transaction_id):
        for transaction in self.transactions:
            if transaction.id == transaction_id:
                return transaction
        return None

    def remove_transaction(self, transaction_id):

        for transaction in self.transactions:

            if transaction.id == transaction_id:

                self.transactions.remove(transaction)

                if transaction.type == "Income":
                    self.balance -= transaction.amount
                else:
                    self.balance += transaction.amount

                self.save()

                return True

        return False

    def update_transaction(self, transaction_id, new_title, new_amount):

        for transaction in self.transactions:

            if transaction.id == transaction_id:

                old_amount = transaction.amount

                if transaction.type == "Income":

                    new_balance = self.balance - old_amount + new_amount

                    if new_balance < 0:
                        return False

                    self.balance = new_balance

                else:

                    available_balance = self.balance + old_amount

                    if new_amount > available_balance:
                        return False

                    self.balance = available_balance - new_amount

                transaction.title = new_title
                transaction.amount = new_amount

                self.save()

                return True

        return False

    def save(self):
        save_transaction(self.transactions)

    def reset_data(self):
        self.transactions.clear()
        self.balance = 0
        self.next_id = 1
        self.save()
        return True
