import numpy as np
import matplotlib.pyplot as plt


years = list(range(1910, 2101))
initial_population = 1.75  # in billions
growth_rate = 0.011  # 1.1% annual growth rate
population = [initial_population * (1 + growth_rate) ** (year - 1910) for year in years]
# Note: Data Inaccurate, Population Continously Increaes by 1.1% 

# Adding more Data
years = [1800, 1850, 1900] + years
population = [1.0, 1.262, 1.650] + population

plt.plot(years, population)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Population Growth per year by 1.1%")
plt.yticks([0, 2, 4, 6, 8, 10],
           ['0', '2B', '4B', '6B', '8B', '10B'])
plt.show()