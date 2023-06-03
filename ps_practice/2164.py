from collections import deque

N = int(input())

deck = deque()
for i in range(N):
    deck.append(i+1)

for j in range(N-1):
    deck.popleft()
    top = deck.popleft()    
    deck.append(top)

print(deck[0])