class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        result = [""]
        
        for char in s:
            if char.isalpha():
                # For letters, duplicate existing prefixes: one lower, one upper
                result = [sub + c for sub in result for c in (char.lower(), char.upper())]
            else:
                # For digits/symbols, just append the character as is
                result = [sub + char for sub in result]
                
        return result