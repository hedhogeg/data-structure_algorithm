import sys

N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
M = int(input())
check = list(map(int, sys.stdin.readline().split()))

deck = dict()
for card in cards:
    if card in deck:
        deck[card] += 1
    else:
        deck[card] = 1

output = []
for num in check:
    result = 0
    if num in deck:
        result = deck[num]
    output.append(result)

print(*output)
