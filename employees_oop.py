import pyodbc
from connect_oop import *

class NWEmployee(MSDBConnection):

    def __sql_query(self, sql_query): #the encapsulation makes the method private - can only be called using other methods
        return self.cursor.execute(sql_query)


# method to get all employee data
    def get_all_employee(self):
        query = "SELECT * FROM Employees"
        result = self._MSDBConnection__sql_query(query)
        return result.fetchone()

#method to get one employee by id
    def get_one_employee_by_id(self):
        query = "SELECT * FROM Employees"
#method to search for one employee by name or last name

#add all these to the run_products