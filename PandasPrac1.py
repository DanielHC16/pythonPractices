import pandas as pd

dict = {
    "Country":["Brazil", "Russia", "India", "China", "South Africa"],
    "Capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "Area":[8.516, 17.10, 2.286, 9.597, 1.221],
    "Population":[200.4, 143.5, 1252, 1357, 52.98]}
    
brics = pd.DataFrame(dict)
brics.index = ['BR', 'RU', 'IN', 'CH', 'SA']
#print(brics)

""""
# Selecting from a Dictionary
print(dict['Country'][0])
print(dict["Capital"][0])
print(dict['Area'][0])
print(dict["Population"][0])
"""

# Column Access using []
#print(brics['Country'])
#print(type(brics["Country"])) # Series is a 1 dimensional array that can be labeled. A bunch of series is a Dataframe
#print(brics[["Country"]])
#print(type(brics["Country", "Capital"])) # DataFrame 
#print((brics[["Country", "Capital"]])) # SubDataFrame

# Row Access using []
#print(brics[1:4]) # List Slicing

# Using pandas - loc(label-based), iloc(integer position-based)

# Row Access using loc
#print(brics.loc['RU']) # Series
#print(brics.loc[['RU']]) # DataFrame
#print(brics.loc[['RU', 'IN', 'CH']])

# Row and Column loc
#print(brics.loc[['RU', 'IN', 'CH'], ['Country', 'Capital']]) # Select Row and Column using loc 
#print(brics.loc[:, ['Country', 'Capital']]) # List Slicing + Row and Column Selection using loc

# Row Access using iloc
print(brics.iloc[1])
print(brics.iloc[[1]])
print(brics.iloc[[1, 2, 3]])

# Row and Column iloc
print(brics.iloc[[1], [1, 2, 3]])
print(brics.iloc[:, [0, 1]])