#take input for three sides of triangles, check if triangle is possible with the input sides.
side1 = int(input("Enter the first side:"))
side2 = int(input("Enter the second side:"))
side3 = int(input("Enter the third side:"))


if side1+side2 > side3 and side1+side3 > side2 and side2+side3 > side1:
    print("Triangle is  possible.")

else:
    print("Triangle is not possible.")

