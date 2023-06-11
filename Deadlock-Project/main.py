from operator import add

def detect(process, allocation, request, work):
    n = len(process)
    m = len(work)

    # Create copies of the allocation and work lists
    work_copy = list(work)

    f = [0] * n
    ans = [0] * n
    ind = 0
    for k in range(n):
        f[k] = 0

    need = [[0 for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = request[i][j] - allocation[i][j]

    while ind < n:
        found = False
        for p in range(n):
            if f[p] == 0:
                for j in range(m):
                    if need[p][j] > work_copy[j]:
                        break

                if j == m - 1:
                    for k in range(m):
                        work_copy[k] += allocation[p][k]
                    ans[ind] = p
                    ind += 1
                    f[p] = 1
                    found = True

        if not found:
            return True

    return False


if __name__=='__main__':
	'''
	n=int(input('Enter number of processes: '))
	process=list(range(n))

	r=int(input('Enter number of resources: '))

	allocation=input('Enter allocation: ').split()
	request=input('Enter request: ').split()
	available=input('Enter available resources: ')
	'''

	process=[0, 1, 2, 3, 4]
	allocation=[[0, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]]
	request=[[0, 0, 0], [2, 0, 2], [0, 0, 0], [1, 0, 0], [0, 0, 2]]
	available=[0, 0, 0]


	is_deadlock = detect(process, allocation, request, available)
	if is_deadlock:
		print("Deadlock detected.")
	else:
		print("No deadlock detected.")

