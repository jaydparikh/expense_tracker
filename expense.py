# Define expense object as a class
from category import Category

class Expense():
    
    def __init__(self,amount : float,category : Category, description = "NA"):
        self.amount = amount
        self.category = category
        self.description = description
    
    def get_amount(self):
        return self.amount
    
    def get_category(self):
        return self.category
    
    def get_description(self):
        return self.description

if __name__ == "__main__":
    # Create a Category object
    food_category = Category("Food")

    # Create an Expense object
    expense1 = Expense(100, food_category, "Lunch at McDonald's")

    # Print expense details
    print("Amount:", expense1.amount)
    print("Category:", expense1.category.name)
    print("Description:", expense1.description)

    