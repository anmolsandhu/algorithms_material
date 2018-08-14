

class Heap():

	def __init__(self):
		self.size = -1
		self.heap = []

	def add_element(self, element):
		self.heap.append(element)
		self.size += 1
		self.shift_up(self.size)


	def shift_up(self, position):
		
		current_position = position
		while current_position > 0:
			temp = current_position
			if current_position % 2 != 0:
				current_position = (current_position / 2) 
			else:								
				current_position = (current_position / 2) - 1

			if current_position >= 0:
				if self.heap[current_position] < self.heap[temp]:	
					parent_Val = self.heap[current_position]
					self.heap[current_position] = self.heap[temp]
					self.heap[temp] = parent_Val
				else:
					break

	def extract_max(self):
		max_val_in_heap = self.heap[0]
		self.heap[0] = self.heap[self.size]
		self.size -= 1
		self.shift_down(0)
		self.heap.pop()
		return max_val_in_heap


	def shift_down(self, position):
		print "in shift shift_down"
		current_position = position
		while current_position <= self.size:
			print self.heap
			index_of_max = self.get_max_child(current_position)
			print "max index is ",  index_of_max
			if index_of_max < 0 :
				break

			if self.heap[current_position] < self.heap[index_of_max]:
				temp = self.heap[current_position]
				self.heap[current_position] = self.heap[index_of_max]
				self.heap[index_of_max] = temp
				current_position = index_of_max
			else:
				break


			# count += 1
			# if count == 13:
			# 	break



	def get_max_child(self, position):
		print "psoition is ", position, "value is  ", self.heap[position]
		if ((2 * position) + 1 ) <= self.size and ((2 * position) + 2)  <= self.size:
			print "comparing position ", ((2 * position) + 1 ) , " and ", ((2 * position) + 2 )
			if self.heap[((2 * position) + 1 )] > self.heap[((2 * position) + 2 )]:
				return ((2 * position) + 1 )
			else:
				return ((2 * position) + 2 )
		elif ((2 * position) + 1 ) == self.size:
			return ((2 * position) + 1)
		else:
			return -1

	def remove_element(self, element):

		element_index = 0
		for i in xrange(size + 1):
			if self.heap[i] == element:
				element_index = i
				break

		#set the value to infinity
		self.heap[element_index] = float("inf")

		#shift it up to top and extract it
		self.shift_up(element_index)
		self.extract_max()
		self.heap.pop()

	def change_priority(self, element_prev_val, element_new_val):

		element_index = 0
		for i in xrange(size + 1):
			if self.heap[i] == element:
				element_index = i
				break

		#set the value to infinity
		self.heap[element_index] = float("inf")

		#shift it up to top and extract it
		self.shift_up(element_index)
		self.extract_max()
		self.heap.pop()

		#add the new element with new val
		self.add_element(element_new_val)

	def build_heap(self, array):
		i = len(array) / 2
		self.heap = array
		self.size = len(array) - 1
		while i  >= 0:
			self.shift_down(i)
			i = i - 1

	def heap_sort(self, array):
		
		self.build_heap(array)
		for i in xrange(self.size):
			temp = self.heap[self.size]
			self.heap[self.size] = self.heap[0]
			self.heap[0] = temp
			self.size = self.size - 1
			self.shift_down(0)





h = Heap()

# h.add_element(6)
# h.add_element(7)
# h.add_element(2)
# h.add_element(4)
# h.add_element(1)
# h.add_element(13)
# h.add_element(6)
# h.add_element(43)
# h.add_element(32)
# h.add_element(21)
# # print h.heap
# # print h.extract_max()
# # print h.heap
a = [1,2,3,4,5,6,7,8,9,10]
h.build_heap(a)
h.heap_sort(a)
print h.heap