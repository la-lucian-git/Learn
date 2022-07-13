main_number = 15
user_input = 0

while True:
    user_input = int(input("Give me a number between 0 and 20: "))
    print(f"You entered: {user_input}")
    if user_input == main_number:
        break