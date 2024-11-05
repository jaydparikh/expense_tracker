Setup:
**Clone the Repository**:
git clone <repository-url>
cd <repository-directory>

Create a virtual environment
python -m venv venv

Activate the Virtual Environment:
python -m venv venv

Install Dependencies:
pip install -r requirements.txt

Prepare Data Files:
Ensure that the data directory contains the following files:
categories.txt: A text file containing the list of categories, one per line.
expenses.csv: A CSV file containing the list of expenses with columns: amount, category, description.



User Notes:
Running the Application:

To start the application, run the following command:
python src/main.py

Main Menu Options:

1. Add Expense: Add a new expense by entering the amount, category, and description.
2. Modify Expense: Modify an existing expense by selecting its index and updating the details.
3. Delete Expense: Delete an existing expense by selecting its index.
4. View All Expenses: View a list of all recorded expenses.
5. View Categories: View a list of all available categories.
6. Add Category: Add a new category to the list.
7. View Expenses by Category: View expenses filtered by a specific category.
8. Quit: Save the data and exit the application.

Data Persistence:
The application saves the expenses to expenses.csv and categories to categories.txt upon quitting.
Ensure these files are not deleted or moved to maintain data integrity.

Error Handling:
The application handles invalid inputs and file not found errors gracefully, providing appropriate error messages to the user.

Dependencies:
Ensure all dependencies listed in requirements.txt are installed in the virtual environment for the application to function correctly.
