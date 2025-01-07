class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    self.prev = None
    
class dll:
  def __init__(self):
    self.head = None
    
  def is_empty(self):
    if self.head is None:
      print()
      print("list completely is empty")
    else:
      print("list not empty")
      
  def size(self):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.next 
    return count
  
  def search(self, key): 
    current = self.head 
    found = False 
    while current: 
      if key == current.data: 
        print(f"{key} found") 
        found = True 
        break 
      current = current.next
    if not found: 
      print(f"{key} not found")
      
      
  def add_at_begin(self, data):
    new = Node(data)
    if self.head is None:
      self.head = new
    else:
      current = self.head
      new.next = self.head
      current.prev = new
      self.head = new
      
  def add_at_end(self, data):
    new = Node(data)
    if self.head is None:
      self.head = new
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new
      new.prev = current
      
  def add_at_spec_pos(self, data, position):
    new = Node(data)
    if self.head is None:
      self.head = new
    else:
      current = self.head
      for i in range(1, position-1):
        current = current.next
      current.next.prev = new
      new.next = current.next
      current.next = new
      new.prev = current
      
  def del_at_begin(self):
    if self.head is None:
      return 'list is empty'
    current = self.head
    self.head = current.next
    current.next = None
    current.next.prev = None
    
  def del_at_end(self):
    if self.head is None:
      return 'list is empty'
    before = self.head
    current = self.head.next
    while current.next:
      current = current.next 
      before = before.next
    before.next = None
    current.prev = None
    
  def del_at_spec_pos(self, position):
    if self.head is None:
      return 'list is empty'
    before = self.head
    current = self.head.next
    for i in range(1, position-1):
      current = current.next 
      before = before.next
    before.next = current.next 
    current.next.prev = before
    current.next = None
    current.prev = None
    
  def display(self):
    node = []
    current = self.head
    while current:
      node.append(str(current.data))
      current = current.next
    print("<->".join(node))
    
    
l = dll()
l.add_at_end(2)
l.add_at_end(3)
l.add_at_end(4)
l.add_at_end(5)
l.add_at_begin(1)
l.is_empty()
l.size()
l.search(6)
l.search(4)
l.display()
l.del_at_end()
l.display()