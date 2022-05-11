import pyodbc
import pandas as pd
db = pyodbc.connect('Driver={SQL server};' 'server=Nisarbasha;' 'Database=Testdata;' 'Trusted_connection=yes;')
cursor = db.cursor()
cursor.execute('if OBJECT_ID(\'demotext\') IS NOT NULL DROP TABLE demotext')
db.commit()
res=cursor.execute('select * from demotext')
print(res)
try:
    record = cursor.execute("select * from demotext")
    if record:
        cursor.execute('drop table demotext')
        cursor.execute('create table demotext(empid nvarchar(30), empname nvarchar(40), salary int')
        db.commit()
except Exception as e:
    cursor.execute('create table demotext(empid nvarchar(30), empname nvarchar(40), salary int)')
    db.commit()


file = pd.read_excel(r'D:\Demotest01.xlsx')
file.to_csv(r'D:\Datasheet.csv', index=None, header=True)