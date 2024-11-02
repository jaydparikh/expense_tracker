# Import modules
from expensetracker import ExpenseTracker
from expense import Expense
from category import Category
from filehandling import *


def main():
    while True:
        print("*"*5,"Input Options","*"*5)
        print("1. Add Expense")
        print("2. Modify Expense")
        print("3. Delete Expense")
        print("4. View All Expenses")
        print("5. View Categories")
        print("6. Add Category")
        print("7. View Expenses by Category")
        print("8. Quit")
        print("*"*5, "*"*5)
        choice = input("Enter your choice: ",)
        
        if choice == "1": #Add Expense
            print("Add an expense to below existing categories or create a new one")
            tracker.view_categories()
            try:
                user_amount = input("Enter Amount: ").strip()
                user_category = input("Enter Category: ").strip().lower()
                user_description = input("Enter Description: ").strip().lower()
                expense = Expense(user_amount,Category(user_category),user_description)
                tracker.add_expense(expense)
            except ValueError as e:
                print(f'Invalid input: {e}')
        
        elif choice =="2": #Modify Expense
            print("You have made the following expenses till now")
            tracker.view_expenses()
            try:
                user_index = int(input("Which one do you want to modify: "))
                user_amount = input("Enter Amount: ").strip().lower()
                user_category = input("Enter Category: ").strip().lower()
                user_description = input("Enter Description: ").strip().lower()
                expense = Expense(user_amount,Category(user_category),user_description)
                tracker.modify_expense(user_index,expense)
            except ValueError as e:
                print(f'Invalid input: {e}')
        
        elif choice =="3": #Delete Exepnse
            print("You have made the following expenses till now")
            tracker.view_expenses()
            user_index = int(input("Which one do you want to delete: ").strip())
            tracker.delete_expense(user_index)
        
        elif choice == "4": #View All Expenses
            print("You have made the following expenses till now")
            tracker.view_expenses()
        
        elif choice == "5": #View Categories
            print("You have following categories available")
            tracker.view_categories()
        
        elif choice == "6": #Add category
            print("You have following categories available")
            tracker.view_categories()
            try:
                user_category = input("What category would you like to add: ").strip().lower()
                tracker.add_category(user_category)
            except TypeError as e:
                print(f"Error: {e}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "7": #View Expenses by Category
            print("You have following categories available")
            tracker.view_categories()
            user_category = input("What category would you like to view for: ").strip().lower()
            tracker.view_expenses_bycategory(user_category)
        
        elif choice == "8": #Quit
            save_categories(tracker)
            save_expenses(tracker)
            print("Exiting the expense tracker.")
            break
        
        else:
            print("** Incorrect input, please try again **")
        
if __name__ == "__main__":
    tracker = ExpenseTracker()
    
    try:
        read_categories(tracker)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    
    try:
        read_expenses(tracker)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    
    main()