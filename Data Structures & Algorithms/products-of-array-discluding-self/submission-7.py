class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # DIVISION
        prod = 1
        num_of_zero = 0 
        for n in nums:
            if n == 0:
                num_of_zero += 1
            else: 
                prod *= n
        ans = []
        if num_of_zero == 0:
            for num in nums: 
                ans.append(int(prod/num))
        elif num_of_zero == 1 : 
            for num in nums: 
                if num != 0:
                    ans.append(0)
                else:
                    ans.append(prod)
        else: 
            return [0]*len(nums)
        return ans
        # BRUTE FORCE 
        # ans = [1]*len(nums)
        # for i in range(len(nums)):  
        #     for j in range(len(nums)):
        #         if j != i: 
        #             ans[i] = ans[i]*nums[j]
        # return ans
                    