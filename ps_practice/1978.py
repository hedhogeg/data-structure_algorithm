import math

N = int(input())
num_list = list(map(int, input().split()))
count = 0

for num in num_list:
    if num == 1:
        continue
    result = True
    A = math.floor(math.sqrt(num))
    for i in range(2, A+1):
        if num % i == 0:
            result = False
    if result:
        count += 1

print(count)