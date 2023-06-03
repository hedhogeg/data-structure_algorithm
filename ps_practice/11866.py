N, K = map(int, input().split())

circle = [i+1 for i in range(N)]
result = '<'
count = 1
index = K
while True:
    result += str(circle[index-1])
    result += ', '
    if count == N:
        break
    circle.pop(index-1)
    length = len(circle)
    index = index+K-1
    while index > length:
        index -= length

    count += 1

result = result[:-2] + '>'
print(result)