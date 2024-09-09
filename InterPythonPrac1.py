# Hacker Statistics
import numpy as np
#np.random.rand() # Psuedo random numbers


# Coin Flip
#np.random.seed(123)
coin = np.random.randint(0, 2) # Randomly Generate 0 or 1
if coin == 0:
    print("Heads")
else:
    print("Tails")

# Dice
landed = np.random.randint(1, 7) # Spots on a dice
print(landed, "point Dice roll")
print(np.random.randint(1, 7), "point Dice roll")

# Dice game 

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1, 7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice, "point/s rolled")
print("Current Step:", step)