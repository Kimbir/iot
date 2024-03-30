class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        print(f"Dog name: {self.name}")
    def get_age(self):
        print(f"Dog age: {self.age}")
    def roll_over(self):
        print(f'Dog rolling')
    def sit(self):
        print('Dog sitting')
my_dog = Dog('Willie', 6)
my_dog.get_name()
my_dog.get_age()
my_dog.roll_over()
my_dog.sit()
print(f'')
my_dog = Dog('Lucy', 3)
my_dog.get_name()
my_dog.get_age()
my_dog.roll_over()
my_dog.sit()
print(f'')