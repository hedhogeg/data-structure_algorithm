A, B, C = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))
time_list = [0] * 101

for truck in [first, second, third]:
    for i in range(truck[0], truck[1]):
        time_list[i] += 1

price = A*time_list.count(1) + 2*B*time_list.count(2) + 3*C*time_list.count(3)
print(price)
