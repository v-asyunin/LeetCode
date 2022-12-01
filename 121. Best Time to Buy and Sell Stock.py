class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        if len(prices) < 2:
            return 0

        minPriceInPast = prices[0]
        Profit = 0
        for price in prices:

            if price < minPriceInPast:
                minPriceInPast = price

            if price - minPriceInPast > Profit:
                Profit = price - minPriceInPast

        return Profit

x = Solution()

prices = [10, 7, 5, 8, 11, 9]
print(prices, '->', x.maxProfit(prices))

prices = [1, 3, 5, 8, 11, 20]
print(prices, '->', x.maxProfit(prices))

prices = [2, 2, 2, 2, 2, 2]
print(prices, '->', x.maxProfit(prices))

prices = [1]
print(prices, '->', x.maxProfit(prices))

prices = []
print(prices, '->', x.maxProfit(prices))
