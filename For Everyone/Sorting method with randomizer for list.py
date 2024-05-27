#set = {"fuck", "blyatt", "yawa"}
#print("blyatt" in set) #this method is used to check if the thing is in there

#tes = {"a", "b", "c"}
#tes.add("d")
#print(tes) this method is used to add something on the set

#setA = {"a", "b", "c",}
#SetB = {"c", "d" , "g"}
#setA.update(SetB)
#print(setA) used to update something by using the .update 

list = {"Kurva", "Polska", "Balkans"}
print(list)
lmao = input("Would?: ")
if lmao == "yes sir":
    list.discard(input("remove something: "))
    print(list)
else:
    print("okay")    