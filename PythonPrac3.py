import numpy as np

names = ['Kurt', 'Daniel', 'Elai', 'Laliza', 'Dennis']
np_names = np.array(names)
numbers = [12.23, 09.16, 12.05, 05.20, 04.24]
np_numbers = np.array(numbers)

comparison = names[0] < names[1]
sortedComp = sorted(names)
#print(sortedComp)
#print(comparison)
#print(sorted(numbers))
#print(sortedComp)
#print(10 < np_numbers)

#print(np.logical_and(np_numbers < 13, np_numbers > 16))
#print(np.logical_or(np_numbers > 10, np_numbers < 16))
#print(np.logical_not(np_numbers > 10, np_numbers < 16))
#print(np_numbers[np.logical_and(np_numbers > 10, np_numbers < 16)]) # Numbers only

z = 9

if z % 2 == 0:
    print("checking: ", str(z))
    print("Z is divisible by 2")

elif z % 3 == 0:
    print("checking: ", str(z))
    print("Z is divisible by 3")

else :
    print("checking: ", str(z))
    print("Z is neither divisible by 2 or 3")
