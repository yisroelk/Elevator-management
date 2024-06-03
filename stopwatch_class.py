import time
class StopWatch:
    def __init__(self):
        self.startTime = time.time()

    def get_elapsed_time(self):
        elapsedTime = ((time.time() - self.startTime))
        return elapsedTime
    
# a = StopWatch()
# print(a.get_elapsed_time())

# time.sleep(7)
# print(a.get_elapsed_time())


# x = a.get_elapsed_time()

# print(f'{x:.4f}')
        