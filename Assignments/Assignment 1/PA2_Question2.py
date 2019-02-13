#Finding out whether a year is a leap year or not

year = input ("Please enter the year that is greater than 100: ")

if year <= 100:
    print "Error: Year is less than or equal to 100"

if year % 4 != 0:
    print year ,"is not a leap year!"
           
if year % 100 == 0:
    if year % 400 == 0:
        print year ,"is a leap year!"
    else:
        print year ,"is not a leap year!"
else:
    if year % 4 == 0:
        print year ,"is a leap year!"
        

        

