is_true = True
is_false = False

print("")
print("is_true = True --->", is_true)
print("is_false = False --->", is_false)
print("")

# AND [BOTH HAVE TO BE TRUE] / OR [AT LEAST ONE HAS TO BE TRUE]
true_and_true = is_true and is_true
true_and_false = is_true and is_false
true_or_false = is_true or is_false
false_and_false = is_false and is_false
false_or_true = is_false or is_true

print("true_and_true = is_true and is_true --->", true_and_true)
print("true_and_false = is_true and is_false --->", true_and_false)
print("true_or_false = is_true or is_false --->", true_or_false)
print("false_and_false = is_false and is_false --->", false_and_false)
print("false_and_true = is_false and is_true --->", false_or_true)
print("")

print("Arithmetic Operators: +, -, *, /, %, //, **")
print("Comparison Operators: <, >, ==, <=, >=, !=")
print("Logical Operators: and, or, not")