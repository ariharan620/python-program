class Queue:
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return self.queue==0
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.queue.pop(0)
    def peek (self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.queue [0]
    def size (self):
        return len (self.queue)
x=Queue()
x.enqueue(10)
x.enqueue(20)
x.enqueue(30)
print(x.queue)
x.dequeue()
print(x.queue)
print(x.peek())
print(x.size())
x.size()
