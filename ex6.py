# Assigns text to variable X, inserts parameter into format character
x = "There are %d types of people." % 10

# assigns text string to variable
binary = "binary"

# assigns text string to variable
do_not = "don't"

# Assigns text to variable Y, text contains two format characters
# that will be replaced with text from variables "binary" and "do_not"
y = "Those who know %s and those who %s." % (binary, do_not)

# prints X
print x

# Prints Y
print y 

# Prints a string  where the format character
# is replaced with another string from variable X
print "I said: %r." % x 

# Prints a string where the format character
# is replaced with another string from variable Y 
print "I also said: '%s'." % y 

# Assigns the value of False to variable "hilarious"
hilarious = False

# Assigns a string to variable "joke_evaluation"
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints two strings, concatenated
print joke_evaluation % hilarious

# Assigns a string to variable W 
w = "This is the left side of..."

# Assigns a string to variable E 
e = "a string with a right side."

# Prints tow strings from variables W and E, concatenated. 
print w + e