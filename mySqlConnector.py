import mysql.connector

# Connecting and querying using mysql connector
cnx = mysql.connector.connect(user='testUser', 
                              password='testPassword',
                              host='127.0.0.1',
                              database='testPythonDb')

if cnx and cnx.is_connected():

    with cnx.cursor() as cursor:
        result = cursor.execute("SELECT * FROM TestData")

        rows = cursor.fetchall()
        for rows in rows:
            print(rows)

    cnx.close()

else:
    print("Could not connect")