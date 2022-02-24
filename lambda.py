#used to operte on input and produce output


def add(x,y):
    return x+y
print(add(5,6))

#Using lambda fxn
print((lambda x,y: x+y)(5,7))

#Another example
def double(x):
    return x*2
lambda_notation = (lambda x:x*2)
sequence = [1,2,3,4,5,6,7,8]
#using list comprehension
double = (x*2 for x in sequence)
print(double)
double = (double(5) for x in sequence)
print(double)
double= ((lambda x: x*2)(5) for x in sequence)
print(double)
double = map(double, sequence)
print(double)
double = list(map((lambda x:x*2)(5), sequence))
print(double)