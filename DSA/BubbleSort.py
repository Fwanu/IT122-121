def fuck(array):

    for x in range(len(array)):   

        for y in range(0, len(array)-1-x):
        
            x1 = y
            x2 = y + 1

            if array[x1] > array[x2]:
                
                temp = array[x1]
                array[x1] = array[x2]
                array[x2] = temp


    return array            
                
arr = []

for x in range(0,10):
    countdown = 10 - x
    inp = int(input("Enter a number here {0} times more: ".format(countdown)))
    arr.append(inp)

fuck(arr)
print("""The sorted goes as follows: 
      {0}
      The maximum is: {1}
      The minimum is: {2}
      And all of it summed up is: {3}""""".format(arr, min(arr), max(arr), sum(arr)))

print("Passed by Francis Niño Cahoy BSIT 1R13")

