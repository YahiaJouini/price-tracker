import mysql.connector
try:
    db=mysql.connector.connect(
        host='localhost',
        user="root",
        password=''
    )
    cursor = db.cursor()
    req = "CREATE DATABASE IF NOT EXISTS Price_Tracker"
    cursor.execute(req)
    if cursor.rowcount > 0:
        print("DataBase created successfully")
    else:
        print('DataBase already exists')
except:
    print('make sure to run your MySQL GUI')

