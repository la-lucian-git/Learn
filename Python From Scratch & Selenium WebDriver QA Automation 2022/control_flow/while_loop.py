flag = True
i = 0
j = 0

while flag and i <= 5:
    print("Hello!")
    i += 1

print("")
while flag:
    print("Hello!")
    if j <= 5:
        j += 1
    else:
        flag = False