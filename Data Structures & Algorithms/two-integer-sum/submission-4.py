class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i,n in enumerate(nums): 
            num_dict[n]=i
        print(num_dict)
        for i,n in enumerate(nums):
            diff = target - n
            print(target, n,diff)
            if diff in num_dict and num_dict[diff] != i:
                return [min(num_dict[diff],i), max(num_dict[diff],i)]
        