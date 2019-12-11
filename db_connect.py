import pyodbc

#These are our variables we have to connect
server = 'localhost,1433'
database = 'Northwind'
user_name = 'SA'
password = 'Passw0rd2018'

#Making the connection
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+user_name+';PWD='+ password)

#Making a cursor
cursor = docker_Northwind.cursor() # creates an object which is a cursor

#Executing Some SQL Commands
cursor.execute("SELECT  * FROM Customers WHERE city LIKE 'London' ")
# #Cursor will maintain state
#
# #Fetching Data from the executed SQL command and printing
# row = cursor.fetchone()
# print(row)
#
# #By printing fetchone() again it will print the next row of information
# print(cursor.fetchone())
# print(cursor.fetchone())
#
# # Accessing Specific Data / or column
#     # Use the column name as an Attribute of the entry
# row = cursor.fetchone()
# print(row)
# print(row.CompanyName, row.ContactName)

# Fetchall Method - bad practice
rows_all = cursor.fetchall()
print(rows_all)
print(len(rows_all))
print(type(rows_all))

for row in rows_all:
    print(row.ContactName, row.CompanyName, row.Fax)

# to get lots of data use a while loop and fetch one at a time
rows = cursor.execute("SELECT * FROM Products")

while True:
    record = rows.fetchone()
    if record is None:
        break
    else:
        print(record.UnitPrice)