from operator import add

def detect(process, allocation, request, work):
    n = len(process)
    m = len(work)

    avail = list(work)
        
    # Allocation Matrix
    alloc = [list(row) for row in allocation]
        
    # MAX Matrix
    max = [list(row) for row in request]
        
    f = [0] * n
    ans = [0] * n
    ind = 0
    found = False
    for k in range(n):
        f[k] = 0
        
    need = [[ 0 for i in range(m)]for i in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = max[i][j] - alloc[i][j]
    y = 0
    for k in range(5):
        for i in range(n):
            if (f[i] == 0):
                flag = 0
                for j in range(m):
                    if (need[i][j] > avail[j]):
                        flag = 1
                        break

                if (flag == 0):
                    ans[ind] = i
                    ind += 1
                    for y in range(m):
                        avail[y] += alloc[i][y]
                    f[i] = 1
                    found = True

    if not found:
        return False
    else:
        return True



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


    is_deadlock = detect(process, allocation, request, available)
    if is_deadlock:
        print("Deadlock detected.")
    else:
        print("No deadlock detected.")

