import numpy as np
import pandas as pd

world_score = {"Philippines":123.45,
         "Korea":246.89,
         "Japan":137.91 }

np_heights = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weights = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weights / np_heights ** 2
meas = np.array([np_heights, np_weights])

brics = pd.read_csv(r"C:\Users\Hardy\OneDrive\Desktop\Datasets\brics.csv", index_col=0)
""""
# 1 Looping through a dictionary
for key, value in world_score.items() :
    print(key + " : " + str(value))

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for x, y in europe.items() :
    print("the capital of " + x + " is " + y)

# 2 Looping a numpy array
for val in bmi :
    print(val)

# Looping a 2D numpy array
for val in np.nditer(meas) :
    print(val)
"""

# Looping through a pandas dataframe 

#for lab, row in brics.iterrows() :
    #print(lab)
    #print(row)
    # Selective print
   # print(lab + " : " + row["Capital"])

# Sample printout w/o CV data   
#for lab, row in cars.iterrows() :
    #print(lab + ": " + str(row['cars_per_cap']))

# Adding Column

# Creating a series on every iteration
#for lab, row in brics.iterrows() :
 #   brics.loc[lab, "Name_Length"] = len(row["Country"])
#print(brics)

# Easier and more effective method ^^
for lab, row in brics.iterrows() :
    brics["Name_Length"] = brics["Country"].apply(len)
print(brics)