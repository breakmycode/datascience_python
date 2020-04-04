import pandas as pd 
weather_data = [('1/1/2017', 32,6,'Rain'),('1/2/2017', 35,7,'Sunny'),('1/1/9', 23,9,'Snow')]
df = pd.DataFrame(weather_data, columns=['day', 'temperature','windspeed','event'])
#=df.shape
a1=df.tail()
a2=df.columns # prints coloumns in a table
a3=df.day #print particular column data 
#df['day'] #Another  way of accessing columns
# if I want the data for two columns then the syntax goes like  following 
a4=df[['day','event']]
a5=df['temperature'].max()# prints max temperature
a6=df['temperature'].min()#prints min temperature
a7=df['temperature'].describe()# it displays  all the values such as std,min,maximum temperature that is required 
a8=df[df.temperature == df.temperature.max()]# this will tell which row has the maximum temperature 

# select only day coloumn which has the maximum temperature
a9=df.day[df.temperature == df.temperature.max()]
print(a9)
