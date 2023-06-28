import mysql.connector
try:
    db=mysql.connector.connect(
        host='localhost',
        user="root",
        password="",
        database='Price_Tracker'
    )
    cursor=db.cursor()
    cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name ='products'")
    res=cursor.fetchall()
    if res[0][0]==0:
        req="create table products(id int Primary Key,name varchar(300),price decimal(5,2), reduction_percentage decimal(5,2),link varchar (200))"
        cursor.execute(req)
        print("Table created successfully")
    else:
        print("The table already exists")
except:
    print('make sure to run your MySQL GUI')