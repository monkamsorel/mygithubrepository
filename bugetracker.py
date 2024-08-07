
def expenses(balance):
    amount = float(input("Enter amount you want to spend:"))
    if amount > balance:
        print("Insufficient Balance")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount


def income():
    amount = float(input("Enter today income amount: "))

    if amount < 0:
        print("This is not a valid amount")
        return 0
    else:
        return amount


def current_balance(in_balance):
    print(f"Your current balance is: {in_balance:2f} XAF")


def save_to_file(balance, filename):
    with open(filename, 'w') as file:
        file.write(f"{balance}")


def load_from_file(filename):
    with open(filename, 'r') as file:
        balance = file.read()
    return float(balance)


def main():
    file_name = 'database.txt'
    income_balance = 0.0
    try:
        income_balance = load_from_file(file_name)
    except FileNotFoundError:
        print("No existing transaction file found. Starting fresh.")
    is_running = True
    while is_running:

        print("""
        Daily Budget Tracker
        0.To check monthly record
        1.To add income of the day
        2.To make expenses of the day
        3. current balance
        4. to save and exit   
        """)

        option = int(input("Enter an option(1-4): "))

        if option == 1:
            income_balance += income()

        elif option == 2:
            income_balance -= expenses(income_balance)

        elif option == 3:
            current_balance(income_balance)

        elif option == 4:
            save_to_file(income_balance, file_name)
            break

        else:
            print("that is not a valid option")

    print("""
    Transaction recorded! Have a nice day""")


main()
