# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.

def is_inside_bounds(x, y):
    if 0<=x<=10 and 0<=y<=10:
        return True
    return False

print(is_inside_bounds(5, 87))
