from collections import deque

def idxAfterPrint(deque, idx):
    m = max(deque)
    l = len(deque)
    while deque[0] < m:
        replace = deque.popleft()
        deque.append(replace)
        idx = l - 1 if idx == 0 else idx - 1
    v = deque.popleft()
    idx -= 1

    return v, idx

T = int(input())
ans_list = []

for _ in range(T):
    N, M = map(int, input().split())
    docs = deque(map(int, input().split()))
    
    p = docs[M]

    v, idx = idxAfterPrint(docs, M)
    count = 1

    while v != p or idx >= 0:
        v, idx = idxAfterPrint(docs, idx)
        count += 1

    ans_list.append(count)

for index in ans_list:
    print(index)