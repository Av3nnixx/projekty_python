class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {}
        for s in strs:
            x = list(s)
            x.sort()
            if tuple(x) not in hashmap:
                hashmap[tuple(x)] = []
                hashmap[tuple(x)].append(s)
            else:
                hashmap[tuple(x)].append(s)
        return  list(hashmap.values())

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))