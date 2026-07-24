import csv
from pathlib import Path
from transaction import Transaction
from datetime import date

FILE_PATH = Path(__file__).parent/"transaction.csv"


def save_transaction(transactions):
    with FILE_PATH.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "id",
            "title",
            "type",
            "amount",
            "date"
        ])

        for transaction in transactions:
            writer.writerow([
                transaction.id,
                transaction.title,
                transaction.type,
                transaction.amount,
                transaction.created_at.isoformat()

            ])


def load_transaction():
    transactions = []

    if not FILE_PATH.exists():
        with FILE_PATH.open("w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "id",
                "title",
                "type",
                "amount",
                "date"
            ])

    with FILE_PATH.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            transaction = Transaction(
                title=row[1],
                amount=float(row[3])
            )
            transaction.id = int(row[0])
            transaction.type = row[2]
            transaction.created_at = date.fromisoformat(row[4])

            transactions.append(transaction)

        return transactions
