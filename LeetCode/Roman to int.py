class Solution(object):
    def romanToInt(self, s):
        total = 0
        values = {"I": 1,
                     "V":5,
                     "X":10,
                     "L":50,
                     "C":100,
                     "D":500,
                     "M":1000,
                    "W":1001}
        next_value = 0
        for i in range(len(s)):
            current = values[s[i]]
            if i < len(s) - 1:
                next_value = values[s[i + 1]]
            else:
                next_value  = 0
            if current < next_value:
                total -= current
            else:
                total += current
        return total
x = Solution()
user_input = input()
print(x.romanToInt(user_input))