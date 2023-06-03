from collections import deque

T = int(input())
empty_deque = deque([])
for _ in range(T):
    func = input()
    n = int(input())
    if n == 0:
        arr = input()
        arr = empty_deque
    else:
        arr = deque(map(int, input()[1:-1].split(',')))

    error = False
    left_first = True
    for f in func:
        if f == 'R':
            if left_first:
                left_first = False
            else:
                left_first = True
        elif f == 'D':
            if arr == empty_deque:
                error = True
                break
            else:
                if left_first:
                    arr.popleft()
                else:
                    arr.pop()
        else:
            error = True
            break
    if left_first == False:
        arr.reverse()
    
    if error:
        print('error')
    else:
        print(str(list(arr)).replace(' ',''))
