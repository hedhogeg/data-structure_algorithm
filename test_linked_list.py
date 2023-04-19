# Test data structures
from linked_list import LinkedList

print('--------------------')
linked = LinkedList()
linked.insertAt(0, 0)
linked.insertAt(1, 1)
linked.insertAt(1, 2)
linked.insertAt(2, 3)
linked.insertAt(2, 4)
linked.printAll()

print('----------------')
linked.clear()
linked.printAll()

print('-------------')
linked.insertLast(1)
linked.insertLast(2)
linked.insertLast(3)
linked.insertLast(4)
linked.printAll()

print('---------------------')
linked.deleteAt(0)
linked.deleteAt(1)
linked.printAll()

print('----------------------')
linked.deleteLast()
linked.printAll()

print('------------------')
linked.insertLast(3)
linked.insertLast(4)
a = linked.getNode(0)
print(a)