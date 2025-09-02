# Algorithm Templates

This reference guide provides ready-to-use code templates for common algorithm patterns. Use these templates as starting points when solving problems.

## Table of Contents
- [Binary Search](#binary-search)
- [Two Pointers](#two-pointers)
- [Sliding Window](#sliding-window)
- [Fast & Slow Pointers](#fast--slow-pointers)
- [Breadth-First Search](#breadth-first-search)
- [Depth-First Search](#depth-first-search)
- [Backtracking](#backtracking)
- [Union Find](#union-find)
- [Trie](#trie)
- [Dynamic Programming](#dynamic-programming)
- [Monotonic Stack](#monotonic-stack)
- [Heap Operations](#heap-operations)

## Binary Search

### Standard Binary Search
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  # Target not found
```

### Binary Search for Leftmost Occurrence
```python
def binary_search_leftmost(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            result = mid  # Found target, but continue searching left
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result
```

### Binary Search on Answer Space
```python
def binary_search_answer(possible_answers, is_valid):
    left, right = min(possible_answers), max(possible_answers)
    
    while left <= right:
        mid = left + (right - left) // 2
        if is_valid(mid):
            # Found a valid answer, but try to optimize further
            result = mid
            right = mid - 1  # For minimizing, use right = mid - 1
            # For maximizing, use: left = mid + 1
        else:
            # Current value is not valid
            left = mid + 1  # For minimizing
            # For maximizing, use: right = mid - 1
            
    return result
```

## Two Pointers

### Opposite Direction Two Pointers
```python
def two_pointers_opposite(nums, target):
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]  # Found target
        elif current_sum < target:
            left += 1  # Increase sum by moving left pointer
        else:
            right -= 1  # Decrease sum by moving right pointer
            
    return [-1, -1]  # Target not found
```

### Same Direction Two Pointers
```python
def two_pointers_same_direction(nums):
    slow = 0  # Slow pointer / write pointer
    
    for fast in range(len(nums)):  # Fast pointer / read pointer
        # Process current element at fast pointer
        if condition(nums[fast]):
            # Do something with slow pointer
            nums[slow] = nums[fast]  # Example: copy element
            slow += 1
            
    return slow  # Often the new length or position
```

## Sliding Window

### Fixed Size Sliding Window
```python
def sliding_window_fixed(nums, k):
    window_sum = sum(nums[:k])  # Sum of first k elements
    result = window_sum
    
    for i in range(k, len(nums)):
        # Remove leftmost element and add next element
        window_sum = window_sum - nums[i-k] + nums[i]
        result = max(result, window_sum)
        
    return result
```

### Variable Size Sliding Window
```python
def sliding_window_variable(s, condition):
    left = 0
    result = 0  # For max length
    window_state = {}  # Or any data structure to track window state
    
    for right in range(len(s)):
        # Add current element to window state
        window_state[s[right]] = window_state.get(s[right], 0) + 1
        
        # Shrink window while condition is not met
        while not is_valid(window_state):
            # Remove leftmost element from window
            window_state[s[left]] -= 1
            if window_state[s[left]] == 0:
                del window_state[s[left]]
            left += 1
            
        # Update result
        result = max(result, right - left + 1)
        
    return result
```

## Fast & Slow Pointers

### Cycle Detection
```python
def has_cycle(head):
    if not head or not head.next:
        return False
        
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next          # Move one step
        fast = fast.next.next     # Move two steps
        
        if slow == fast:  # Cycle detected
            return True
            
    return False  # No cycle
```

### Find Cycle Start
```python
def find_cycle_start(head):
    if not head or not head.next:
        return None
        
    # Detect cycle
    slow = head
    fast = head
    has_cycle = False
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            has_cycle = True
            break
            
    if not has_cycle:
        return None
        
    # Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
        
    return slow  # Cycle start node
```

## Breadth-First Search

### BFS on Graph
```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return result
```

### BFS for Shortest Path
```python
from collections import deque

def shortest_path(graph, start, end):
    if start == end:
        return 0
        
    visited = set([start])
    queue = deque([(start, 0)])  # (node, distance)
    
    while queue:
        node, distance = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor == end:
                return distance + 1
                
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
                
    return -1  # No path found
```

## Depth-First Search

### DFS Recursive
```python
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
        
    visited.add(node)
    result = [node]
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
            
    return result
```

### DFS Iterative
```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # Add neighbors in reverse order to process in the original order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return result
```

## Backtracking

### Backtracking Template
```python
def backtracking(choices, state, solutions):
    if is_valid_solution(state):
        solutions.append(state.copy())  # Add copy of current state
        return
        
    for choice in choices:
        if is_valid(state, choice):
            # Make choice
            state.append(choice)
            
            # Recurse
            backtracking(choices, state, solutions)
            
            # Undo choice (backtrack)
            state.pop()
```

### Subset Generation
```python
def subsets(nums):
    result = []
    
    def backtrack(start, curr):
        # Add current subset to result
        result.append(curr[:])
        
        for i in range(start, len(nums)):
            # Include nums[i] in current subset
            curr.append(nums[i])
            
            # Recurse to next position
            backtrack(i + 1, curr)
            
            # Backtrack
            curr.pop()
    
    backtrack(0, [])
    return result
```

## Union Find

### Union Find with Path Compression
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
        
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
            
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
                
        return True
```

## Trie

### Trie Implementation
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
        
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

## Dynamic Programming

### 1D Dynamic Programming
```python
def one_dimensional_dp(n, initial_conditions):
    # Initialize DP array with base cases
    dp = [0] * (n + 1)
    dp[0] = initial_conditions
    
    for i in range(1, n + 1):
        # Compute dp[i] based on previous states
        dp[i] = function_of_previous_states(dp, i)
        
    return dp[n]
```

### 2D Dynamic Programming
```python
def two_dimensional_dp(n, m):
    # Initialize DP table with base cases
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    # Set base cases
    for i in range(n + 1):
        dp[i][0] = base_case_value
        
    for j in range(m + 1):
        dp[0][j] = base_case_value
        
    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = function_of_previous_states(dp, i, j)
            
    return dp[n][m]
```

## Monotonic Stack

### Next Greater Element
```python
def next_greater_element(nums):
    n = len(nums)
    result = [-1] * n  # Default to -1 (no greater element)
    stack = []  # Stack to store indices
    
    for i in range(n):
        # While stack is not empty and current element is greater than element at stack's top
        while stack and nums[i] > nums[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = nums[i]  # Set next greater element
            
        stack.append(i)
        
    return result
```

## Heap Operations

### Heap for Top K Elements
```python
import heapq

def find_top_k(nums, k):
    # Min heap approach (keeping k largest elements)
    min_heap = []
    
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
            
    return min_heap
```

### Custom Comparator with Heap
```python
import heapq

def custom_heap_sort(items, key_function):
    # Create list of tuples: (key, item)
    heap_items = [(key_function(item), item) for item in items]
    
    # Heapify the list
    heapq.heapify(heap_items)
    
    # Extract items in order
    result = []
    while heap_items:
        _, item = heapq.heappop(heap_items)
        result.append(item)
        
    return result
```

## Additional Resources

For each algorithm pattern, remember these key principles:

1. **Understand the basic template**
2. **Recognize when to apply the pattern**
3. **Identify variations needed for specific problems**
4. **Practice with different constraints and edge cases**

These templates provide starting points - you'll often need to adapt them based on specific problem requirements.
