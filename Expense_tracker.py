import csv
import os

FILE_NAME = "expenses.csv"

def add_record(r_type):
    cat = input("Category (Food, Travel, Salary, etc.): ").strip().title()
    try:
        amt = float(input("Amount: "))
        if amt <= 0:
            print("Amount 0 se bada hona chahiye.")
            return
    except ValueError:
        print("Amount mein sirf number dalein.")
        return
    note = input("Description: ").strip()

    with open(FILE_NAME, "a", newline="") as f:
        csv.writer(f).writerow([r_type, cat, amt, note])
    print("Record save ho gaya!")

def get_records():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return list(csv.DictReader(f))

def show_balance():
    rows = get_records()
    inc = sum(float(r["Amount"]) for r in rows if r["Type"] == "Income")
    exp = sum(float(r["Amount"]) for r in rows if r["Type"] == "Expense")
    print(f"\nIncome: {inc:.2f} | Expense: {exp:.2f} | Balance: {inc - exp:.2f}")

def view_by_category():
    rows = get_records()
    totals = {}
    for r in rows:
        if r["Type"] == "Expense":
            c = r["Category"]
            totals[c] = totals.get(c, 0.0) + float(r["Amount"])
    print("\n--- Expenses by Category ---")
    for c, a in totals.items():
        print(f"{c}: {a:.2f}")

def show_history():
    rows = get_records()
    print("\n--- Transaction History ---")
    for r in rows:
        print(f"{r['Type']} | {r['Category']} | {r['Amount']} | {r['Note']}")

def main():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            csv.writer(f).writerow(["Type", "Category", "Amount", "Note"])

    while True:
        print("\n1. Add Income  2. Add Expense  3. Balance  4. By Category  5. History  6. Exit")
        ch = input("Choice: ").strip()
        if ch == "1": add_record("Income")
        elif ch == "2": add_record("Expense")
        elif ch == "3": show_balance()
        elif ch == "4": view_by_category()
        elif ch == "5": show_history()
        elif ch == "6": break
        else: print("Galat choice!")

if __name__ == "__main__":
    main()