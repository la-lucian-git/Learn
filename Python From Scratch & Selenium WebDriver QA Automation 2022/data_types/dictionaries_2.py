capitals = {
    "USA": "Washington",
    "France": "Paris",
    "Turkey": "Ankara",
}
print("")
print(capitals, type(capitals))

all_keys = capitals.keys()  # Returns dict_keys type/class, all_keys[0] ---> 'dict_key' object is not subscriptable
all_keys_list = list(capitals.keys())  # Casting dict_keys to list
all_values = capitals.values()

print("all_keys = capitals.keys() --->", all_keys)
print("all_values = capitals.values() --->", all_values)

print("")
print("type(all_keys) --->", type(all_keys))
print('all_keys_list = list(capitals.keys()) --->', all_keys_list, type(all_keys_list))