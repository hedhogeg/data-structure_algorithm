from stack import Stack

s = Stack()
print('--------------')
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print(s.pop().data)
print(s.pop().data)
print(s.pop().data)
print(s.pop().data)

print('--------------')
s.push(5)
s.push(6)
s.push(7)
s.push(8)
print(s.get().data)
s.pop()
print(s.get().data)
print(f'isEmpty : {s.isEmpty()}')
s.pop()
s.pop()
s.pop()
print(f'isEmpty : {s.isEmpty()}')
print(s.pop())