# python3 시간초과 pypy3만 통과함.
N, M, B = map(int, input().split())
time = 0
height = 0

ground = []
for _ in range(N):
    row = list(map(int, input().split()))
    ground.append(row)

min_ground = min(map(min, ground))
max_ground = max(map(max, ground))

time = 256*500*500
for i in range(min_ground, max_ground+1):
    used = 0
    digged = 0
    for x in range(N):
        for y in range(M):
            if ground[x][y] > i:
                digged += ground[x][y] - i
            else:
                used += i - ground[x][y]

    if used > digged + B:
        continue

    count = digged * 2 + used

    if time >= count:
        time = count
        height = i

print(time, height)
