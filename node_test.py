# Linked list exploration - Nick Bruno
# 05/10/2019

import math
import random
import time

# Define the node class, which contains the data and the pointer to the next node
class node:
	def __init__(self, data = None):
		self.data = data
		self.next = None

#Define the linked list class, which contains the head (beginning) of the list, and other functions to edit/view/retrieve the list
class linked_list:

	def __init__(self):
		self.head = node()
		self.totalNodes = 0

	def append(self, data):
		new_node = node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node
		self.totalNodes += 1
		

	#def length(self):
	#	cur = self.head
	#	total = 0
	#	while cur.next != None:
	#		total += 1
	#		cur = cur.next
	#	return total

	def display(self):
		elems = []
		cur_node = self.head
		while cur_node.next != None:
			cur_node = cur_node.next
			elems.append(cur_node.data)
		print(elems)

	def get(self, index):
		if index >= self.length():
			print("ERROR: 'Get' Index out of range!")
			return None
		cur_idx = 0
		cur_node = self.head
		while True:
			cur_node = cur_node.next
			if cur_idx == index:
				return cur_node.data
			cur_idx += 1

	def erase(self, index):
		if index >=self.length():
			print("ERROR: 'Erase' Index out of range!")
			return None
		cur_idx = 0
		cur_node = self.head
		while True:
			last_node = cur_node
			cur_node = cur_node.next
			if cur_idx == index:
				last_node.next = cur_node.next
				return
			cur_idx += 1
		self.totalNodes -= 1

	def findMiddle(self):
		slowPtr = self.head
		fastPtr = self.head
		cnt = 0
		while slowPtr != None and fastPtr != None:
			slowPtr = slowPtr.next
			fastPtr = fastPtr.next.next
			cnt += 1
		middle = slowPtr.data
		middleIdx = cnt-1
		return middleIdx, middle
	
	def find_mid(self):
		mid_idx = int(round(self.totalNodes/2))
		mid_node = self.head
		cnt = 0
		while cnt <= mid_idx:
			mid_node = mid_node.next
			cnt+=1
		return mid_idx, mid_node.data	

my_list = linked_list()

for i in range(11):
	my_list.append(random.randint(1,10))

print(my_list.display())

# Method 1 to find data point in middle of array using built in counter
start_time = time.time()
[mid_idx1, mid_node1] = my_list.find_mid()
end_time = time.time()
time1 = end_time - start_time
print("The index of the middle term in the list is: {} \nAnd the value is: {}\n This took {} seconds".format(mid_idx1, mid_node1, time1))

# Method 2
#start_time = time.time()
#[mid_idx2, mid_node2] = my_list.findMiddle()
#end_time = time.time()
#time2 = end_time - start_time
#print("The index of the middle term in the list is: {} \nAnd the value is: {}\n This took {} seconds".format(mid_idx2, mid_node2, time2))







