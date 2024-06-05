import time

class StopWatch:
    """
    Represents a stopwatch for measuring elapsed time.
    """

    def __init__(self):
        """
        Initializes a StopWatch instance with the current time.
        """
        self.start_time = time.time()

    def get_elapsed_time(self):
        """
        Gets the elapsed time since the stopwatch was started.
        
        Returns:
            Elapsed time in seconds.
        """
        elapsed_time = time.time() - self.start_time
        return elapsed_time

        