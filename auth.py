from database import connect_db

def register():
    conn = connect_db()
    cursor = conn.cursor()

    roll = input("Enter Roll No: ")
    username = input("Enter Username: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    query = "INSERT INTO users (roll_no, username, email, password) VALUES (%s, %s, %s, %s)"
    values = (roll, username, email, password)

    cursor.execute(query, values)
    conn.commit()

    print("Registration Successful")

def login():
    conn = connect_db()
    cursor = conn.cursor()

    email = input("Enter Email: ")
    password = input("Enter Password: ")

    query = "SELECT * FROM users WHERE email=%s AND password=%s"
    values = (email, password)

    cursor.execute(query, values)
    result = cursor.fetchone()

    if result:
        print("Login Successful")
    else:
        print("Invalid Credentials")
