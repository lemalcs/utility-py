from datetime import datetime
import time

# Generates fibonacci numbers
class FibonacciIterator:

    # `max``parameter define the maximum number to generate
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1    
            return self.n2
        else: 
            self.aux = self.n1 + self.n2
            if self.aux <= self.max:
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux    
            else:
                raise StopIteration
            


if __name__ == "__main__":
    fibonacci = FibonacciIterator(144)
    for element in fibonacci:
        print(element)
        time.sleep(1)