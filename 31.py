# Merge two sorted Linked Lists using recursion

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		
	def printList(self):
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next

	def append(self, new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
			return
		last = self.head
		while last.next:
			last = last.next
		last.next = new_node

def mergeLists(head1, head2):
	temp = None
	if head1 is None:
		return head2
	if head2 is None:
		return head1
	if head1.data <= head2.data:
		temp = head1
		temp.next = mergeLists(head1.next, head2)

	else:
		temp = head2
		temp.next = mergeLists(head1, head2.next)
	return temp

if __name__ == '__main__':
	list1 = LinkedList()
	list1.append(5)
	list1.append(10)
	list1.append(15)


	list2 = LinkedList()
	list2.append(2)
	list2.append(3)
	list2.append(20)


	list3 = LinkedList()

	list3.head = mergeLists(list1.head, list2.head)

	print("Merged Linked List is:")
	list3.printList()


