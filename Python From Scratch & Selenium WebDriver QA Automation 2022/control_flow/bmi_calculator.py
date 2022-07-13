# underweight < 18.5
# normal > 18.5 and 25 <=
# overweight > 25 and 30 <=
# obese > 30
# BMI = weight/height^2

weight = float(input("Enter your weight [kg]: "))
height = float(input("Enter your height [m]: "))
bmi = weight/height**2

print("")
if bmi < 18.5:
    print(f"Calculated BMI: {bmi:.2f}, you are underweight.")
elif 18.5 < bmi <= 25:
    print(f"Calculated BMI: {bmi:.2f}, you are normal.")
elif 25 < bmi <= 30:
    print(f"Calculated BMI: {bmi:.2f}, you are overweight.")
else:
    print(f"Calculated BMI: {bmi:.2f}, you are obese.")