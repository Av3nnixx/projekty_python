class Solution(object):
    def maxProfit(self, prices):
        min_value = prices[0]
        min_value_index = 0
        max_profit = 0
        for i,price in enumerate(prices):
            if price < min_value:
                min_value = price
                min_value_index = i
            else:
                if price - min_value > max_profit:
                    max_profit = price - min_value
        return max_profit

solution = Solution()
print(solution.maxProfit([3,2,6,5,0,3]))