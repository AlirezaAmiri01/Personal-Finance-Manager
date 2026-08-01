import customtkinter as ctk
from ui.styles import *
from utils.validators import validate_title, validate_amount


class EditTransaction(ctk.CTkFrame):
    def __init__(self, parent, manager, app, transaction):
        super().__init__(parent, fg_color=BACKGROUND)

        self.manager = manager
        self.app = app
        self.transaction = transaction

        self.create_widgets()

    # --------------
    # widgets
    # -------------
    def create_widgets(self):

        self.title_label = ctk.CTkLabel(
            self,
            text="Edit Transaction",
            font=TITLE_FONT,
            text_color=TEXT
        )
        self.title_label.pack(pady=(30, 20))

        form = ctk.CTkFrame(self, fg_color="transparent")
        form.pack()

        ctk.CTkLabel(
            form,
            text="Title:",
            font=TEXT_FONT,
            text_color=TEXT
        ).grid(row=0, column=0, sticky="w", padx=(0, 15), pady=10)

        self.title_entry = ctk.CTkEntry(form, width=300, height=40)
        self.title_entry.grid(row=0, column=1, pady=10)
        self.title_entry.insert(0, self.transaction.title)

        ctk.CTkLabel(
            form,
            text="Amount:",
            font=TEXT_FONT,
            text_color=TEXT
        ).grid(row=1, column=0, sticky="w", padx=(0, 15), pady=10)

        self.amount_entry = ctk.CTkEntry(form, width=300, height=40)
        self.amount_entry.grid(row=1, column=1, pady=10)
        self.amount_entry.insert(0, str(self.transaction.amount))

        self.save_button = ctk.CTkButton(
            self,
            text="Save Changes",
            command=self.save_changes,
            fg_color=BUTTON,
            hover_color=BUTTON_HOVER,
            width=180,
            height=40
        )
        self.save_button.pack(pady=25)

        self.message_label = ctk.CTkLabel(
            self,
            text="",
            font=TEXT_FONT,
            text_color=SECONDARY_TEXT
        )
        self.message_label.pack()

    # ------------
    # save
    # -----------

    def save_changes(self):
        title = self.title_entry.get()
        amount = self.amount_entry.get()

        if not validate_title(title):
            self.message_label.configure(
                text="Invalid title", text_color=ERROR_TEXT)
            return

        if not validate_amount(amount):
            self.message_label.configure(
                text="Invalid amount", text_color=ERROR_TEXT)
            return

        amount = float(amount)

        result = self.manager.update_transaction(
            self.transaction.id, title, amount)

        if result:
            self.message_label.configure(
                text="Updated successfully",
                text_color=SUCCESS_TEXT
            )

        else:
            self.message_label.configure(
                text="This transaction can't be updated",
                text_color=ERROR_TEXT
            )
