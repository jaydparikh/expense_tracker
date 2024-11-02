#Module to handle csv file read and write
import csv
from expensetracker import ExpenseTracker
from expense import Expense
from category import Category

# Read data from expenses csv file
def read_expenses(tracker):
    tracker.expenses = [] #start with a blank expense list in tracker
    with open('data/expenses.csv',"r") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) #first line is header
        for row in csvreader: 
            amount = int(row[0])
            category = row[1]
            description = row[2]
            expense = Expense(amount,Category(category),description) 
            tracker.add_expense(expense)

# Read data from categories csv file
def read_categories(tracker):
    with open('data/categories.txt',"r") as file:
        lines = file.readlines()
        for line in lines:
            category = line.strip()
            if category:
                tracker.add_category(category)

# Write data to expenses file
def save_expenses(tracker):
    with open('data/expenses.csv',"w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["amount", "category", "description"])
        for expense in tracker.expenses:
            row = [expense.get_amount(),expense.get_category().name,expense.get_description()]
            csvwriter.writerow(row)


# Write data to categories file
def save_categories(tracker):
    with open('data/categories.txt',"w") as file:
        for category in tracker.categories:
            file.writelines(category.get_name() + "\n")


if __name__ == "__main__":
    
    tracker = ExpenseTracker()
    # read categories
    print("read categories")
    read_categories(tracker)
    tracker.view_categories()
    
    # read expenses
    print("read expenses")
    read_expenses(tracker)
    tracker.view_expenses()

    # write categories
    print("write categories")
    tracker.add_category("test1")
    save_categories(tracker)
    read_categories(tracker)
    tracker.view_categories()
    print("*"*5)

    # write expenses
    print("write expenses")
    expense1 = Expense(100, Category("nothing"), "Lunch at Dominos")
    tracker.add_expense(expense1)
    save_expenses(tracker)
    read_expenses(tracker)
    tracker.view_expenses()
    print("*"*5)
