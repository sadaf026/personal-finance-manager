import csv
import os
from expense import Expense

FILE_NAME = "expenses.csv"

expenses = []

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 4:
                amount, category, date, description = row
                expenses.append(Expense(amount, category, date, description))


def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")

    expense = Expense(amount, category, date, description)
    expenses.append(expense)

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, date, description])

    print("\n✅ Expense added & saved successfully!\n")


def view_expenses():
    if not expenses:
        print("\nNo expenses found.\n")
        return

    print("\n--- All Expenses ---")
    for exp in expenses:
        print(exp)
    print()

def view_total_expense():
    if not expenses:
        print("\nNo expenses found.\n")
        return

    total = 0.0
    for exp in expenses:
        total += float(exp.amount)

    print(f"\n💰 Total Expense: ₹{total}\n")

def view_category_summary():
    if not expenses:
        print("\nNo expenses found.\n")
        return

    category_totals = {}

    for exp in expenses:
        category = exp.category
        amount = float(exp.amount)

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\n📊 Category-wise Summary:")
    for category, total in category_totals.items():
        print(f"{category} : ₹{total}")
    print()

def view_monthly_summary():
    if not expenses:
        print("\nNo expenses found.\n")
        return

    monthly_totals = {}

    for exp in expenses:
        month = exp.date[:7]   # YYYY-MM
        amount = float(exp.amount)

        if month in monthly_totals:
            monthly_totals[month] += amount
        else:
            monthly_totals[month] = amount

    print("\n📅 Monthly Expense Summary:")
    for month, total in monthly_totals.items():
        print(f"{month} : ₹{total}")
    print()

def export_category_summary():
    if not expenses:
        print("\nNo expenses to export.\n")
        return

    category_totals = {}

    for exp in expenses:
        category = exp.category
        amount = float(exp.amount)

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    with open("category_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Total Amount"])

        for category, total in category_totals.items():
            writer.writerow([category, total])

    print("\n📁 Category summary exported to category_summary.csv\n")


def menu():
    while True:
       print("PERSONAL FINANCE MANAGER")
       print("1. Add Expense")
       print("2. View Expenses")
       print("3. View Total Expense")
       print("4. View Category-wise Summary")
       print("5. View Monthly Summary")
       print("6. Export Category Summary")
       print("7. Exit")


       choice = input("Enter your choice: ")

       if choice == "1":
         add_expense()
       elif choice == "2":
         view_expenses()
       elif choice == "3":
         view_total_expense()
       elif choice == "4":
         view_category_summary()
       elif choice == "5":
         view_monthly_summary()
       elif choice == "6":
        export_category_summary()
       elif choice == "7":
        print("Goodbye 👋")
       break


    else:  print("❌ Invalid choice. Try again.\n")

#  THIS MUST BE THE LAST PART OF THE FILE
if __name__ == "__main__":
    load_expenses()
    menu()

