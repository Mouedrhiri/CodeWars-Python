# Implement a method that accepts 3 integer values a, b, c.
# The method should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).


# IMPORTANT!!!!!!:
# Required Knowledge. A triangle is a valid triangle, If and only If, the sum of any two sides of a triangle is greater than the third side. 
# For Example, let A, B and C are three sides of a triangle.
# Then, A + B > C, B + C > A and C + A > B.

def is_triangle(a, b, c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        return True
    else:
        return False
