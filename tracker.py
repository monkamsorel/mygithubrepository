"""Step
1: Define
Features and Data
Structure

Features:
1.
Add
income and expenses.
2.
Categorize
transactions.
3.
View
current
balance.
4.
Generate
monthly
reports.
5.
Save and load
data
to /
from a file.

Data
Structure:
- Each
transaction
will
be
a
dictionary
with amount, category, and description.
- Transactions
will
be
stored in a
list.

Step
2: Implement
Functions

Let
's implement functions to add transactions, calculate the balance, save to a file, and load from a file.

1.
Adding
a
Transaction

python"""


def add_transaction(transactions, amount, category, description):
    transactions.append({'amount': amount, 'category': category, 'description': description})


"""
2.
Calculating
Balance

python"""


def calculate_balance(transactions):
    return sum(tx['amount'] for tx in transactions)


"""3.
Saving
Data
to
a
File

python"""


def save_to_file(transactions, filename):
    with open(filename, 'w') as file:
        for tx in transactions:
            file.write(f"{tx['amount']},{tx['category']},{tx['description']}\n")


"""4.
Loading
Data
from a File

python"""


def load_from_file(filename):
    transactions = []
    with open(filename, 'r') as file:
        for line in file:
            amount, category, description = line.strip().split(',')
            transactions.append({'amount': float(amount), 'category': category, 'description': description})
    return transactions


"""Step
3: User
Interface

We
will
create
a
simple
text - based
interface
using
input()
to
get
user
commands and print()
to
display
information.

python"""


def main():
    transactions = []
    filename = 'transactions.txt'

    # Load existing transactions if file exists
    try:
        transactions = load_from_file(filename)
    except FileNotFoundError:
        print("No existing transaction file found. Starting fresh.")

    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add Transaction")
        print("2. View Balance")
        print("3. Generate Report")
        print("4. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_transaction(transactions, amount, category, description)
            print("Transaction added.")

        elif choice == '2':
            balance = calculate_balance(transactions)
            print(f"Current Balance: {balance}")

        elif choice == '3':
            print("Monthly Report:")
            categories = set(tx['category'] for tx in transactions)
            for category in categories:
                category_total = sum(tx['amount'] for tx in transactions if tx['category'] == category)
                print(f"{category}: {category_total}")

        elif choice == '4':
            save_to_file(transactions, filename)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

"""Explanation

1.
add_transaction: Adds
a
new
transaction
to
the
list.
2.
calculate_balance: Calculates
the
current
balance
by
summing
up
the
amounts
of
all
transactions.
3.
save_to_file: Saves
all
transactions
to
a
specified
file.
4.
load_from_file: Loads
transactions
from a specified

file.
5.
main: Implements
the
main
program
loop:
- Loads
existing
transactions
from a file

(if available).
- Displays
a
menu
for the user to choose actions.
- Handles
user
inputs
to
add
transactions, view
the
balance, generate
reports, and save
data before exiting."""
