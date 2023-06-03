from collections import deque

T = int(input())
ans_list = []

for _ in range(T):
    N, M = map(int, input().split())
    docs = deque(map(int, input().split()))
    
    p = docs[M]
    v = 10
    idx = M

    count = 0
    while v != p or idx >= 0:
        m = max(docs)
        l = len(docs)
        while docs[0] < m:
            replace = docs.popleft()
            docs.append(replace)
            idx = l - 1 if idx == 0 else idx - 1
        v = docs.popleft()
        idx -= 1
        count += 1
    
    ans_list.append(count)

for index in ans_list:
    print(index)