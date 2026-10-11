class Solution(object):
    def containsDuplicate(self, nums):
        result = False
        nums = sorted(nums)
        for num in range(len(nums) - 1):
            print(num)
            if nums[num] == nums[num + 1]:
                result = True
        return  result
