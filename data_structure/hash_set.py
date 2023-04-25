from hash_table import HashTable

class HashSet:
    def __init__(self) -> None:
        self.table = HashTable()

    # 1. 모든 데이터 출력
    def printAll(self):
        for i in range(len(self.table.arr)):
            current_node = self.table.arr[i].head
            while current_node != None:
                print(current_node.data.key)
                current_node = current_node.next

    # 2. 데이터 삽입
    def add(self, data):
        if self.table.getData(data) == None:
            self.table.setData(data, -1)

    # 3. 해당 데이터가 있는지 확인
    def isContain(self, data):
        return (self.table.getData(data) != None)
    
    # 4. 데이터 제거
    def remove(self, data):
        self.table.removeData(data)

    # 5. 전체 데이터 제거
    def clear(self):
        for i in range(len(self.table.arr)):
            self.table.arr[i].clear()

    # 6. 데이터가 없는지 확인
    def isEmpty(self):
        empty = True
        for i in range(len(self.table.arr)):
            if self.table.arr[i].length > 0:
                empty = False
                break

        return empty