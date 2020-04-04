import pandas as pd 
# merging is like the joins in sql datbase operations 

temperature_df = pd.DataFrame({"city":["mumbai","delhi","bangalore","hyderabad"],"temperature":[32,45,30,40]})

humidity_df = pd.DataFrame({"city":["mumbai","delhi","bangalore"],"humidity":[68,65,75]})

#merge two dataframes with out explicity mention index , here based on 'city 

df1 = pd.merge(temperature_df, humidity_df, on='city', how='inner')
# now in temperature dataframe , we had hyderabad , but in humdity we didnt have the hyderabad 
# for overcoming this problem , we have to do outer Join

#OUTER-JOIN
df2= pd.merge(temperature_df, humidity_df, on='city', how='outer')

print(df1)

