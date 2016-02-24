# Ex 32a, source: http://codepad.org/QN7Z05Uq


userlist = []

for i in range(0, 100):
    i = raw_input("Add an element (a user name): ")
    userlist.append(i)
    q = raw_input("Do you want to quit? (y/n) > ")
    if q != "n":
	    break
		
print userlist

for i in userlist: # Note that this does not empty the list completely
    print "This was popped: %r" % userlist.pop(-1)
    print "This is the list now: %r" % userlist