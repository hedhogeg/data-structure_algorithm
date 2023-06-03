N = int(input())

table = {}
step = [[N]]
cnt = 0
if N != 1:
    while 1 not in table:
        next_step = []
        for num in step[-1]:
            if num%3 == 0:
                divide3 = num // 3
                if divide3 not in table and divide3 >= 1:
                    table[divide3] = cnt
                    next_step.append(divide3)
            if num%2 == 0:
                divide2 = num // 2
                if divide2 not in table and divide2 >= 1:
                    table[divide2] = cnt
                    next_step.append(divide2)
            minus = num - 1
            if minus not in table and minus >= 1:
                table[minus] = cnt
                next_step.append(minus) 
        step.append(next_step)
        cnt += 1

print(cnt)