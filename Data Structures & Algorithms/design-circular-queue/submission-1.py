class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.limit = k
        self.curr_size = 0
        self.front = self.back = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        temp = Node(value)
        # print(temp.value)
        temp.next = self.front
        self.curr_size += 1
        if not self.front:
            # empty queue
            self.back = temp
            self.front = self.back
            self.front.next = self.back
        else:
            self.back.next = temp
            self.back = temp
        # print(self.front.value)
        print(self.back.value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.curr_size -= 1
        if self.front == self.back:
            # last node
            self.front = None
            self.back = None
        else:
            self.back.next = self.front.next
            temp = self.front
            self.front = self.front.next
            del temp
        return True        

    def Front(self) -> int:
        if self.front:
            return self.front.value
        return -1

    def Rear(self) -> int:
        if self.back:
            return self.back.value
        return -1
        
    def isEmpty(self) -> bool:
        return not self.curr_size
    
    def isFull(self) -> bool:
        return self.curr_size == self.limit


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()