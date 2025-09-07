
"""
1.  Pre-computation analysis:
    *   We are given an array of integers (can be positive, negative, or zero).
    *   The array can be of any length, including empty, but the problem usually expects at least two elements.
    *   The value k is a non-negative integer.
    *   The task is to find the number of unique k-diff pairs in the array.
        A k-diff pair is defined as an integer pair (i, j), where i != j and |nums[i] - nums[j]| == k.

2.  Problem Definition:
    *   Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
    *   Unique means that the pair (i, j) and (j, i) are considered the same, and only counted once.

3.  Brute-Force Analysis:
    *   The brute-force approach would be to check all possible pairs (i, j) with i < j and count those with |nums[i] - nums[j]| == k.
    *   To avoid duplicates, we can use a set to store pairs in sorted order.
    *   This approach has O(n^2) time complexity, which is not efficient for large arrays.

4.  Optimal Solution:
    *   The optimal solution uses sorting and two pointers, or a hash map for frequency counting.
    *   For k > 0, we can use a set or hash map to check if num + k exists for each unique num.
    *   For k == 0, we count elements that appear more than once.
    *   Both approaches reduce the time complexity to O(n log n) (for sorting) or O(n) (for hash map).
"""

"""
5.  Optimal Implementation:
"""

def findPairs(nums: list[int], k: int) -> int:
    """
    Two-pointer approach after sorting:
    *   Sort the array to bring duplicates together and allow efficient pair searching.
    *   Use two pointers (i, j) to scan for pairs with difference k.
    *   Skip duplicates to ensure unique pairs.
    *   Time complexity: O(n log n) due to sorting, O(n) for the two-pointer scan.
    """
    nums.sort()
    n = len(nums)
    i, j = 0, 1
    count = 0
    while j < n:
        if i == j or nums[j] - nums[i] < k:
            j += 1
        elif nums[j] - nums[i] > k:
            i += 1
        else:
            count += 1
            i += 1
            j += 1
            while j < n and nums[j] == nums[j - 1]:
                j += 1
    return count


# Optimized solution using hash map (Counter):
from typing import List
from collections import Counter
def findPairsOptimized(nums: List[int], k: int) -> int:
    """
    Hash map approach:
    *   Count the frequency of each number using Counter.
    *   For k == 0, count numbers that appear more than once (pairs of identical numbers).
    *   For k > 0, for each unique number, check if num + k exists in the map.
    *   Each valid pair is counted only once.
    *   Time complexity: O(n)
    """
    counter = 0
    freqMap = Counter(nums)
    if k == 0:
        for key, value in freqMap.items():
            # For k = 0, only pairs of identical numbers are valid
            if value > 1:
                counter += 1
    else:
        for key in freqMap:
            if key + k in freqMap:
                counter += 1
    return counter


"""
6.  Complexity:
    *   Two-pointer solution: O(n log n) (sort) + O(n) (scan) = O(n log n)
    *   Hash map solution: O(n) (build map and scan)
    *   Space complexity: O(n) for hash map
"""

"""
7.  Testing:
    *   Test cases to verify correctness for both k = 0 and k > 0.
    *   Edge cases: duplicates, no pairs, negative numbers, empty array.
"""
if __name__ == "__main__":
    nums1 = [3,1,4,1,5]
    nums2 = [1,3,1,5,4]
    nums3 = [1,2,4,4,3,3,0,9,2,3]
    print(findPairs(nums1, 2))
    print(findPairs(nums2, 0))
    print(findPairs(nums3, 3))