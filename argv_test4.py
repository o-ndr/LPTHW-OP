# source https://gist.github.com/macloo/8493442
# see http://bit.ly/mmpython2 for the quiz 

# to run:
#         python argv_test4.py gators.txt first.txt

from sys import argv 
script, file1, file2 = argv

f1 = open(file1)
f2 = open(file2)

print '''
The length of %s is %d bytes, and the length of %s is %d bytes.
''' % (file1, len(f1.read()), file2, len(f2.read()))

f1.close()
f2.close()
