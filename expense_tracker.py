import csv

FILE_NAME = "expenses.csv"
expenses = []


def save_expenses():
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "category", "amount"]
        )
        writer.writeheader()
        writer.writerows(expenses)


def load_expenses():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)

    except FileNotFoundError:
        pass


def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses added yet.")
    else:
        print("\nYour Expenses:")
        print("-------------------------")

        for i, expense in enumerate(expenses, start=1):
            print(
                f"{i}. {expense['name']} - "
                f"{expense['category']} - ₹{expense['amount']}"
            )


def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total spending: ₹", total)


def delete_expense():
    if len(expenses) == 0:
        print("No expenses to delete.")
        return

    view_expenses()

    try:
        number = int(input("Enter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            save_expenses()

            print(
                f"Deleted: {deleted['name']} "
                f"- ₹{deleted['amount']}"
            )
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


# Load saved expenses when the program starts
load_expenses()

print("PERSONAL EXPENSE TRACKER")
print("-------------------------")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid option. Please try again.")