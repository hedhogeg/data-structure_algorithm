from linked_list import LinkedList

class Stack():
    def __init__(self) -> None:
        self.arr = LinkedList()

    # 1. 삽입
    def push(self, data):
        self.arr.insertAt(0, data)

    # 2. 삭제
    def pop(self):
        try:
            return self.arr.deleteAt(0)
        except:
            return None

    # 3. 참조
    def get(self):
        return self.arr.getNode(0)

    # 4. 데이터가 없는지 확인
    def isEmpty(self):
        return (self.arr.length == 0)
