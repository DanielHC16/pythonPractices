import pandas as pd 
import numpy as np

brics = pd.read_csv(r"C:\Users\Hardy\OneDrive\Desktop\Datasets\brics.csv", index_col=0)

#print(brics)

#is_huge = brics.loc[:, "Area"] > 8

#print(brics[is_huge]) # Subset Pandas DataFrame

# Selected a specific column
# Performed Comparison
# Stored in a diff. variable
# print

# One-line method

#print(brics[brics["Area"] > 8])

# Boolean Operator on Pandas Dataframe

#print(brics[np.logical_and(brics["Area"] > 8, brics["Area"] < 10)])

lotsa_pops = brics['Population'] > 200
print("Population greater than 200:\n", brics[lotsa_pops])

specific_pops = np.logical_and(brics['Population'] > 200, brics['Population'] < 1300)
print("Population greater than 200 and less than 1300:\n ", brics[specific_pops])