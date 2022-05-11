import pyodbc
import pandas as pd
db = pyodbc.connect('Driver={SQL server};' 'server=Nisarbasha;' 'Database=Testdata;' 'Trusted_connection=yes;')
cursor = db.cursor()
tablename='nisarr'
l1=['empid', 'empname', 'salary']
clmstr=''
for i in l1:
  clmstr += i+' int, '
print(str)

#cursor.execute('create table {}(empid nvarchar(30), empname nvarchar(40), salary int)'.format(tablename))
#cursor.execute('create table {}({})'.format(tablename,clmstr))
cursor.execute('create table {}(empis int)'.format(tablename))
db.commit()
#record = cursor.execute("select * from demotext")
