import mysql.connector

#-------------------------
# DATABASE CONNECTION
#-------------------------

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

