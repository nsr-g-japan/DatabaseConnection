l = []
s = ''
#l1=['empid', 'nvarchar(200)', 'empname', 'int', 'select data', '', 'id', 'nvarchar(200)', 'select data', 'select data', '']
#l1=['empid', 'int', 'empname', 'nvarchar(200)', 'salary', 'int', '', 'id', 'int', 'ename', 'nvarchar(200)', 'select data', '']
#l1=['empid', 'nvarchar(200)', 'empname', 'nvarchar(200)', 'select data', '', 'id', 'int', 'select data', 'demo', 'nvarchar(200)', '']


l1=['empid', 'nvarchar(200)', 'select data', 'salary', 'int', 'done', 'id', 'int', 'select data', 'demo', 'nvarchar(200)', 'done']

for i in l1:
    if i != 'select data':
        s = s + i +","+ " "
print(s)
l2=s.split('done')
print(l2)
x=''





#l.remove('')
