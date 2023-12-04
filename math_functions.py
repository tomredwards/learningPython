
def add_two(left, right):
    i_left = int(left)
    i_right = int(right)
    return i_left + i_right


def add_many(*args):
    sum = 0

    for arg in args:
       sum += arg

    return sum


