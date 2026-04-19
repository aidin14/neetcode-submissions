class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # SOLUTION 1
        # ans = nums
        # for i in range(len(nums)):
        #     ans.append(nums[i])
        # return ans
        ans = []

        # SOLUTION 2
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans

        # n = len(nums)
        # ans = [0]*(2*n)
        # for i, num in enumerate(nums):
        #     ans[i]=num
        #     ans[i+n]=num
        # return ans