class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(current_path):
            # Base Case: If the path length equals nums length, we found a permutation!
            if len(current_path) == len(nums):
                result.append(current_path.copy())
                return
            
            # Recursive Case: Try each number in nums
            for num in nums:
                if num not in current_path:
                    current_path.append(num)       # 1. Choose
                    backtrack(current_path)         # 2. Explore
                    current_path.pop()             # 3. Unchoose (Backtrack)
        
        backtrack([])
        return result