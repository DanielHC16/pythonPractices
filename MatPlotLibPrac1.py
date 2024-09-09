import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2012]
pop = [2.519, 3.692, 5.263, 6.972]

dogs = ["Warwick", "Batusai", "Tisoy"]
age = [8, 7, 4]

values = [0.23, 2.4, 2.45, 2.56, 5.12, 5.66, 7.77, 8.8, 9.2, 9.12, 11.11, 12.23]

# Plot
plt.plot(year, pop)
plt.xlabel('Year')
plt.xscale('log') # Logarithmic Scale
plt.ylabel('Population (in billions)')
plt.title('World Population Over Years')
plt.show()
plt.clf()

# Scatter
plt.scatter(dogs, age)
plt.xlabel("Dog Names")
plt.ylabel("Age")
plt.title("the Camacho Dogs")
plt.show()
plt.clf()

# Histogram

plt.hist(values) # plt.hist(variable, bins=)
plt.show()
plt.clf()