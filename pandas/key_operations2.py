import pandas as pd
df  = pd.read_csv('weather_data_cities.csv')
g = df.groupby('city')
#for city,city_df in g:# Indices has been copied 
    #print(city)
    #print(city_df)
#print(g.max()) #find maximum temperature in each of the cities.
#print(g.mean())
print(g.describe())