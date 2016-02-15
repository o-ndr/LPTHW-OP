name = 'Oleksandr Pysaryuk'
age = 36 #not a lie
height = 185 # centimeters
weight = 85 #kilograms
eyes = 'grey'
teeth = 'white'
hair = 'brown'
weight_in_lb = weight / 0.453
height_in_inches = height / 2.54
height_in_feet = height / 30.48
height_in_feet_and_inches = height_in_inches / 12


print "Let's talk about %s." % name
print "He's %d cm tall." % height
print "He's %d inches tall." % height_in_inches
print "He's %d ft tall." % height_in_feet
print "He's %d ft tall." % height_in_feet_and_inches
print "He is %d kg heavy." % weight
print "He is %d lb heavy." % weight_in_lb
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to et it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
