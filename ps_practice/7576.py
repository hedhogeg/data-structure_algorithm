M, N = map(int, input().split())

box = []
for _ in range(N):
    row = list(map(int, input().split()))
    box.append(row)

def oneDay(arr, box):
    next_day = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for x, y in arr:
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
                continue
            if box[next_y][next_x] == 0:
                box[next_y][next_x] = 1
                next_day.append((next_x, next_y))

    return list(set(next_day))

first = [(j, i) for i in range(N) for j in range(M) if box[i][j] == 1]
cnt = 0
left = oneDay(first, box)
while len(left) > 0:
    cnt += 1
    left = oneDay(left, box)

zeros = [(i, j) for i in range(N) for j in range(M) if box[i][j] == 0]
result = -1 if len(zeros) > 0 else cnt
print(result)