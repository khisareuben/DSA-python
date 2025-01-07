class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
class linkedlist:
  def __init__(self):
    self.head = None
    
  
  def is_empty(self):
    if self.head == None:
      print("The list is empty")
      print()
    else:
      print("list not empty")
      print()
      
  def size(self):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.next 
    total = print(f"size : {count}")
    print()
    return total
  
  def search(self, key):
    current = self.head
    while current:
      if current.data == key:
        output = print(f"{key} is found")
        print()
        return output
        break
      else:
        current = current.next
        
  def add_at_begin(self, data):
    new = Node(data)
    new.next = self.head
    self.head = new
    
  def add_at_end(self, data):
    new = Node(data)
    if self.head == None:
      self.head = new
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new
      
  def add_at_spec_pos(self, data, position):
    new = Node(data)
    current = self.head
    for i in range(1, position-1):
      current = current.next
    new.next = current.next
    current.next = new
    
  def del_at_begin(self):
    current = self.head
    self.head = current.next
    current.next = None
    
  def del_at_end(self):
    prev = self.head
    current = self.head.next
    while current.next:
      current = current.next 
      prev = prev.next
    prev.next = None
    
  def del_at_spec_pos(self, position):
    prev = self.head
    current = self.head.next
    for i in range(1, position-1):
      current = current.next
      prev = prev.next
    prev.next = current.next
    current.next = None
    
  def screen(self):
    node = []
    current = self.head
    while current:
      node.append(str(current.data))
      current = current.next
    print("-> ".join(node))
    print()
    
l = linkedlist()
l.add_at_end(2)
l.add_at_end(3)
l.add_at_end(4)
l.add_at_end(5)
l.add_at_begin(1)
l.screen()
l.size()
l.is_empty()
l.search(3)
l.del_at_end()
l.screen()