# Our function is called with two arguments: a and b.
# We print out what our function is doing, in this case "ADDING."
# Then we tell Python to do something kind of backward:\
# we return the addition of a + b.
# You might say this as, "I add a and b then return them."

# Python adds the two numbers.
# Then when the function ends, any line that runs it
# will be able to assign this a + b result to a variable. E.g. to "age" below.
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b 

def multiply(a, b):
	print "MULPTIPLYING %d * %d" % (a, b)
	return a * b 
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b 
	

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# I'm taking the return value of one function
# and using it as the argument of another function.
# add is a function. age and subtract are arguments. 
# age will be added to the result of the operations done in subtract
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "can you do it by hand?"
# -4391?