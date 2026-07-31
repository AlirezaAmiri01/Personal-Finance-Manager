import customtkinter as ctk
from utils.validators import validate_amount, validate_title
from transaction import Transaction
from ui.styles import *


class AddExpense(ctk.CTkFrame):
    def __init__(self, parent, manager, app):
        super().__init__(parent, fg_color=BACKGROUND)

        self.manager = manager
        self.app = app

        self.create_widgets()

    # ----------------
    # widgets
    # ---------------

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(
            self,
            text="Add Expense",
            font=TITLE_FONT,
            text_color=TEXT
        )
        self.title_label.pack(pady=30)

        self.title_entry = ctk.CTkEntry(self, placeholder_text="Title")
        self.title_entry.pack(padx=30, pady=10)

        self.amount_entry = ctk.CTkEntry(self, placeholder_text="Amount")
        self.amount_entry.pack(padx=30, pady=10)

        self.save_button = ctk.CTkButton(
            self, text="Save", command=self.save_expense)
        self.save_button.pack(pady=20)

        self.message_label = ctk.CTkLabel(
            self,
            text="",
            font=TEXT_FONT,
            text_color=SECONDARY_TEXT
        )
        self.message_label.pack(pady=15)

    # ---------------
    # save expense
    # ---------------

    def save_expense(self):
        title = self.title_entry.get()

        amount = self.amount_entry.get()

        if not self.validate_inputs(title, amount):
            return

        amount = float(amount)

        transaction = Transaction(title, amount)
        transaction.type = "Expense"

        success = self.manager.add_expense(transaction)

        if success:
            self.clear_inputs()

            self.message_label.configure(
                text="Expense added successfully",
                text_color=SUCCESS_TEXT
            )

        else:
            self.message_label.configure(
                text="Not enough balance",
                text_color=ERROR_TEXT
            )

    # ---------------------
    # validation inputs
    # --------------------

    def validate_inputs(self, title, amount):
        if not validate_title(title):
            self.message_label.configure(
                text="Invalid title", text_color=ERROR_TEXT)
            return False

        if not validate_amount(amount):
            self.message_label.configure(
                text="Invalid amount", text_color=ERROR_TEXT)
            return False

        return True

    # ----------------
    # clear inputs
    # ---------------

    def clear_inputs(self):
        self.title_entry.delete(0, "end")
        self.amount_entry.delete(0, "end")
