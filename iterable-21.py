class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1
    
count = Countdown(7)

for number in count:
    print(number)