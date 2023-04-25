from doubly_linked_list import DoublyLinkedList

class Deque:
    def __init__(self) -> None:
        self.arr = DoublyLinkedList()

    # 1. 모든 데이터 출력
    def printAll(self):
        self.arr.printAll()

    # 2. head에 삽입
    def addFirst(self, data):
        self.arr.insertAt(0, data)

    # 3. head에서 삭제
    def removeFirst(self):
        return self.arr.deleteAt(0)

    # 4. tail에 삽입
    def addLast(self, data):
        self.arr.insertAt(self.arr.length, data)

    # 5. tail에서 삭제
    def removeLast(self):
        return self.arr.deleteLast()
    
    # 6. 데이터 없는지 확인
    def isEmpty(self):
        return (self.arr.length == 0)