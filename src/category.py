# Define category object as a class

class Category:
    
    def __init__(self,name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name cannot be empty")
        self.name = name

    def get_name(self):
        return self.name
    
    def __eq__(self,other):
        if isinstance(other, Category):
            return self.name == other.name
        return False
    
    def __hash__(self):
        return hash(self.name) 

    
if __name__ == "__main__":
    # Create a Category object
    food_category = Category("food")

    # Print category details
    print(food_category.get_name())
    print("*"*5)

    #check to ensure unique values in set of categories
    set1 = {Category("food"), Category("utilities")}
    set1.add(Category("food"))
    set1.add(Category("travel"))
    for i in set1:
        print(i.get_name())
    print("*"*5)