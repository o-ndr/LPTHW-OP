# imports argv argument variable (aka argv feature) from the sys module (aka package)
# This variable holds the arguments you pass to your Python script.
from sys import argv

# This code unpacks argv so it gets assigned to the two variables I work with.
# It just says, "Take whatever is in argv, unpack it,
# and assign it to all of these variables on the left in order." 
script, filename = argv

# In this code, I use the open command. 
# This command takes a parameter and returns a value.
# The returned value is assigned to my on variable txt.
txt = open(filename)

# Prints the format string with the name of the file form the filename variable.
# Filename variable contains the name of the file I'd type in the command line.
print "Here's your file %r:" % filename

# This code prints the contents of the file. 
# We call a function on the txt named read.
# I got the file from open command (line 13 above)
# I can give this file a command by adding a dot (.) and the name of command
# txt.read() says, "Hey txt! Do your read command with no parameters!"
print txt.read()

# Prints the string 
print "Type the filename again:"
# Assigns the file name taken form the user input to the file_again variable
file_again = raw_input("> ")

# This code uses the open command
# which takes the file_again variable as a parameter
# (that parameter will be the name of the file taken from user input)
# and returns the value that is assigned to my own txt_again variable 
txt_again = open(file_again)

# This code prints out the contents of the file. How?
# The function read() with no parameters is called on the txt_again variable.
# The txt_again contains the file that was "opened" in line 35
# I give this file a read command by adding a dot (.) and the read command
print txt_again.read()