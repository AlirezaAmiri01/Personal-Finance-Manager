class Manager:

    def __init__(self):
        self.transactions = []
        self.next_id = 1
        self.balance = 0

    def add_income(self, transaction):
        transaction.id = self.next_id
        self.next_id += 1
        if transaction.amount > 0:
            self.transactions.append(transaction)
            self.balance += transaction.amount
            transaction.type = "income"
            return True
        else:
            return False

    def add_expense(self, transaction):
        transaction.id = self.next_id
        self.next_id += 1
        if transaction.amount > 0 and transaction.amount <= self.balance:
            self.transactions.append(transaction)
            self.balance -= transaction.amount
            transaction.type = "expense"
            return True
        else:
            return False

    def show_incomes(self):
        incomes_list = []
        for transaction in self.transactions:
            if transaction.type == "income":
                incomes_list.append(transaction)
        return incomes_list

    def show_expenses(self):
        expenses_list = []
        for transaction in self.transactions:
            if transaction.type == "expense":
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
                if transaction.type == "income":
                    self.balance -= transaction.amount
                else:
                    self.balance += transaction.amount
                return True
        return False
