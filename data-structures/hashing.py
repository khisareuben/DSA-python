class SimpleHashing:
  def __init__(self, size):
    self.size = size
    self.buckets = [[] for _ in range(size)]
    
  def hash(self, value):
    total = 0
    for char in value:
      total += ord(char)  
    return total % self.size
  
  def add(self, value):
    index = self.hash(value)
    bucket = self.buckets[index]
    if value not in bucket:
      bucket.append(value)
      
  def remove(self, value):
    index = self.hash(value)
    bucket = self.buckets[index]
    if value in bucket:
      bucket.remove(value)
      
  def display(self):
    print("Hash Table:")
    for i, bucket in enumerate(self.buckets):
      print(f"Bucket {i}: {bucket}")
    
    
    
hash_set = SimpleHashing(size=10)

hash_set.add("Charlotte")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Michaela")
hash_set.add("Bob")

hash_set.display()
hash_set.remove("Jens")
print()
hash_set.display()