import pandas as pd 
df = pd.read_csv('nyc_weather.csv')  #path of the directory, here nyc_weather is in the same directory so we have defined only the sngle path 
#ques1 - What was the maximum temmperature of new york in the month of january ?
m=df['Temperature'].max()
print(m)
#Q2 On which day it rains?
r=df['EST'][df['Events']== 'Rain']
print(r)
#q3 what was the average speed of the wind during the month ?
s=df['WindSpeedMPH'].mean()
print(s)
