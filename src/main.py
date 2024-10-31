# Import modules
from expensetracker import ExpenseTracker
from expense import Expense
from category import Category


def main():
    while True:
        print("************************************")
        print("1. Add Expense")
        print("2. Modify Expense")
        print("3. Delete Expense")
        print("4. View All Expenses")
        print("5. View Categories")
        print("6. Add Category")
        print("7. View Expenses by Category")
        print("8. Quit")
        print("***********************************")
        choice = input("Enter your choice: ",)
        
        if choice == "1": #Add Expense
            user_amount = input("Enter Amount:")
            user_category = Category("New")
            user_description = input("Enter Description")
            expense = Expense(user_amount,user_category,user_description)
            tracker.add_expense(expense)
            print("1")
            print(expense)
            print(tracker.expenses)
        elif choice =="2":
            print("2")
        elif choice =="3":
            print("3")
        elif choice == "4": #View All Expenses
            tracker.view_expenses()
            print("4")
        elif choice == "5":
            print("5")
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            break
        
if __name__ == "__main__":
    tracker = ExpenseTracker()
    main()