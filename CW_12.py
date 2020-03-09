# use map metod
names = ['Sam', 'Don', 'Daniel'] 
names = map(hash,names)
print(list(names))

# find colour red
colors = ['red', 'green', 'black', 'red', 'brown', 'red', 'blue', 'red', 'red', 'yellow']

def is_red(str):
    return str == 'red'

new_colors = filter(is_red,colors)
print(list(new_colors))

# use append and map
str_list = ['1','2','3','4','5','7']
num = []
for i in str_list:
    num.append(int(i))
    
num_list = map(int,str_list)
print(num)

# use map to change km to miles 
f = lambda x: round(x * 1.6, 2)
miles = [1,2,3]
km = map(f,miles)
print(list(km))