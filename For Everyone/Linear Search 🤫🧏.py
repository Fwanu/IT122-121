# Clark Daryll B Omasdang ಥ⁠‿⁠ಥ
# IT1R13 
#Linear Search
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
    
aris = []
uwahh = int(input("How many index would you put UwU: "))
for plap in range(uwahh):
    plap = (input("Oi m8 Enter your stuff: "))
    aris.append(plap)
    aris.sort()
    print("Your arrays ༼⁠ ⁠つ⁠ ⁠◕⁠‿⁠◕⁠ ⁠༽⁠つ:", aris)
    target = aris
    

stuffed = input("Which stuff would you like to pick ⊂⁠(⁠´⁠･⁠◡⁠･⁠⊂⁠ ⁠):")
result = linear_search(aris, stuffed)
print(stuffed ,"Is found at index:", result)
