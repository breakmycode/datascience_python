import pandas as pd 
#this is a hasmap or in terms of python it is called ddictionary 
india_weather = pd.DataFrame({"city":["mumbai","delhi","bangalore"],"temperature":[32,45,30], "humidity":[80,60,78]})
us_weather = pd.DataFrame({"city":["newyork","chicago","oriando"],"temperature":[62,65,75], "humidity":[21,14,35]})

#concate two dataframes 
df = pd.concat([india_weather,us_weather])

# if we want continous index
df1 = pd.concat([india_weather,us_weather], ignore_index=True)

# if i want to concatenate the df by columns side by side not below one row to another 
df2 = pd.concat([india_weather,us_weather], axis=1)

print(df2)