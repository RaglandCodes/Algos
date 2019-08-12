'''

LeetCode 122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if prices == []:
            return 0
            
        bought  = prices[0]
        current_profit = 0
        a = 0
        
        for i in range(1, len(prices)):
            
            if prices[i] < bought:
                a += current_profit
                current_profit = 0
                bought = prices[i]
            elif prices[i] >= bought:
                if (prices[i] - bought) > current_profit:
                    current_profit = prices[i] - bought
                else:
                    bought = prices[i]
                    a += current_profit
                    current_profit = 0
        
        return a+current_profit
                