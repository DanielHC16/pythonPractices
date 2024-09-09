import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

# Simulate random walk 500 times
all_walks = []
for i in range(500):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            # If dice is less than or equal to 2, move 1 step down (cannot be below 0)
            step = max(0, step - 1)
        elif dice <= 5:
            # If dice is 3, 4, or 5, move 1 step up
            step = step + 1
        else:
            # If dice is 6, move a random number of steps between 1 and 6
            step = step + np.random.randint(1, 7)

        # Small chance of falling to step 0
        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t (transpose of all_walks)
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]

# Plot histogram of ends, display plot
#plt.hist(ends)
#plt.show()

# Count how many values in 'ends' are greater than or equal to 60
count = 0
for x in ends:
    if x >= 60:
        count += 1
print("End game step count less than or equal to 60:", count)

# Calculate the percentage of values in 'ends' that are greater than or equal to 60
count_percent = (count / len(ends)) * 100
print("Estimated Chance of at least reaching 60 steps high: ", count_percent, "%")
