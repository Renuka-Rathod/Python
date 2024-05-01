import mysql.connector

# Function to validate the mobile number
def validate_mobile_number(mobile_no):
    if len(mobile_no) != 10:
        return False
    return True

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(user='root', 
                              password='renuka123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()

# Take input from the user
name = input("Enter name: ")
mobile_no = input("Enter mobile number: ")

# Validate the mobile number
if not validate_mobile_number(mobile_no):
    print("Mobile number should be exactly 10 digits.")
    exit()

# Insert the user input into the database
query = "INSERT INTO mobileuser (name, mobile_no) VALUES (%s, %s)"
values = (name, mobile_no)
cur.execute(query, values)

# Commit the transaction and close the connection
cnx.commit()
cnx.close()
