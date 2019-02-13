#This program is used to determine the cost on a order of hats

def order_total(num):
	
	hats = num
	boxes = hats / 2
	singles = hats % 2
	cost_box = 50.00
	cost_single = 10.00
	shipping = 2 * hats
	total_cost = (boxes * cost_box) + (singles * cost_single) + shipping
	return total_cost

def order_total_overnight(num):
	
	hats = num
	cost_single = 10.00
	if (hats <= 5):
		shipping = 32.00
	elif (hats > 5 && hats <=20)
		shipping = 45.00
	elif (hats > 20)
		shipping = 3.00 * hats
	total_cost = (cost_single * hats) + shipping
	return total_cost

hats = input ("How many hats?")
shipping = raw_input("Use overnight shipping (Y/N)?"
if (shipping == 'y'):
	cost = order_total_overnight(hats)
else:
	cost = order_total(hats)
