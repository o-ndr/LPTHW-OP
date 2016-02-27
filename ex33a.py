# Ex 33a
# source: http://codepad.org/gGRRi2qW

# NOTE if you increment by the same number you start with,
# you can print out the results of a times table, e.g.
# 7, 14, 21, 28 ...

def initialize():
	i = int(raw_input("Type a low whole number: "))
	j = int(raw_input("Type a high whole number: "))
	k = int(raw_input("Type a number for incrementing: "))
	numbers = []
	return i, j, k, numbers
	
def make_numbers():
	i, j, k, numbers = initialize()
	while i < j:
		print "At the top i is %d" % i # to show us how it works
		numbers.append(i)
		
		i = i + k
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i # also to show how it works 
		
		print "The numbers: "
		
	# print each item in the list on a new line
	for num in numbers:
		print num
	# run another function
	repeat_it()
	
def repeat_it():
	again = raw_input("Go again? (y/n) ")
	if again != "n":
		make_numbers()
		
make_numbers()
