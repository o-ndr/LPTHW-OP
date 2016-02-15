from sys import argv

script, user_first_name, user_last_name = argv
pronto = '> '

print "Hi %s %s, I'm the %s script." % (user_first_name, user_last_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s %s?" % (user_first_name, user_last_name)
likes = raw_input(pronto)

print "Where do you live, %s %s?" % (user_first_name, user_last_name)
lives = raw_input(pronto)

print "What kind of computer do you have?"
computer = raw_input(pronto)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)