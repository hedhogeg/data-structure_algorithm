from hash_set import HashSet

s = HashSet()
print(f'is empty : {s.isEmpty()}')
print('--------add data---------')
s.add(1)
s.add(1)
s.add(2)
s.add(3)
s.printAll()
print(f'is empty : {s.isEmpty()}')

print(f'is contain 1 : {s.isContain(1)}')
print('------remove 1--------')
s.remove(1)
s.printAll()
print(f'is empty : {s.isEmpty()}')
print(f'is contain 1 : {s.isContain(1)}')

print('------clear--------')
s.clear()
s.printAll()
print(f'is empty : {s.isEmpty()}')