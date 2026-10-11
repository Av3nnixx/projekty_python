class Solution(object):
    def twoSum(self, nums, target):
        for i,num in enumerate(nums):
            table = nums
            for index,t in enumerate(table):
                if num + t == target and i != index:
                    return [i,index]

solution = Solution()
print(solution.twoSum([3,3],6))
