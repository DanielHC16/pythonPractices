# Manual List Method
pop = [273753191, 7425057, 33573874]
countries = ["Indonesia", "Laos", "Malaysia"]

ind_alb = countries.index("Laos")
print(ind_alb)
print(pop[ind_alb])

# Dictionaries
TopSeaPop = {"Indonesia":273753191, "Laos":7425057, "Malaysia":33573874} # Key-Value Pairs
print(TopSeaPop["Indonesia"])
print("3rd Most Populated SEA Country - Malaysia, Population:", TopSeaPop["Malaysia"]) # Pass the key, get the value 

team = ['Daniel', 'Tim', 'King', 'Iwag']
specialist = ['Lead', 'Fullstack', 'Frontend', 'Backend']

DreamTeam = {'Daniel':'Data', 'Tim':'Fullstack', 'King':'Frontend', 'Iwag':'Backend'}
print(DreamTeam)
print(DreamTeam['Daniel']) 
print(DreamTeam.keys()) # Keys have to be immutable - boolean, int, string
DreamTeam['Daniel'] = 'Lead' # Add more values to a Dictionary
print(DreamTeam)
print('Daniel' in DreamTeam)
#del(DreamTeam['Frieda']) # Deletes a Key
#print(DreamTeam)