# python code "merge sheets in one excel to one sheet"
import openpyxl
import pandas as pd
import random

workbook_url = 'C:/Users/SADEGHI/Desktop/New folder (2)/file/bazresi.xlsx'
all_dfs = pd.read_excel(workbook_url,sheet_name=None , skiprows=2 , header = 1)

p = list(range(1,23))

df_2 = pd.DataFrame()

# l = list(all_dfs.items())
for n in p:
    r = str(n)
    all_dfs = pd.read_excel(workbook_url,sheet_name=r , skiprows=1)
    # g = pd.concat([all_dfs] , ignore_index=True)
    df_2 = df_2.append(all_dfs)

df_2.to_excel(r'C:/Users/SADEGHI/Desktop/New folder (2)/file/behavior1.xlsx', sheet_name='sheet1', index = False,header=True)

# warning !!! : copy writting 2021  mnm & mrs