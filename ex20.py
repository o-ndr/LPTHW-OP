from sys import argv

script, input_file = argv

# Function that takes one argument which will be a file.
# When the function is called, it will read the contents of the file
# and print it all out
def print_all(f):
	print f.read()

# when called with argument (file name), the method seek
# will take us back to position zero within the file 	
def rewind(f):
	f.seek(0)
# for the object f, do this method/function seek

# when called, the function takes 2 arguments - 
# line count and file name (see below, current_line and current_file) 
def print_a_line(line_count, f):
	print line_count, f.readline()
# Inside readline() is code that scans each byte of the file
# until it finds a \n character, then stops reading the file
# to return what it found so far.
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)	

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# variable current line is defined as 1
# the variable is passed into function print_a_line as 1st argument "line_count"
# the function runs with 2 arguments - 1 and file name, 
# and prints line_count, then method readline is run on a file
# (which apparently reads and stores in memory the content of that line)
# and then that corresponding line is printed out
current_line = 1
print_a_line(current_line, current_file)

# below is where variable current_line becomes 2 (1 + 1)
# Function print_a_line takes 2 arguments: 2 and file.
# Function returns (prints out) 2 + the line that has been
# read from the file, as specified in the function - print line_count, f.readline()
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line (current_line, current_file)


	