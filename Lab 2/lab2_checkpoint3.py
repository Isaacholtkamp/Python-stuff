name = raw_input ("Please insert customer's name: ")
num_nights = input ("Please enter their stay: ")
telecharge = input ("Please enter phone charge: ")
charge = num_nights * 55
etax = charge * .1
totbill = charge + etax + telecharge

print "Customer's full name: ", name
print "Number of nights: ", num_nights
print "Total room service charge ($): ", charge
print "Telephone charge ($): ", telecharge
print "River Bend Hotel Bill (Customer : ", name
print "Total room charge ($): ", charge
print "Total entertainment charge ($): ", etax
print "Total bill ($): ", totbill
