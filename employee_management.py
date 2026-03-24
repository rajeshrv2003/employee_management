import mysql.connector

# -----------------------------
# DATABASE CONNECTION
# -----------------------------

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = conn.cursor()

# -----------------------------
# CREATE DATABASE
# -----------------------------

cursor.execute("CREATE DATABASE IF NOT EXISTS employee_db")
cursor.execute("USE employee_db")

# -----------------------------
# CREATE TABLE
# -----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
emp_id INT PRIMARY KEY,
name VARCHAR(50),
department VARCHAR(50),
salary INT,
city VARCHAR(50)
)
""")

# -----------------------------
# ADD EMPLOYEE
# -----------------------------


def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = int(input("Enter Salary: "))
    city = input("Enter City: ")

    query = "INSERT INTO employees VALUES (%s,%s,%s,%s,%s)"
    values = (emp_id, name, dept, salary, city)

    cursor.execute(query, values)
    conn.commit()

    print("Employee Added Successfully")

# -----------------------------
# VIEW EMPLOYEES
# -----------------------------


def view_employees():

    cursor.execute("SELECT * FROM employees")

    records = cursor.fetchall()

    print("\nEmployee List\n")

    for row in records:
        print(row)

# -----------------------------
# UPDATE EMPLOYEE
# -----------------------------


def update_employee():

    emp_id = int(input("Enter Employee ID to update: "))
    salary = int(input("Enter New Salary: "))

    query = "UPDATE employees SET salary=%s WHERE emp_id=%s"

    cursor.execute(query, (salary, emp_id))
    conn.commit()

    print("Employee Updated")

# -----------------------------
# DELETE EMPLOYEE
# -----------------------------


def delete_employee():

    emp_id = int(input("Enter Employee ID to delete: "))

    query = "DELETE FROM employees WHERE emp_id=%s"

    cursor.execute(query, (emp_id,))
    conn.commit()

    print("Employee Deleted")

# -----------------------------
# MAIN MENU
# -----------------------------


while True:

    print("\n===== Employee Management System =====")
    print("1 Add Employee")
    print("2 View Employees")
    print("3 Update Employee")
    print("4 Delete Employee")
    print("5 Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        view_employees()

    elif choice == 3:
        update_employee()

    elif choice == 4:
        delete_employee()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
