def circle_area(radius, height):
    area = 3.14 * radius * radius
    volume_cyl = area * height
    return volume_cyl

x = input("Please enter the radius: ")
y = input("Please enter the height: ")
print "The total volume is", circle_area(x, y)
