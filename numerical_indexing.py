import pandas as pd 
df  = pd.DataFrame([1,2,3,4,5,6,7,8,9,19], index=[49,48,47,46,45,1,2,3,4,5])

#row numbers are the default indices 
#now we want some different indices



# now i want to access these alies , i want to know what is the value of the data stored at the index 46
# access by row number 
# here wewill use loc and iloc 
# loc= location( it used index  , iloc=index location( it used the row umber )

a1=df.loc[46]

a2=df.iloc[8]

print(a2)




