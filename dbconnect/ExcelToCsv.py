import pandas as pd

file = pd.read_excel(r'D:\test.xlsx')
file.to_csv(r'D:\Newsheet.csv', index=None, header=True)

