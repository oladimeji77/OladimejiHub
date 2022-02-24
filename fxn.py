#to reuse a code

from cgitb import reset
from tkinter import Y


def fxn():
    pass

def squareroot(name):
    return name**2
sqr3 = squareroot(6)
print(sqr3)

def add2(num=0):   #you can save the result of a print function, use return instead so that the value can be stored in a variable
    return num+2
seven = add2(7)
nothing = add2() # it will not fail because it was set to a value by default.
print(seven)
print(nothing)


##Built-in python  functioms
# max and min
print(max(2,3))  #return max number 3
print(max([1,4,3,6,8,9])) #returns max number in a list
print(min(5,7))  #return min number

#Enumerate fxn

mylist = ['a', 'b', 'c']
index = 0
for letter in mylist:
    print(letter) 
    print(f'is at {index}')
    index = index+1
    print("")

mylist2 = ['d', 'e', 'f']
for item in enumerate(mylist2):
    print(item)

#Now unpack the tuple pair
for index,item in enumerate(mylist2):
    print(item)
    print(f"is at index: {index}")
    print("")

#Join function

mylist3 = ['a', 'b', 'c']
print("".join(mylist3))
print("--".join(mylist3))
print("+".join(mylist3))

#Fxn excersie Secret check, scheck if the work "secret" is in a string.

def secret_check(text):
    if "secret" in text:
        return True
    else:
        return False
print(secret_check("my little secret"))
#Alternatively, which is also d best way
def secret_check(text):
    return "secret" in text.lower()        # "secret in text"this is going to return a boolean, .lower incase of an edge case of capital letter "SECRET"
print(secret_check("my little SEcret"))


#Exercise 2 Check if Vowel is in a string

def vowel_check(mystring):
    for letter in mystring:
        for vowel in "aeiou":
            if vowel==letter:
                return vowel
print(vowel_check("yidjgh"))

#Calling fxn

def add(x,y):
    print(x+y)
add(8,4)
def add(x,y=5): #default value for y in case it is not specifed
    print(x+y)
add(5)
#defaul value ust be in the end of the parameter list e.g def add(def add(x=6,y=5) and not def add(x=4,y)
def add(x,y):
    return(x+y)
add(8,4)  #this would no print 12, but rather would return None
#All function return None by default
result = add(6,3)
print(result)

def division(dividend, divisor):
    if divisor != 0:
        return dividend/divisor
    else:
        return "Nonesense divison"
result2 =division(76,2)
print(result2) 

#Taking multiple arguments Pcking arguments

def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(3,2,4))
#unpacking arguments
def add(x,y):
    return x+y
nums= [4,5]
print(add(*nums))