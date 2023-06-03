n, m = map(int, input().split())

union = dict()
for _ in range(m):
    order, a, b = map(int, input().split())
    if a < b:
        smaller = a
        other = b
    else:
        smaller = b
        other = a
    if order == 0:
        if smaller not in union and other not in union:
            union[smaller] = smaller
            union[other] = smaller
        elif smaller in union and other not in union:
            union[other] = union[smaller]
        elif smaller not in union and other in union:
            union[smaller] = smaller
            for key in [k for k, v in union.items() if v == union[other]]:
                union[key] = smaller
        else:
            for key in [k for k, v in union.items() if v == union[other]]:
                union[key] = union[smaller]
    else:
        if a in union:
            if b in union:
                if union[a] == union[b]:
                    print('yes')
                else:
                    print('no')
            else:
                print('no')
        else:
            print('no')