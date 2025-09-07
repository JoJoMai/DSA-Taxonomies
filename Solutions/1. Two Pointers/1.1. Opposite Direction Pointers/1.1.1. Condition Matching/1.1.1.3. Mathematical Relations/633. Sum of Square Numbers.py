from typing import List
from math import isqrt

def judgeSquareSum(c: int) -> bool:
    """
    Check if there exist integers a, b such that:
        a^2 + b^2 = c
    Key properties:
    - Range of a and b: [0, sqrt(c)]
    - Opposite pointers: one starts low, one high
    - Movement is guided by comparing res with target c
    """

    a, b = 0, isqrt(c)

    while a <= b:
        res = a*a + b*b
        if res == c:
            return True
        elif res > c:
            b -= 1   # sum too big, shrink high pointer
        else:
            a += 1   # sum too small, grow low pointer

    return False
