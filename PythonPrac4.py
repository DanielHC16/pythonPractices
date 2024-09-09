X = 0

#while X < 10: # while is a repeated if statement
 #   X += 1 
  #  print(X)

    # while condition :
        # expression

error = 50

#while error > 1:
 #   error = error / 4 # update variable
  #  print(error)

offset = 12

#while offset != 0 :
 #   print("correcting...")
  #  if offset > 0 :
   #   offset = offset - 1
    #else : 
     # offset = offset + 1
    #print(offset)

# for loop
# for variable in sequence : 
    # expression

fam_num = [04.24, 5.20, 12.23, 09.16, 12.05] 

for birthDate0 in fam_num:
    print(birthDate0)

for index, birthDate in enumerate(fam_num):
    print("Index: " + str(index) + ': ' + str(birthDate))

for letter in "Camacho":
    print(letter.capitalize())