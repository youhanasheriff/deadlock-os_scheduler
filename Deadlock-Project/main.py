from operator import add

def detect(process, allocation, request, work):
    """
    Detects if a deadlock exists in the system.

    Args:
        process (list): List of process IDs.
        allocation (list): List of resource allocations for each process.
        request (list): List of resource requests for each process.
        work (list): List of available resources.

    Returns:
        bool: True if a deadlock is detected, False otherwise.
    """
    n = len(process)
    m = len(work)

    # Create copy of allocation and request matrices
    allocation_copy = [row[:] for row in allocation]
    request_copy = [row[:] for row in request]

    # Create a list to track finished processes
    finished = [False] * n

    # Initialize a list to store the safe sequence
    safe_sequence = []

    # Calculate the initial work
    work = [work[j] - sum(allocation_copy[i][j] for i in range(n)) for j in range(m)]

    # Repeat until all processes are finished or deadlock is detected
    while True:
        # Find a process that is not finished and can be satisfied with available resources
        process_found = False
        for i in range(n):
            if not finished[i] and all(request_copy[i][j] <= work[j] for j in range(m)):
                # Process can be satisfied, allocate its resources
                work = list(map(add, work, allocation_copy[i]))
                finished[i] = True
                safe_sequence.append(process[i])
                process_found = True

        # If no process is found, break the loop
        if not process_found:
            break

    # If all processes are finished, no deadlock exists
    if all(finished):
        print("No deadlock detected.")
        return False

    # Deadlock detected, print the safe sequence and return True
    print("Deadlock detected. Safe sequence:", safe_sequence)
    return True


if __name__=='__main__':
	# '''
	# n=int(input('Enter number of processes: '))
	# process=list(range(n))

	# r=int(input('Enter number of resources: '))

	# allocation=input('Enter allocation: ').split()
	# request=input('Enter request: ').split()
	# available=input('Enter available resources: ')
	# '''

	# process=[0, 1, 2, 3, 4]
	# allocation=[[0, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]]
	# request=[[0, 0, 0], [2, 0, 2], [0, 0, 0], [1, 0, 0], [0, 0, 2]]
	# available=[0, 0, 0]

	# detect(process, allocation, request, available)
    process = [0, 1, 2, 3]
    allocation = [[0, 1], [2, 0], [0, 3], [1, 0]]
    request = [[0, 0], [2, 0], [0, 0], [0, 0]]
    available = [1, 1]

    detect(process, allocation, request, available)



