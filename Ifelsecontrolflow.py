#Control flow if, else and elif

if 1>2:
    print("Yep!")

if 1==2:
    print("Yep!")

username = "users"
Check = "Admin"
permission =True
if username == Check and permission:
    print("Access Granted")
elif username == "users":
     print("No admin access")
else:
    print("access denied")

#Numeber Game
number = 45
user_input=input("Enter 'y' if you want to play").lower()
if user_input == "y":
    user_number = int(input("Enter a number"))
    if user_number == 7:
        print("You guessed correctly")
    elif number - user_number in (1, -1): # abs(number - user_number) ==1Y
        
        print("you are off by one")
    else:
        print("You are totally off")

