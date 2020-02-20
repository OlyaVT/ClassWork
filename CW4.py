#з двох чисел визначити, яке з них більше

a = input()
b = input()

if a > b:
    print (a, "is bigger then {}".format(b))
print (b, "is bigger then {}".format(a))

#визначити чи число парне

a = int(input())
if a%2 == 0:
    print ("The number {0} is even".format(a))
else:
    print ("The number {0} is odd".format(a))

#в межах від 1 до 100 вивести непарні числа

print (list(range(1,100,2)))

#в межах від 1 до 100 вивести парні числа
i=0
while i<100:
    if i % 2 == 0:
        print(i)
    i=i+1
#або
print(list(range(0,100, 2)))

#визначити чи є в списку непарні числа
first_list = [3, 5, 8]
for i in first_list:
    if i%2 == 0:
        print("There is odd number")
        break