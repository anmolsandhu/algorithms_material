

comb = []
bogus = []

def generate_substrings(current , leftover, check_word, found):
	global comb
	global bogus
	if len(leftover) == 0:
		comb.append(current)
		return
	else:

		backtrack, found = check_condition(current, check_word)
		if backtrack == True:
			bogus.append(current)
			return

		comb.append(current)
		#print current
		for i in range(len(leftover)):
			remain = leftover[0:i] + leftover[i+1:]
			generate_substrings(current + leftover[i], remain, check_word)



def check_condition(word, check_word):

	check_word_len = len(check_word)
	word_len = len(word)

	flag = False
	if len(word) > len(check_word):
		return True
	for i in range(len(word)):
		if word[i] != check_word[i]:
			flag = True
			break
	if flag == True and len(word) == len(check_word):
		return [True, 1]

	return flag





generate_substrings("", "abcdnjimliopltpandjnadj", "anmol")
print comb
print bogus















		


