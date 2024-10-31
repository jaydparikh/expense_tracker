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
        for index,item in enumerate(self.expenses):
            print(f"Expense No.{index+1} Amount:{item.amount}, Category:{item.category.name}, Description:{item.description}")


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
    tracker.view_expenses()