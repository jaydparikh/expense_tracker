# Define category object as a class

class Category:
    
    def __init__(self,name = "MISC",description = "NA"):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
if __name__ == "__main__":
    # Create a Category object
    food_category = Category("Food", "food,beverages,water")

    # Print category details
    print(food_category.name)
    print(food_category.description)