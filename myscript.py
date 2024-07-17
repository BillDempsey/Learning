class Person:
    def __init__(self, height, weight, name):
        self.height = height
        self.weight = weight
        self.name = name

user = Person(182, 80, "Bill")

print(user.name)
