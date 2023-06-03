T = int(input())

def fibonacci(n, memo, memo2):
    try:
        return memo2[n]
    except:
        if n == 0:
            memo[n] = n
            memo2[0] = [1, 0]
        elif n == 1:
            memo[n] = n
            memo2[1] = [0, 1]
        else:
            memo[n] = fibonacci(n-1, memo, memo2) + fibonacci(n-2, memo, memo2)
            memo2[n] = [memo2[n-1][0]+memo2[n-2][0], memo2[n-1][1]+memo2[n-2][1]]
        return memo2[n]

for i in range(T):
    num = int(input())
    memo = dict()
    memo2 = dict()
    a = fibonacci(num, memo, memo2)
    print(f'{a[0]} {a[1]}')