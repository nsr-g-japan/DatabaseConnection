import pandas as pd

excel_file = 'C:\\Users\\nisar\\g-japan.com\\GJN Workspace - Documents\\000 GJN_Projects\\3. Excel Templates\\00_SQL Testing\\Factforpowerapps.xlsx'
all_sheets = pd.read_excel(excel_file, sheet_name=None)
sheets = all_sheets.keys()

for sheet_name in sheets:
    sheet = pd.read_excel(excel_file, sheet_name=sheet_name)
    sheet.to_csv('D:\\test%s.csv' % sheet_name, index=False)
