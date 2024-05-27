userinfo = []

# Ask the user how many pieces of information they want to input (maximum of 3)
numfo = int(input("How many info you want to reveal numbers only: "))
numfo = min(numfo, 3)  # Limit the number of information pieces to 3

# Input user information
for i in range(numfo):
    info = input(f"User information: ")
    userinfo.append(info)

# Display user information
print("\nUser Information:")
print(userinfo)

choice = (input("Would you like to update your information Yes/No: "))
#Choice again if you said yes
if choice.lower() == "yes":
    newuser = []
    user = int(input("Enter on how many you want to reveal numbers only ;): "))
    user = min(user, 3)
    
    for i in range(user):
       infoo = input(f"User information: ")
       newuser.append(infoo)
    print("\nNew User Information:")
    print(newuser)
    
elif choice.lower() == "no":
    print("ight fam no problem")    
    