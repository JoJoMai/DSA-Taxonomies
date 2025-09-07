from typing import List

def minimizeMax(nums: List[int], p: int) -> int:
    n = len(nums)
    # 1. sort the array, sorting will help finding the pairs with the smallest diff fast
    nums.sort()
    
    # 2. implement binary search, why? because I am trying to find a diff, a match, a result of manipulating a pair, the data is large, 10^9, so binary is way to go
    a = 0 # smallest possible diff
    b = nums[-1] - nums[0] # largest possible diff
    lastGoodGuess = b
    def can_form_p_pairs(mid):
        pairs = 0
        i = 1
        while (i < n):
            if nums[i] - nums[i-1] <= mid:
                pairs += 1
                i += 2
            else:
                i += 1
            if pairs >= p:
                return True
        return False
    while (a <= b): # they collapses we found the ideal result
        mid = (b + a) // 2
        if can_form_p_pairs(mid):
            b = mid - 1
            lastGoodGuess = mid
        else :
            a = mid + 1
    return lastGoodGuess

if __name__ == "__main__":
	nums1 = [10,1,2,7,1,3]
	p1 = 2
	result1 = minimizeMax(nums1, p1)
	print(f"Input: nums = {nums1}, p = {p1}")
	print(f"Output: {result1}")
	print()
	
	nums2 = [4,2,1,2]
	p2 = 1
	result2 = minimizeMax(nums2, p2)
	print(f"Input: nums = {nums2}, p = {p2}")
	print(f"Output: {result2}")
	print()
	
	nums3 = [3,3,3,3]
	p3 = 2
	result3 = minimizeMax(nums3, p3)
	print(f"Input: nums = {nums3}, p = {p3}")
	print(f"Output: {result3}")
	print()