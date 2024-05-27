# - Made by Francis Niño Cahoy

arr = []
arr1 = []

try:
    arrsize = int(input("How many input?: "))

except ValueError:
    print("that aint a number")

for x in range(0, arrsize):
    
    try:
        arr.append(int(input("Insert number here: ")))
        
    except ValueError:
        print("Not a number")
        
    

arsum = sum(arr)
arverage = arsum / len(arr)
arr1 = arr.copy()
arr1.sort()
arr1verse = arr1.copy()
arr1verse.reverse()


print("""      average is {}
      sum is {}
      sorted is {}
      reversed is {}
      original list is {}""".format(arverage, arsum, arr1, arr1verse, arr))