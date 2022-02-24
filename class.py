class Student:
    def __init__(self):
        self.name = "Oladimeji"
        self.age = 27
ola =Student()
print(ola.age)
print(ola.name)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
Eni = Student('Enitan', 34)
print(Eni.age)
print(Eni.name)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def average_grade(self):  #This function needs to be called to be used on an object
        return sum(self.grade)/len(self.grade)
Ufuoma = Student("Ufuoma", (50,34,56,78))  #Class call
print(Student.average_grade(Ufuoma)) #Calling the class on an object
print(Ufuoma.average_grade()) #alternative way of Calling the class on an object

#Magic method are init, str, repr. They dont need to be called during an object call
gclass Vehicle:
    def __init__(self, type, brand):
        self.type = type
        self.brand = brand 
    # def __str__(self):  #str method
    #     return f"My ride is {self.type} by {self.brand}"
    def __repr__(self):  #repr method
        return f"Vehicle: {self.type} and Brand: {self.brand}" #you need to comment str to see repr

car = Vehicle("Car", "Toyota")
print(car)

####################################################################
class Device:
    def __init__(self, name, connection_mode):
        self.name = name
        self.connection_mode = connection_mode
        self.connect = True
    def __str__(self):
        return f"This is a good {self.name}"
    def disconnect(self):
        return f"{self.name} has been disconnected"
        s
keyboard = Device("Keyboard", "PS2")
print(keyboard)
disc_keyboard = Device.disconnect(keyboard)
print(disc_keyboard)

class Printer(Device):
    def __init__(self, name, connection_mode, capacity):
        super().__init__(name, connection_mode)
        self.capacity = capacity
        self.remaining_pages = capacity
    def __str__(self):
        return f"{super().__str__()}, the remaining page is: {self.remaining_pages}"
    def print(self, pages):
        if not self.connect:
            print("Your printer is diconnected")
            return
        print(f"you are Printing {pages} pages")
        self.remaining_pages -= pages

HP = Printer("HP", "USB", 500)
print(HP)
print(HP.print(345))



