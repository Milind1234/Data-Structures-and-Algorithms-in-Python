class Queue:
    def __init__(self , maxSize):
        self.maxSize = maxSize
        self.items = maxSize * [None]
        self.start = -1
        self.top = -1
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def enqueue(self , value):
        if self.isFull():
            return "Queue is Full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return f"Enqueued {value}"
        
        
                
new_Queue = Queue(3)
print("Is Queue Full ?:",new_Queue.isFull())
print("Is Queue Empty ?",new_Queue.isEmpty())
print(new_Queue.enqueue(1))
print(new_Queue.enqueue(2))
print(new_Queue.enqueue(3))
print(new_Queue.enqueue(4))
print(new_Queue)