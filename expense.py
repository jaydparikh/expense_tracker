# Define expense object as a class
import category

class Expense():
    
    def __init__(self,amount,category : category, description = "NA"):
        self.amount = amount
        self.category = category
        self.description = description
    
    def get_amount(self):
        return self.amount
    
    def get_category(self):
        return self.category
    
    def get_description(self):
        return self.description

    

    