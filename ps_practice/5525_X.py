N = int(input())
M = int(input())
S = input()

len_p = 2*N + 1

count = 0
check = []
I_in = False
O_in = False
for s in S:
    if s == 'I':
        if O_in:
            check.append(0)
            check = [i+1 for i in check]
        else:
            check = [1]

        if len_p in check:
            check.remove(len_p)
            count += 1
        I_in = True
        O_in = False
    else:
        if I_in:
            check = [i+1 for i in check]
        else:
            check = [0]
        O_in = True
        I_in = False

print(count)