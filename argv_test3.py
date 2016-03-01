# source https://gist.github.com/macloo/8493442
# see http://bit.ly/mmpython2 for the quiz 

# CAREFUL - do not give the name of a file you want to keep 
# use a junk file only! Or name a file that does not exist 
# after you run this, check the folder conatining this file & check the contents of the junk file 

# to run:
#          python argv_test3.py junkfile.txt

from sys import argv
script, filename = argv

target = open(filename, 'w')
target.close() 