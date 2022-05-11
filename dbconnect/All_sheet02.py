import pandas as pd

excel_file = 'D:\Demotest01.xlsx'
df = pd.read_excel(excel_file, sheet_name=None)
xlsx = pd.ExcelFile(excel_file)
PC_sheets = []
for sheet in xlsx.sheet_names:
    PC_sheets.append(xlsx.parse(sheet))
    global PC
    PC = pd.concat(PC_sheets)

PC.to_csv('D:\Demo0000.csv', encoding='utf-8', index=False)
