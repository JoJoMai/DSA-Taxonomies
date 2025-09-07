
"""
1.  Pre-computation analysis:
    *   We are given an array of positive integers.
    *   The array length is always even (as per problem statement).
    *   The task is to pair up the numbers such that the largest sum among all pairs is minimized.
    *   The array can be large, so an efficient solution is needed.

2.  Problem Definition:
    *   Given an array nums of even length, pair up the elements into n/2 pairs.
    *   For each pair, compute the sum. Return the minimum possible value of the maximum pair sum.

3.  Brute-Force Analysis:
    *   Try all possible pairings and compute the maximum sum for each configuration.
    *   This approach is not feasible for large arrays due to factorial time complexity.

4.  Optimal Solution:
    *   Sort the array.
    *   Pair the smallest element with the largest, the second smallest with the second largest, and so on.
    *   This greedy approach ensures the maximum pair sum is minimized.
    *   Time complexity is dominated by sorting: O(n log n).
"""

"""
5.  Optimal Implementation:
"""
from typing import List

def minPairSum(nums: List[int]) -> int:
    """
    Greedy two-pointer approach:
    *   Sort the array to align smallest and largest elements.
    *   Use two pointers (a, b) from both ends, pairing nums[a] + nums[b].
    *   Track the maximum sum among all pairs.
    *   Return the largest sum found, which is minimized by this strategy.
    *   Time complexity: O(n log n) for sorting, O(n) for pairing.
    """
    n = len(nums)
    if n == 2:
        return nums[0] + nums[1]
    nums.sort()
    a = 0
    b = n - 1
    maxPairSum = 0
    while a < b:
        maxPairSum = max(maxPairSum, nums[a] + nums[b])
        a += 1
        b -= 1
    return maxPairSum


"""
6.  Complexity:
    *   Time complexity: O(n log n) (sort) + O(n) (pairing) = O(n log n)
    *   Space complexity: O(1) if sorting in-place, O(n) otherwise
"""

"""
7.  Testing:
    *   Test with small and large arrays, including edge cases.
    *   Verify that the returned value is the minimized maximum pair sum.
"""
if __name__ == "__main__":
    nums1 = [3,5,2,3]
    nums2 = [3,5,4,2,4,6]
    print(minPairSum(nums1))
    print(minPairSum(nums2))