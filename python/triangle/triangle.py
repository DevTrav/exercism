def is_valid_triangle(sides):
    return len(sides) == 3 and sum(sides) - max(sides) > max(sides)

def equilateral(sides):
    return is_valid_triangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    return is_valid_triangle(sides) and len(set(sides)) <= 2

def scalene(sides):
    return is_valid_triangle(sides) and len(set(sides)) == 3

 #Test cases
triangle1 = [5, 5, 5]
triangle2 = [5, 5, 8]
triangle3 = [3, 4, 5]
triangle4 = [0, 0, 0]  # This violates the triangle inequality

assert equilateral(triangle1)
assert isosceles(triangle1)
assert not scalene(triangle1)

assert not equilateral(triangle2)
assert isosceles(triangle1)
assert not scalene(triangle2)

assert not equilateral(triangle3)
assert not isosceles(triangle3)
assert scalene(triangle3)

assert not is_valid_triangle(triangle4)#
print("All assertions passed.")