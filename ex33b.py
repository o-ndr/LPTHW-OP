# source http://codepad.org/VUzevLxv

# The two tests here produce exactly the same list (array) at the end.

# initialize vars
i = 7 
j = 70
k = 70
numbers = []

print "\nThe 'for' loop:\n"

# ----------------------------------------
# test 1 is a for loop, using range()

for i in range(i, j, k): #3rd arg is optonal, it is the increment
	print "At the top i is %d" % i # to show us how it works
	numbers.append(i) # put i into the list, numbers
	print "Numbers now: ", numbers
	print "At the bottom is is %d" % i # also to show us how it works
	print
	
for num in numbers:
	print num,
	
# re-set vars
i = 7
j = 70
k = 7 
numbers = []

print"\nThe 'while' loop:\n"

# ----------------------------------------
# test 2 is a while loop
while i < j:
	print "At the top is is: %d" % i # to show us how it works
	numbers.append(i) # put i into the list, numbers
	i = i + k # NOTE how this is different from test 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i # also to show how it works
	print
	
for num in numbers:
	print num,