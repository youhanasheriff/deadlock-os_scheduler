from simulator.schedulers.scheduler import Scheduler

class FCFS(Scheduler):
    """First Come First Serve (FCFS) scheduler."""

    def __init__(self):
        super(FCFS, self).__init__()

    def perform_schedule(self):
        """
        We simply sort the processes by the time that they come in by, and
        only change process as the processes finish their execution on the
        CPU.
        """
        if not self.active:  # If no active process
            if self.q:  # If there are processes in the queue
                self.active = self.q.popleft()
            return self.active

        if self.q:  # If there are processes in the queue
            self.active = self.q.popleft()
        else:
            self.active = None

        return self.active
