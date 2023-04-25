# 재귀함수란?
def myFunction(num):
    if num > 10:
        return
    print(num)
    myFunction(num+1)

# 재귀함수의 위력 - 팩토리얼
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num-1)

# 재귀적으로 생각하기 1. 배열의 합  
def sumArray(arr):
    if len(arr) == 1:
        return arr[0]
    return sumArray(arr[:-1]) + arr[-1]

# 재귀적으로 생각하기 2. 문자열의 길이
def stringLength(str):
    if len(str) == 0:
        return 0
    return stringLength(str[:-1]) + 1

# 재귀적으로 생각하기 3. 지수함수
def power(x, n):
    if n == 0:
        return 1
    return power(x, n-1) * x

print(power(2, 5))