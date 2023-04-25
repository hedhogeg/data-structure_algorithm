from doubly_linked_list import DoublyLinkedList

class HashData:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

# 인덱스가 0 ~ 9까지 총 10개의 칸을 갖는 해시 테이블
class HashTable:
    def __init__(self) -> None:
        self.arr = []
        for i in range(10):
            self.arr.append(DoublyLinkedList())

    def hashFunction(self, number):
        return number % 10

    # 1. 데이터 삽입
    def setData(self, key, value):
        self.arr[self.hashFunction(key)].insertAt(0, HashData(key, value))
    
    # 2. 데이터 읽기
    def getData(self, key):
        current_node = self.arr[self.hashFunction(key)].head
        while current_node != None:
            if current_node.data.key == key:
                return current_node.data.value
            current_node = current_node.next

        return None
    
    # 3. 데이터 삭제
    def removeData(self, key):
        linked_list = self.arr[self.hashFunction(key)]
        current_node = linked_list.head
        deleted_idx = 0
        while current_node != None:
            if current_node.data.key == key:
                return linked_list.deleteAt(deleted_idx)
            current_node = current_node.next
            deleted_idx += 1

        return None