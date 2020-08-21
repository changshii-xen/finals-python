class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def birthday(self):
        self.age += 1
dog1 = Dog(name='Fluffy',age=12,breed='pitbull')
dog1.birthday()
print(dog1)
