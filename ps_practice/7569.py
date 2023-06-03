M, N, H = map(int, input().split())

box = []
for h in range(H):
    board = []
    for _ in range(N):
        row = list(map(int, input().split()))
        board.append(row)
    box.append(board)

def oneDay(arr, box):
    next_day = []
    dx = [0, 0, -1, 1, 0, 0]
    dy = [-1, 1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    for x, y, z in arr:
        for i in range(6):
            next_x = x + dx[i]
            next_y = y + dy[i]
            next_z = z + dz[i]
            if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N or next_z < 0 or next_z >= H:
                continue
            if box[next_z][next_y][next_x] == 0:
                box[next_z][next_y][next_x] = 1
                next_day.append((next_x, next_y, next_z))

    return list(set(next_day))

first = [(j, i, k) for k in range(H) for i in range(N) for j in range(M) if box[k][i][j] == 1]
cnt = 0
left = oneDay(first, box)
while len(left) > 0:
    cnt += 1
    left = oneDay(left, box)

zeros = [(i, j, k) for k in range(H) for i in range(N) for j in range(M) if box[k][i][j] == 0]
result = -1 if len(zeros) > 0 else cnt
print(result)