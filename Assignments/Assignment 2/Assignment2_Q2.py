# This program is for converting a date to a different style

def convert_format(date):
	month_entered = date[0:1]
	day = date[3:4]
	year = date[5:6]
	months =  ["January", "February", "March", "April", \
	"May", "June", "July", "August", "September", "October", "November", "December"]
	for i in months:
		if months = month_entered:
			print months[i]
	print (" " + day + "/ ")
	print (year)
	
date = input ("Please enter the date(mm/dd/yy): ")
print ("The date is " + convert_format(date))