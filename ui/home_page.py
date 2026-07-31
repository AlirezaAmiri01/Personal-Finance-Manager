import customtkinter as ctk
from ui.widgets import InfoCard
from ui.styles import *


class HomePage(ctk.CTkFrame):

    def __init__(self, parent, manager, app):
        super().__init__(parent, fg_color=BACKGROUND)

        self.manager = manager
        self.app = app
        self.cards = {}

        self.build_page()

    # --------------
    # page
    # --------------

    def build_page(self):

        self.create_header()
        self.create_cards_frame()
        self.create_cards()

    # ------------------
    # header
    # ------------------

    def create_header(self):

        self.page_title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 28, "bold")
        )

        self.page_title.pack(anchor="nw", padx=30, pady=(30, 20))

    # -----------------
    # cards frame
    # -----------------

    def create_cards_frame(self):

        self.cards_frame = ctk.CTkFrame(self, fg_color=BACKGROUND)

        self.cards_frame.grid_columnconfigure(0, weight=1)

        self.cards_frame.grid_columnconfigure(1, weight=1)

        self.cards_frame.grid_rowconfigure(0, weight=1)

        self.cards_frame.grid_rowconfigure(1, weight=1)

        self.cards_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 30)
        )

    # -----------------
    # create cards
    # -----------------

    def create_cards(self):

        cards = [
            ("Balance", self.manager.show_balance()),
            ("Income", len(self.manager.show_incomes())),
            ("Expense", len(self.manager.show_expenses())),
            ("Transactions", len(self.manager.show_all()))
        ]

        positions = [
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 1)
        ]

        for card, position in zip(cards, positions):

            title, value = card

            widget = InfoCard(self.cards_frame, title, value)

            self.cards[title] = widget

            widget.grid(
                row=position[0],
                column=position[1],
                padx=20,
                pady=20,
                sticky="nsew"
            )

    # -----------------
    # refresh dashboard
    # -----------------

    def refresh_dashboard(self):

        self.cards["Balance"].update_value(self.manager.show_balance())

        self.cards["Income"].update_value(len(self.manager.show_incomes()))

        self.cards["Expense"].update_value(len(self.manager.show_expenses()))

        self.cards["Transactions"].update_value(len(self.manager.show_all()))
