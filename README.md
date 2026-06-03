Employee Management System
Overview
The Employee Management System is a menu-driven Python application that integrates with a MySQL database to manage employee records. The project demonstrates database connectivity, SQL query execution, CRUD operations, and basic reporting using Python and MySQL Connector.
The application automatically creates the employee table if it does not exist and provides an interactive command-line interface for managing employee information.
________________________________________
Features
•	Connects Python to MySQL Database
•	Automatically creates employee table using CREATE TABLE IF NOT EXISTS
•	Insert new employee records
•	View all employee records
•	Update employee salary information
•	Delete employee records
•	Search employees by Employee ID
•	Display total employee count
•	Calculate total salary expenditure
•	Uses parameterized SQL queries for secure database operations
•	Menu-driven command-line interface
________________________________________
Technologies Used
•	Python 3
•	MySQL
•	MySQL Connector/Python
________________________________________
Database Schema
Employees Table
Column Name	Data Type	Description
emp_id	INT	Employee ID (Primary Key)
emp_name	VARCHAR (100)	Employee Name
Dept	VARCHAR (50)	Department Name
Salary	FLOAT	Employee Salary
________________________________________
Project Structure
employee-management-system/
•	employee_management_system.py
•	README.md
•	screenshots/
________________________________________
Installation
1. Clone the Repository
git clone <repository-url>
cd employee_management_system
2. Install Dependencies
pip install mysql-connector-python
3. Configure MySQL
Update the database connection details in the Python script:
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="test"
)
4. Run the Application
employee_management_system.py
________________________________________
Application Menu
===== Employee Management System =====

1. Insert Employee
2. View All Employees
3. Update Employee
4. Delete Employee
5. Search Employee
6. Employee Count
7. Total Salary
8. Exit
________________________________________
Sample Functionality
Insert Employee
Enter the empid: 101
Enter the employee name: John
Enter the department: IT
Enter the salary: 75000
Search Employee
Enter the emp_id: 101
(101, 'John', 'IT', 75000)
Employee Count
Employee Count: 5
Total Salary
Total Salary: 325000
________________________________________
SQL Concepts Used
•	CREATE TABLE
•	INSERT
•	SELECT
•	UPDATE
•	DELETE
•	COUNT()
•	SUM()
•	WHERE Clause
•	PRIMARY KEY
•	Parameterized Queries
________________________________________
Python Concepts Used
•	Functions
•	Loops
•	Conditional Statements
•	Database Connectivity
•	Exception Handling
•	User Input Validation
•	CRUD Operations
________________________________________
Learning Outcomes
Through this project, I gained hands-on experience with:
•	Python and MySQL integration
•	Database design and management
•	Writing SQL queries in Python
•	Implementing CRUD operations
•	Using parameterized queries to prevent SQL injection
•	Error handling using try-except blocks
•	Building menu-driven command-line applications
________________________________________
Future Enhancements
•	CSV file import functionality
•	Excel file integration using Pandas
•	Department-wise salary reports
•	Average salary calculations
•	Cloud database integration
________________________________________
Author
Mariya Preena
ETL Developer | Python Learner | Data Analytics Enthusiast
Skills Demonstrated
Python • SQL • MySQL • Database Connectivity • CRUD Operations • Exception Handling • Data Management

