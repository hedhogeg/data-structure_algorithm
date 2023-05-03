from time import time

def simpleFibonacci(n):
    if n == 0 or n == 1:
        return n
    return simpleFibonacci(n-2) + simpleFibonacci(n-1)

def DPfibonacci(n, memo):
    if n == 0 or n == 1:
        return n
    
    try:
        _ = memo[n]
    except:
        memo[n] = DPfibonacci(n-2, memo) + DPfibonacci(n-1, memo)

    return memo[n]

simple_start = time()
print(simpleFibonacci(33))
simple = time() - simple_start
print(f'재귀 피보나치 실행 시간 : {simple}초')

DP_start = time()
print(DPfibonacci(33, {}))
dP = time() - DP_start
print(f'메모이제이션 피보나치 실행 시간 : {dP}초')