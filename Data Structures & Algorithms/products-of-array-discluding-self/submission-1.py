class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix_list = [1] * (len(nums) + 1) # starts at 1 always
        # suffix_list = [1] * (len(nums) + 1)
        # for i in range(1, len(nums)):
        #     prefix_list[i] = prefix_list[i - 1] * nums[i - 1]
        # for j in range((len(nums) - 2), -1, -1):
        #     suffix_list[j] = nums[j+1] * suffix_list[j + 1]
        # res = []
        # for k in range(len(nums)):
        #     res.append(prefix_list[k] * suffix_list[k])
        # return res
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for j in range(n - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res
        