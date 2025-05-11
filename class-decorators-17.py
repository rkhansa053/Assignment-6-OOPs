def add_greeting(cls):
    def greet(self):
        return f"Hello from Decorator!"
    
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hi, I'm {self.name}"
    
person = Person("Khansa Rahman")

print(person.greet())