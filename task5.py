def get_area(side1, side2, side3):
    #calculating perimeter of the triangle
    s = (side1 + side2 + side3) / 2
    return  (s*(s - side1) * (s - side2) * (s - side3)) ** 0.5


print(get_area(5, 3, 5))
