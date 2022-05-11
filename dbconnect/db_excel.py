import pyodbc
import pandas as pd
db = pyodbc.connect('Driver={SQL server};' 'server=Nisarbasha;' 'Database=Testdata;' 'Trusted_connection=yes;')
cursor = db.cursor()
tablename='demotext'
l1=['empid', 'empname', 'salary']
clmstr=''
for i in l1:
  clmstr += i+' int, '
print(str)

cursor.execute('if OBJECT_ID(\'{0}\') IS NOT NULL DROP TABLE {0}'.format(tablename))
#cursor.execute('create table {}(empid nvarchar(30), empname nvarchar(40), salary int)'.format(tablename))
cursor.execute('create table {}({})'.format(tablename,clmstr))
db.commit()
#record = cursor.execute("select * from demotext")




#cursor.execute("BULK INSERT demotext FROM 'D:\Datasheet.csv' WITH (format = 'CSV', FIRSTROW= 2, FIELDTERMINATOR=',', "
 #              "ROWTERMINATOR='\n');")
#cursor.execute('select * from demotext')
#rows = cursor.fetchall()

#for row in rows:
 #   print(row)

# cursor.execute('create table emp(id int, emp_name nvarchar(40))')
# cursor.execute('drop table demo01')


db.commit()
