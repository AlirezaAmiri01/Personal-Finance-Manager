from transaction import Transaction
from manager import Manager
from storage import save_transaction, load_transaction


def main_menu():

    print("===== WELCOME TO MENU =====\n")
    print("1.Add Income\n")
    print("2.Add Expense\n")
    print("3.Remove Transaction\n")
    print("4.Search Transaction\n")
    print("5.Show Transactions\n")
    print("0.Exit\n")


def show_menu():

    print("===== WELCOME TO SHOW MENU ======\n")
    print("1.Show Income\n")
    print("2.Show Expens\n")
    print("3.Show Balance\n")
    print("4.Show all\n")
    print("5.Cancel\n")


def main():

    manager = Manager()
    loading = load_transaction()
    for transaction in loading:
        manager.transactions.append(transaction)

    while True:
        main_menu()
        try:
            main_choice = int(input("Enter your choice: "))
        except ValueError:
            print("justr enter a number from 0 to 5")
            continue

        if main_choice == 1:
            title = input("Enter  your title: ")
            try:
                amount = float(input("Enter your amount: "))
            except ValueError:
                print("invalid value")
                continue

            transaction = Transaction(title, amount)
            manager.add_income(transaction)
            print("your transaction added")

        elif main_choice == 2:
            title = input("Enter  your title: ")
            try:
                amount = float(input("Enter your amount: "))
            except ValueError:
                print("invalid value")
                continue
            transaction = Transaction(title, amount)
            manager.add_expense(transaction)
            print("your transaction added")

        elif main_choice == 3:
            try:
                transaction_id = int(input("Enter an id: "))
            except ValueError:
                print("just enter a number")
            rm_transaction = manager.remove_transaction(transaction_id)
            if rm_transaction:
                print("Transaction removed")
            else:
                print("not found")

        elif main_choice == 4:

            try:
                transaction_id = int(input("Enter an id: "))
            except ValueError:
                print("just enter a number")
            search = manager.search_transaction(transaction_id)
            if search:
                print(search)
            else:
                print("Transaction not found")

        elif main_choice == 5:
            show_menu()
            try:
                show_choice = int(input("Enter a number from 1 to 5"))
            except ValueError:
                print("just Enter a number from 1 to 5")

            if show_choice == 1:
                show_incomes = manager.show_incomes()
                for transaction in show_incomes:
                    print(transaction)

            elif show_choice == 2:
                show_expenses = manager.show_expenses()
                for transaction in show_expenses:
                    print(transaction)

            elif show_choice == 3:
                show_balance = manager.show_balance()
                print(f"balance: {show_balance}")

            elif show_choice == 4:
                for transaction in show_all:
                    print(transaction)

                show_balance = manager.show_balance()
                print(f"\nBalance: {show_balance}")

            elif show_choice == 5:
                print("Cancled")
                continue

        elif main_choice == 0:
            print("bye")
            save_transaction(manager.transactions)
            break

        else:
            print("just enter a number from 0 to 5")


if __name__ == "__main__":
    main()
