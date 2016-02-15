from sys import argv

script, myfilename = argv

print "I am writing now into file %r." % myfilename

target = open(myfilename, 'w')

print "Type the text into your own file:"

text_in_ownfile = raw_input("text in file: ")

print "Writing the above into a file now."

target.write(text_in_ownfile)

target.close()


