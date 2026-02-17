import mysql.connector
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passsword="rajanmysql",
        database="exam_portal"
    )

