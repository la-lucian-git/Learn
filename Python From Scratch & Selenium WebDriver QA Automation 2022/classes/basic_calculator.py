"""
Create a class that has basic calculating functions.

You can have as many methods as you like but here are few suggestions.
* method to take two numbers and add them and return the sum
* method to take two numbers and subtract the second number from the first number and return the diff
* method to take two numbers and return the multiplication of the two
* method to divide two numbers and return the result (first number divided by second number)

"""


class BasicCalculator:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x / y


class BasicCalculatorV2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x * self.y


my_cal = BasicCalculator()
my_sum = my_cal.add(3, 231)
print(f"Sum of 3 and 231 is: {my_sum}.")
print("-" * 70)

my_cal_v2 = BasicCalculatorV2(10, 3)
my_prod = my_cal_v2.multiply()
print(f"Prod of 10 and 3 is: {my_prod}.")
print("-" * 70)
