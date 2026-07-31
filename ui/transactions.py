import customtkinter as ctk
from ui.widgets import TransactionCard
from ui.styles import *


class TransactionsPage(ctk.CTkFrame):

    def __init__(self, parent, manager, app):

        super().__init__(parent, fg_color=BACKGROUND)

        self.manager = manager
        self.app = app

        self.create_widgets()

    # ----------
    # widgets
    # ----------

    def create_widgets(self):

        self.title_label = ctk.CTkLabel(
            self,
            text="Transactions",
            font=TITLE_FONT,
            text_color=TEXT
        )
        self.title_label.pack(anchor="w", padx=30, pady=(30, 20))

        # -----------------------------------
        # search: frame,entry,button
        # -----------------------------------

        self.search_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.search_frame.pack(fill="x", padx=30, pady=(0, 20))
        self.search_frame.grid_columnconfigure(0, weight=1)

        self.search_message = ctk.CTkLabel(
            self,
            text="",
            font=TEXT_FONT,
            text_color=SECONDARY_TEXT
        )

        self.search_message.pack(pady=(0, 10))

        self.search_entry = ctk.CTkEntry(
            self.search_frame,
            placeholder_text="Transaction ID...",
            corner_radius=15,
            height=40
        )

        self.search_entry.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0, 10)
        )

        self.search_button = ctk.CTkButton(
            self.search_frame,
            text="Search",
            command=self.search_transaction,
            corner_radius=15,
            fg_color=BUTTON,
            hover_color=BUTTON_HOVER,
            width=100,
            height=40
        )

        self.search_button.grid(
            row=0,
            column=1,
            padx=(0, 10)
        )

        self.show_all_button = ctk.CTkButton(
            self.search_frame,
            text="Show All",
            command=self.show_transactions,
            corner_radius=15,
            fg_color=BUTTON,
            hover_color=BUTTON_HOVER,
            width=100,
            height=40
        )

        self.show_all_button.grid(
            row=0,
            column=2
        )

        # ---------------------
        # scrollabele frme
        # ---------------------

        self.list_frame = ctk.CTkScrollableFrame(
            self,
            fg_color=BACKGROUND,
            corner_radius=15
        )
        self.list_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 30)
        )

        self.show_transactions()

    # -------------
    # search func
    # --------------

    def clear_transactions(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()

    def search_transaction(self):

        self.clear_transactions()

        self.search_message.configure(text="")

        keyword = self.search_entry.get().strip()

        if keyword == "":
            self.search_message.configure(
                text="Please enter a transaction ID.",
                text_color=SECONDARY_TEXT
            )
            return

        if not keyword.isdigit():
            self.search_message.configure(
                text="Transaction ID must be a number.",
                text_color=ERROR_TEXT
            )
            return

        transaction = self.manager.search_transaction(int(keyword))

        if transaction is None:
            self.search_message.configure(
                text="No transaction found.",
                text_color=SECONDARY_TEXT
            )
            return

        card = TransactionCard(
            self.list_frame,
            transaction,
            self.manager,
            self.app
        )

        card.pack(fill="x", padx=20, pady=12)

    # ----------
    # show
    # ----------

    def show_transactions(self):

        self.search_message.configure(text="")
        self.clear_transactions()
        transactions = self.manager.show_all()

        if not transactions:

            empty_label = ctk.CTkLabel(
                self.list_frame,
                text="No transactions yet",
                font=SUBTITLE_FONT,
                text_color=SECONDARY_TEXT
            )

            empty_label.pack(pady=80)
            return

        for transaction in transactions:
            card = TransactionCard(
                self.list_frame, transaction, self.manager, self.app)
            card.pack(fill="x", padx=20, pady=12)
