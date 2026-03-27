import mysql.connector
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="rajanmysql",
        database="exam_portal"
    )

