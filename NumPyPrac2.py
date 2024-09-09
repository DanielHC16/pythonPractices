# Generate Data 
# matplotlib practice

import numpy as np
import matplotlib.pyplot as plt

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)

np_city = np.column_stack((height, weight))

print("Generated Data: ", np_city)
print("Average Height: ", np.mean(np_city[:, 0]))
print("Average Weight: ", np.mean(np_city[:, 1]))
print("Median Height: ", np.median(np_city[:, 0]))
print("Median Weight: ", np.median(np_city[:, 1]))
print("Correlation Between Height and weight: \n", np.corrcoef(np_city[:, 0], np_city[:, 1]))

plt.hist((np_city[:, 0], np_city[:, 1]), bins = 4)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height and Weight of a City")
plt.show()
# Note, Data Probably Not Accurate 