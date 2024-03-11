# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

arr = []
pop = 0
i = 1

while i != 0:
    
    
    info = input("Input information here one by one, then input e- if done: ")
    arr.append(info)
    print(arr)
    
    
    if info == "e-":
        arr.pop(-1)
        print()
        print("\n {0}".format(arr))
        
        cloop = 1
        
        while cloop == 1:    
        
            try:
                choice = int(input("""1 - edit
2 - update/add
3 - insert
4 - remove
5 - end
Pick a choice: """))
                
    
            except ValueError:
                print("That's not a number bruv")
                continue
            
            if choice == 1:
            
                lop1 = True
            
                while lop1 == True:
                    print("\n{0}".format(arr))
                    arrcount = len(arr)
            
                    bleh = int(input("Insert number of sequence you wanna edit: "))
                
                
                    if bleh > arrcount:
                        print("Bruh, that's called adding")
                    
                    elif bleh < 0:
                        print("I don't hold negative indexes moron")
                    
                    else:
                        replace = input("What do you want to replace this data with?: ")
                    
                    arr[bleh-1] = replace
                    print("\n{0}".format(arr))
                    
                    break
                
            if choice == 2:
            
                lop2 = True
                
                while lop2 == True:
                    print("\n{0}".format(arr))
                    info = input("Input information here one by one, then input e- if done: ")
                    arr.append(info)
                    print(arr)
    
    
                    if info == "e-":
                        arr.pop(-1)
                        print()
                        print("{0}".format(arr))
                        lop2 = False
                        break
                    
            if choice == 3:
                
                lop3 = True
                
                while lop3 == True:
                    arrcount = len(arr)
            
                    bleh = int(input("Insert number of sequence you wanna edit: "))
                
                
                    if bleh > arrcount:
                        print("Bruh")
                    
                    elif bleh < 0:
                        print("Bruh")
                    
                    else:
                        replace = input("What do you want to input here? (it shifts all the value order to the right): ")
                    
                    arr.insert(bleh-1, replace)
                    print("\n{0}".format(arr))
                    
                    break
                    
            if choice == 4:
                
                lop4 = True
                
                while lop4 == True:
                    arrcount = len(arr)
            
                    bleh = int(input("Insert number of sequence you wanna edit: "))
                
                
                    if bleh > arrcount:
                        print("Bruh, that's called adding")
                    
                    elif bleh < 0:
                        print("I can't delete that order moron")
                    
                    
                    
                    arr.pop(bleh-1)
                    print("\n{0}".format(arr))
                    
                    break
                
            if choice == 5:
                
                print("\n{0}".format(arr))
                i = 0
                break
                
            
            
                
            # put in end
            if choice > 5 or choice <= 0:
                print("That's not a choice mate")
                continue
        
        print("GG I'm done")
    
    
