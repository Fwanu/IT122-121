def bub(array):

    for x in range(len(array)):   

        for y in range(0, len(array)-1-x):
        
            x1 = y
            x2 = y + 1

            if array[x1] > array[x2]:
                
                temp = array[x1]
                array[x1] = array[x2]
                array[x2] = temp


    return array            
                

def sel(array):
    for x in range(len(array)):
        
            
        smol = min(array[x:])
        smolin = array.index(smol)
            
            
            
        if array[smolin] < array[x]:
            temp = array[x]
            array[x] = smol
            array[smolin] = temp
            
     
    return array       
            
            
def ins(array):
    for x in range(1, len(array)):
        y = x - 1
        xx = array[x]
        
        while y >= 0 and xx < array[y]:
            array[y+1] = array[y]
            y = y - 1
            
        array[y + 1] = xx
        
    return array

            
arrbub = [26,48,12,92,28,6,33]
arrsel = [26,48,12,92,28,6,33]
arrins = [26,48,12,92,28,6,33]

print("{} - bubble sort - It works by detecting and swapping value one by one to the right or the left position beside it continously using the formula arrlen - 1 \n".format(bub(arrbub))) 
print("{} - insertion sort - It works by detecting the smallest value and moving it to the n+1 index where n starts at 0 until all values are at their correct positions\n".format(ins(arrins)))
print("{} - selection sort - It works by making the 1st index (arrindex[0]) as a middle point where everything smaller than it is moved to the index before it and the value higher than it moved to the index after it. the new arrindex[0] then becomes the middle point until n loop are finished and all values are organized".format(sel(arrsel)))


"""3. What are the advantages and disadvantages of each of the following sorting algorithms?

d.	Bubble Sort - super simple | time complexity is super duper long, and a waste of ram
e.	Selection Sort - super simple | time complexity is best out of 3
f.	Insertion Sort - efficient for small data set | really slow on big data sets, also needs set to be already sorted in a way cus it'll take too long if not

"""
