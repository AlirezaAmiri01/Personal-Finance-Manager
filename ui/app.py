import customtkinter as ctk
from ui.home_page import HomePage
from manager import Manager
from ui.add_income import AddIncome
from ui.add_expense import AddExpense
from ui.transactions import TransactionsPage
from ui.styles import *
from ui.edit_transaction import EditTransaction
from tkinter import messagebox


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.manager = Manager()

        self.current_page = None

        self.configure_window()
        self.create_layout()

    # --------------
    # create window
    # --------------

    def configure_window(self):
        ctk.set_appearance_mode("Dark")
        self.title("Finance Manager")
        self.geometry("900x600")

    # --------------
    # create layout
    # --------------

    def create_layout(self):
        self.create_main_frame()
        self.configure_grid()
        self.create_sidebar()
        self.create_content()
        self.show_home_page()

    # --------------------
    # create main frame
    # --------------------

    def create_main_frame(self):
        self.main_frame = ctk.CTkFrame(
            self, fg_color=BACKGROUND, corner_radius=15)
        self.main_frame.pack(fill="both", expand=True)

    # -------------------------
    # configure grid
    # -------------------------

    def configure_grid(self):
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.main_frame.grid_columnconfigure(1, weight=4)

        self.main_frame.grid_rowconfigure(0, weight=1)

    # ------------------
    # create sidebar
    # ------------------

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self.main_frame, width=220, fg_color=SIDEBAR, corner_radius=15)

        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.create_sidebar_buttons()

    # -----------------------
    # create content frame
    # -----------------------

    def create_content(self):

        self.content = ctk.CTkFrame(self.main_frame, fg_color=BACKGROUND)

        self.content.grid(row=0, column=1, sticky="nsew")

    # ------------
    # home page
    # ------------

    def show_home_page(self):
        self.show_page(HomePage)

    # -------------
    # change page
    # -------------

    def show_page(self, page, *args):

        if self.current_page:
            self.current_page.destroy()

        self.current_page = page(
            self.content,
            self.manager,
            self,
            *args
        )

        self.current_page.pack(fill="both", expand=True)

    # -------------------
    # sidebar buttons
    # -------------------

    def create_sidebar_buttons(self):
        buttons = [
            ("Dashboard", self.show_home_page),
            ("Add Income", lambda: self.show_page(AddIncome)),
            ("Add Expense", lambda: self.show_page(AddExpense)),
            ("Transactions", lambda: self.show_page(TransactionsPage)),
            ("Reset", self.reset_app),
            ("Exit", self.destroy)
        ]
        for text, command in buttons:
            button = ctk.CTkButton(
                self.sidebar,
                text=text,
                text_color=TEXT,
                command=command,
                fg_color=BUTTON,
                hover_color=BUTTON_HOVER,
                corner_radius=15,
                height=42
            )
            button.pack(fill="x", pady=10, padx=20)

    def reset_app(self):
        answer = messagebox.askyesno(
            "Reset",
            "Are you sure you want to delete all transactions?"
        )

        if answer:
            self.manager.reset_data()
            messagebox.showinfo("Reset", "App reset successfully")

            self.show_home_page()
