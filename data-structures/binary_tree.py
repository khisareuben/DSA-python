class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

	def visit(self, node):
		print(node.val, end=" ")

	def preorder(self, current):
		if current is None:
			return
		self.visit(current)
		self.preorder(current.left)
		self.preorder(current.right)

	def inorder(self, current):
		if current is None:
			return
		self.inorder(current.left)
		self.visit(current)
		self.inorder(current.right)

	def postorder(self, current):
		if current is None:
			return
		self.postorder(current.left)
		self.postorder(current.right)
		self.visit(current)

	def insert(self, data):
		if self.val:
			if data < self.val:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.val:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.val = data


	def search(self, target):
		if target < self.val:
			if self.left is None:
				print(str(target) + " is not found")
				return
			else:
				return self.left.search(target)
		elif target > self.val:
			if self.right is None:
				print(str(target) + " is not found")
				return
			else:
				return self.right.search(target)
		else:
			print(str(target) + " is found")
			return


	def findMinValue(self, node):
		current = node
		while current.left:
			current = current.left
		return current


	def delete(self, key):
		if self is None:
			return self
		if key < self.val:
			if self.left:
				self.left = self.left.delete(key)
		elif key > self.val:
			if self.right:
				self.right = self.right.delete(key)
		else:
			if self.right is None:
				temp = self.left
				self = None
				return temp
			elif self.left is None:
				temp = self.right
				self = None
				return temp
			temp = self.findMinValue(self.right)
			self.val = temp.val
			self.right = self.right.delete(temp.val)
		return self

root = Node(50)
root.insert(30)
root.insert(70)
root.insert(20)
root.insert(40)
root.insert(60)
root.insert(80)

print("preorder: ", end=" ")
root.preorder(root)
print()
print("Inorder: ", end=" ")
root.inorder(root)
print()

root.search(30)
root.search(100)
root.delete(80)

print("Postorder: ", end=" ")
root.postorder(root)
print()