class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        arr.sort() # Sorting is the correct first step
        answer = 0

        for i in range(n - 2):
            # The two-pointer approach starts from the element after i
            a = i + 1
            b = n - 1
            
            while a < b:
                current_sum = arr[i] + arr[a] + arr[b]
                
                if current_sum < target:
                    a += 1
                elif current_sum > target:
                    b -= 1
                else: # current_sum == target
                    # This is where the correct counting logic goes
                    
                    # Case 1: The pointers are on different numbers
                    if arr[a] != arr[b]:
                        count_a = 1
                        while a + 1 < b and arr[a] == arr[a + 1]:
                            count_a += 1
                            a += 1
                        
                        count_b = 1
                        while b - 1 > a and arr[b] == arr[b - 1]:
                            count_b += 1
                            b -= 1
                        
                        answer += count_a * count_b
                        a += 1 # Move to the next new number
                        b -= 1 # Move to the next new number
                        
                    # Case 2: The pointers are on the same number
                    else:
                        # We need to choose 2 numbers from the block of identical numbers
                        # The size of this block is (b - a + 1)
                        m = b - a + 1
                        answer += m * (m - 1) // 2
                        break # We have counted all pairs for this i, so we can exit the while loop

        return answer % MOD