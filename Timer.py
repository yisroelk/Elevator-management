import time

class Timer:
    """
    Represents a timer for tracking time intervals.
    """

    def __init__(self, set_timer_time):
        """
        Initializes a Timer instance with a set time interval.
        
        Args:
            set_timer_time: Time interval in seconds.
        """
        self.start_time = time.time()
        self.remaining_time = 0
        self.set_timer_time = set_timer_time

    def time_remaining(self):
        """
        Calculates the remaining time on the timer.
        
        Returns:
            Remaining time in seconds.
        """
        current_time = time.time()
        if self.start_time + self.set_timer_time > current_time:
            self.remaining_time = self.start_time + self.set_timer_time - current_time
            return self.remaining_time
        else:
            return 0



