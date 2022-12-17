# Define a function to return the type of triangle
def typeOfTriangle(sideOne, sideTwo, sideThree):
    # Check if both sideOne and sideTwo are equal or sideOne and sideThree are equal
    if sideOne == sideTwo or sideOne == sideThree:
        # Now that either sideOne is equal to sideTwo or sideOne = sideThree, we can make an equilateral triangle check by checking if sideTwo and sideThree are equal too
        if sideTwo == sideThree:
            # Since all the 3 sides are equal, the triangle is an equilateral triangle
            return('Equilateral triangle')
        else:
            # Not all 3 sides are equal, but 2 sides are equal and hence the triangle is an Isosceles triangle
            return('Isosceles triangle')
    elif sideTwo == sideThree:
            # This executes if sideOne is not equal to both sideTwo and sideThree. Here, if sideTwo and sideThree are equal, the triangle is an Isosceles triangle since two sides are equal
        return('Isosceles triangle')
    else:
        # If no sides are equal, the triangle is a Scalene triangle
        return('Scalene triangle')

# Declare three sides of a triangle
sideOne = 10
sideTwo = 20
sideThree = 20
# Declare a variable to store the type of the triangle returned
triangle = typeOfTriangle(sideOne, sideTwo, sideThree)
print(triangle)

# Output => Isosceles triangle
