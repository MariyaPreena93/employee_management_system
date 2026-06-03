
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",        # your server name
    user="root",             # your MySQL username
    password="",  # your MySQL password
    database="test"    # database name
)

if conn.is_connected():
    print("Connected to MySQL database")

cursor = conn.cursor()

def create_tab():
    query = """CREATE TABLE IF NOT EXISTS employees
    (emp_id int primary key,
    emp_name varchar(100),
    dept varchar(50),
    salary float
    )"""

    cursor.execute(query)
    conn.commit()
    print ("table created successfully")

create_tab()

#insert values
def insert_val():
    try:
        empid = int(input("Enter the empid:"))
        emp_name = input("Enter the employee name:")
        dept = input("Enter the department:")
        salary = float(input("Enter the salary:"))

        query = "insert into employees (emp_id, emp_name, dept, salary) values (%s,%s,%s,%s)"
        values = (empid,emp_name,dept,salary)

        cursor.execute(query,values)
        conn.commit()
        print("values inserted successfully")

    except mysql.connector.Error as err:
        print("Error:", err)

#update data

def update_val():
    empid = int(input("Enter the emp_id:"))
    new_sal = float(input("Enter the new salary:"))

    query = """update employees
            set salary = %s
            where emp_id = %s"""

    values = (new_sal,empid)
    cursor.execute(query,values)
    conn.commit()
    
    if cursor.rowcount > 0:
        print("Salary updated successfully")
    else:
        print("Employee ID not found")

#Delete data
def delete_val():
    empid = int(input("Enter the emp_id:"))

    query = "Delete from employees where emp_id = %s"
    values = (empid,)

    cursor.execute(query,values)
    conn.commit()

    if cursor.rowcount > 0:
        print("Employee deleted successfully")
    else:
        print("Employee ID not found")

#Search employee
def Search_emp():
    empid = int(input("Enter the emp_id:"))

    query = "Select * from employees where emp_id = %s"
    values = (empid,)

    cursor.execute(query,values)
    row = cursor.fetchone()

    if row:
        print(row)
    else:
        print("Employee not found")

#view data
def view_val():
    query = "select * from employees"
    cursor.execute(query)
    rows = cursor.fetchall()

    print("\nEmployee records")
    print("-"*40)

    for row in rows:
        print(row)

#Count
def emp_count():
    query = "select count(*) from employees"
    cursor.execute(query)
    row = cursor.fetchone()
    print("Employee Count:",row[0])

#Total salary
def Total_sal():
    query = "select sum(salary) from employees"
    cursor.execute(query)
    row = cursor.fetchone()
    print("Total Salary:",row[0])   
        

while True:

    print("\n=====Employee Managment system=====")
    print("1.Insert Employee")
    print("2.view all Employees")
    print("3.update Employee")
    print("4.delete Employee")
    print("5.Search Employee")
    print("6.Employee Count")
    print("7.Total Salary")
    print("8.Exit")

    choice = input("Enter your choice:")

    if choice=="1":
        insert_val()

    elif choice=="2":
        view_val()

    elif choice=="3":
        update_val()

    elif choice=="4":
        delete_val()

    elif choice=="5":
        Search_emp()

    elif choice=="6":
        emp_count()

    elif choice=="7":
        Total_sal()

    elif choice=="8":
        print("program exited")
        break

    else:
        print("Invalid choice try again")

cursor.close()
conn.close()
        
        
        
        
        

    
   


    
