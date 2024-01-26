import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import openpyxl


class ExpenseTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.expenses = []
        self.categories = {'Groceries', 'Transportation', 'Entertainment'}

        # GUI Components
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_entry = tk.Entry(root)

        self.description_label = tk.Label(root, text="Description:")
        self.description_entry = tk.Entry(root)

        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.date_entry = tk.Entry(root)

        self.category_label = tk.Label(root, text="Category:")
        self.category_entry = tk.Entry(root)

        self.add_expense_button = tk.Button(root, text="Add Expense", command=self.add_expense)

        # Layout
        self.amount_label.grid(row=0, column=0)
        self.amount_entry.grid(row=0, column=1)

        self.description_label.grid(row=1, column=0)
        self.description_entry.grid(row=1, column=1)

        self.date_label.grid(row=2, column=0)
        self.date_entry.grid(row=2, column=1)

        self.category_label.grid(row=3, column=0)
        self.category_entry.grid(row=3, column=1)

        self.add_expense_button.grid(row=4, column=0, columnspan=2)

    def add_expense(self):
        amount = self.amount_entry.get()
        description = self.description_entry.get()
        date = self.date_entry.get()
        category = self.category_entry.get()

        try:
            amount = float(amount)
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please check your entries.")
            return

        expense = {'Amount': amount, 'Description': description, 'Date': date, 'Category': category}
        self.expenses.append(expense)

        messagebox.showinfo("Success", "Expense added successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerGUI(root)
    root.mainloop()
