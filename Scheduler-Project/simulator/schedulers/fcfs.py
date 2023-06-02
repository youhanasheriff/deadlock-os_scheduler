from simulator.schedulers.scheduler import Scheduler
from simulator.core.process import Process
from typing import List, Tuple

class FCFS(Scheduler):
    """First Come First Serve (FCFS) scheduler."""

    def __init__(self):
        super(FCFS, self).__init__()

    def perform_schedule(self, processes: List[Process]) -> Tuple[List[Tuple[int, int]], float]:
        """
        Perform the FCFS scheduling algorithm.

        Args:
            processes (List[Process]): List of Process objects.

        Returns:
            Tuple[List[Tuple[int, int]], float]: A tuple containing the list of context switch events and the average waiting time.
        """
        # Sort the processes by arrival time
        sorted_processes = sorted(processes, key=lambda p: p.arrival_time)

        # Initialize variables
        context_switches = []
        current_time = 0
        total_waiting_time = 0.0

        # Iterate through the sorted processes
        for process in sorted_processes:
            # Calculate waiting time for the process
            waiting_time = max(0, current_time - process.arrival_time)
            total_waiting_time += waiting_time

            # Add context switch event
            context_switches.append((current_time, process.id))

            # Update current time
            current_time += process.burst_time

        # Calculate average waiting time
        average_waiting_time = total_waiting_time / len(sorted_processes)

        # Return the context switch events and average waiting time
        return context_switches, average_waiting_time
