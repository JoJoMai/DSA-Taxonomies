"""
Problem:
Given an array of integers nums and an integer target
find the number of unique pairs (i, j)
such that i < j and nums[i] + nums[j] < target.
"""
from typing import List

def	twoSumLessThanK(nums, target):
	nums.sort()
	n = len(nums)
	a = 0
	b = n - 1
	count = 0
	while (a < b):
		res = nums[a] + nums[b]
		if res < target:
			count += (b - a)
			a += 1
		else:
			b -= 1
	return count


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    target = 5
    result = twoSumLessThanK(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")