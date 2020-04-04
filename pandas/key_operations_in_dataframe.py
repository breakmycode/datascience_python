import pandas as pd 
#import xlrd
df = pd.read_excel('weather_data.xlsx')
df.to_csv('new.csv')
df.to_csv('new_noIndex.csv', index=False)
df.to_excel('new.xlsx', sheet_name='weather_data',index=False)