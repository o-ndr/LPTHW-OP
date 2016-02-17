# functions
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b) 
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b 
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b 


# variables
guests = multiply(3, 4) # 3 families, 4 persons each
seats = add(2, 7) # coz two more seats for hosts
pizzas = multiply(guests, 2) # each guest eats 2 pizzas, wow
mushrooms = multiply(pizzas, 12) # 12 mushrooms on each pizza 


print "Seats: %d, Guests: %d, Pizzas: %d, Mushrooms: %d" % (seats, guests, pizzas, mushrooms)

fake_formula_solved = divide((add(guests, seats)),(subtract (pizzas, mushrooms)))  

print "Solution to some fake math example is ", fake_formula_solved