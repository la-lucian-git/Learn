capitals = {
    "USA": "Washington",
    "France": "Paris",
    "Turkey": "Ankara",
}

print(capitals, type(capitals))

print("")
france_capital_1 = capitals["France"]
france_capital_2 = capitals.get("France")
none_capital = capitals.get("Romania")  # get will return None vs dict["key"] will error out ---> KeyError

print('france_capital = capitals["France"] --->', france_capital_1)
print('france_capital_2 = capitals.get("France") --->', france_capital_2)
print('none_capital = capitals.get("Romania") --->', none_capital)

capitals["Kenya"] = "Nairobi"
print('capitals["Kenya"] = "Nairobi" --->', capitals)

capitals.update({"India": "New Delhi"})
print('capitals.update({"India": "New Delhi"}) --->', capitals)