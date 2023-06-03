N = int(input())
M = int(input())

def get(n, dic, s):
    s.add(n)
    if n in dic:
        arr = dic[n]
        for i in arr:
            if i not in s:
                get(i, dic, s)

network = dict()
for _ in range(M):
    start, end = map(int, input().split())
    if start in network:
        network[start] += [end]
    else:
        network[start] = [end]
    if end in network:
        network[end] += [start]
    else:
        network[end] = [start]

virus = set()
get(1, network, virus)
print(len(virus)-1)