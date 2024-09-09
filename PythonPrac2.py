import math

Grades = [98, 99, 93, 96, 92]
maxFunc = max(Grades)

roundFunc = round(3.143, 2) # Round Function, (Input, Decimal Place to Round)
roundFunc2 = round (99.84) # Round Function, No Specifier

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

#help(round) - help() - Explains what a function does 
print(maxFunc)
print(roundFunc)
print(roundFunc2)
print(math.pi)