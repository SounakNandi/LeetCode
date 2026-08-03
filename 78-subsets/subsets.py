class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = [[]]
        
        for num in nums:
            # For every existing subset, create a new subset that includes `num`
            result += [curr + [num] for curr in result]
            
        return result