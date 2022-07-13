my_list = ["house", "car", "bike", "boat"]
string = "Brave-bold war-band is sneaky strong."
string_to_list = string.split()

print("")
for i in my_list:
    print(i)

print("")
for i in string:
    print(i)

print("")
for i in string_to_list:
    print(i)

print("")
for i in string_to_list:
    if len(i) > 4:
        print(i)