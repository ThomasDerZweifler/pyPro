import pandas as pd

# sudo apt-get install python3-xlrd

# index_col=0 tells pandas that column 0 is the index and not data 
dfs = pd.read_excel('test.xlsx', sheet_name='Tabelle1')
print(dfs.head())