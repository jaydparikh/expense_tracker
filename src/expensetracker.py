# Define ExpenseTracker object as class
from expense import Expense
from category import Category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = []
    
    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
    
    def view_expenses(self):
        for i in self.expenses:
            print(f"Amount: {i.amount}, Category: {i.category.name}, Description: {i.description}")



if __name__ == "__main__":
    # Create a Category object
    food_category = Category("Food")

    # Create Expense objects
    expense1 = Expense(100, food_category, "Lunch at McDonald's")
    expense2 = Expense(200, food_category, "Dinner at Domino's")

    # Track Expenses
    tracker = ExpenseTracker()
    tracker.add_expense(expense1)
    tracker.add_expense(expense2)

    # View expenses
    print(tracker.expenses)
    tracker.view_expenses()