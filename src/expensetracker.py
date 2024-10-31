# Define ExpenseTracker object as class

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = []
    
    def add_expense(self, expense):
        self.expenses.append(expense)
    
    def view_expenses(self):
        for i in self.expenses:
            print(f"Amount: {i.amount}, Category: {i.category.name}, Description: {i.description}")



if __name__ == "__main__":
    print("need to add")