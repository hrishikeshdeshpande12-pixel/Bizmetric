import pyodbc
from datetime import datetime  # Added for unique filenames/timestamps

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-F993VFLL\\SQLEXPRESS;'
    'Database=BANKEDATA;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

def view_menu():
    cursor.execute("SELECT*FROM Menu")
    rows = cursor.fetchall()

    print("\n-----Hotel Menu -------")
    for r in rows:
        print(f"ID: {r.item_id} | Name: {r.item_name} | Price:{r.price}")
    print()

def save_bill_to_file(items, grand_total):
    """Saves the final bill into a .txt file"""
    filename = f"Receipt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(filename, "w") as f:
        f.write("========== HOTEL RECEIPT ==========\n")
        f.write(f"Date: {datetime.now()}\n")
        f.write("-----------------------------------\n")
        for item in items:
            f.write(f"{item['name']} | Qty: {item['qty']} | Total: {item['total']}\n")
        f.write("-----------------------------------\n")
        f.write(f"GRAND TOTAL: {grand_total}\n")
        f.write("===================================\n")
    
    print(f"Digital receipt saved as: {filename}")

def print_final_bill(items, grand_total):
    print("\n========== Final Hotel Bill ==============")
    for item in items:
        print(f"{item['name']} | Qty:{item['qty']} | Total: {item['total']}")
    
    print("---------------------------")
    print(f"GRAND TOTAL BILL: {grand_total}")
    print("============================================\n")

def take_order():
    items = []
    grand_total = 0

    while True:
        view_menu()
        item_id = int(input("Enter item ID to order: "))
        qty = int(input("Enter quantity: "))

        cursor.execute("SELECT item_name,price FROM Menu WHERE item_id = ?",(item_id,))
        result = cursor.fetchone()

        if not result:
            print("Invalid item ID!")
            continue

        name,price = result
        total = price * qty

        cursor.execute("INSERT INTO Orders(item_id,quantity,total_price) VALUES (?, ? ,?)",(item_id,qty,total))

        items.append({"name": name,"qty":qty ,"total":total})
        grand_total += float(total)

        more = input("Add more items? (y/n): ").lower()
        if more != 'y':
            break
    
    conn.commit()

    print("\n Order placed successfully !")
    print_final_bill(items, grand_total)
    
    # CALLING FILE HANDLING HERE
    save_bill_to_file(items, grand_total)
            

def view_orders():
    cursor.execute("""SELECT o.order_id,m.item_name,o.quantity,o.total_price FROM Orders o JOIN Menu m ON o.item_id = m.item_id""")

    rows = cursor.fetchall()

    print("\n------ ALL  ORDERS ----------")
    grand_total = 0

    for r in rows:
        print(f"OrderID: {r.order_id}| Item :{r.item_name} | Qty: {r.quantity} | Total: {r.total_price}")
        grand_total += float(r.total_price)
    print("-------------------------------")
    print(f"FINAL TOTAL OF ALL ORDERS: {grand_total}")    
    print()


def main():
    while True:
        print(""" =========== SIMPLE HOTEL SYSTEM
              1. View Menu 
              2. Take Order(Multiple Items)
              3. View All Orders
              4. Exit""")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_menu()
        elif choice == '2':
            take_order()
        elif choice == '3':
            view_orders()
        elif choice == '4':
            print("Thank you! Visit again ")
            break
        else:
            print("Invalid choice! Try again")


if __name__ == "__main__":
    main()
