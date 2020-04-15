import math

x1 = float(input('Enter x1 co-ordinate : '))
x2 = float(input('Enter x2 co-ordinate : '))
y1 = float(input('Enter y1 co-ordinate : '))
y2 = float(input('Enter y2 co-ordinate : '))

distance = float(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
print('Distance between to point is {} m^2: '.format(distance))
