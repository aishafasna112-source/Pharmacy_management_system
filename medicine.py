from db import connect

def add_medicine():
    conn = connect()
    c = conn.cursor()

    name = input("Medicine name: ")
    qty = int(input("Quantity: "))
    price = float(input("Price: "))

    c.execute("INSERT INTO medicines (name, quantity, price) VALUES (?, ?, ?)",
              (name, qty, price))

    conn.commit()
    conn.close()
    print("Medicine added!")


def view_medicine():
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT * FROM medicines")
    data = c.fetchall()

    print("\n--- Medicines ---")
    for row in data:
        print(row)

    conn.close()


def update_medicine():
    conn = connect()
    c = conn.cursor()

    name = input("Enter medicine name to update: ")
    qty = int(input("New quantity: "))
    price = float(input("New price: "))

    c.execute("UPDATE medicines SET quantity=?, price=? WHERE name=?",
              (qty, price, name))

    conn.commit()
    conn.close()
    print("Medicine updated!")


def delete_medicine():
    conn = connect()
    c = conn.cursor()

    name = input("Enter medicine name to delete: ")

    c.execute("DELETE FROM medicines WHERE name=?", (name,))

    conn.commit()
    conn.close()
    print("Medicine deleted!")