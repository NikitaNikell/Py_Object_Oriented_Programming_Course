
class FibonacciIterator:

    def __init__(self, num):
        self.num = num
        self.current = 0
        self.next = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.num:
            result = self.current
            self.current, self.next = self.next, self.current + self.next
            self.count += 1
            return result
        else:
            raise StopIteration


fibonacci_iter = FibonacciIterator(3
                                   )

for number in fibonacci_iter:
    print(number)
