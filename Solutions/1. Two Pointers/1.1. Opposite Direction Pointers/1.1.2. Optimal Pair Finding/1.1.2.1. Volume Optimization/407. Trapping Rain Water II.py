"""
1.	Pre-computation analysis:
	*	we are given a 2D array (matrix) of positive integers, range [1, 10^6]
	*	the matrix dimensions can be between 1x1 and 200x200
	*	meaning we don't have to handle empty matrix case
		but the data size is moderate, allowing for more complex approaches
	*	this is a 3D extension of the 1D trapping rain water problem

2.	Problem Definition:
	*	we are given a 2D matrix where each cell represents the height of a block
	*	we need to compute how much water can be trapped after raining
	*	water can only be trapped if it's surrounded by higher blocks
	*	water flows out from the boundaries (edges of the matrix)
	*	the key insight: water level at any point is determined by the minimum
		height along any path to the boundary
"""

from typing import List
import math

"""
Two-Pointer approach for smaller matrices:
This uses the concept of "water level propagation" from boundaries inward
"""

def trapRainWaterTwoPointer(heightMap: List[List[int]]) -> int:
    if not heightMap or not heightMap[0]:
        return 0
    
    rows = len(heightMap)
    cols = len(heightMap[0])

    if rows < 3 or cols < 3:
        return 0
    
    water_level = []
    for x in range(rows):
        row = []
        for y in range(cols):
            if x == 0 or x == rows-1 or y == 0 or y == cols-1:
                row.append(heightMap[x][y])
            else:
                row.append(math.inf)
        water_level.append(row)

    changed = True
    while changed:
        changed = False
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                min_neighbor = min(
                    water_level[i-1][j], water_level[i+1][j],
                    water_level[i][j-1], water_level[i][j+1]
                )
                new_level = max(heightMap[i][j], min_neighbor)
                if new_level < water_level[i][j]:
                    water_level[i][j] = new_level
                    changed = True

    total = 0
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            total += water_level[i][j] - heightMap[i][j]
    return total

"""
7.	Key Insights:
    *   This extends 1D two-pointer technique to 2D
    *   Water flows to the boundary with minimum "escape cost"
    *   Process cells in order of their minimum reachable water level
    *   Similar greedy principle: always handle the most constrained cell first
"""

"""
8.	Testing:
"""
if __name__ == "__main__":
    # Test case 1: Simple valley
    heightMap1 = [
        [1,4,3,1,3,2],
        [3,2,1,3,2,4],
        [2,3,3,2,3,1]
    ]
    
    # Test case 2: Multiple valleys
    heightMap2 = [
        [3,3,3,3,3],
        [3,2,2,2,3],
        [3,2,1,2,3],
        [3,2,2,2,3],
        [3,3,3,3,3]
    ]
    
    # Test case 3: No water can be trapped
    heightMap3 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    heightMap4 = [
        [12,13,1,12],
        [13,4,13,12],
        [13,8,10,12],
        [12,13,12,12],
        [13,13,13,13]
    ]
    
    print(f"Test 1: {trapRainWaterTwoPointer(heightMap1)}")
    print(f"Test 2: {trapRainWaterTwoPointer(heightMap2)}")
    print(f"Test 3: {trapRainWaterTwoPointer(heightMap3)}")
    print(f"Test 4: {trapRainWaterTwoPointer(heightMap4)}")
