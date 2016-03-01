# Source https://gist.github.com/macloo/8493442
# see http://bit.ly/mmpython2 for the quiz 
# compare the way this runs to the way argv_test2.py runs 

# to run:
#          python argv_test1.py first.txt

from sys import argv
script, filename = argv 
txt = open(filename)
print txt.read()
print "-" * 10
print filename
txt.close()