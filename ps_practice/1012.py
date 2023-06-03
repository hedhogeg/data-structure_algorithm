T = int(input())

def find(arr, M, N):
    coord = (-1, -1)
    finished = False
    for y in range(N):
        if not finished:
            for x in range(M):
                if arr[y][x] == 1:
                    coord = (x, y)
                    finished = True
                    break
    
    return [coord]

# 1에 인접한 네 곳 중에 1이 있는지 확인해서 0으로 바꾸고 위치 return
def check(arr, coord, M, N):
    next_coord = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for c in coord:
        x = c[0]
        y = c[1]
        field[y][x] = 0
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
                continue
            if arr[next_y][next_x] == 1:
                arr[next_y][next_x] = 0
                next_coord.append((next_x, next_y))

    return next_coord
            
# 한 지렁이가 커버하는 영역
def worm(arr, coord, M, N):
    left = check(arr, coord, M, N)
    while len(left) > 0:
        left = check(arr, left, M, N)

result = []
for t in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(M)] for n in range(N)]
    for k in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    cnt = 0
    cabbage = find(field, M, N)
    while cabbage != [(-1, -1)]:
        cnt += 1
        worm(field, cabbage, M, N)
        cabbage = find(field, M, N)
    
    result.append(cnt)

for r in result:
    print(r)