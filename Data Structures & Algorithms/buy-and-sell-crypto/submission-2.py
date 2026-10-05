class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        lowest_buy = prices[0]
        best_profit = 0
        for i in prices:
            if i < lowest_buy:
                lowest_buy = i
            if i - lowest_buy > best_profit:
                best_profit = i - lowest_buy
       
        return best_profit


     
