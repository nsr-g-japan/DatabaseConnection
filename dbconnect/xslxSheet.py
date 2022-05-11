import csv

import openpyxl
from openpyxl import load_workbook

ws = load_workbook('D:\Demotest01.xlsx')
sheets=ws.get_sheet_names()
print(sheets)
sheet_value_arr = []
print(sheets)