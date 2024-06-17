def login():
    while True:
        username = input("Enter the  username: ")
        password = input("Enter the password: ")

       
        if username == "qwerty" and password == "12345":
            return True
        else:
            print("Invalid credentials. Please enter a valid username and password.")
            return False

def get_income():
    while True:
        try:
            income = float(input("Enter your monthly income: "))
            if income > 0:
                return income
            else:
                print("Income should be greater than 0, Enter a valid amount for Income.")
        except ValueError:
            print("Invalid input. Please enter a valid number for income.")

def add_expense(balance, category, expenses):
    try:
        expense_description = input("Enter expense description: ")
        expense_amount = float(input("Enter expense amount: "))

        if expense_amount > 0 and expense_amount <= balance:
            expenses.append((expense_description, expense_amount, category))
            balance -= expense_amount
            print(f"Expense '{expense_description}' of {expense_amount} added successfully "
                  f"in the category {category}!")
        elif expense_amount <= 0:
            print("Expense amount should be greater than zero.")
        else:
            print("Insufficient balance. Expense cannot exceed the remaining balance.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the expense amount.")

    return balance

def generate_receipt(income, balance, expenses):
    total_expenses = income - balance
    savings = balance
    print("\nReceipt of your Expenditure:")
    print(f"Total Expenses: {total_expenses}")
    print(f"Remaining Balance: {balance}")
    print(f"Savings: {savings}")
    print("Breakdown of your expenditure:")
    for category in ['Rent', 'Utilities', 'Groceries', 'Entertainment', 'Transportation', 'Miscellaneous']:
        category_expenses = [expense[1] for expense in expenses if expense[2] == category]
        category_percentage = (sum(category_expenses) / income) * 100
        print(f"  - {category}: {category_percentage:.2f}%")

def main():
    print("****The ExpenseShell****")


    if not login():
        return

    
    income = get_income()
    balance = income
    expenses = []

    while True:
        print("\nCategories Of expenses:")
        print("1. Rent")
        print("2. Utilities")
        print("3. Groceries")
        print("4. Entertainment")
        print("5. Transportation")
        print("6. Miscellaneous")
        print("7. View Remaining Balance")
        print("8. Generate Receipt")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            category_dict = {
                '1': 'Rent',
                '2': 'Utilities',
                '3': 'Groceries',
                '4': 'Entertainment',
                '5': 'Transportation',
                '6': 'Miscellaneous'
            }
            category = category_dict[choice]
            balance = add_expense(balance, category, expenses)
        elif choice == '7':
            print(f"Remaining Balance: {balance}")
        elif choice == '8':
            generate_receipt(income, balance, expenses)
        elif choice == '9':
            print("You have a exciting expense Management.Thanku!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()

