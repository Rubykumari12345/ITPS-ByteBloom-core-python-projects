import json
import os

FILE_NAME = "inventory.json"
LOW_LIMIT = 5

def load_inv():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}

def save_inv(inv):
    with open(FILE_NAME, "w") as f:
        json.dump(inv, f, indent=4)

def add_prod(inv):
    pid = input("Product ID: ").strip().upper()
    name = input("Product Name: ").strip().title()
    try:
        price = float(input("Price: "))
        qty = int(input("Quantity: "))
    except ValueError:
        print("Galat input!")
        return
    inv[pid] = {"name": name, "price": price, "qty": qty}
    save_inv(inv)
    print("Product added!")

def update_prod(inv):
    pid = input("Update Product ID: ").strip().upper()
    if pid not in inv:
        print("Product nahi mila.")
        return
    name = input("New Name (blank = same): ").strip().title()
    price = input("New Price (blank = same): ").strip()
    if name: inv[pid]["name"] = name
    if price: inv[pid]["price"] = float(price)
    save_inv(inv)
    print("Product updated!")

def delete_prod(inv):
    pid = input("Delete Product ID: ").strip().upper()
    if inv.pop(pid, None):
        save_inv(inv)
        print("Product deleted!")
    else:
        print("Product nahi mila.")

def stock_move(inv, mode):
    pid = input("Product ID: ").strip().upper()
    if pid not in inv:
        print("Product nahi mila.")
        return
    try:
        q = int(input(f"{mode} quantity: "))
    except ValueError:
        print("Galat quantity!")
        return
    if mode == "IN":
        inv[pid]["qty"] += q
    elif mode == "OUT":
        if inv[pid]["qty"] < q:
            print("Stock kam hai!")
            return
        inv[pid]["qty"] -= q
    save_inv(inv)
    print("Stock updated!")

def low_stock(inv):
    print("\n--- Low Stock Warnings ---")
    for pid, d in inv.items():
        if d["qty"] <= LOW_LIMIT:
            print(f"LOW STOCK: {d['name']} ({pid}) -> Qty: {d['qty']}")

def main():
    inv = load_inv()
    while True:
        print("\n1. Add  2. Update  3. Delete  4. Stock-In  5. Stock-Out  6. Low Stock  7. View All  8. Exit")
        ch = input("Choice: ").strip()
        if ch == "1": add_prod(inv)
        elif ch == "2": update_prod(inv)
        elif ch == "3": delete_prod(inv)
        elif ch == "4": stock_move(inv, "IN")
        elif ch == "5": stock_move(inv, "OUT")
        elif ch == "6": low_stock(inv)
        elif ch == "7":
            for pid, d in inv.items():
                print(f"{pid} | {d['name']} | Price: {d['price']} | Qty: {d['qty']}")
        elif ch == "8": break
        else: print("Galat choice!")

if __name__ == "__main__":
    main()