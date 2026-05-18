from db import connect

def register():
    conn = connect()
    c = conn.cursor()

    username = input("Username: ")
    password = input("Password: ")
    role = input("Role (admin/pharmacist/inventory): ")


    try:
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                  (username, password, role))
        conn.commit()
        print("User registered!")
    except:
        print("Username already exists!")

    conn.close()

def login():
    conn = connect()
    c = conn.cursor()

    username = input("Username: ")
    password = input("Password: ")

    c.execute("SELECT role FROM users WHERE username=? AND password=?",
              (username, password))

    user = c.fetchone()
    conn.close()

    if user:
        print("Login successful!")
        return user[0]
    else:
        print("Invalid login!")
        return None