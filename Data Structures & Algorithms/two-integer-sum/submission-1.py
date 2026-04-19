class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {} 
        for i in range(len(nums)): 
            nums_dict[nums[i]] = i

        for i in range(len(nums)): 
            j = nums_dict.get(target-nums[i])
            if i != j and j != None: 
                return [i,j]
        return []