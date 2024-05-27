#By Clark Daryll B Omasdang
#IT1R13

from collections import deque

def my_stack():
    cat = deque()
    return cat
    
def push(cat):    
    for muc in range(4):
        cat.append(input("Type something: "))
        print("Your current values sir:\n", cat)
        
    elgato = input("Which one would you like to be gone left or right last value?: ")
    
    if elgato.lower() == "left":    
        cat.popleft()
        print("It's gone now so here you go:\n", cat)
    elif elgato.lower() == "right":
        cat.pop()
        print("Gone reduced to atoms:\n", cat)

stack = my_stack()
push(stack)

    