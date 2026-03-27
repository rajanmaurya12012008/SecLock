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
    
    # Get the last inserted user_id
    user_id = cursor.lastrowid
    
    conn.close()
    
    print("Registration Successful")
    return user_id, email, password


def login():
    conn = connect_db()
    cursor = conn.cursor()

    email = input("Enter Email: ")
    password = input("Enter Password: ")

    query = "SELECT id, score, total FROM users WHERE email=%s AND password=%s"
    values = (email, password)

    cursor.execute(query, values)
    result = cursor.fetchone()
    conn.close()

    if result:
        print("Login Successful")
        user_id = result[0]
        score = result[1] if result[1] is not None else 0
        total = result[2] if result[2] is not None else 0
        return user_id, score, total
    else:
        print("Invalid Credentials")
        return None, None, None


def update_score(user_id, score, total):
    print(f"Score update attempt: {score}/{total}")
    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE users SET score=%s, total=%s WHERE id=%s"
    cursor.execute(query, (score, total, user_id))
    conn.commit()
    conn.close()
    