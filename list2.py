numbers = [1,2,3]
double = []

for num in numbers:
    double.append(num *2)

print(double)

#Alternatively use list comprehension
numbers2 = [1,2,3]
double2 = [num2 * 2 for num2 in numbers2 ]

print(double2)

# to get items in a list strting with a letter e.g D
friends = ['deji', 'dami', 'deolu', 'habas']
start_d = []
for friend in friends:
    if friend.startswith('d'):
        start_d.append(friend)
print(start_d)

#Alternatively use list comprehension
friends2 = ['deji', 'dami', 'deolu', 'habas']
start_d2 = [friend2 for friend2 in friends2 if friend2.startswith('d') ]
print(start_d2)

print(friends2 is start_d2) #false
print("friends2: ", id(friends2), "start_d2: ", id(start_d2))

#to make 2 list thesame thing
friends2 = start_d2
print(friends2 is start_d2)



 