import pyodbc
from connect_oop import *

class NWProducts(MSDBConnection):

    def __sql_query(self, sql_query): #the encapsulation makes the method private - can only be called using other methods
        return self.cursor.execute(sql_query)

    # Method to list or read all
    def read_all(self):
        #Build the sql query
        query = "SELECT * FROM Products"

        #execute the query
        data = self.__sql_query(query)

        #return an iterable object
        return data

    # Method to read one
    #set the ID to then use to read
    def set_id(self):
        id = int(input('select an ID'))
        return id

    def read_one(self,id):
        query = f"SELECT * FROM Products WHERE ProductID = {id}"
        result = self.__sql_query(query)
        return result.fetchone()

# PRINT ALL PRODUCTS USIGN THE WHILE LOOP AND FETCHONE()
    def print_all(self):
        query = "SELECT * FROM Products"
        data = self.__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(f"ID:{record.ProductID} - {record.ProductName} £{record.UnitPrice}")


#Method to prints the top 10 products by price - formatted
    def top_10_by_price(self):
        query = "SELECT TOP 10 * FROM Products ORDER BY UnitPrice DESC"
        result = self.__sql_query(query)
        while True:
            record = result.fetchone()
            if record is None:
                break
            print(f"Name: {record.ProductName} - £{record.UnitPrice}")
        return 'All Done'
#Method to prints the bottom 10 products by price - formatted

# Search product by name








table_products = NWProducts()

#prints the top 10 products by price
products = table_products.top_10_by_price()
print(products)

# #Getting all products
# products = table_products.read_all()
# print(products.fetchone())
#
# #getting
# product = table_products.read_one()
# print(product)
#
# all_products = table_products.read_all()
# print(all_products.fetchone())
#
# while True:
#      record = all_products.fetchone()
#      if record is None:
#          break
#      print(record)