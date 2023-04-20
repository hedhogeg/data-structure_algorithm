class Node():
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self):
        data = str(self.data)
        next = str(self.next)
        result = f'< data : {data}, next : {next} >'
        
        return result

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    # 1. 모든 데이터 출력
    def printAll(self):
        result = ''
        current_node = self.head
        if current_node == None:
            print('This linked list is empty!')
        else:
            while current_node != None:
                result += str(current_node.data)
                result += ' > '
                current_node = current_node.next
            print(result[:-3])

    # 2. 모든 데이터 삭제
    def clear(self):
        self.head = None
        self.length = 0

    # 3. 인덱스 삽입
    def insertAt(self, index, data):
        if index > self.length or index < 0:
            raise IndexError
        
        new_node = Node(data)
        
        if index == 0: # 맨 앞에 삽입 : head 변경 필요
            new_node.next = self.head
            self.head = new_node
        else:  # 이외의 위치에 삽입 : 하나하나 참조해서 가서 삽입
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

        self.length += 1

    # 4. 맨 끝 삽입 (추가)
    def insertLast(self, data):
        self.insertAt(self.length, data)
    
    # 5. 인덱스 삭제
    def deleteAt(self, index):
        if index >= self.length or index < 0:
            raise IndexError
        
        current_node = self.head
        if index == 0: # 맨 앞 삭제 : head 변경 필요
            deleted = current_node
            self.head = current_node.next

            self.length -= 1
            return deleted
        else:
            for i in range(index-1):
                current_node = current_node.next
            deleted = current_node.next
            current_node.next = current_node.next.next

            self.length -= 1
            return deleted

    # 6. 맨 끝 삭제
    def deleteLast(self):
        return self.deleteAt(self.length-1)
    
    # 7. 인덱스 참조
    def getNode(self, index):
        if index >= self.length or index < 0:
            raise IndexError
        
        current_node = self.head
        for i in range(index):
                current_node = current_node.next
        
        return current_node
