from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN/ENTER."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to a file."

target.write('%s\n%s\n%s\n' % (line1,line2,line3))
# Solution above taken from http://stackoverflow.com/questions/6394170/very-basic-python-question-strings-formats-and-escapes


print "And finally, we close it."
target.close()
