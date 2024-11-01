# Define ExpenseTracker object as class
from expense import Expense
from category import Category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = {Category("food"), Category("grocery"), Category("travel")} #pre defined categories 
    
    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
        self.add_category(expense.category.get_name())
    
    def view_expenses(self):
        for index,item in enumerate(self.expenses):
            print(f"Expense No.{index+1} Amount:{item.get_amount()}, Category:{item.get_category().get_name()}, Description:{item.get_description()}")

    def modify_expense(self,user_index, expense: Expense):
        self.expenses[user_index-1] = expense
        self.add_category(expense.category.get_name())

    def delete_expense(self,user_index):
        del self.expenses[user_index-1]
    
    def add_category(self,category_name):
        category= Category(category_name)
        self.categories.add(category)

    def view_categories(self):
        for i in self.categories:
            print(i.get_name())

    def view_expenses_bycategory(self, category_name):
        for index,item in enumerate(self.expenses):
            if item.category.get_name() == category_name:
                print(f"Expense No.{index+1} Amount:{item.get_amount()}, Category:{item.get_category().get_name()}, Description:{item.get_description()}")


if __name__ == "__main__":
    # Track Expenses
    tracker = ExpenseTracker()

    # View Categories
    print("view categories")
    tracker.view_categories()
    print("*"*5)
    
    # Create a Category object
    utility_category = Category("utilities")

    # Create Expense objects
    expense1 = Expense(100, utility_category, "Lunch at McDonald's")
    expense2 = Expense(200, utility_category, "Dinner at Domino's")

    # Add Expenses
    tracker.add_expense(expense1)
    tracker.add_expense(expense2)
    
    # View expenses
    print("view expenses")
    tracker.view_expenses()
    print("*"*5)

    #Modify expense
    print("modify expenses")
    expense3 = Expense(300, Category("food"), "Dinner at ShivSagar")
    tracker.modify_expense(1,expense3)
    tracker.view_expenses()
    print("*"*5)

    #Delete expense
    print("delete expense")
    tracker.delete_expense(2)
    tracker.view_expenses()
    print("*"*5)

    #Add category
    print("Add Category")
    tracker.add_category("entertainmenT".strip().lower())
    tracker.add_category("FOOD".strip().lower())
    tracker.view_categories()
    print("*"*5)

    #View expenses by category
    print("view expenses by category")
    tracker.view_expenses_bycategory("food")
    print("*"*5)
