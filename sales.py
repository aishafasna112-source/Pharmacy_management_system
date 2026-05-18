from db import connect

def sell_medicine():
    conn = connect()
    c = conn.cursor()

    name = input("Medicine name: ")
    qty = int(input("Quantity: "))

    c.execute("SELECT quantity, price FROM medicines WHERE name=?", (name,))
    data = c.fetchone()

    if data:
        stock, price = data

        if stock >= qty:
            total = qty * price

            c.execute("UPDATE medicines SET quantity = quantity - ? WHERE name=?",
                      (qty, name))

            c.execute("INSERT INTO sales (medicine_name, quantity, total_price) VALUES (?, ?, ?)",
                      (name, qty, total))

            conn.commit()
            print("Sale completed! Total:", total)
        else:
            print("Not enough stock!")
    else:
        print("Medicine not found!")

    conn.close()


def view_sales():
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT * FROM sales")
    data = c.fetchall()

    print("\n--- Sales ---")
    for row in data:
        print(row)

    conn.close()