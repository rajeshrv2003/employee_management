import mysql.connector

# -------------------------
# DATABASE CONNECTION
# -------------------------

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = conn.cursor()

# ----------------------------
# CREATE DATABASE
# ----------------------------

cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
cursor.execute("USE student_db")

# --------------------------------
# CREATE TABLE
# --------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
student_id INT PRIMARY KEY,
name VARCHAR(50),
department VARCHAR(50),
fees INT,
city VARCHAR(50)
)
""")

# --------------------------
# ADD STUDENT
# --------------------------

def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    fees = int(input("Enter Fees: "))
    city = input("Enter City: ")

    query = "INSERT INTO student VALUES (%s,%s,%s,%s,%s)"
    values = (student_id, name, department, fees, city)

    cursor.execute(query, values)
    conn.commit()

    print("Student added successfully")


# ---------------------------
# VIEW STUDENTS
# ---------------------------

def view_student():

    cursor.execute("SELECT * FROM student")
    records = cursor.fetchall()

    print("\nStudent List\n")

    for row in records:
        print(row)


# -----------------------------
# UPDATE STUDENT
# ----------------------------

def update_student():

    student_id = int(input("Enter student ID to update: "))
    fees = int(input("Enter new fees: "))

    query = "UPDATE student SET fees=%s WHERE student_id=%s"

    cursor.execute(query, (fees, student_id))
    conn.commit()

    print("Student updated successfully")


# ----------------------------
# DELETE STUDENT
# ---------------------------

def delete_student():

    student_id = int(input("Enter student ID to delete: "))

    query = "DELETE FROM student WHERE student_id=%s"

    cursor.execute(query, (student_id,))
    conn.commit()

    print("Student deleted successfully")


# -------------------------
# MAIN MENU
# -------------------------

while True:

    print("\n===== Student Management System =====")
    print("1 Add Student")
    print("2 View Student")
    print("3 Update Student")
    print("4 Delete Student")
    print("5 Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_student()

    elif choice == 3:
        update_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
