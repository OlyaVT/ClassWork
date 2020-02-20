# функція, яка знаходить середнє арифметичне
def avg_tuple(*args):
    sum = 0
    for i in args:
        sum = sum +i
        res = sum / len(args)
    return res
print(avg_tuple(5,6,7))


def avg_tuple(*args):
    Sum = sum(args)
    res = Sum / len(args)
    return res
print(avg_tuple(5,6,7))

#функція, яка повертає абсолютне значення числа

def absol(x):
    """Calculate absolute value"""
    return (x**2)**0.5
print(absol(-5))

def absol(x):
    return abs(x)
print(absol(-9))

#функція, яка знаходить максимальне число з двох

def max_value(a, b):
    """find maximum value"""
    if a > b:
        print (a, "is max")
    elif a == b:
        print("No max")
    else:
        print (b, "is max")
print(max_value(5, 8))

# площі фігур на вибір

def rectangle():
    a = float(input("Input width:"))
    b = float(input("Input height:"))
    print("Square={}".format(a*b))

def triangle():
    a = float(input("Input basis:"))
    h = float(input("Input height:"))
    print("Square={}".format(0.5*a*h))

def circle():
    PI=3.14
    r = float(input("Input radius:"))
    print("Square={}".format(PI*r**2))


figure = input("1 - rectangle, 2 - triangle, 3 - circle:")
if figure == '1':
    rectangle()
elif figure == '2':
    triangle()
elif figure == '3':
    circle()
else:
    print ("Input error")

# функція, яка обчислює суму цифр введеного числа
def sum_values():
    a = int(input("Enter number:"))
    b = [int(x) for x in str(a)]
    c = sum(b)
    print("Sum of values is: ", c)
sum_values()

# калькулятор

def add_num():
    a = int(input("Enter namber a:"))
    b = int(input("Enter namber b:"))
    print ("Sum of a and b is {}".format(a+b))
def subst_num():
    a = int(input("Enter namber a:"))
    b = int(input("Enter namber b:"))
    print ("Difference between a and b is {}".format(a-b))
def mult_num():
    a = int(input("Enter namber a:"))
    b = int(input("Enter namber b:"))
    print ("Product of a and b is {}".format(a*b))
def div_num():
    a = int(input("Enter namber a:"))
    b = int(input("Enter namber b:"))
    print ("Result of division a and b is {}".format(a/b))

calc = input("1 - add, 2 - substruct, 3 - multiply, 4 - divide: ")
if calc == "1":
    add_num()
elif calc == "2":
    subst_num()
elif calc == "3":
    mult_num()
elif calc == "4":
    div_num()
else:
    print ("Wrong choice")



# функція для чисел Фібоначі з рекурсією
def fibo_recur(n):
    if n<=1:
        return n
    else:
        return(fibo_recur(n-1)+fibo_recur(n-2))
print(fibo_recur(4))

# функція, що обчислює дискримінант

def discriminant():
    x = float(input("Enter x:"))
    y = float(input("Enter y:"))
    z = float(input("Enter z:"))
    discriminant = (y**2)-(4*x*z)
    if discriminant > 0:
        print("Discriminant value is ", discriminant)
    elif discriminant == 0:
        print("Discriminant value is ", discriminant)
    elif discriminant < 0:
        print("Discriminant value is ", discriminant)

print(discriminant())
