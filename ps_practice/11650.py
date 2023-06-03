N = int(input())

coord = dict()
for _ in range(N):
    X, Y = map(int, input().split())
    if X in coord.keys():
        coord[X].append(Y)
    else:
        coord[X] = [Y]

sorted_X = sorted(coord.items())
for arr in sorted_X:
    x = arr[0]
    sorted_Y = sorted(arr[1])
    for y in sorted_Y:
        print(x, y)
