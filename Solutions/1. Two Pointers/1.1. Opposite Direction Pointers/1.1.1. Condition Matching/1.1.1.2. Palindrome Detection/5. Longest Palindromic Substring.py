"""
Problem: Given a string s, find the longest palindromic substring in s.
"""

from typing import List

def longestPalindrome(s: str) -> str:    
    def expand(i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1: j]
    longest = ""
    for i in range(len(s)):
        odd = expand(i,i)
        if len(odd) > len(longest):
            longest = odd
        even = expand(i, i+1)
        if len(even) > len(longest):
            longest = even
    return longest
        
if __name__ == "__main__":
    test_cases = [
        "babad",
        "cbbd",
        "a",
        "ac",
    ]
    for s in test_cases:
        print(f"Longest palindromic substring of '{s}': {longestPalindrome(s)}")