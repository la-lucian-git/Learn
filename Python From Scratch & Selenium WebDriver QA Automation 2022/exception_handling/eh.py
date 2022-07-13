try:
    a = 5 / 0
except ZeroDivisionError:
    print("ZeroDivisionError")

print("")
try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}.")

print("")
try:
    a = "$5"
    a = int(a)
except Exception as e:
    print(f"Error: {e}.")


print("")
raise Exception("Custom raise exception!")