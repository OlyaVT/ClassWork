#створити список цілих чисел і знайти їх макс та мін значення
num_list = [int(input("Enter int {}: ".format(i+1))) for i in range(int(input("Enter amount")))]
print(num_list)
print("Max number is:", max(num_list))
print("Min number is:", min(num_list))

#в інтервалі(1-10) визначити числа, які діляться на 2, які діляться на 3 
#та числа, які не діляться на 2 та 3
a = [x for x in range(0, 11) if x%2 == 0]
print (a)
b = [x for x in range(0, 11) if x%2 == 1]
print (b)

c = [x for x in range(0, 11) if x%2 != 0 and x%3 != 0]
print (c)

#факторіал числа
a = int(input("Enter number:"))
fac = 1
if a< 0:
    print ("Sorry, factorial does not exist")
elif a == 0:
    print ("Factirial is 1")
else:
    for i in range(1, a+1):
        fac = fac*i
    print ("The factorial is", fac)

# перевірка чи вірний логін
log = input("Enter login: ")
while log != "First":
    log = input("Try again: ")
    
else:
    print ("Hello user!") 


# написати програму, яка зчитуватиме числа, поки не буде від'ємне число
a = int(input("Enter number>0:"))

while a > 0:
     if a > 0:
        a = int(input('Enter number >0:'))
else:
    print('You entered number <=0')

#на початку на вхід подається кількість елементів, а потім самі елементи
# при появі від'ємного числа програма зупиняється, при 0 - теж

a = int(input("enter number: "))
b = [int(input("Enter values of list: ")) for j in range(a)]
print ("You created list with", a,"elements, which looks like",b)
for i in b:
    while i<= 0:
        if i<= 0:
            print("No list")
            break
        else:
            print("You did good")

#знайти прості числа від 10 до 30б а рушта чисел представити у вигляді добутку

for num in range(10,31):
    if num%2 != 0 and num%3 != 0:
        print([num], '-simple')
    elif num%2 == 0:
        a = int(num/2)
        print ([num], '-is like 2*', a)
# #####