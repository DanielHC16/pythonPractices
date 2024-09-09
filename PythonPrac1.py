nMonths = 12
mSavings = 12000
tSavings = (nMonths * mSavings)
months = ["Jan", "Feb", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
fhMonth = months[0:7]
lhMonth = months[7:12]

birthdays = [["Daniel", "September 16"],
             ["Kurt", "December 23"],
             ["Elaiza", "December 5"],
             ["Laliza", "May 20"],
             ["Dennis", "February 24"]]

pet_dogs = ["Warwick ", 9, "Batusai ", 8, "Tisoy ", 4, "Dobie", 5]
pet_cats = ["KongKong ", 6, "Maya ", 5, "Kidlat ", 4]


del pet_dogs[6:8] # Remove element in a list 


x = ["A", "B", "C"]
y = list(x) # List Slicing Method 1
#y = x[:] # List Slicing Method 2
y[1] = "Z"

print(x)
print(y)

"""print("Dog Pets:", pet_dogs)
print("Cat Pets:", pet_cats)

pet_all = pet_dogs + pet_cats
print("All the pets:", pet_all)

pet_black = pet_dogs[0] + pet_cats[4]
print("Black Colored Pets:", pet_black)
pet_white = pet_dogs[4] + pet_cats[2]
print("White Colored Pets: ", pet_white)
pet_pattern = pet_dogs[2] + pet_cats[0]
print("Patterned Pets: ", pet_pattern)

pet_age = pet_all[1],  pet_all[3],  pet_all[5], pet_all[7], pet_all[9], pet_all[11]
print("Pet Ages in Descending Order:", pet_age)

print("All the months in a year", months[0:12]);
print("Best Month of the Year: ", months[8])
print("First Half of the Year: ", fhMonth)
print("Second Half of the Year: ", lhMonth)
print(birthdays[0])
print(birthdays[3][0:2])
print(birthdays[1][0])"""