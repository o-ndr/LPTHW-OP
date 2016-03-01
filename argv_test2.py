# source https://gist.github.com/macloo/8493442
# see http://bit.ly/mmpython2 for the quiz 
# compare the way this runs to the way argv_test1.py runs 

# the filename you type must be the name of a file in the same folder with this file
# to run:
#          python argv_test2.py

print "Type the name of a text file." # e.g. gators.txt
filename = raw_input("> ")

txt = open(filename)
print txt.read()		# comment this line out and run again. Compare 
print "-" * 10
print filename
txt.close()
