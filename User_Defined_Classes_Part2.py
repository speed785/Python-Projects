#User-Defined Classes part 2

import rectangle

# Create a rectangle of with the defaut values for width and height
r = rectangle.Rectangle()
# Use the mutators to assign values to the instance variables.
r.setWidth(4)
r.setHeight(5)
print("The rectangle has the following measurements:")
# Use the accessor methods to retrive the values of the instance variables.
print("Width is" , r.getWidth())

r.setHeight(5)
print("The rectangle has the following measurements: ")
# Use the accessor methods to retrieve the values of the instance variables. 
print("Width is", r.getWidth())
print("Height is", r.getHeight())
# Use methods to calculate the area and perimeter of the rectangle.
print("Area is", r.area())
print("Perimeter is", r.perimeter())