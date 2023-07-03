# # get the list of drivers installed on the system
# import pyodbc
# for driver in pyodbc.drivers():
#     print(driver)

# # standard steps for python database programming
# # import the database-specific module
# # establish a connection to the database securely
# # cursor object is the intermediate memory through which we will interact with the database
# # use built-in functions to interact with the database
# # commit or rollback
# # fetch the result from the cursor
# # close the resources (close the cursor first and then the connection)
# # Three requirements to connect to the database
# # Driver: driver_name
# # Server Name: SQL_Server_Name
# # Database Name: db_name
# # Connection String: 'DRIVER=driver_name;SERVER=SQL_Server_Name;DATABASE;=db_name;Trusted_Connection'

# 'DRIVER=driver_name;SERVER=sql_server\SQLEXPRESS;DATABASE;=test;Trusted_Connection'

# import pyodbc

# conn = pyodbc.connect('DRIVER=server_driver;SERVER=server_name;DATABASE=Training;Trusted_Connection=yes')

# cursor = conn.cursor()

# cursor.execute('SELECT * FROM Training.dbo.S')

# for row in cursor: # comes out as a tuple
#     for value in row:
#         print(value, end=' ')

# cursor.close()
# conn.close()

# # insert values into a table
# import pyodbc

# conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-230524-1335\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes')

# cursor = conn.cursor()

# id = input("Enter ID: ")
# name = input("Enter Name: ")

# cursor.execute('INSERT INTO Training.dbo.S VALUES (?, ?)', (id, name))

# cursor.commit() # this line is required to commit the changes to the database

# cursor.close()

# conn.close()