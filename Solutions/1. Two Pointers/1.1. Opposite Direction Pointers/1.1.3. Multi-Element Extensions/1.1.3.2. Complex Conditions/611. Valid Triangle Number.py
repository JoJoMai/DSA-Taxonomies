class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        *   we are given an array of positive numbers: nums
            to count all triplets that form can form a triangle
            a triplet that can form a triangle is a triplet where:
            *   a <= b <= c and a + b > c
            so this becomes a condition matching problem, with multiple elements
            Approach:
            *   we sort the array to achieve the a <= b <= c state
            *   we loop in reverse, fixing the largest number and counting all valid pairs
            *   a valid pair is one that its sum is bigger than the number we fixed
        """
        nums.sort()
        n = len(nums)
        count = 0
        for c in range(n - 1, 1, -1):
            a = 0
            b = c - 1
            while (a < b):
                res = nums[a] + nums[b]
                if res > nums[c]:
                    count += b - a
                    b -= 1
                else:
                    a += 1
        return count