import time
class Timer:
    def __init__(self):
        self.startTime = time.time()

    def time_remaining(self, set_time = 3):
        current_time = time.time()
        if self.startTime + set_time > current_time:
            return self.startTime + set_time - time.time()

a = Timer()
while a.time_remaining() > 0:
    print(a.time_remaining())
