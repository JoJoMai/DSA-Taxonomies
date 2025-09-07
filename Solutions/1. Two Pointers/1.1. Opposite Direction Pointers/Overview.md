# Two Pointers Pattern: Opposite Direction

## Overview
The **opposite direction two pointers** pattern is a fundamental technique in algorithm design.  
It involves placing two pointers at the extremes of a range (e.g., array, string, number line) and moving them toward each other.  

The key idea is to **shrink the search space intelligently** while ensuring no valid solution is missed.

---

## When to Use
This pattern is effective when:
- The data has **predictable structure** (sorted, monotonic, or symmetric).
- The problem can be solved by **progressively narrowing a range**.
- Pointer moves can **safely discard part of the space** (without losing valid solutions).

---

## Philosophy
- **Start wide, shrink smart.**
- Pointer movements are guided by a **condition**:
  - Example: too small → move left pointer forward.
  - Example: too large → move right pointer backward.
  - Symmetry checked → move both inward.
- Each move reduces the range until a solution is found or confirmed absent.
- Not every problem with “two ends” suits this pattern (e.g., expanding from center is different).

---

## Common Applications

### Condition Matching
- **Target Sum Variants**:  
  - `167. Two Sum II`  
  - `15. 3Sum`  
  - `18. 4Sum`  
  - `1099. Two Sum Less Than K`
- **Palindrome Detection**:  
  - `125. Valid Palindrome`  
  - `680. Valid Palindrome II`
- **Mathematical Relations**:  
  - `633. Sum of Square Numbers`  
  - `611. Valid Triangle Number`  
  - `69. Sqrt(x)` (Binary Search)

### Optimal Pair Finding
- **Volume Optimization**:  
  - `11. Container With Most Water`  
  - `42. Trapping Rain Water`
- **Distance Optimization**:  
  - `532. K-diff Pairs in an Array`  
  - `1877. Minimize Maximum Pair Sum in Array`
- **Statistical Optimization**:  
  - `2616. Minimize Maximum Difference of Pairs`  
  - `881. Boats to Save People`

### Multi-Element Extensions
- **N-Sum Problems**:  
  - `15. 3Sum`  
  - `16. 3Sum Closest`  
  - `18. 4Sum`
- **Complex Conditions**:  
  - `611. Valid Triangle Number`  
  - `923. 3Sum With Multiplicity`

---

## Key Insights
- The pattern works because **shrinking the range preserves completeness** of the solution.
- The essence is not the data type, but having a **range that can be safely reduced**.
- Variations like **expand around center** are related but distinct.

---

## TL;DR
**Opposite direction two pointers = place markers at both ends → shrink intelligently → converge on solution.**

---

## Example: Two Sum II

```python
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
````

* Sorted array allows safe shrinking of search space.
* Each pointer move either eliminates a smaller or larger element until the sum matches.

---

## Example: Container With Most Water

```python
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
```

* The shorter line limits the area, so moving it inward is safe to potentially improve the result.

