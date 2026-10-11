class Solution:
    def firstUniqChar(self, s):
        hashmap = {} # e : 2
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 0
        for k,v in hashmap.items():
            if v == 0:
                x = s.find(k)
                return x
        return -1
solution = Solution()
print(solution.firstUniqChar("loveleetcode"))