class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateDict = {}
        for key in nums: 
            if key in duplicateDict:
                return True 
            duplicateDict[key] = 1
        return False 
