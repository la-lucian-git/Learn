countries = ["USA", "Mexico", "Canada", "India", "Germany", "Japan"]
countries_type = type(countries)
countries_len = len(countries)

print("")
print('countries = ["USA", "Mexico", "Canada", "India", "Germany", "Japan"] --->', countries)

print("")
print("countries_type = type(countries) --->", countries_type)
print("countries_len = len(countries) --->", countries_len)

countries.append("China")
print("")
print('countries.append("China") --->', countries)

countries.remove("Canada")
print('countries.remove("Canada") --->', countries)

countries.pop()  # Can be assigned to a variable
print('countries.pop() --->', countries)


