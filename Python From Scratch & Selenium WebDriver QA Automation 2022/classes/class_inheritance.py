class Dog:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    @staticmethod
    def eat():
        print("eat...")

    @staticmethod
    def bark():
        print("wooff...")

    @staticmethod
    def breath():
        print("breath...")

    @staticmethod
    def as_security():
        print("My dog is my home security...")


class Cat:  # Repetitive
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    @staticmethod
    def eat():
        print("eat...")

    @staticmethod
    def mew():
        print("mew...")


class Animal:  # Superclass
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


class Mouse(Animal):
    def __init__(self, color, food_type, breed, name):
        super().__init__(color, food_type)
        self.breed = breed
        self.name = name


dog_1 = Dog("Pitbull", "Max")
print(dog_1.breed)
dog_1.eat()
dog_1.breath()
dog_1.as_security()
print("-" * 70)

cat_1 = Cat("Persian Blue", "Sally")
print(cat_1.breed)
cat_1.eat()
cat_1.mew()
print("-" * 70)

mouse_1 = Mouse("White", "Cheese", "LabRat", "Sammy")
print(mouse_1.breed)
mouse_1.eat()
