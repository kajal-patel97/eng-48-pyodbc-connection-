import pyodbc
from connect_oop import *

class NWEmployee(MSDBConnection):


# method to get all employee data
    def get_all_employee(self):
        query = "SELECT * FROM Employees"
        result = self._MSDBConnection__sql_query(query)
        return result.fetchone()

#method to get one employee by id
    def get_one_employee_by_id(self):
        id = int(input('Please enter the Employee ID...'))
        query = f"SELECT * FROM Employees WHERE EmployeeID = {id} "
        result = self._MSDBConnection__sql_query(query)
        while True:
            record = result.fetchone()
            if record is None:
                break
            print(f'Employee ID: {record.EmployeeID} - Name: {record.TitleOfCourtesy} {record.FirstName} {record.LastName}')
        return 'Thank You.'

#method to search for one employee by name or last name
    def search_employee(self):
        name = input('Enter the first name or last name of the employee...')
        query = f"SELECT * FROM Employees WHERE FirstName LIKE '%{name}%' OR LastName = '{name}' "
        result = self._MSDBConnection__sql_query(query)
        while True:
            record = result.fetchone()
            if record is None:
                break
            print(f'Employee ID: {record.EmployeeID}. Name: {record.TitleOfCourtesy} {record.FirstName} {record.LastName}. Title: {record.Title}')
        return 'Completed'

    def __sql_query(self, sql_query): #the encapsulation makes the method private - can only be called using other methods
        return self.cursor.execute(sql_query)

#Create one Employee
    def create_employee(self, first_name, last_name):
        query = f"INSERT INTO Employees (FirstName, LastName) VALUES ('{first_name}','{last_name}') "
        result = self.__sql_query(query)
        self.docker_Northwind.commit()
        return result
# # get the last record to increment from the last ID
# get the id
# increment id
# use incremented id

#update/ change one employee data

#add all these to the run_products

table_employees = NWEmployee()

# #Create an employee
# added_employee = table_employees.create_employee()
# added_employee

# #Search for employee
# employee = table_employees.search_employee()
# print(employee)


# # get one employee by id
# employee = table_employees.get_one_employee_by_id()
# print(employee)