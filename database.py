import sqlite3

connect = sqlite3.connect('devices.db')

cursor = connect.cursor()

cursor.execute("DROP TABLE IF EXISTS DEVICES")

sql = ''' CREATE TABLE DEVICES (
CATEGORY CHAR(20) NOT NULL, 
MODEL CHAR(20), 
SERIAL_NUMBER NUMBER PRIMARY KEY
 )

 '''

cursor.execute(sql)
print("Table Created Succefully.")

def insert_device(category, model, serial_number):
    try:
        cursor.execute("INSERT INTO DEVICES (CATEGORY, MODEL, SERIAL_NUMBER) VALUES (?, ?, ?)", 
                       (category, model, serial_number))
        connect.commit()
        print("Device inserted successfully.")
    except sqlite3.IntegrityError:
        print("Error: Serial number must be unique.")


# insert_device("Laptop", "Dell XPS", 1001)

connect.commit()

connect.close()
