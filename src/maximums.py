def max_of_two(x: int, y: int) -> int:
    if x >= y:
        biggest = x
    else:
        biggest = y
    return biggest

def max_of_three(x: int, y: int, z: int) -> int:
    if max_of_two(x,y) > z:
        biggest = max_of_two(x,y)
    else:
        biggest = z
    return biggest
