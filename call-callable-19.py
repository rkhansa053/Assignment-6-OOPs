class Multiplier:
    def __init__(self, factor):
        self.factor= factor

    def __call__(self, number):
        return number * self.factor
    

multi = Multiplier(6)

print(callable(multi))

result = multi(9)
print(result)