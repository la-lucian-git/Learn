from math import floor, ceil

a = 7.91  # Assign variable a value of 7.91
b = 7.43  # Assign variable b value of 7.43

round_a = round(a)  # Round to 8
round_b = round(b)  # Round to 7

floor_a = floor(a)  # Floor to 7
ceil_b = ceil(b)  # Ceil to 7

print("a = 7.91 --->", a, type(a))
print("b = 7.43 --->", b, type(b))

print("")
print("round_a = round(a) --->", round_a, type(round_a))
print("round_b = round(b) --->", round_b, type(round_b))

print("")
print("floor_a = floor(a) --->", floor_a, type(floor_a))
print("ceil_b = ceil(b) --->", ceil_b, type(ceil_b))

