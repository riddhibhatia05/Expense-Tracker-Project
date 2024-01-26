import openpyxl
from datetime import datetime

class ExpenseTracker: # Class Event Tracker
    def __init__(self):
        self.expenses = []
        self.categories = {'Groceries', 'Transportation', 'Entertainment'}

    def add_expense(self, amount, description, date, category): # Function to add expenses
        expense = {'Amount': amount, 'Description': description, 'Date': date, 'Category': category}
        self.expenses.append(expense)

    def edit_expense(self, index, amount, description, date, category): # Function to edit expenses
        if 0 <= index < len(self.expenses):
            self.expenses[index] = {'Amount': amount, 'Description': description, 'Date': date, 'Category': category}
        else:
            print("Invalid index. Expense not found.")

    def delete_expense(self, index): # Function to delete expenses
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
        else:
            print("Invalid index. Expense not found.")

    def add_category(self, category): # Functions to add category
        self.categories.add(category)

    def export_to_excel(self, filename='expenses.xlsx'): # Function to export data to excel sheet
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(['Date', 'Description', 'Amount', 'Category'])

        for expense in self.expenses:
            sheet.append([expense['Date'], expense['Description'], expense['Amount'], expense['Category']])

        workbook.save(filename)
        print(f'Expenses exported to {filename}')

    def summary(self): # Function to provide summary of overall expenditure
        total_spending = sum(expense['Amount'] for expense in self.expenses)
        print(f'Total Spending: ${total_spending:.2f}')

        category_spending = {category: sum(expense['Amount'] for expense in self.expenses if expense['Category'] == category) for category in self.categories}
        print('Spending by Category:')
        for category, spending in category_spending.items():
            print(f'{category}: ${spending:.2f}')

if __name__ == "__main__":
    expense_tracker = ExpenseTracker()

    while True: # Choice menu
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Edit Expense")
        print("3. Delete Expense")
        print("4. Add Category")
        print("5. Export to Excel")
        print("6. Summary")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1': # Add Expense
            amount = float(input("Enter amount spent: "))
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            expense_tracker.add_expense(amount, description, date, category)

        elif choice == '2': # Edit Expense
            index = int(input("Enter the index of the expense to edit: "))
            amount = float(input("Enter new amount spent: "))
            description = input("Enter new description: ")
            date = input("Enter new date (YYYY-MM-DD): ")
            category = input("Enter new category: ")
            expense_tracker.edit_expense(index, amount, description, date, category)

        elif choice == '3': # Delete Expense
            index = int(input("Enter the index of the expense to delete: "))
            expense_tracker.delete_expense(index)

        elif choice == '4': # Add Category
            category = input("Enter new category: ")
            expense_tracker.add_category(category)

        elif choice == '5': # Export to Excel
            filename = input("Enter the filename for Excel export (default: expenses.xlsx): ")
            expense_tracker.export_to_excel(filename)

        elif choice == '6': # Summary
            expense_tracker.summary()

        elif choice == '0': # Exit
            break

        else:
            print("Invalid choice. Please try again.")
