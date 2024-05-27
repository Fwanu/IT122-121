#Clark Daryll B Omasdang
#IT1R13
#Binary search
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  

momoi = []
nig = int(input("How many arrays?:"))
for n in range(nig):
    n = input("Enter something:")
    momoi.append(n)
    momoi.sort()
    print("Your arrays sir (⁠　⁠･⁠ω⁠･⁠)⁠☞ ", momoi)


kuyashi = input("What number in the list would you like to pick (⁠•⁠‿⁠•⁠): ")
result = binary_search_iterative(momoi, kuyashi)
print(kuyashi, "Is found at index:", result)
