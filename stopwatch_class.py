import time

class StopWatch:
    def __init__(self):
        self.start_time = time.time()

    def get_elapsed_time(self):
        elapsed_time = ((time.time() - self.start_time))
        return elapsed_time

        