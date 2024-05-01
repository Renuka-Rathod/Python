import mysql.connector

# Create new table
cnx = mysql.connector.connect(user='root', 
                              password='renuka123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()

cur.execute("""CREATE TABLE mobile_user( 
            id INT AUTO_INCREMENT PRIMARY KEY, 
            name varchar(20), 
            mobile_no varchar(10));""")
cnx.commit()

# Insert records
records=[
    ('Renuka','9874563210'),
    ('Shagufta','9630008521'),
    ('Moha','7410258963'),
    ('Heena','8520147963'),
    ('Sharu','8541000256'),
    ('renu','9801400752'),
    ('sonu','9632100058'),
    ('raju','8901452630'),
    ('pintu','9631208521'),
    ('bheem','9810008521'),
]

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(user='root', 
                              password='renuka123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()

# Iterate over the records and insert them into the database
for record in records:
    query = "INSERT INTO mobile_user (name, mobile_no) VALUES (%s, %s)"
    cur.execute(query, record)

# Commit the transaction and close the connection
cnx.commit()
cnx.close()

# Select records and display them
cnx = mysql.connector.connect(user='root', 
                              password='renuka123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()
cur.execute("select * from mobile_user")

for row in cur:
    print(row)

cnx.close()
