def cube(x: int) -> int:
    if type(x) not in [int, float]:
        raise TypeError
    return x**3