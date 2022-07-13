class Animal:
    def __init__(self, color, food_type):  # Always runs
        print("I am init!")
        self.color = color  # Class variables
        self.food_type = food_type
        print(f"Variables: {self.color} {self.food_type}")

    @staticmethod
    def move():
        print("Animal moves.")

    def eat(self):
        print("Animal eats.")
        print(f"This animal eats: {self.food_type}.")

    @staticmethod
    def breath(self):
        print("Animal breath")

    def main(self):
        self.eat()
        self.move()
        self.breath()


my_animal_1 = Animal("blue", "burger")
my_animal_2 = Animal("green", "pizza")

my_animal_1.move()
my_animal_1.eat()
