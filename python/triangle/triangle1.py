# Iteration 1
def is_valid_triangle(sides):
    if len(sides) != 3:
        return False

    a, b, c = sorted(sides)
    return a + b > c

def equilateral(sides):
    return is_valid_triangle(sides) and sides[0] == sides[1] == sides[2]

def isosceles(sides):
    return is_valid_triangle(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])

def scalene(sides):
   return is_valid_triangle(sides) and sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]
   

# test case
#triangle1 = [0,0,0]

#assert equilateral(triangle1) == False