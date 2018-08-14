

class trie(object):

	def __init__(self):
		self.edges = None
		self.words = 0
		self.prefixes = 0


def initialize(vertex):
	vertex.words = 0
	vertex.prefixes = 0
	vertex.edges = [None] * 26

def add_word(vertex, word):
	for a in word:
		if a.isalpha():
			pass
		else:
			return "can't add this string to the list it has non alphabets in it"
	adding_word(vertex, word, 0, len(word))

def adding_word(vertex, word, n, word_len):
	if n == word_len:
		vertex.words = vertex.words + 1
		print "word_inserted"
	else:
		vertex.prefix = vertex.prefixes + 1
		char_val = get_char_val(word[n])
		if vertex.edges[char_val] == None:
			new_vertex = trie()
			initialize(new_vertex)
			vertex.edges[char_val] = new_vertex
		n = n+ 1
		adding_word(vertex.edges[char_val], word, n, word_len)



def get_char_val(word):
	if word[0].isupper():
		return ord(word[0]) - 65
	else:
		return ord(word[0]) - 97


def search_word_in_trie(vertex, word, n, word_len):
	if n == word_len :
		if vertex.words > 0:
			return True
		else:
			return False
	else:
		char_val = get_char_val(word[n])
		print char_val, '  ', word[n], "   vertex word  = " , vertex.words 

		if vertex.edges[char_val] != None:
			n = n + 1
			search_word_in_trie(vertex.edges[char_val], word, n, word_len)
		else:
			return False		



a = trie()
initialize(a)
add_word(a, "a")
add_word(a, "aa")
print a.edges[0].edges[0].words
#add_word(a, "singh")

print search_word_in_trie(a, "aa", 0, len("aa"))