import random

a = random.randint(100, 200)
b = random.randrange(30)

my_list = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']

print("")
print(a)

print("")
print(b)

print("")
print(my_list)
print(random.choice(my_list))
print(random.sample(my_list, 2))