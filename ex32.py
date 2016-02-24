the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
	
# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
# Also we can go through mixed lists, too
# Notice how we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i
	
# We can also build lists, first start with an empty one
elements = range(6)
# See this above: Could you have avoided that for-loop entirely
# and just assigned range(0,6) directly to elements?
for i in elements:
	print "Adding %d to the list." % i
	#elements.append(i)
# Append is a function that lists understand
	
# Now we can print them out, too
for i in elements:
	print "Element was: %d" % i
	
# And there's an easier way to do fill in the list in one command
# elements2 = range(6)
# for i in elements2:
#	print "Elements2 item was: %d" % i


