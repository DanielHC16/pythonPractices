# NumPy or Numeric Python - Alternative to Python List: The NumPy Array 
import numpy as np # type: ignore

# Calculation over an Array 
""
grades1 = [94, 96, 95, 92]
grades2 = [94, 92, 98, 94]

weights = [10, 15, 20, 25, 30, 35, 40, 45, 50]
npweights = np.array(weights)

print("The Combined Weight of all Weights is: ", sum(weights), "kg")


npgrades1 = np.array(grades1) # Created np array
npgrades2 = np.array(grades2)

                #0      1       2       3      4
np2D = np.array([[9.16, 12.23, 12.05, 4.24, 5.20], # 0 
                [9.17, 10.27, 8.24, 6.23, 6.66],   # 1
                [1.23, 2.34, 3.45, 9.16, 5.67]])   # 2

print("(Rows, Columns)", np2D.shape) # 3 Rows 5 Columns
print("2nd Row, 4th Column: ", np2D[1][3]) # Calling Specific Index from a 2D Array
print("3rd Row, 3rd Column:" , np2D[2, 2]) 
print("2D Array Slicing and Selecting: \n", np2D[:, 0:3])
print("2nd Row Only: ", np2D[1, :])
print("Adding the 2nd Row, 4th Column + 1st Row, 1st Column: ", np2D[1, 3] + np2D[0, 0])
print("Average of the 2D Array: ", np.mean(np2D[:, :])) # Mean Function, (Finds the Average)
print("Median of the 2D Array: ", np.median(np2D[:, :])) # Median Function, (Sorts, then finds middle value)
print("Median of the 1st Row: ", np.median(np2D[0, :]))
print("Median of the 2nd Row: ", np.median(np2D[1, :]))
print("Median of the 3rd Row ", np.median(np2D[2, :]))
print("2D Array Sorted in Order per row: \n", np.sort(np2D)) # Sort Function
print("Correlation of 1st and 2nd Row: \n ", np.corrcoef(np2D[0, :], np2D[1, :])) # Correlation Function
print("Standard Deviation of 2D Array: ", np.std(np2D)) # Standard Deviation Function 
""""
arr1 = grades1 + grades2 
print("No NumPy: ", arr1)

arr2 = npgrades1 + npgrades2
print("With NumPy: ", arr2)

avg1 = sum(arr1) / len(arr1)
print("Average (Without NumPy): ", avg1)

avg2 = sum(arr2) / len(arr2)
print("Average (With NumPy): ", avg2)

highhonors1 = npgrades1 >= 95
print("1st Grades Greater than or Equal to 95: ", highhonors1) # Boolean Array using np
"""