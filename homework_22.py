from node import Node
class linkedList:
	def __init__(self):
		self.head = None
	def append(self, data):
		newNode = Node(data)
		if self.head == None:
			self.head = newNode
			return
		else:
			lastNode = self.head
			while lastNode.next != None:
				lastNode = lastNode.next
			lastNode.next = newNode
	def prepend(self, data):
		newNode = Node(data)
		if self.head == None:
			self.head = newNode
			return
		else:
			newNode.next = self.head
			self.head = newNode
	def insertAfterNode(self, prevNode, data):
		newNode = Node(data)
		newNode.next = prevNode.next
		prevNode.next = newNode
	def printList(self):
		curNode = self.head
		while curNode != None:
			print(curNode.data)
			curNode = curNode.next
	def deleteNode(self, key):
		curNode = self.head
		if curNode != None and curNode.data == key:
			self.head = curNode.next
			curNode = None
			return
		else:
			prev = None
			while curNode != None and curNode.data != key:
				prev = curNode
				curNode = curNode.next
			if curNode == None:
				print('The data is not found in the list!')
				return
			else:
				prev.next = curNode.next
				curNode = None

lst = linkedList()
lst.append('B')
lst.append('C')
lst.append('E')
lst.prepend('A')
lst.insertAfterNode(lst.head.next.next, 'D')
lst.append('Z')
lst.printList()
print("\n", end = '')
lst.deleteNode('Z')
lst.printList()
