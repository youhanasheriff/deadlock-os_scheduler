from simulator.schedulers.scheduler import Scheduler

class RoundRobin(Scheduler):
    """Constant time quantum Round Robin scheduler."""

    def __init__(self, time_quantum=4):
        super(RoundRobin, self).__init__()

        # Constant time quantum
        self.time_q = time_quantum

        # Tracks the current interval in a time quantum
        self.curr_q = 0

    def perform_schedule(self):
        """
        Returns the next job to execute in the round robin algorithm.

        In this case we simply take the next item in the queue to be the new
        active queue (if there exist one) and push the active item back into
        the queue.
        """
        # Check if there is an active process
        if self.active_process is None:
            # No active process, get the next process from the queue
            if len(self.queue) > 0:
                self.active_process = self.queue.pop(0)
        else:
            # There is an active process, push it back into the queue
            self.queue.append(self.active_process)
            self.active_process = None

        return self.active_process

    def timer_interrupt(self):
        """
        Timer interrupts only when the current active task has run out of
        its time quantum or has stopped execution.
        """
        default = super(RoundRobin, self).timer_interrupt()
        depleted = self.curr_q == 0

        return default or depleted

    def step(self):
        super(RoundRobin, self).step()

        self.curr_q = (self.curr_q + 1) % self.time_q
