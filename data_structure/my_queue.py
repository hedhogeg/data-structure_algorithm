from doubly_linked_list import DoublyLinkedList

class Queue():
    def __init__(self) -> None:
        self.arr = DoublyLinkedList()

    def enqueue(self, data):
        self.arr.insertAt(0, data)

    def dequeue(self):
        try:
            return self.arr.deleteLast()
        except:
            return None
        
    def front(self):
        return self.arr.tail
    
    def isEmpty(self):
        return (self.arr.length == 0)
