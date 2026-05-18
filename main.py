from db import create_tables
from auth import login, register
from medicine import add_medicine, view_medicine, update_medicine, delete_medicine
from sales import sell_medicine, view_sales

create_tables()


def admin_menu():
    while True:
        print("\n=== ADMIN MENU ===")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Update Medicine")
        print("4. Delete Medicine")
        print("5. View Sales")
        print("6. Logout")

        ch = input("Choose: ")

        if ch == "1":
            add_medicine()
        elif ch == "2":
            view_medicine()
        elif ch == "3":
            update_medicine()
        elif ch == "4":
            delete_medicine()
        elif ch == "5":
            view_sales()
        elif ch == "6":
            break
        else:
            print("Invalid choice!")


def pharmacist_menu():
    while True:
        print("\n=== PHARMACIST MENU ===")
        print("1. Sell Medicine")
        print("2. View Medicines")
        print("3. Logout")

        ch = input("Choose: ")

        if ch == "1":
            sell_medicine()
        elif ch == "2":
            view_medicine()
        elif ch == "3":
            break
        else:
            print("Invalid choice!")

def inventory_menu():
    while True:
        print("\n=== INVENTORY MENU ===")
        print("1. Add Medicine")
        print("2. Update Medicine")
        print("3. Delete Medicine")
        print("4. View Medicines")
        print("5. Logout")

        ch = input("Choose: ")

        if ch == "1":
            add_medicine()
        elif ch == "2":
            update_medicine()
        elif ch == "3":
            delete_medicine()
        elif ch == "4":
            view_medicine()
        elif ch == "5":
            break
        else:
            print("Invalid choice!")


while True:
    print("\n=== PHARMACY SYSTEM ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        register()

    elif choice == "2":
        role = login()

        if role == "admin":
            admin_menu()
        elif role == "pharmacist":
            pharmacist_menu()
        elif role == "inventory":
            inventory_menu()
        else:
            print("Invalid role!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")