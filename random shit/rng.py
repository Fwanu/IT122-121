# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random



arraytarget = []
arraylength = len(arraytarget)

while arraylength != 5:
    
    
    
    arrayrand = random.randint(0,100)
    
    arraytarget.append(arrayrand)
    
    print(arraytarget)
    
    arraylength = len(arraytarget)
    
    if arraylength == 5:
        redo = str(input("Do you want to continue? (yes or no): "))
        if redo == "yes":
            arraytarget.clear()
            arraylength = len(arraytarget)
            continue
        else:
            break
