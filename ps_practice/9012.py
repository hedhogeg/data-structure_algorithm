T = int(input())

result_list = []
for _ in range(T):
    string = input()

    VPS = True
    status = []
    for c in string:
        if c == '(':
            status.append(0)
        else:
            try:
                status.pop()
            except IndexError:
                VPS = False
                break
    if len(status) != 0:
        VPS = False

    if VPS:
        result_list.append('YES')
    else:
        result_list.append('NO')

for r in result_list:
    print(r)