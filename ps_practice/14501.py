N = int(input())

schedule = []
for _ in range(N):
    T, P = map(int, input().split())
    schedule.append((T, P))

def consult(table, start, N, money):
    day = table[start]
    next_day = start + day[0]
    if next_day < N:
        money += day[1]
        temp = 0
        for j in range(next_day, N):
            temp_money = money
            recursive_money = consult(table, j, N, temp_money)
            if temp < recursive_money:
                temp = recursive_money
        return temp
    elif next_day == N:
        money += day[1]
        return money
    else:
        return money
    
result_list = []
for i in range(N):
    money = consult(schedule, i, N, 0)
    result_list.append(money)

print(max(result_list))