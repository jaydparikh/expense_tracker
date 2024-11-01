# Define category object as a class

class Category:
    
    def __init__(self,name = "MISC"):
        self.name = name

    def get_name(self):
        return self.name
    
    
if __name__ == "__main__":
    # Create a Category object
    food_category = Category("Food")

    # Print category details
    print(food_category.get_name())