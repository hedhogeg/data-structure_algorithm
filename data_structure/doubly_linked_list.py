class Node():
    def __init__(self, data, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        data = str(self.data)
        next = 'exist' if self.next else None
        prev = 'exist' if self.prev else None
        result = f'< data : {data}, next : {next}, prev : {prev} >'
        
        return result

class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
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
            if self.head != None: # 데이터가 있는 경우
                self.head.prev = new_node
            self.head = new_node
        elif index == self.length: # 맨 뒤에 삽입 : tail 변경 필요
            new_node.prev = self.tail
            self.tail.next = new_node
        else:  # 이외의 위치에 삽입 : 하나하나 참조해서 가서 삽입
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            new_node.next = current_node.next
            new_node.prev = current_node
            current_node.next = new_node
            new_node.next.prev = new_node

        if new_node.next == None: # new_node가 맨 뒤에 있는 경우
            self.tail = new_node
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
            if self.head.next == None: # 데이터가 하나일 때
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

            self.length -= 1
            return deleted
        elif index == self.length-1: # 맨 뒤 삭제 : tail 변경 필요
            deleted = self.tail
            if self.tail.prev == None: # 데이터가 하나일 때
                self.head = None
                self.tail = None
            else:
                deleted.prev.next = None
                self.tail = deleted.prev

            self.length -= 1
            return deleted
        else: # 이외 : 하나하나 참조해서 가서 삭제
            for i in range(index-1):
                current_node = current_node.next
            deleted = current_node.next
            current_node.next = current_node.next.next
            current_node.next.prev = current_node

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
