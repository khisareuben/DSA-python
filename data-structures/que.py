class Queue:
  def __init__(self):
    self.queue = []
    
  def enque(self, data):
    self.queue.append(data)
    
  def deque(self):
    if len(self.queue) < 1:
      return "list is empty"
    else:
      return self.queue.pop(0)
    
  def size(self):
    print(len(self.queue))
    
  def display(self):
    print(self.queue)
    

q = Queue()
q.enque(1)
q.enque(2)
q.enque(3)
q.enque(4)
q.enque(5)
q.size()
q.display()
q.deque()
q.display()