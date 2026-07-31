import customtkinter as ctk
from ui.styles import *


class InfoCard(ctk.CTkFrame):

    def __init__(self, parent, title, value):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18,
            border_width=1,
            border_color=BORDER
        )

        self.title = title
        self.value = value

        self.build_card()

        self.bind("<Enter>", lambda e: self.configure(fg_color=CARD_HOVER))

        self.bind("<Leave>", lambda e: self.configure(fg_color=CARD))

    # -----------------
    # build card
    # -----------------

    def build_card(self):

        self.title_label = ctk.CTkLabel(
            self,
            text=self.title,
            font=SUBTITLE_FONT,
            text_color=TEXT
        )

        self.title_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(15, 10)
        )

        separator = ctk.CTkFrame(self, height=1, fg_color=BORDER)

        separator.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=5
        )

        self.value_label = ctk.CTkLabel(
            self,
            text=str(self.value),
            font=TITLE_FONT,
            text_color=TEXT
        )

        self.value_label.grid(
            row=2,
            column=0,
            sticky="w",
            padx=20,
            pady=(10, 15)
        )

    # -----------------
    # update value
    # -----------------

    def update_value(self, new_value):

        self.value_label.configure(text=str(new_value))


class TransactionCard(ctk.CTkFrame):

    def __init__(self, parent, transaction, manager, app,):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=18,
            border_width=1,
            border_color=BORDER
        )
        self.manager = manager
        self.app = app

        self.transaction = transaction

        self.create_widgets()

        self.bind_hover()

    # -----------------
    # hover
    # -----------------

    def bind_hover(self):

        self.bind("<Enter>", lambda e: self.configure(fg_color=CARD_HOVER))

        self.bind("<Leave>", lambda e: self.configure(fg_color=CARD))

    # -----------------
    # widgets
    # -----------------

    def create_widgets(self):

        self.grid_columnconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text=self.transaction.title,
            font=SUBTITLE_FONT,
            text_color=TEXT
        )

        self.title_label.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            padx=20,
            pady=(15, 15)
        )

        separator = ctk.CTkFrame(self, height=1, fg_color=BORDER)
        separator.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=20,
            pady=(0, 10)
        )

        labels = [

            ("ID:", self.transaction.id),

            ("Amount:", f"${self.transaction.amount}"),

            ("Type:", self.transaction.type),

            ("Date:", self.transaction.created_at.strftime("%Y/%m/%d"))
        ]

        for row, (name, value) in enumerate(labels, start=2):

            ctk.CTkLabel(
                self,
                text=name,
                font=LABEL_FONT,
                text_color=SECONDARY_TEXT
            ).grid(
                row=row,
                column=0,
                sticky="w",
                padx=20,
                pady=5
            )

            value_color = TEXT

            if name == "Amount:" or name == "Type:":
                if self.transaction.type == "Income":
                    value_color = SUCCESS
                else:
                    value_color = ERROR

            ctk.CTkLabel(
                self,
                text=value,
                font=TEXT_FONT,
                text_color=value_color
            ).grid(
                row=row,
                column=1,
                sticky="w",
                padx=20,
                pady=5
            )

        self.delete_button = ctk.CTkButton(
            self,
            text="Delete",
            command=self.delete_transaction,
            fg_color=ERROR_TEXT,
            hover_color=ERROR
        )

        self.delete_button.grid(
            row=len(labels)+2,
            column=1,
            padx=20,
            pady=15,
            sticky="e"
        )

        self.grid_rowconfigure(len(labels)+3, minsize=10)

    def delete_transaction(self):

        self.manager.remove_transaction(self.transaction.id)
        self.destroy()
