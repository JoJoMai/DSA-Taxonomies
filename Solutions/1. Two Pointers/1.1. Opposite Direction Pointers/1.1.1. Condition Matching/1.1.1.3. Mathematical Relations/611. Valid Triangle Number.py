from typing import List

def triangleNumber(nums: List[int]) -> int:
    """
    Count the number of triplets that can form a valid triangle.

    Key properties:
    - Triangle inequality: for sides (a, b, c) with a <= b <= c,
      we only need to check: a + b > c.
    - Sorting allows us to fix the largest side c and search pairs (a, b).
    """

    nums.sort()
    n = len(nums)
    count = 0

    # Fix the largest element nums[i] as side c
    for i in range(n - 1, 1, -1):
        a, b = 0, i - 1

        # Two pointers on [0 ... i-1]
        while a < b:
            if nums[a] + nums[b] > nums[i]:
                # nums[a+1] ... nums[b-1] with nums[b] will also work,
                # so count them all at once
                count += b - a
                b -= 1
            else:
                # too small, need bigger sum → move left pointer
                a += 1

    return count
