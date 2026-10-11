class Solution(object):
    def isPalindrome(self, x):
        hashmap = {}
        reverse = ""
        for l in reversed(str(x)):
            reverse += l
            hashmap[x] = reverse
        index,key = next(iter(hashmap.items()))
        if str(index) == str(key):
            return True
        return  False
solution = Solution()
print(solution.isPalindrome(141))