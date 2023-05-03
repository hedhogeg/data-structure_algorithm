from time import time

def simpleFibonacci(n):
    if n == 0 or n == 1:
        return n
    return simpleFibonacci(n-2) + simpleFibonacci(n-1)

# memoization
def memoFibonacci(n, memo):
    if n == 0 or n == 1:
        return n
    
    try:
        _ = memo[n]
    except:
        memo[n] = memoFibonacci(n-2, memo) + memoFibonacci(n-1, memo)

    return memo[n]

# tabulation
def tabFibonacci(n):
    if n == 0 or n == 1:
        return n
    
    table = [0, 1]
    for i in range(2, n+1):
        table.append(table[i-2] + table[i-1])

    return table[n]
    

simple_start = time()
print(simpleFibonacci(33))
simple = time() - simple_start
print(f'재귀 피보나치 실행 시간 : {simple}초')

memo_start = time()
print(memoFibonacci(33, {}))
memoization = time() - memo_start
print(f'메모이제이션 피보나치 실행 시간 : {memoization}초')

table_start = time()
print(tabFibonacci(33))
tabulation = time() - table_start
print(f'타뷸레이션 피보나치 실행 시간 : {tabulation}초')