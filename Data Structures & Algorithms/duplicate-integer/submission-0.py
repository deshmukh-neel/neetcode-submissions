class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for x in nums:
            num_set.add(x)
        if len(num_set) == len(nums):
            return False
        else:
            return True