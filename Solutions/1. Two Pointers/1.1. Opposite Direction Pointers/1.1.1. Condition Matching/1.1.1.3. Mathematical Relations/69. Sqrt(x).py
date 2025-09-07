from typing import List

def mySqrt(x: int) -> int:
        # we are looking for a value between 0 and x
        # that satisfy this condition: val * val = x
        # we can use binary search to reduce the complexity to O(log n)
        minVal = 0
        maxVal = x
        bestVal = 0
        while (minVal <= maxVal):
            mid = (minVal + maxVal) // 2
            res = mid * mid
            if res == x:
                return mid
            elif res < x:
                bestVal = max(mid, bestVal)
                minVal = mid + 1
            else:
                maxVal = mid - 1
        return bestVal
