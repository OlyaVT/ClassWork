# create class polygon and rectangle
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides= [float(input("Enter side"+str(i+1)+":"))for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)

    def findArea(self):
        a, b = self.sides
        area = a*b
        print("The area of rectangle is %0.2f" %area)

r = Rectangle()
r.inputSides()
r.findArea()

#create class car which has 3 parameters and 2 methods
class Car:
    def __init__(self, name, make, model):
        self.car_name = f'car {name}'
        self.car_make = f'from  {make}'
        self.car_model = f'model  {model}'

    def start(self):
        print(f'Your {self.car_name}, {self.car_model} {self.car_make} has started.')

    def stop(self):
        print(f'Your {self.car_name}, {self.car_model} {self.car_make} has stopped.')


i = Car('Hyundai', 'South Korea', 'I40')
i.start()
i.stop()

#create class car and class person
class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f'Hello, my name is {self.name}')


class Car:
    def __init__(self, name):
        self.name = name

    def move(self, speed):
        print(f'Max speed {self.name} is {speed} km/h')


person_info = Person("Olya")
person_info.info()

car_name = Car("I40")
car_name.move("170")