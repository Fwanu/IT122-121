# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
i = 0
while i != 1:
 name = str(input('insert your name here: '))
 namecon = name.isalpha()
 while namecon == False:
    print("Invalid input")
    name = str(input("Insert your name here: "))
    namecon = name.isalpha()
 else:
    print("pass")
    namecon == True
 age = str(input('insert your age here: '))
 agecon = age.isnumeric()
 while agecon == False:
    print("Invalid input")
    age = str(input('insert your age here: '))
    agecon = age.isnumeric()
 else:
    print("pass")
    agecon == True
 print("I'm {0}, and I'm {1} years old".format(name, age))        
 loopcon = str(input('Do you want to continue?(yes/no): '))
 if loopcon == "yes":
     i = 0
 else:
     i = 1