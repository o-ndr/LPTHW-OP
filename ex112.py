name = raw_input("What is your name?")
print "Hello, %s." % name

weight = raw_input("How much do you weigh?")
height = raw_input("How tall are you?")
age = raw_input("How old are you?")

print "So, you are %s old, %s tall and %s heavy." % (age, height, weight)

# The code below is taken from here: http://www.cyberciti.biz/faq/python-raw_input-examples/
print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Backup")
print ("2. User management")
print ("3. Reboot the server")
print (30 * '-')
 
## Get input ###
choice = raw_input('Enter your choice [1-3] : ')
 
### Convert string to int type ##
choice = int(choice)
 
### Take action as per selected menu-option ###
if choice == 1:
        print ("Starting backup...")
elif choice == 2:
        print ("Starting user management...")
elif choice == 3:
        print ("Rebooting the server...")
else:    ## default ##
        print ("Invalid number. Try again...")
 