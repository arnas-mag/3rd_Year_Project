import pyodbc;

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER= root;DATABASE= group_project;Trusted_Connection=yes;')

cursor = connection.cursor()
cursor.execute("show tables")

while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row.version)

    cursor.close()
    connection.close()