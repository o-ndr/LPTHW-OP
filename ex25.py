# I add the 'sentence' variable in Python (run python -i in git bash)
# then assign the sentence with a few words to the variable

# words = ex25.break_words(sentence) means:
# 1: create variable 'words'
# 2: run function 'break_words' with argument 'sentence' on 'ex25'.
# 3: This function breaks words (using .split method/function on the values of the arguments. 
# The argument was 'stuff', in Python I created sentence variable,
# it's value was then used as argument for the break_words function
# so the function used its own variable 'words' did the .split,
# and returned the broken words as 'words'
# When I type 'words' in Python, I get this:
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']


def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	"""Sorts the words"""
	return sorted(words)
	
def print_first_word(words):
	"""Prints the first word after popping it off"""
	word = words.pop(0)
	print word
# How can the words.pop function change the words variable?
# That's a complicated question, but in this case words is a list,
# and because of that you can give it commands
# and it'll retain the results of those commands. 
	
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word
	
# After I run 2 previous functions (ex25.print(first_word(words) & 
# ex25.print_last_word(words))
# the 1st and last words are popped, and variable words will contain
# less 1st and last element of the array words:
# >>> words
# 'good', 'things', 'come', 'to', 'those', 'who']
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
# when this function is run with argument sentence, the value of 'sentence'
# is changed by function 'sort_sentence"
# (sentence gets sorted alphabetically, result is 'words')
# then 'words' is used as argument with which the 2 functions are run
# and they return the popped 1st and last items of the words array
# and they are printed out (because last line in each of those functions is "print word") 

	
	
	
