# Define ExpenseTracker object as class
from expense import Expense
from category import Category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = {Category("food"), Category("grocery"), Category("travel")} #pre defined categories 
    
    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
    
    def view_expenses(self):
        for index,item in enumerate(self.expenses):
            print(f"Expense No.{index+1} Amount:{item.get_amount()}, Category:{item.get_category().name}, Description:{item.get_description()}")

    def modify_expense(self,user_index, expense: Expense):
        self.expenses[user_index-1] = expense

    def delete_expense(self,user_index):
        del self.expenses[user_index-1]
    
    def add_category(self,category_name):
        category= Category(category_name)
        self.categories.add(category)

    def view_categories(self):
        for i in self.categories:
            print(i.get_name())


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
    print("*"*5)

    #Modify expense
    expense3 = Expense(300, food_category, "Dinner at ShivSagar")
    tracker.modify_expense(1,expense3)
    tracker.view_expenses()
    print("*"*5)

    #Delete expense
    tracker.delete_expense(2)
    tracker.view_expenses()
    print("*"*5)

    #Add category
    tracker.add_category("Utilities".lower())
    tracker.view_categories()
