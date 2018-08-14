

class list_node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

head = list_node(1)
head.next = list_node(2)
head.next.next = list_node(3)
head.next.next.next = list_node(4)
head.next.next.next.next = list_node(5)
head.next.next.next.next.next = list_node(6)


# current = head 
# while(current):
# 	print current.data
# 	current = current.next



def odd_even_combination(head):

	current = head;

	# check_condition = True

	# if(!check_condition):
	# 	return head

	odd_head  = head
	even_head = head.next

	odd = odd_head
	even = even_head

	current = even_head.next

	is_odd = True

	while(current != None):

		if is_odd:
			#print current.data, "  odd"
			odd.next = current
			odd = current
			is_odd = False
		else:
			#print current.data , "  even"
			even.next = current
			even = current
			is_odd = True
		
		current = current.next

	odd.next = even_head
	even = None

	return odd_head




def print_list(head):
	current = head 
	while(current):
		print current.data
		current = current.next


print_list(head)

f = odd_even_combination(head)

print "odd even list"

print_list(f)










