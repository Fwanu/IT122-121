loop = 5
print("Welcome to the average-ier; This baby averages everything you input upto five times. Inputting anything but a number will end the program and prints out the average early\n")

for x in range(0, loop): # can be turned to while loop for infinite average-ing
    try:
        equals += int(input("Insert number here: ")) # += adds number from equals and input method and storing to equals variable
    except:
        print("not a number mate")
        break
        
    
average = equals / x

print("The average of those numbers is {0}".format(average))
