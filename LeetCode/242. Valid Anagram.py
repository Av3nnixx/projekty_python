class Solution(object):
    def isAnagram(self, s, t):
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        return  s == t
solution = Solution()
print(solution.isAnagram("anagram","nagaram"))