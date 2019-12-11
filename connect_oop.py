import pyodbc

class MSDBConnection():

    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.user_name = 'SA'
        self.password = 'Passw0rd2018'


        self.docker_Northwind = pyodbc.connect( 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.user_name + ';PWD=' + self.password)

        self.cursor = self.docker_Northwind.cursor()

    def __sql_query(self, sql_query): #the encapsulation makes the method private - can only be called using other methods
        return self.cursor.execute(sql_query)


    # Method to list or read all

    # Method to read one


    # Method to create one
            # 2 step process
                # ask for input  --> front end
                # create one --> makes things persistence

    # Method to update one

    # Method to destroy one
