from deque import Deque

d = Deque()

print('--------------')
print(f'is empty : {d.isEmpty()}')
d.addFirst(1)
d.addFirst(2)
d.addFirst(3)
d.addFirst(4)
d.addFirst(5)
d.printAll()
print(f'is empty : {d.isEmpty()}')

print('------------')
d.removeFirst()
d.printAll()
d.removeFirst()
d.printAll()

print('------------')
d.addLast(6)
d.addLast(7)
d.printAll()

print('---------------')
d.removeLast()
d.printAll()
d.removeLast()
d.printAll()