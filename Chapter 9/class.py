class Dog:
    def __init__(self, name, age):
        """untill now i'll not understand class"""
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} is rolled_over!")



dog1 = Dog('willi', 7)
print(dog1.name)
print(dog1.age)
dog1.sit()
dog1.roll_over()