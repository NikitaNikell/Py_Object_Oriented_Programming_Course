import time


class Value:

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"Invalid data type {self.name.upper()}")
        setattr(instance, self.name, value)


class DeltaClock:

    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        if dt.clock1.get_time() - dt.clock2.get_time() > 0:
            return time.strftime('%H: %M: %S', time.gmtime(dt.clock1.get_time() - dt.clock2.get_time()))
        return "00: 00: 00"

    def __len__(self):
        return abs(dt.clock1.get_time() - dt.clock2.get_time())


class Clock:
    hours = Value()
    minutes = Value()
    seconds = Value()

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        result = (self.hours * 3600) + (self.minutes * 60) + self.seconds
        return result




dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))

print(dt) # 01: 30: 00
len_dt = len(dt) # 5400

print(len(dt))