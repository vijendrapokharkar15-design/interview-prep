# ============================================
# LeetCode #121 - Best Time to Buy & Sell Stock
# Difficulty: Easy
# Topic: Arrays, Sliding Window, Greedy
# Date: 02/04/2026
# Status: Accepted ✅
# ============================================

# PROBLEM:
# Given an array of stock prices, find the maximum profit
# by buying on one day and selling on a later day.

# Example:
# Input:  prices = [7, 1, 5, 3, 6, 4]
# Output: 5  (buy at 1, sell at 6)

# APPROACH: Track Running Minimum
# Scan left to right — one pass
# Track the cheapest price seen so far
# At every step calculate profit if sold today
# Keep the best profit seen

# TIME:  O(n) — one single pass
# SPACE: O(1) — only two variables used

class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')   # impossibly high starting minimum
        max_profit = 0             # start at 0 (worst case = don't trade)

        for price in prices:

            if price < min_price:              # found a cheaper buy day?
                min_price = price              # update our best buy price

            elif price - min_price > max_profit:   # better profit today?
                max_profit = price - min_price     # update best profit

        return max_profit

# ============================================
# TEST CASES
# ============================================
solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Expected: 5
print(solution.maxProfit([7, 6, 4, 3, 1]))      # Expected: 0
print(solution.maxProfit([2, 4, 1]))             # Expected: 2

# ============================================
# WHAT I LEARNED
# ============================================
# - Track running minimum as you scan left to right
# - Profit at any point = current price - min price seen so far
# - Greedy pattern: always keep the locally best option
# - float('inf') is a great trick for initialising minimums