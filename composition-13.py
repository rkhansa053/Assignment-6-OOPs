class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
    

    def start(self):
        return f"The {self.engine_type} engine is starting."
    
class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def start_car(self):
        return f"{self.brand} car is starting. {self.engine.start()}"
    
engine = Engine("V8")

car = Car("Toyota", engine)
print(car.start_car())

