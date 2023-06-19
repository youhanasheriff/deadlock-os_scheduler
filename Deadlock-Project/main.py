from operator import add

def detect(process, allocation, request, work):
    n = len(process)
    m = len(work)

    # Create copies of the allocation and work lists
    allocation_copy = [list(row) for row in allocation]
    work_copy = list(work)

    f = [0] * n
    ans = []
    completed = 0

    need = [[0 for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = request[i][j] - allocation[i][j]

    while completed < n:
        found = False
        for p in range(n):
            if f[p] == 0:
                for j in range(m):
                    if need[p][j] > work_copy[j]:
                        break
                else:
                    for k in range(m):
                        work_copy[k] += allocation_copy[p][k]
                    ans.append(p)
                    f[p] = 1
                    completed += 1
                    found = True

        if not found:
            return False, []

    return True, ans


if __name__=='__main__':
    '''
    n=int(input('Enter number of processes: '))
    process=list(range(n))

    r=int(input('Enter number of resources: '))

    allocation=input('Enter allocation: ').split()
    request=input('Enter request: ').split()
    available=input('Enter available resources: ')
    '''

    # process=[0, 1, 2, 3, 4]
    # allocation=[[0, 1, 0 ],[ 2, 0, 0 ],[3, 0, 2 ],[2, 1, 1] ,[ 0, 0, 2]]
    # request=[[7, 5, 3 ],[3, 2, 2 ],[ 9, 0, 2 ],[2, 2, 2],[4, 3, 3]]
    # available=[3, 3, 2]

    process=[0, 1, 2, 3, 4]
    allocation=[[0, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]]
    request=[[0, 0, 0], [2, 0, 2], [0, 0, 0], [1, 0, 0], [0, 0, 2]]
    available=[0, 0, 0]

    is_deadlock, safe_sequence = detect(process, allocation, request, available)

    if is_deadlock:
        print("Deadlock detected.")
        # print("Safe Sequence:", safe_sequence)
    else:
        print("No deadlock detected.")

